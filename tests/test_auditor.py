import json
from pathlib import Path

import pytest

from auditor import InputValidationError, audit, load_package


ROOT = Path(__file__).resolve().parents[1]


def test_load_package_has_five_authorities(package):
    assert package.project_id == "DEMO-LANTERN-VAULT"
    assert len(package.records) == 5


def test_problematic_case_is_red_with_five_validated_findings(package, problematic_scene):
    report = audit(package, problematic_scene)
    assert report.overall_signal == "red"
    assert len(report.findings) == 5
    assert sum(item.evidence_validated for item in report.findings) == 5
    assert [item.authority_id for item in report.findings] == [
        "AUTH-001", "AUTH-002", "AUTH-003", "AUTH-004", "AUTH-005"
    ]


def test_problematic_quotes_match_expected_fixture(package, problematic_scene):
    report = audit(package, problematic_scene)
    expected = json.loads(
        (ROOT / "demo_data" / "expected-findings.json").read_text(encoding="utf-8")
    )
    actual = [
        {
            "authority_id": finding.authority_id,
            "severity": finding.severity,
            "authority_quote": finding.authority_quote,
            "audited_quote": finding.audited_quote,
        }
        for finding in report.findings
    ]
    assert actual == expected["findings"]


def test_clean_case_is_green_with_zero_findings(package, clean_scene):
    report = audit(package, clean_scene)
    assert report.overall_signal == "green"
    assert report.findings == []


def test_invalid_json_has_readable_error():
    with pytest.raises(InputValidationError, match="line 1, column 2"):
        load_package("{")


def test_empty_scene_has_readable_error(package):
    with pytest.raises(InputValidationError, match="Scene text is empty"):
        audit(package, "  ")
