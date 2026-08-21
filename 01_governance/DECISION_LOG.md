# Decision Log

## Decision status

- CONFIRMED: explicitly decided by the founder
- PROVISIONAL: working choice pending evidence
- DEFERRED: intentionally postponed
- REJECTED: considered and not selected

## D-001: Build toward a multi-tenant SaaS

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: The long-term target is a SaaS product other people can use.
- Consequence: tenant, authorization, billing, audit, and data-boundary concerns must remain architecturally possible even if not built in the first prototype.

## D-002: Use Grok Bot as a clean-room capability benchmark

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: Target functional parity or better without copying branding, proprietary implementation, or exact assets.
- Consequence: maintain a sourced parity matrix and independent product identity.

## D-003: Begin with one extremely capable persistent agent

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: Build core persistence, execution, approvals, observability, artifacts, and verification before visible agent teams.
- Consequence: group chat, many agents, skills, and routines are later stages.

## D-004: Support multiple model providers

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: GPT, Claude, DeepSeek, and future models should be replaceable through a model abstraction and routing layer.
- Consequence: no provider-specific behavior may define core task state, memory, approvals, or authorization.

## D-005: Use repository files as shared model state

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: GPT, Claude, and execution models coordinate through versioned files and task records.
- Consequence: chat memory and verbal summaries are non-authoritative.

## D-006: Initial beachhead customer

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: Begin discovery with technical founders and small startup teams while comparing research and engineering workflows.
- Evidence required: interviews, pilot willingness, workflow access, measurable pain, and technical feasibility.

## D-007: Primary differentiation

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: Test verified completion and model-transparent orchestration as the primary wedge, with stronger isolation as a secondary advantage.
- Evidence required: customer value, technical performance, cost, and competitive comparison.

## D-008: First client surface

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: A web control plane may precede native desktop and mobile applications.
- Evidence required: whether the first workflow requires local takeover, deep OS integration, or mobile supervision.

## D-009: S0-003 out-of-scope file modification

- Date: 2026-08-21
- Status: CONFIRMED
- Decision type: PROCESS_EXCEPTION
- Founder decision: Do not retroactively modify S0-003's `allowed_files_to_change`.

S0-003 modified governance files outside its originally authorized file scope. The modifications were relevant to the task, but the process deviation should remain visible rather than being erased by retroactively broadening the task definition.

The existing changes are accepted as a one-time documented exception.

Going forward:

1. A task must not modify files outside `allowed_files_to_change`.
2. If additional files become necessary, the task scope must be amended before modifying them.
3. The reason for the scope amendment must be recorded.
4. Reviewers should flag unauthorized changes even when the content itself is correct.

## Stage 0 author reconciliation note — 2026-08-21

This note records scope, not a new decision:

- Current primary-source research does not change D-001 through D-005.
- D-006, D-007, and D-008 remain provisional founder hypotheses. No customer evidence was added by Stage 0.
- The reference product's documented shared-computer boundary is evidence about Grok Bot, not a selected architecture for this project.
- No final architecture, MVP workflow, customer wedge, or model-role assignment was selected.
