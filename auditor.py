"""Deterministic, local, data-oriented continuity audit engine."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass

from pydantic import ValidationError

from evidence import calculate_signal, validate_finding_evidence
from models import AuditReport, AuthorityRecord, ContinuityPackage, Finding, FindingType


class InputValidationError(ValueError):
    """Readable input error suitable for the UI."""


@dataclass(frozen=True)
class Detector:
    domain: str
    pattern: re.Pattern[str]
    finding_type: FindingType
    explanation: str
    recommended_action: str
    confidence: float = 0.99

    def detect(self, record: AuthorityRecord, scene: str) -> str | None:
        match = self.pattern.search(scene)
        return match.group("quote") if match else None


DETECTORS: tuple[Detector, ...] = (
    Detector(
        domain="chronology",
        pattern=re.compile(
            r"(?P<quote>At 06:15, the evacuation was already underway)", re.IGNORECASE
        ),
        finding_type="contradiction",
        explanation="The scene starts the evacuation before the protected time.",
        recommended_action="Align the scene time with 06:40 or later, or request a human authority change.",
    ),
    Detector(
        domain="character",
        pattern=re.compile(
            r"(?P<quote>putting her full weight on her left ankle)", re.IGNORECASE
        ),
        finding_type="protected_state_violation",
        explanation="Mara bears weight on an ankle whose medical restriction remains active.",
        recommended_action="Keep weight off the left ankle unless a human confirms the seal was removed.",
    ),
    Detector(
        domain="object",
        pattern=re.compile(
            r"(?P<quote>Mara pulled the brass key from her pocket)", re.IGNORECASE
        ),
        finding_type="protected_state_violation",
        explanation="The scene gives Mara an object that remains sealed and inaccessible.",
        recommended_action="Remove the key from the scene or record an approved access-state change.",
    ),
    Detector(
        domain="relationship",
        pattern=re.compile(
            r"(?P<quote>Ivo gave him their old three-tap handshake)", re.IGNORECASE
        ),
        finding_type="continuity_leak",
        explanation="The familiar handshake implies a prior relationship before the first meeting.",
        recommended_action="Stage a first encounter or move the familiarity after the docking hearing.",
    ),
    Detector(
        domain="location",
        pattern=re.compile(
            r"(?P<quote>Mara sprinted across the north bridge)", re.IGNORECASE
        ),
        finding_type="contradiction",
        explanation="The scene crosses a location whose protected state is closed.",
        recommended_action="Use an open route or obtain a human-approved location-state change.",
    ),
)


def load_package(raw_json: str) -> ContinuityPackage:
    """Parse and validate a continuity package with a concise error message."""
    if not raw_json.strip():
        raise InputValidationError("Continuity package is empty.")
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise InputValidationError(
            f"Continuity package is not valid JSON (line {exc.lineno}, column {exc.colno})."
        ) from exc
    try:
        return ContinuityPackage.model_validate(payload)
    except ValidationError as exc:
        first = exc.errors()[0]
        location = ".".join(str(part) for part in first["loc"])
        raise InputValidationError(
            f"Continuity package failed validation at {location}: {first['msg']}"
        ) from exc


def _candidate_finding(
    record: AuthorityRecord, detector: Detector, audited_quote: str, index: int
) -> Finding:
    return Finding(
        finding_id=f"F-{index:03d}-{record.id}",
        type=detector.finding_type,
        severity=record.severity_if_breached,
        authority_id=record.id,
        authority_quote=record.source.quote,
        audited_quote=audited_quote,
        explanation=detector.explanation,
        recommended_action=detector.recommended_action,
        confidence=detector.confidence,
        evidence_validated=False,
    )


def audit(package: ContinuityPackage, scene: str) -> AuditReport:
    """Audit a scene locally using the detector registry and linked authorities."""
    if not scene.strip():
        raise InputValidationError("Scene text is empty.")

    candidates: list[Finding] = []
    for record in package.records:
        if record.status == "deprecated":
            continue
        for detector in DETECTORS:
            if detector.domain != record.domain:
                continue
            quote = detector.detect(record, scene)
            if quote:
                candidates.append(
                    _candidate_finding(record, detector, quote, len(candidates) + 1)
                )

    findings = [
        validate_finding_evidence(candidate, package, scene) for candidate in candidates
    ]
    signal = calculate_signal(findings)
    validated_count = sum(item.evidence_validated for item in findings)
    fingerprint = hashlib.sha256(
        (package.model_dump_json() + "\n" + scene).encode("utf-8")
    ).hexdigest()[:12]
    summary = (
        f"{validated_count} validated finding(s) from {len(package.records)} "
        f"authority record(s). Human review is required."
    )
    return AuditReport(
        audit_id=f"AUD-{fingerprint.upper()}",
        model="deterministic-local-rules-v1",
        overall_signal=signal,
        summary=summary,
        findings=findings,
        human_decision_required=True,
    )
