import json

from auditor import audit
from exporters import export_json, export_markdown
from models import AuditReport


def test_markdown_export_contains_dual_evidence(package, problematic_scene):
    markdown = export_markdown(audit(package, problematic_scene))
    assert "# Continuity Audit Report" in markdown
    assert "Authority quote:" in markdown
    assert "Audited quote:" in markdown
    assert "No changes are applied automatically." in markdown


def test_json_export_is_valid_and_round_trips(package, problematic_scene):
    exported = export_json(audit(package, problematic_scene))
    payload = json.loads(exported)
    restored = AuditReport.model_validate(payload)
    assert restored.overall_signal == "red"
    assert len(restored.findings) == 5
