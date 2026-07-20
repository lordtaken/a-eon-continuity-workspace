"""Streamlit interface for the local A-Eon Continuity Auditor."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from auditor import InputValidationError, audit, load_package
from exporters import export_json, export_markdown
from models import AuditReport


ROOT = Path(__file__).resolve().parent
DEMO = ROOT / "demo_data"
NOTICE = "No changes are applied automatically."
LOCKS = [
    "ATLAS_REFERENCE_ONLY",
    "SYNTHETIC_DATA_ONLY",
    "NO_PRIVATE_DATA_TRANSFER",
    "NO_REAL_CANON_TRANSFER",
    "NO_SOURCE_CODE_TRANSFER",
    "NO_VISUAL_ASSET_COPY",
    "NO_DRIVE_CONNECTION",
    "NO_AUTOMATIC_REWRITE",
    "NO_SILENT_CHANGES",
    "NO_DATABASE",
    "NO_AUTHENTICATION",
    "NO_MULTIAGENT",
    "NO_SITE_PUBLICATION",
]


def read_demo(name: str) -> str:
    return (DEMO / name).read_text(encoding="utf-8")


def initialize_state() -> None:
    defaults = {
        "package_text": read_demo("continuity-package.json"),
        "scene_text": read_demo("new-scene.md"),
        "report": None,
        "audit_error": None,
        "loaded_case": "Problematic demo",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def load_case(scene_name: str, label: str) -> None:
    st.session_state.package_text = read_demo("continuity-package.json")
    st.session_state.scene_text = read_demo(scene_name)
    st.session_state.loaded_case = label
    st.session_state.report = None
    st.session_state.audit_error = None


def render_finding(finding) -> None:
    validation = "VALIDATED" if finding.evidence_validated else "EXCLUDED"
    with st.container(border=True):
        st.markdown(
            f"**{finding.finding_id}** · `{finding.type}` · "
            f"**{finding.severity.upper()}** · Evidence `{validation}`"
        )
        st.caption(f"Linked authority · {finding.authority_id}")
        left, right = st.columns(2)
        with left:
            st.markdown("**Exact authority quote**")
            st.info(finding.authority_quote)
        with right:
            st.markdown("**Exact audited quote**")
            st.warning(finding.audited_quote)
        st.markdown(f"**Why it matters:** {finding.explanation}")
        st.markdown(f"**Next human action:** {finding.recommended_action}")


st.set_page_config(
    page_title="A-Eon Continuity Workspace",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(
    """
    <style>
      :root { color-scheme: dark; }
      .stApp {
        background:
          radial-gradient(circle at 75% -10%, rgba(159, 116, 57, .18), transparent 35rem),
          linear-gradient(155deg, #11130f 0%, #171914 52%, #10120f 100%);
      }
      h1, h2, h3 { font-family: Georgia, 'Times New Roman', serif; letter-spacing: -.02em; }
      [data-testid="stMetric"] {
        background: rgba(31, 34, 27, .86); border: 1px solid rgba(192, 164, 102, .25);
        border-radius: .5rem; padding: .8rem 1rem;
      }
      [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(27, 30, 24, .74); border-color: rgba(192, 164, 102, .24);
      }
      .aeon-kicker { color: #c8ad73; font: 600 .74rem/1.4 ui-monospace, monospace; letter-spacing: .16em; }
      .aeon-subtitle { color: #aeb3a5; max-width: 56rem; }
      .aeon-notice {
        position: sticky; top: 2.8rem; z-index: 99; margin: .8rem 0;
        padding: .72rem 1rem; border: 1px solid #a96748; border-radius: .4rem;
        background: rgba(76, 40, 29, .95); color: #f3ddd0; font-weight: 700;
      }
      .aeon-locks { font: .72rem/1.9 ui-monospace, monospace; color: #b8c49d; overflow-wrap: anywhere; }
      @media (max-width: 700px) {
        [data-testid="stHorizontalBlock"] { flex-direction: column; }
        [data-testid="column"] { width: 100% !important; }
        .block-container { padding-left: 1rem; padding-right: 1rem; }
      }
      @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation: none !important; transition: none !important; scroll-behavior: auto !important; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)
initialize_state()

st.markdown('<div class="aeon-kicker">A-EON / LOCAL CONTINUITY CONTROL</div>', unsafe_allow_html=True)
st.title("A-Eon Continuity Workspace")
st.markdown(
    '<p class="aeon-subtitle">Evidence-based continuity control for complex creative projects · '
    "Operational module: Continuity Auditor</p>",
    unsafe_allow_html=True,
)
st.markdown(f'<div class="aeon-notice">{NOTICE}</div>', unsafe_allow_html=True)

workspace_tab, audit_tab, evidence_tab = st.tabs(["Workspace", "Audit", "Evidence"])

with workspace_tab:
    st.subheader("Synthetic project workspace")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Project", "Lantern Vault")
    col2.metric("Active sources", "5")
    col3.metric("Protected rules", "4")
    col4.metric("Open risks", "5 demo")

    left, right = st.columns([1.25, 1])
    with left:
        with st.container(border=True):
            st.markdown("### Resume work")
            st.caption("SYNTHETIC CHECKPOINT · C1-DEMO-017")
            st.markdown("**Last operation**  · Continuity packet prepared")
            report: AuditReport | None = st.session_state.report
            status = report.overall_signal.upper() if report else "NOT RUN"
            st.markdown(f"**Last audit state** · {status}")
            st.markdown("**Next action** · Review evidence and make a human decision")
            st.markdown("**Input type** · Continuity package + scene")
        with st.container(border=True):
            st.markdown("### Active sources")
            st.markdown(
                "Master Timeline · Mara Character Sheet · Object Register · "
                "Relationship Matrix · Location State Register"
            )
    with right:
        with st.container(border=True):
            st.markdown("### Active locks")
            st.markdown(
                '<div class="aeon-locks">' + "<br>".join(f"◈ {lock}" for lock in LOCKS) + "</div>",
                unsafe_allow_html=True,
            )

with audit_tab:
    st.subheader("Run a local audit")
    st.caption("Load a synthetic case, paste or upload both inputs, then run the deterministic engine.")
    button_left, button_right = st.columns(2)
    if button_left.button("Load problematic demo", use_container_width=True):
        load_case("new-scene.md", "Problematic demo")
    if button_right.button("Load clean demo", use_container_width=True):
        load_case("clean-scene.md", "Clean demo")

    package_upload = st.file_uploader("Upload continuity package JSON", type=["json"])
    scene_upload = st.file_uploader("Upload scene Markdown or text", type=["md", "txt"])
    package_text = st.text_area(
        "Continuity package JSON",
        key="package_text",
        height=260,
        help="Paste a complete local continuity package. Nothing is transmitted.",
    )
    scene_text = st.text_area("Scene to audit", key="scene_text", height=260)

    st.caption(f"Loaded source · {st.session_state.loaded_case}")
    st.markdown(f"**{NOTICE}**")
    if st.button("Run local continuity audit", type="primary", use_container_width=True):
        try:
            if package_upload is not None:
                package_text = package_upload.getvalue().decode("utf-8")
            if scene_upload is not None:
                scene_text = scene_upload.getvalue().decode("utf-8")
            package = load_package(package_text)
            st.session_state.report = audit(package, scene_text)
            st.session_state.audit_error = None
            st.success("Audit complete. Open the Evidence tab to review the human decision package.")
        except UnicodeDecodeError:
            st.session_state.audit_error = "Uploaded files must use UTF-8 encoding."
        except InputValidationError as exc:
            st.session_state.audit_error = str(exc)

    if st.session_state.audit_error:
        st.error(st.session_state.audit_error)

with evidence_tab:
    report = st.session_state.report
    if report is None:
        st.subheader("No audit report yet")
        st.info("Open Audit, load either synthetic demo, and run the local continuity audit.")
    else:
        st.subheader("Evidence review")
        validated = sum(item.evidence_validated for item in report.findings)
        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Overall signal", report.overall_signal.upper())
        metric2.metric("Findings", len(report.findings))
        metric3.metric("Validated pairs", validated)
        st.markdown(report.summary)
        st.markdown(f"**{NOTICE} Human decision required.**")

        for finding in report.findings:
            render_finding(finding)
        if not report.findings:
            st.success("No validated continuity conflicts were found in this scene.")

        markdown = export_markdown(report)
        json_report = export_json(report)
        download_left, download_right = st.columns(2)
        download_left.download_button(
            "Download Markdown",
            data=markdown,
            file_name=f"{report.audit_id}.md",
            mime="text/markdown",
            use_container_width=True,
        )
        download_right.download_button(
            "Download JSON",
            data=json_report,
            file_name=f"{report.audit_id}.json",
            mime="application/json",
            use_container_width=True,
        )
