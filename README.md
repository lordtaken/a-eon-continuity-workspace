# A-Eon Continuity Workspace

**Continuity Auditor** is a small, local Streamlit application that checks a new
scene against a typed continuity package. It produces an auditable decision
packet, never an automatic rewrite.

> No changes are applied automatically.

## Problem

Long creative projects distribute important decisions across timelines,
character sheets, object registers, relationship maps, and location states. A
new scene can contradict one of those authorities without making the conflict
easy to trace. This workspace connects every finding to two literal citations:
the linked authority and the submitted scene.

## Flow

1. Load, paste, or upload a continuity package in JSON.
2. Load, paste, or upload a scene in Markdown or plain text.
3. Run the deterministic local audit.
4. Review the recalculated red, amber, or green signal.
5. Inspect both exact quotes, the explanation, and the recommended human action.
6. Export the same essential evidence as Markdown or JSON.

The single Streamlit application contains the required **Workspace**, **Audit**,
and **Evidence** tabs. Session state retains only the current in-memory inputs
and report; there is no database, authentication, or persistent user storage.

## Install and run

Python 3.11 or later is required.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

On macOS or Linux, replace the last two interpreter paths with
`.venv/bin/python`.

Run the verification suite:

```powershell
python -m compileall .
.\.venv\Scripts\python.exe -m pytest
```

## Synthetic corpus

All demonstration data is fictional and authorized for this build. The
`demo_data/` directory contains:

- `continuity-package.json`: five synthetic authority records;
- `new-scene.md`: a problematic scene that produces **red**, exactly **5
  findings**, and **5 validated evidence pairs**;
- `clean-scene.md`: a compliant scene that produces **green** and **0 findings**;
- `expected-findings.json`: the authorized behavioral-oracle expectations used
  by the tests.

The original handoff specifications and expected behavior remain in the
repository for traceability. They contain no Work prototype code, private canon,
credentials, or production integrations. `HANDOFF_INPUT_PACKAGE_MANIFEST.json`
is the immutable manifest of that incoming handoff and intentionally records its
original `demo/` paths; the runnable delivery corpus is consolidated only under
`demo_data/`.

## Local deterministic engine

`auditor.py` uses a small detector registry organized by continuity domain. A
detector extracts the conflicting scene substring; the linked record supplies
severity and the authority citation. The engine does not return a prewritten
report. `evidence.py` verifies that both quotes are literal substrings before a
finding can influence the signal:

- red: a validated `critical` or `high` finding exists;
- amber: a validated `medium` finding exists and none is higher;
- green: no validated finding exists, or only validated `low` findings exist.

Pydantic models reject malformed packages and reports with readable errors.
Markdown and JSON exporters use the same typed report displayed in Evidence.

## No API or external runtime

The product is fully local:

```text
OPENAI_API_KEY_REQUIRED = NO
LIVE_API_CALLS = ZERO
AI_RUNTIME = DISABLED
```

There is no OpenAI SDK, network client, API-key lookup, executable AI adapter,
Drive connection, or deployment configuration in the runtime code.

## How GPT-5.6 was used

The primary Codex session ran on GPT-5.6 Sol (`gpt-5.6-sol`). In that same
session, GPT-5.6 read the authorized handoff, created the new Git repository,
authored the typed contracts, detector registry, evidence validation,
traffic-light calculation, exporters, Streamlit interface, tests, documentation,
and delivery packaging, then ran the documented local verification commands and
made only evidence-driven P0 delivery repairs.

The supplied Work result was used only as a behavioral oracle; its code was not
present, requested, searched, or copied. No subagents were opened. GPT-5.6 was
used for repository construction through the Codex ChatGPT session only: the
delivered application is deterministic and local, and it does not embed or call
GPT-5.6, the OpenAI API, or any other AI runtime.

## Human control and limits

- Findings are rule-based and cover the authorized demonstration domains; this
  C1 build is not a general semantic reasoning system.
- A green report means no configured rule matched validated evidence. It does
  not prove that a scene is globally correct.
- Recommendations are review prompts. The application never edits the scene or
  continuity package.
- Inputs remain in the Streamlit session. Users should still avoid private data
  in this synthetic evaluation build.
- No P1 filters, copy controls, AI adapter, persistence, or publication are
  included.

## Demonstration in under three minutes

1. Start Streamlit and show the visible locks in **Workspace** (20 seconds).
2. In **Audit**, select **Load problematic demo**, run the audit, and open
   **Evidence** (45 seconds).
3. Show red, five findings, five validated pairs, and one pair of exact quotes
   (50 seconds).
4. Download Markdown or JSON (20 seconds).
5. Return to **Audit**, select **Load clean demo**, run it, and show green with
   zero findings (35 seconds).

Total target: approximately 2 minutes 50 seconds.
