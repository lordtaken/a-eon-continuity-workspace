from evidence import validate_finding_evidence
from models import Finding


def _finding(**changes):
    values = {
        "finding_id": "F-TEST",
        "type": "contradiction",
        "severity": "critical",
        "authority_id": "AUTH-001",
        "authority_quote": "The evacuation begins at 06:40 on 14 October 2147.",
        "audited_quote": "At 06:15, the evacuation was already underway",
        "explanation": "Test finding.",
        "recommended_action": "Review it.",
        "confidence": 1.0,
        "evidence_validated": False,
    }
    values.update(changes)
    return Finding(**values)


def test_authority_quote_is_validated_against_linked_record(package, problematic_scene):
    assert validate_finding_evidence(_finding(), package, problematic_scene).evidence_validated


def test_invalid_authority_quote_is_rejected(package, problematic_scene):
    result = validate_finding_evidence(
        _finding(authority_quote="Invented authority quote"), package, problematic_scene
    )
    assert not result.evidence_validated


def test_invalid_scene_quote_is_rejected(package, problematic_scene):
    result = validate_finding_evidence(
        _finding(audited_quote="Invented scene quote"), package, problematic_scene
    )
    assert not result.evidence_validated
