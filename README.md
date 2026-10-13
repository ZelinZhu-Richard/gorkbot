# GorkBot Project Repository

> Working codename only. The final product name must be selected independently and must not imply affiliation with xAI, Cursor, or Grok.

This repository is the source of truth for designing and building a model-agnostic persistent-agent platform.

The long-term capability benchmark is clean-room functional parity with Grok Bot, followed by measurable improvement in areas such as model choice, verified completion, security isolation, cost governance, portability, and inspectable collaboration.

## Current status

- Active program: Engineering Preview
- Current phase: E3 technical validation and model/system qualification; the E1 specification gate and E2 architecture gate are independently `VERIFIED / PASSED`
- Earlier Engineering Preview tasks: `E0-001`, `E1-001`, `E1-002`, and `E2-001` through `E2-006` are `VERIFIED`; `E4-E5` are `NOT_STARTED`
- Startup/customer track: preserved and deferred by D-016; S1-003 was not executed
- Architecture: `EP-ARCH-C01` Integrated Transactional Local Core accepted at the E2 gate; `ADR-E2-001..009` accepted; no implementation authorized
- Engineering Preview target: one local user and one persistent software-engineering agent working on real repositories with durable state, independent verification, and evidence bundles
- Customer wedge: not selected or validated; S1-001 and S1-002 remain verified research inputs
- Model roles: not locked; benchmarks have not run
- Code: no application implementation yet
- Public repository: yes, so never commit secrets, private customer data, access tokens, credentials, or confidential documents

```yaml
E3-001: VERIFIED
E3-002: VERIFIED — PHASE_A_PROTOCOL_CRITERIA_FROZEN_HARNESS_IMPLEMENTABLE
E3-003: READY
E3-004: BACKLOG — blocked pending E3-003 Phase A verification
E3-005: BACKLOG / DO_NOT_RUN
E3-006: BACKLOG / DO_NOT_RUN
E3-007: BACKLOG
E3-008: BACKLOG
E3 gate: NOT_EVALUATED

E3-QPA-001 authoritative values: null / null / null
E3-002 QPA proposal: 1 / 3 / 2 — AUTHOR_PROPOSAL_NOT_APPROVED

AUTONOMY_ELIGIBLE: NOT_ELIGIBLE
AUTONOMOUS_BUILD_AUTHORIZED: NO
```

E3 verification can establish autonomy eligibility only. A separate explicit Founder decision is required to authorize autonomous build execution.

## Start here

Every planning or coding model must read these files in order:

1. `MASTER_OPERATING_PROMPT.md`
2. `AGENTS.md`
3. `01_governance/PROJECT_STATE.yaml`
4. `01_governance/TASK_REGISTRY.yaml`
5. `00_inbox/prepared_materials/01_FOUNDER_BRIEF.md`
6. The remaining files listed by the active task

The next command for the planning model is:

```text
MODE: EXECUTE_TASK_E3-003

Read MASTER_OPERATING_PROMPT.md, AGENTS.md, PROJECT_STATE.yaml, TASK_REGISTRY.yaml, and every current E3-003 files_to_read entry.
Treat the repository as the sole authoritative project state.
Execute only the current E3-003 registry entry, within its stated scope and allowed paths. Do not execute, re-author, or modify the already verified E3-001 or E3-002 tasks.
Follow E3-003's objective, acceptance criteria, required tests, lifecycle, and prohibitions exactly. In particular, do not run a model/system or benchmark, make a provider or paid call, access credentials, assign a model role, create an eligibility result, begin E3-004, alter accepted E2/ADR semantics, write application code, resume S1-003, mark `AUTONOMY_ELIGIBLE`, or authorize autonomous build.
```

## Repository principles

- Evidence before architecture
- One reliable persistent agent before visible multi-agent teams
- External-state verification before claims of completion
- Hard authorization controls instead of relying only on model judgment
- Model providers remain replaceable
- Repository files, not chat memory, preserve project state
- One author, one challenger, one verifier for consequential work
- Small vertical slices before platform breadth
- No fabricated customer evidence, benchmark results, or product observations

## Main input package

The prepared founder materials are in:

```text
00_inbox/prepared_materials/
```

Actual unmodified screenshots, recordings, transcripts, customer notes, papers, and prior code should be placed in:

```text
00_inbox/uploaded_originals/
```

Do not overwrite original evidence. Add derived notes elsewhere and cite the original path.
