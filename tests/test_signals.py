from evidence import calculate_signal
from models import Finding


def _finding(severity="low", validated=True):
    return Finding(
        finding_id=f"F-{severity}-{validated}",
        type="risk",
        severity=severity,
        authority_id="AUTH-X",
        authority_quote="Authority",
        audited_quote="Scene",
        explanation="Explanation",
        recommended_action="Review",
        confidence=0.8,
        evidence_validated=validated,
    )


def test_signal_red_for_validated_high():
    assert calculate_signal([_finding("high")]) == "red"


def test_signal_green_without_findings():
    assert calculate_signal([]) == "green"


def test_invalid_critical_evidence_does_not_govern_signal():
    assert calculate_signal([_finding("critical", validated=False)]) == "green"


def test_signal_amber_for_validated_medium_only():
    assert calculate_signal([_finding("medium")]) == "amber"
