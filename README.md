# GorkBot Project Repository

> Working codename only. The final product name must be selected independently and must not imply affiliation with xAI, Cursor, or Grok.

This repository is the source of truth for designing and building a model-agnostic persistent-agent platform.

The long-term capability benchmark is clean-room functional parity with Grok Bot, followed by measurable improvement in areas such as model choice, verified completion, security isolation, cost governance, portability, and inspectable collaboration.

## Current status

- Active program: Engineering Preview
- Current phase: E1 product specification; E1-001 is ready and not started
- Engineering Preview task status: `E0-001`: `VERIFIED`; `E1-001`: `READY`; `E1-002`: `BACKLOG`; `E2-E5`: `NOT_STARTED`
- Startup/customer track: preserved and deferred by D-016; S1-003 was not executed
- Architecture: not selected
- Engineering Preview target: one local user and one persistent software-engineering agent working on real repositories with durable state, independent verification, and evidence bundles
- Customer wedge: not selected or validated; S1-001 and S1-002 remain verified research inputs
- Model roles: not locked; benchmarks have not run
- `AUTONOMY_ELIGIBLE`: `NOT_ELIGIBLE`
- `AUTONOMOUS_BUILD_AUTHORIZED`: `NO`; E3 verification would establish eligibility only, and a separate explicit founder decision is required to authorize autonomous build execution
- Code: no application implementation yet
- Public repository: yes, so never commit secrets, private customer data, access tokens, credentials, or confidential documents

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
MODE: PLAN_STAGE_E2

Read MASTER_OPERATING_PROMPT.md, AGENTS.md, PROJECT_STATE.yaml, TASK_REGISTRY.yaml, and every E1-001 files_to_read entry.
Treat the repository as the sole authoritative project state.
Author only the Engineering Preview v0.1 product and correctness specification within E1-001's allowed paths; mark E1-001 READY_FOR_REVIEW, not VERIFIED, and create a factual handoff.
Do not select architecture, execute E2/E3 work, run paid APIs or benchmarks, write application code, resume S1-003, or authorize autonomous build mode.
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
