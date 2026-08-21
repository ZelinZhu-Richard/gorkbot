# GorkBot Project Repository

> Working codename only. The final product name must be selected independently and must not imply affiliation with xAI, Cursor, or Grok.

This repository is the source of truth for designing and building a model-agnostic SaaS platform for persistent AI teammates.

The long-term capability benchmark is clean-room functional parity with Grok Bot, followed by measurable improvement in areas such as model choice, verified completion, security isolation, cost governance, portability, and inspectable collaboration.

## Current status

- Stage: 0, founder inputs and research foundation
- Architecture: not selected
- MVP: not selected
- Customer wedge: provisional, not validated
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

The first command for the planning model is:

```text
MODE: INITIALIZE

Read MASTER_OPERATING_PROMPT.md, AGENTS.md, the governance files, and every file in 00_inbox/prepared_materials.
Treat the repository as the sole authoritative project state.
Perform Stage 0 initialization and execute only tasks marked READY in TASK_REGISTRY.yaml.
Do not begin application implementation.
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
