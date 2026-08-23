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

## D-010: Initial Stage 0 author runtime

- Date: 2026-08-21
- Status: CONFIRMED
- Decision type: EXECUTION_PROVENANCE
- Founder confirmation: The original `MODE: INITIALIZE` author pass for Stage 0 was executed in Codex, not directly in the ChatGPT interface using GPT-5.6 Sol.

Consequence:
- Stage 0 provenance should identify the author runtime as Codex.
- Any more specific underlying model identifier should remain unknown unless it was explicitly exposed by the Codex runtime.
- Do not retroactively label the author as GPT-5.6 Sol without evidence.

## D-011: S1-001 provisional discovery beachhead

- Date: 2026-08-23
- Status: PROVISIONAL
- Decision: Test first with a founder, head of product, or product-marketing lead at a 3–30 person B2B SaaS company that tracks 5–15 named competitors without a dedicated competitive-intelligence analyst. The narrow job is a verification-first weekly ledger of material official-source product, pricing, documentation, and changelog changes, with an approval-gated master-record update. Keep the small-software-team GitHub issue-to-reviewed-PR workflow as the explicit counter-hypothesis.
- Scoring context: H2 scored `76.8/100` and H1 scored `75.6/100`; the author treats the 1.2-point gap as a directional tie because one level on a weight-6 criterion changes the total by 1.2 points. H1 receives the first discovery slot based on lower-sensitivity initial inputs and founder-stated reach, neither of which is customer evidence.
- Primary differentiation hypothesis: test verified before/after delta evidence, explicit unknown states, approval, and external-state readback. Citations alone are not differentiated, and model transparency is not assumed to be a purchasing driver.
- Evidence required: the predeclared problem, delegation/differentiation, commitment/payment, and prototype-feasibility gates in `03_product/S1-001_CUSTOMER_WORKFLOW_SCORECARD.md`.
- Reversal rule: reopen this decision if any H1 problem gate fails, current alternatives are satisfactory without a material gap, the paid-pilot gate fails, authenticated/private sources are required for the first valuable version, or H2 produces stronger artifact, pilot, or payment evidence.
- Non-decision: D-006 and D-007 remain provisional. No final segment, workflow, pricing, architecture, model/provider role, benchmark, application implementation, market demand, or traction is confirmed.

## D-012: Stage 1 discovery allocation after S1-001 challenger review

- Date: 2026-08-23
- Status: CONFIRMED
- Decision type: FOUNDER_DISCOVERY_ALLOCATION
- Supersedes: D-011 only with respect to provisional discovery prioritization.

### Decision

H1 and H2 will proceed as co-equal discovery candidates.

Neither H1 nor H2 is selected as the final beachhead customer/workflow.

H1:
Verification-first competitor-change workflow for small B2B SaaS teams.

H2:
Verification-first software-engineering workflow centered on independently verified completion evidence around issue-to-PR work.

H8:
The challenger-added independent PR reproduce-and-verify hypothesis should be formally scored and evaluated during the S1-001 fix, but is not yet elevated to co-equal discovery status.

### Rationale

The S1-001 challenger found that:

1. H2 scored slightly above H1 in the original model.
2. The H1/H2 ranking is highly sensitive to small scoring changes.
3. H1's original differentiation was weakened by current SMB competitive-monitoring products.
4. H1's original preference was partly driven by feasibility and founder-access assumptions already represented in the score.
5. H2's issue-to-PR market is also highly competitive, but independently verified completion evidence remains an unresolved potential differentiator.
6. There is currently zero direct customer evidence for either hypothesis.

Therefore the evidence is insufficient to privilege either H1 or H2 before customer discovery.

### Consequences

- S1-001 must not portray H1 as the sole provisional beachhead.
- The scoring model must be corrected and sensitivity made explicit.
- H1 and H2 must receive comparable discovery effort and falsification criteria.
- Customer evidence, not founder preference or small score differences, should determine which survives.
- D-006 and D-007 remain PROVISIONAL.
- No final customer, MVP workflow, pricing, architecture, or model role is selected.

## Stage 0 author reconciliation note — 2026-08-21

This note records scope, not a new decision:

- Provenance: written in the initial Stage 0 author batch under S0-001's `DECISION_LOG.md` allowance on behalf of the S0-002 and S0-003 research outcomes; attribution was clarified during F-S0-001-02 remediation. It changed no D-00x status.

- Current primary-source research does not change D-001 through D-005.
- D-006, D-007, and D-008 remain provisional founder hypotheses. No customer evidence was added by Stage 0.
- The reference product's documented shared-computer boundary is evidence about Grok Bot, not a selected architecture for this project.
- No final architecture, MVP workflow, customer wedge, or model-role assignment was selected.
