"""Literal evidence validation and deterministic traffic-light calculation."""

from __future__ import annotations

from collections.abc import Iterable

from models import ContinuityPackage, Finding, Signal


def validate_finding_evidence(
    finding: Finding, package: ContinuityPackage, scene: str
) -> Finding:
    """Return a copy whose evidence flag reflects both linked literal citations."""
    record = next(
        (item for item in package.records if item.id == finding.authority_id), None
    )
    authority_valid = bool(
        record
        and finding.authority_quote
        and finding.authority_quote in record.source.quote
    )
    scene_valid = bool(finding.audited_quote and finding.audited_quote in scene)
    return finding.model_copy(
        update={"evidence_validated": authority_valid and scene_valid}
    )


def calculate_signal(findings: Iterable[Finding]) -> Signal:
    """Calculate a signal from validated evidence only."""
    severities = {
        finding.severity for finding in findings if finding.evidence_validated
    }
    if severities.intersection({"critical", "high"}):
        return "red"
    if "medium" in severities:
        return "amber"
    return "green"
