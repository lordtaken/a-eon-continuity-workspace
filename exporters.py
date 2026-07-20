"""Markdown and JSON report exporters."""

from __future__ import annotations

from models import AuditReport


def export_json(report: AuditReport) -> str:
    return report.model_dump_json(indent=2)


def export_markdown(report: AuditReport) -> str:
    lines = [
        "# Continuity Audit Report",
        "",
        f"- Audit ID: `{report.audit_id}`",
        f"- Overall signal: **{report.overall_signal.upper()}**",
        f"- Summary: {report.summary}",
        "- Human decision required: **Yes**",
        "",
        "> No changes are applied automatically.",
    ]
    if not report.findings:
        lines.extend(["", "## Findings", "", "No validated continuity conflicts found."])
        return "\n".join(lines) + "\n"

    lines.extend(["", "## Findings"])
    for finding in report.findings:
        lines.extend(
            [
                "",
                f"### {finding.finding_id} — {finding.severity.upper()}",
                "",
                f"- Type: `{finding.type}`",
                f"- Authority: `{finding.authority_id}`",
                f"- Evidence validated: **{'Yes' if finding.evidence_validated else 'No'}**",
                f"- Authority quote: “{finding.authority_quote}”",
                f"- Audited quote: “{finding.audited_quote}”",
                f"- Explanation: {finding.explanation}",
                f"- Recommended action: {finding.recommended_action}",
            ]
        )
    return "\n".join(lines) + "\n"
