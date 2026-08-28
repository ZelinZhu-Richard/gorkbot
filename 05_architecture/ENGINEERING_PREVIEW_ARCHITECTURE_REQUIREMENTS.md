# Engineering Preview Architecture Requirements

Status: **E2-001 AUTHOR BASELINE — READY_FOR_REVIEW; NOT VERIFIED**

Baseline version: `EP-ARCH-REQ-0.1`

Frozen E1 input: independently VERIFIED / `E1_GATE_PASSED`

Architecture selection: **NOT_SELECTED**

Accepted ADRs: **0**

Base commit: `0338c615c7098a7c7e7afd1f09ff44be9db94109`

## 1. Purpose and authority

This document answers one question: **what properties must every acceptable Engineering Preview architecture possess, independent of implementation technology?** It is the decision contract for E2-002 and later E2 work. It does not generate a candidate, choose a mechanism, assign a provider/model, score an alternative, create an ADR, or authorize E3 or implementation.

The frozen E1 source set was mechanically re-extracted as 127 canonical IDs:

| Family | Count | Canonical source |
|---|---:|---|
| Functional requirements (`FR`) | 56 | PRD §7 |
| Reliability hard invariants (`RR`) | 15 | Correctness contract §14.1; mirrored in PRD §10 |
| Future compatibility (`FC`) | 9 | PRD §12 |
| Preview SLOs (`SLO`) | 4 | Correctness contract §14.2 |
| Measure-only metrics (`MET`) | 4 | Correctness contract §14.2 |
| User flows (`UF`) | 16 | User flows §§3–18 |
| Security-negative families (`NEG`) | 23 | Correctness contract §15 |
| **Total** | **127** | Exact set in the companion traceability CSV |

Primary architecture dispositions are **119 `HARD_CONSTRAINT`**, **0 `WEIGHTED_PREFERENCE`**, and **8 `JUSTIFIED_NON_ARCHITECTURE_DRIVING`**. The eight SLO/MET outcomes are empirical rather than structural candidate truths; their measurement seams are still mandatory through `AR-TST-003` and `AR-PERF-002`. This is not a waiver. The six weighted architecture preferences in §8 are secondary comparison criteria derived from E1 concerns; they do not replace any canonical E1 requirement's hard or empirical disposition.

The companion [traceability CSV](ENGINEERING_PREVIEW_E1_ARCHITECTURE_TRACEABILITY.csv) is normative for the one-primary-disposition mapping. If a future edit changes the frozen E1 set or semantics, it requires a prospective E1 amendment and independent reverification before this baseline may be regenerated.

## 2. Decision-class semantics

| Class | Meaning | Selection consequence | Evidence rule |
|---|---|---|---|
| `HARD_CONSTRAINT` | A semantic, security, recovery, evidence, compatibility-floor, or testability property every candidate must satisfy. | Any demonstrated failure rejects the candidate. No score or preference compensates. | Candidate supplies direct design evidence and a credible compliance path; unresolved hard compliance is not a pass. |
| `WEIGHTED_PREFERENCE` | A comparative quality attribute applied only after hard compliance. | May distinguish hard-pass candidates under prospectively frozen governance. | No candidate-specific score or winner exists in E2-001. |
| `UNKNOWN_REQUIRING_SPIKE` | A selection-relevant feasibility fact that cannot be resolved on paper after E2-002 describes mechanisms. | Receives no favorable, zero, midpoint, or assumed-pass score; blocks selection until E2-004 closes it or the candidate is rejected. | E2-003 classifies; E2-004 alone may execute a bounded preselection spike. No such spike is declared or run here. |
| `E3_VALIDATION_OBLIGATION` | A postselection empirical validation that can test a selected mechanism without redefining architecture truth. | Carries an owner, evidence contract, failure/reversal condition, and ADR linkage into E3. It cannot defer an architecture-blocking unknown. | Obligations are registered in §9; no E3 work is authorized here. |
| `JUSTIFIED_NON_ARCHITECTURE_DRIVING` | A frozen requirement whose observed value/result is empirical or product-operation evidence rather than an architecture property. | It is not scored as structural compliance, but its instrumentation/test seam may be a hard architecture requirement. | Exact justification and supporting AR/E3 obligation appear in the trace CSV. |

Hard constraints are evaluated before preferences. `UNKNOWN`, missing evidence, unsupported condition, or incompatible semantics never count as hard-pass. A user/founder approval may authorize an allowed effect but may not waive a hard architecture constraint.

## 3. Authoritative state and completion model

The logical architecture must preserve these semantic classes even if a candidate colocates their physical storage:

| Semantic class | Required contents | Authority |
|---|---|---|
| **AUTHORITATIVE STATE** | Task/agent/attempt identity and contract; conversation/message authority; plan and predicates; task/control/reconciliation/wait/blocker/disposition axes; operation/effect state; approvals; model-route provenance; artifact/evidence identity; verification runs/verdict; causal history and integrity state. | May authorize transitions and contribute to completion only after validation under current ownership/version. |
| **DERIVED PROJECTION** | UI status, activity views, searchable indexes, rendered transcript, aggregate dashboards, cached read models. | Rebuildable; never grants authority or proves completion. |
| **EPHEMERAL WORKING CONTEXT** | In-memory caches, live process/session state, transient model prompt assembly, local scheduling hints. | Replaceable; loss may affect latency but cannot destroy authoritative truth. |
| **LOSSY SUMMARY** | Compacted context or concise resume block. | Derived, source/version/trust-bound, invalidatable, and never a substitute for approvals, evidence, security policy, or completion predicates. |

A completed disposition is valid only when every required E1 conjunct is true on the exact current candidate/revision: admitted current authority; adequate predicate set; all applicable predicates satisfied; valid profile-complete evidence; every material operation terminal and accounted; required effects freshly read back as known succeeded; no material unknown effect; no active wait/control/reconciliation/blocker/pending approval or event; and a current eligible independent `PASSED` verification. Partial output, executor narration, a killed process, a previous revision's pass, or a weighted score cannot satisfy this conjunction.

## 4. Architecture requirement register

Field meanings are literal: **class** and **hard constraint** govern candidate admissibility; **source E1 IDs** are normative sources; **description** is the requirement; **rationale** explains why it drives architecture; **domains** resolve through §7; **required observable property** is future evidence; **prohibited architectural outcome** is a fail condition; **evaluation linkage** points to the frozen suite; **E3 obligation** resolves through §9; **future compatibility** is bounded; **uncertainty** preserves unknown mechanisms; and **provenance** enforces Level A/B/C discipline.

### AR-COR-001 — Stable durable identities

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-001`, `FR-002`, `UF-01`, `UF-08`, `FC-001`
- **Description:** Agent, task, attempt, operation, workspace, artifact, approval, effect, and verification identities must be explicit, stable, and distinct from process, model-session, client-window, and machine-path identity.
- **Rationale:** Recovery, exact ownership, deduplication, and later remote execution are impossible if identity is incidental to a live process.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D04_DURABLE_STATE_PERSISTENCE`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`
- **Required observable property:** A task acknowledged before interruption is reread under the same task identity while replacement process/session identities are separately visible.
- **Prohibited architectural outcome:** Identity reuse, identity loss after acknowledgement, or treating a process/session/window/path as the task or agent.
- **Evaluation linkage:** EP-WF-006; EP-CTL-014..024; EP-NEG-FUTURE-01.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Identity contracts remain usable by remote workers, multiple clients, and concurrent agents without implementing those features now.
- **Uncertainty:** Identity serialization and storage mechanism are E2 candidate decisions.
- **Provenance:** Level A property re-derived from frozen E1; external lifecycle patterns are corroboration only.

### AR-COR-002 — Versioned admitted task contract and plan

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-003`, `FR-005`, `FR-006`, `FR-037`, `UF-01`, `UF-06`
- **Description:** The admitted request, authority, scope, exclusions, limits, predicate inventory, plan, and redirects must be versioned authoritative records with explicit supersession and causal linkage.
- **Rationale:** A model narration or overwritten plan cannot prove which work was authorized or which predicates govern completion.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`, `D11_APPROVAL_PERMISSION_SYSTEM`
- **Required observable property:** Every material operation points to the current admitted task/plan version; prior versions and redirect causes remain inspectable.
- **Prohibited architectural outcome:** Silent scope growth, destructive overwrite of authority, or execution under a superseded plan.
- **Evaluation linkage:** EP-WF-001..003; EP-CTL-007..013; EP-NEG-AUTH-01.
- **E3 validation obligation:** `NONE`
- **Future compatibility impact:** Versioned contracts permit later clients and workers to reconstruct authority without sharing one memory image.
- **Uncertainty:** The physical record representation is unselected.
- **Provenance:** Level A property from frozen E1.

### AR-COR-003 — Orthogonal canonical state semantics

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-007`, `FR-060`, `RR-008`, `UF-15`
- **Description:** Task phase, control, reconciliation, wait reasons, blockers, attempt disposition, verification state, operation/effect state, and agent availability must remain separate authoritative concepts with explicit legal and invalid combinations.
- **Rationale:** Collapsing independent axes creates false completion and erases concurrent pause, recovery, blocker, verification, or effect facts.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D03_TASK_WORKFLOW_ORCHESTRATION`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** All required legal tuples reconstruct exactly and invalid tuples are rejected; any primary display label is a derived projection.
- **Prohibited architectural outcome:** One fused status scalar as authority, model prose setting state, or client disconnect changing execution truth.
- **Evaluation linkage:** EP-CTL-001..024; state-combination map; EP-FALSE-021.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Separate state components remain serializable across future client and worker boundaries.
- **Uncertainty:** Projection and persistence mechanisms are unselected.
- **Provenance:** Level A property; explicit task/execution state is required, while any particular state-machine implementation is Level B.

### AR-COR-004 — Non-compensating completion gate

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-065`, `FR-066`, `RR-008`
- **Description:** Completion must be a derived conjunction over exact current authority, adequate and satisfied predicates, valid evidence, terminal/accounted operations, resolved effects, absence of active control/recovery/waits/blockers, and an eligible independent PASS on the exact revision.
- **Rationale:** No score, model assertion, useful partial output, or human preference can compensate for a false completion conjunct.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** A false conjunct deterministically prevents authoritative COMPLETED; rejected claims and escaped false-terminal completion remain distinct records.
- **Prohibited architectural outcome:** Weighted completion, executor self-certification, or completion with an unknown effect, stale pass, missing check, pending approval, or active recovery.
- **Evaluation linkage:** EP-FALSE-001..021; all nine adequacy variants; release non-compensating blockers.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** The gate is a provider- and deployment-neutral product invariant.
- **Uncertainty:** None at the semantic level.
- **Provenance:** Level A property from the E1 completion contract.

### AR-COR-005 — Predicate adequacy and truthful noncompletion

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-025`, `FR-065`, `FR-067`, `RR-009`, `UF-03`, `UF-15`
- **Description:** Every material request, task-class, governing, scope, security, and correctness obligation must map to an objective predicate or justified NOT_APPLICABLE record; missing, weak, irrelevant, skipped, flaky, failed, or unverifiable predicates yield truthful noncompletion.
- **Rationale:** Passing a conveniently narrow check set is not proof that the requested behavior exists.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** A coverage map identifies each obligation, oracle, evidence, gap, and consequence; partial, blocked, failed, cancelled, and unverified outcomes stay distinct.
- **Prohibited architectural outcome:** Weak-oracle completion, silently dropped predicates, or verifier infrastructure error treated as a pass or implementation failure.
- **Evaluation linkage:** VER-ADQ-01..09; EP-FALSE-001..013; EP-WF-005; EP-NEG-VER-02.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Objective predicates remain portable across providers and deployment shapes.
- **Uncertainty:** Irreducible judgment criteria must remain bounded and cannot override deterministic ground truth.
- **Provenance:** Level A property from E1; no hidden chain-of-thought is required.

### AR-COR-006 — Exact state and revision binding

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-015`, `FR-065`, `NEG-VER-02`, `UF-06`, `UF-14`
- **Description:** Checks, artifacts, evidence, approvals where state-sensitive, and verification verdicts must bind to the exact authoritative candidate/base/revision and become stale or invalid when a material bound fact changes.
- **Rationale:** A pass for an old candidate cannot establish correctness of a mutated one.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`, `D10_GIT_INTEGRATION`, `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`
- **Required observable property:** Post-verification mutation preserves the old run for history but makes the current aggregate UNVERIFIED until the new state is verified.
- **Prohibited architectural outcome:** Floating evidence references, stale approval/check/verdict reuse, or mutation hidden behind an unchanged display label.
- **Evaluation linkage:** EP-FALSE-007/014; EP-EVID-003; EP-NEG-VER-02; COMP-04/11.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Stable version binding supports later distributed readback without requiring distributed implementation now.
- **Uncertainty:** Revision identity mechanism is unselected.
- **Provenance:** Level A property.

### AR-COR-007 — Single accountable ownership and stale-writer rejection

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-008`, `RR-004`, `FC-002`, `NEG-RACE-01`
- **Description:** Every authoritative mutation and dispatch must carry current accountable ownership/version; stale, duplicate, or superseded writers must be rejected and their attempts accounted for.
- **Rationale:** Concurrent or replacement workers otherwise can corrupt state or duplicate effects.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D04_DURABLE_STATE_PERSISTENCE`, `D06_EVENT_OPERATION_HISTORY`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`
- **Required observable property:** A two-owner or restart race admits one legal persisted outcome and exposes rejected stale activity.
- **Prohibited architectural outcome:** Silent multi-owner mutation, last-write-wins without authority, or stale projection influencing newer authority.
- **Evaluation linkage:** EP-WF-007; EP-CTL-015/023; EP-NEG-RACE-01; EP-NEG-FUTURE-01.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Provides a minimum future multi-writer seam without implementing multi-writer coordination.
- **Uncertainty:** Ownership-transfer protocol is candidate-owned.
- **Provenance:** Level A property; compare-and-swap or journal patterns remain Level B.

### AR-DUR-001 — Acknowledged authoritative durability

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-002`, `FR-030`, `RR-001`
- **Description:** Acknowledgement of any authority, task, message, plan, control, approval, effect, artifact, evidence, or verification mutation required for recovery may occur only after the declared supported local persistence boundary can recover exactly that mutation.
- **Rationale:** An acknowledgement that can disappear fabricates durable continuity.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D04_DURABLE_STATE_PERSISTENCE`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`
- **Required observable property:** Crash immediately after acknowledgement recovers exactly one valid mutation with no acknowledged-record loss.
- **Prohibited architectural outcome:** Acknowledge-before-durable-record, best-effort recovery presented as exact, or lossy compaction of authority.
- **Evaluation linkage:** EP-WF-006; EP-CTL-014..018; RR-001 protocol coverage.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** The supported local boundary must be explicit so later machine/remote durability can extend rather than silently reinterpret it.
- **Uncertainty:** Media, commit grouping, and physical persistence mechanism are unselected.
- **Provenance:** Level A property.

### AR-DUR-002 — Restart recovery and reconciliation ownership

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-031`, `RR-002`, `UF-07`, `UF-08`
- **Description:** Supported client, orchestrator, worker, executor, verifier, and machine interruptions must have distinct recovery semantics; every affected nonterminal task resumes from the latest valid acknowledged state or enters an explicit recovering, blocked, failed, or uncertain condition.
- **Rationale:** Restart must not guess continuity or confuse presentation loss with execution loss.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D04_DURABLE_STATE_PERSISTENCE`, `D06_EVENT_OPERATION_HISTORY`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Recovery records interruption class, recovered authority, owner transition, reconciliation work, and final truthful state.
- **Prohibited architectural outcome:** Fabricated resume, silent regression, duplicate ownership, or client reconnect terminating healthy work.
- **Evaluation linkage:** EP-CTL-014..024; EP-WF-006..008; SLO-003 protocol.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Recovery contracts cannot assume one permanent process or client.
- **Uncertainty:** Supported interruption boundary and implementation mechanism are candidate declarations.
- **Provenance:** Level A property; cloud-worker lifecycle designs are Level B only.

### AR-DUR-003 — Idempotent operation accounting and uncertain effects

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-032`, `RR-003`, `NEG-RACE-01`, `NEG-EXT-01`
- **Description:** Every operation/effect request, dispatch attempt, receipt, readback, retry, and reconciliation must have stable identity and declared idempotency; acknowledgement loss or ambiguous dispatch must remain OUTCOME_UNCERTAIN until authoritative readback resolves it.
- **Rationale:** Guessing failure after a lost response creates duplicate consequential effects.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D08_EXECUTION_PROCESS_CONTROL`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Crash-around-effect produces one confirmed effect, known no-start, known failure, or explicit uncertainty, with no blind retry.
- **Prohibited architectural outcome:** Assuming success or failure from missing acknowledgement, reusing identity ambiguously, or unrecorded duplicate effects.
- **Evaluation linkage:** EP-CTL-019/023; EP-FALSE-015; EP-NEG-EXT-01; COMP-02/10.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Stable identities and readback contracts support later remote effect executors.
- **Uncertainty:** Per-capability idempotency/readback mechanisms are E2/E3 declarations.
- **Provenance:** Level A property; an operation journal is a Level B pattern.

### AR-DUR-004 — Durable ordered control and bounded interruption

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-033`, `RR-005`, `RR-006`, `UF-04`, `UF-05`, `UF-06`, `UF-07`
- **Description:** Pause, stop, force-stop/fence, redirect, and resume must be durable ordered commands with separate request, acknowledgement, effectiveness, reconciliation, and final times; productive work stops under superseded authority and interruption closes within declared finite bounds.
- **Rationale:** Process death is not rollback, effect reconciliation, or task completion.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D08_EXECUTION_PROCESS_CONTROL`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D18_OBSERVABILITY_LOGGING`
- **Required observable property:** Control races have one recorded winner; descendants terminate or lose authority; unresolved effects are explicit; stop closes CANCELLED, never COMPLETED.
- **Prohibited architectural outcome:** Unbounded STOPPING, post-control productive dispatch, untrusted non-interruptibility, or kill-as-success.
- **Evaluation linkage:** EP-CTL-001..013; EP-FALSE-011; COMP-03/14; SLO-002 protocol.
- **E3 validation obligation:** `E3V-002`
- **Future compatibility impact:** Control contracts must cross a future worker boundary without assuming in-process cancellation.
- **Uncertainty:** Force/fence mechanisms and supported host behavior require candidate declaration and E3 validation.
- **Provenance:** Level A property.

### AR-DUR-005 — Corruption, partial-write, and evolution safety

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-014`, `FR-035`, `FC-008`
- **Description:** Durable records and file updates must be versioned and either complete or detectably interrupted; incompatible, corrupt, incomplete, or unknown data must fail or migrate visibly while preserving original evidence.
- **Rationale:** Silent repair or overwrite destroys recovery truth and migration reversibility.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D04_DURABLE_STATE_PERSISTENCE`, `D06_EVENT_OPERATION_HISTORY`, `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Fault injection yields a valid old/new state or an explicit recoverable/blocked/failed state with the original bytes/evidence retained.
- **Prohibited architectural outcome:** Silent acceptance, silent downgrade, partial state treated as current, or destructive migration.
- **Evaluation linkage:** EP-CTL-024; FIX-RECOVERY-001; repository interrupted-write variants.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Explicit versions and visible migration allow schema/event evolution.
- **Uncertainty:** Atomicity, integrity, and migration mechanisms are candidate-owned.
- **Provenance:** Level A property; content addressing is not required.

### AR-DUR-006 — Retention, hold, cleanup, and deletion accountability

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-048`, `RR-012`, `NEG-CLEAN-01`
- **Description:** Every state, evidence, artifact, workspace, credential, and process class must have explicit retention and cleanup ownership; holds prevent conflicting cleanup, and cleanup/deletion requires scoped reread or explicit uncertainty while historical activity remains accountable.
- **Rationale:** Cleanup is a consequential operation that can destroy user state or verification evidence.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D04_DURABLE_STATE_PERSISTENCE`, `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Cleanup affects only proven task-owned targets, retains required evidence, records logical versus physical deletion claims, and reconciles leftovers.
- **Prohibited architectural outcome:** Cleanup by path assumption, link-following deletion, erasing history, or unsupported erasure claims.
- **Evaluation linkage:** EP-NEG-CLEAN-01; retention/hold/deletion evidence rules; COMP-14.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Retention contracts can later accept tenant/principal scopes without claiming multi-tenancy now.
- **Uncertainty:** Retention periods and physical erasure capabilities are not selected.
- **Provenance:** Level A property.

### AR-DAT-001 — Authoritative, derived, ephemeral, and lossy-state separation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-007`, `FR-036`, `FR-062`, `NEG-CTX-01`
- **Description:** The architecture must label and enforce distinct classes for authoritative domain state, derived projections, ephemeral working context, and lossy summaries; only authoritative state can grant authority or establish completion.
- **Rationale:** A UI projection, cache, transcript rendering, telemetry stream, or summary cannot safely become accidental authority.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`, `D15_CONTEXT_MEMORY_COMPACTION`, `D18_OBSERVABILITY_LOGGING`
- **Required observable property:** Every projection/summary identifies source versions and can be discarded/rebuilt without loss of authority or evidence.
- **Prohibited architectural outcome:** Projection-as-authority, cache-only durable facts, or summary promotion of untrusted/stale text.
- **Evaluation linkage:** EP-NEG-CTX-01; EP-NEG-AUDIT-01; reconnect and recovery cases.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Replaceable projections support additional clients without multiplying sources of truth.
- **Uncertainty:** Storage colocation is allowed; semantic authority separation is mandatory.
- **Provenance:** Level A property; derived transcript projection is a Level B pattern.

### AR-DAT-002 — Versioned causal history and integrity state

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-003`, `FR-044`, `FR-062`, `RR-014`, `NEG-AUDIT-01`
- **Description:** Material authority, denial, approval/revocation, operation/effect/readback, secret-boundary, recovery, artifact, check, and verification history must preserve ordering, correlation, version, actor, and integrity/gap/tamper state.
- **Rationale:** Current snapshots alone cannot establish why an effect occurred or whether evidence was substituted.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Drops, duplicates, reorderings, substitutions, or unexplained gaps are detected/accounted and block affected verification/completion.
- **Prohibited architectural outcome:** Reconstructing authority from telemetry, digest-only correctness claims, or silently rewriting history.
- **Evaluation linkage:** EP-NEG-AUDIT-01; EP-NEG-EVID-01; evidence validation rules.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Causal identities and versions permit later ordering/conflict designs.
- **Uncertainty:** Append structure, hashing, signing, and storage topology are unselected.
- **Provenance:** Level A property; journal and hash-chain patterns are Level B.

### AR-CTX-001 — Durable conversation continuity outside model context

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-036`, `FR-060`, `RR-012`, `UF-13`
- **Description:** Original requests, admitted messages, corrections, authority changes, decisions, evidence references, and task state needed to resume must persist outside any bounded model invocation context.
- **Rationale:** An invocation context is finite and replaceable; it cannot be the only record of work or authority.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D15_CONTEXT_MEMORY_COMPACTION`
- **Required observable property:** A resumed invocation reconstructs a bounded context manifest from durable records and identifies omitted material without losing task truth.
- **Prohibited architectural outcome:** Conversation/session memory as sole authority or restart requiring private hidden reasoning.
- **Evaluation linkage:** EP-NEG-CTX-01; restart/reconnect cases; evidence profile validation.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Supports later clients and workers consuming the same logical contract.
- **Uncertainty:** Retrieval/indexing mechanism is unselected.
- **Provenance:** Level A property.

### AR-CTX-002 — Provenanced compaction and summary invalidation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-036`, `RR-004`, `NEG-CTX-01`, `UF-13`
- **Description:** Compaction may affect only derived working context; every summary must retain source/version/trust provenance, be invalidated or recomputed when governing inputs change, and never omit or supersede approval, revocation, policy, security, evidence, or completion facts.
- **Rationale:** Lossy summaries can otherwise amplify prompt injection or preserve stale authority.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D15_CONTEXT_MEMORY_COMPACTION`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** A malicious or stale summary is discarded, and authoritative facts omitted from it remain recoverable.
- **Prohibited architectural outcome:** Summary-derived grants, destructive compaction, or context reduction deleting authoritative evidence.
- **Evaluation linkage:** EP-NEG-CTX-01; long-context/restart variants.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Summary contracts can cross provider/context limits without coupling truth to one context window.
- **Uncertainty:** Summary format and retrieval method are unselected.
- **Provenance:** Level A property; context-summary blocks are Level B.

### AR-WSP-001 — Read-only repository admission and condition disposition

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-009`, `FR-010`, `UF-01`
- **Description:** Before untrusted content or mutating work, the architecture must bind repository identity and base state under a minimal read grant, enumerate every applicable one of the sixteen repository-condition families, compose constraints, and fail closed on rejected or unresolved unknown conditions.
- **Rationale:** Workspace and safety decisions require a trusted base and explicit repository-condition truth.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D09_ISOLATION_SANDBOXING`, `D10_GIT_INTEGRATION`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Preflight independently rereads identity, revision, topology, tracked/untracked/ignored/generated and extension facts before mutation.
- **Prohibited architectural outcome:** Mutation before admission, unknown condition treated as supported, or repository text granting admission authority.
- **Evaluation linkage:** EP-REPO-001..016; EP-WF-019; RC-01..16.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Repository-condition contracts remain explicit for future remote workers.
- **Uncertainty:** Admission implementation and supported-condition subset are candidate declarations.
- **Provenance:** Level A property.

### AR-WSP-002 — Isolation-before-mutation and task/workspace binding

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-012`, `RR-007`, `UF-02`
- **Description:** After read-only base capture and before any potentially mutating reproduction, dependency hook, diagnosis command, test/build action, or edit, a task-identified isolated workspace or semantically equivalent non-interference boundary must be established and durably bound.
- **Rationale:** Reproduction itself can mutate or execute untrusted code and cannot safely run in original user state by default.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D08_EXECUTION_PROCESS_CONTROL`, `D09_ISOLATION_SANDBOXING`, `D10_GIT_INTEGRATION`
- **Required observable property:** Ordering evidence proves bind-before-dispatch and a separable task diff with original user state unchanged.
- **Prohibited architectural outcome:** Potentially mutating work in the original checkout without explicit product rule plus authenticated authority.
- **Evaluation linkage:** EP-WF-004/009/019; ORDER-PREMATURE-MUTATING-REPRODUCTION; EP-NEG-DESTRUCT-01.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Workspace identity prevents future tasks/agents from corrupting one another.
- **Uncertainty:** No workspace, container, copy, or virtualization mechanism is selected.
- **Provenance:** Level A property.

### AR-WSP-003 — Filesystem confinement and adversarial path handling

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-013`, `FR-014`, `RR-015`, `NEG-FS-01`
- **Description:** Every read, write, execution, archive, and cleanup target must be normalized and authorized under roots with defenses for aliases, traversal, symlink/hard-link/swap, special files, mounts, archives, size expansion, and topology changes.
- **Rationale:** A nominal in-root path does not prove that the effective object or effect remains in scope.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D09_ISOLATION_SANDBOXING`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Canaries outside authorized roots remain byte-identical through adversarial path and cleanup races.
- **Prohibited architectural outcome:** Out-of-root read/write/delete, following changed topology without revalidation, or treating path strings as object identity.
- **Evaluation linkage:** EP-NEG-FS-01; EP-NEG-CLEAN-01; COMP-07.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Scope carries explicit owner/resource identity rather than a global path assumption.
- **Uncertainty:** Enforcement mechanism is unselected.
- **Provenance:** Level A property.

### AR-WSP-004 — Original user-state and dirty-material protection

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-011`, `FR-015`, `RR-007`, `NEG-DESTRUCT-01`
- **Description:** Tracked, untracked, ignored, generated, nested, linked-workspace, shared-ref, and ambiguous pre-existing material is user-owned; inclusion, exclusion, mutation, staging, commit, transport, and cleanup must be explicit and reconciled against initial/final state.
- **Rationale:** An allowed root does not make pre-existing user material task-owned.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D09_ISOLATION_SANDBOXING`, `D10_GIT_INTEGRATION`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Before/after byte/ref/index inventories show zero unrelated loss or silent mixing and identify all included/excluded/unavailable material.
- **Prohibited architectural outcome:** Discarding or silently incorporating dirty/untracked/ignored/generated/user state.
- **Evaluation linkage:** EP-REPO-002/003/016; EP-NEG-DESTRUCT-01; EP-GIT-006..020.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Explicit ownership avoids cross-task corruption.
- **Uncertainty:** Supported dirty-state policy remains a candidate declaration constrained by RC-01..16.
- **Provenance:** Level A property.

### AR-WSP-005 — Stale-workspace detection and scoped cleanup reconciliation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-048`, `FC-002`, `NEG-CLEAN-01`, `NEG-FUTURE-01`
- **Description:** Workspace identity, base authority, ownership, and cleanup scope must be revalidated after interruption or concurrent change; stale workspaces cannot dispatch or present current evidence, and cleanup must account for processes, temporary credentials, and artifacts.
- **Rationale:** A workspace may remain at a valid path while no longer representing current authority.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D09_ISOLATION_SANDBOXING`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`
- **Required observable property:** Changed identity/base/owner yields a stale or recovery state; cleanup rereads exact scope and leaves other tasks/users untouched.
- **Prohibited architectural outcome:** Path-only identity, stale workspace execution, or cleanup that crosses task ownership.
- **Evaluation linkage:** EP-NEG-CLEAN-01; EP-NEG-FUTURE-01; dirty-repository recovery COMP-05.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Required owner scoping supports concurrent tasks without implementing them in v0.1.
- **Uncertainty:** Cleanup and stale-detection mechanisms are unselected.
- **Provenance:** Level A property.

### AR-EXE-001 — Versioned capability contracts and boundary validation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-022`, `FR-040`, `FR-041`, `RR-011`, `NEG-SCHEMA-01`, `NEG-CMD-01`
- **Description:** Every capability/tool contract must have stable identity, version, owner, schemas, effect/reversibility/idempotency/network/credential/Git/approval classes, limits, and cancellation/settle semantics; every trust boundary validates size, type, enums, version, unknown fields, correlation, and adversarial inputs/results.
- **Rationale:** Text labels and cooperative model behavior cannot enforce executable authority.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D08_EXECUTION_PROCESS_CONTROL`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Invalid requests dispatch zero effects; invalid effectful results are not consumed and enter readback/reconciliation.
- **Prohibited architectural outcome:** Unknown contract execution, widening repair, command injection, or treating tool success prose as authority.
- **Evaluation linkage:** EP-NEG-SCHEMA-01; EP-NEG-CMD-01; EP-WF-011.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Versioned contracts provide the extension seam for future tools/connectors.
- **Uncertainty:** Schema and invocation technology are unselected.
- **Provenance:** Level A property.

### AR-EXE-002 — Declared operation lifecycle and bounded output

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-020`, `FR-021`, `RR-014`
- **Description:** Before launch, every command/action must declare task/workspace/working-directory binding, normalized operation, environment policy, bounds, cancellation class, expected effect, and authority; results preserve timing, exit/termination, bounded stdout/stderr or artifact references, timeout/cancel, and effect certainty.
- **Rationale:** An opaque terminal transcript cannot support recovery, policy, or verification.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D08_EXECUTION_PROCESS_CONTROL`, `D18_OBSERVABILITY_LOGGING`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Success, nonzero exit, timeout, cancellation, output truncation, lost response, and uncertain effect remain distinguishable and correlated.
- **Prohibited architectural outcome:** Launch without a validated operation record, unbounded output, or flattening termination into success prose.
- **Evaluation linkage:** EP-CTL-* operation cases; EP-WF-011; OR-CONTROL-TIMELINE/OR-RESOURCE-BOUND.
- **E3 validation obligation:** `E3V-002`
- **Future compatibility impact:** Operation contracts can be executed locally or remotely without changing product semantics.
- **Uncertainty:** Terminal/process adapter is unselected.
- **Provenance:** Level A property.

### AR-EXE-003 — Process-tree control, bounds, force termination, and fencing

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-033`, `FR-040`, `RR-006`, `NEG-TERM-01`
- **Description:** Execution authority and resource bounds must extend to descendants; cooperative cancellation, bounded settle, safe/available force termination or authority fencing, and post-interruption reconciliation must be structurally supported.
- **Rationale:** Stopping only a parent process leaves orphaned work and effects.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D08_EXECUTION_PROCESS_CONTROL`, `D09_ISOLATION_SANDBOXING`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** No productive descendant survives accepted stop authority; any unkillable work is fenced/accounted and effects are terminal or uncertain.
- **Prohibited architectural outcome:** Permanent non-interruptibility, orphan processes, uncontrolled descendants, or kill interpreted as rollback/completion.
- **Evaluation linkage:** EP-NEG-TERM-01; EP-CTL-005; COMP-14.
- **E3 validation obligation:** `E3V-002`
- **Future compatibility impact:** Fencing semantics permit future remote workers where local process kill is unavailable.
- **Uncertainty:** Host-specific process-tree and fencing support requires E3 validation.
- **Provenance:** Level A property.

### AR-EXE-004 — Untrusted execution-surface classification

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-027`, `FR-045`, `NEG-GIT-01`, `NEG-SUPPLY-01`, `NEG-NET-01`
- **Description:** Package scripts, build/test hooks, downloaded binaries, Git hooks/helpers/filters/signers/transports, and network-sensitive commands must be separately classified as executable/effectful capabilities; retrieval or repository declaration grants no execution, credential, network, or helper authority.
- **Rationale:** Nominal development commands can execute arbitrary untrusted code or egress data.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D08_EXECUTION_PROCESS_CONTROL`, `D10_GIT_INTEGRATION`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Unauthorized hooks/scripts/helpers/connections do not execute and their unmet preconditions or denials are recorded.
- **Prohibited architectural outcome:** Implicit execution through package/Git tooling or read permission implying egress.
- **Evaluation linkage:** EP-NEG-GIT-01; EP-NEG-SUPPLY-01/02; COMP-12/13.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** New capability types inherit explicit classification rather than ambient authority.
- **Uncertainty:** Enforcement adapter is unselected.
- **Provenance:** Level A property.

### AR-GIT-001 — Normative Git/effect classification enforcement

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-023`, `FR-024`, `NEG-GIT-01`
- **Description:** The architecture must represent and enforce the verified thirty-row Git/effect matrix, keeping primary effect class, v0.1 disposition, and approval rule independent and composing target/ownership sensitivity conservatively.
- **Rationale:** Git commands vary from read-only local inspection to destructive or remote consequential effects; one Git permission is unsafe.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D10_GIT_INTEGRATION`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Every Git action resolves to one matrix row; prohibited actions remain denied even with approval; supported remote effects require exact approval and readback.
- **Prohibited architectural outcome:** Unclassified Git actions, local authority implying remote/helper authority, or approval enabling PROHIBITED_V0_1.
- **Evaluation linkage:** EP-GIT-001..030; GE-01..30; EP-NEG-GIT-01.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Classification is independent of any Git invocation library or local/remote executor.
- **Uncertainty:** Invocation mechanism is unselected.
- **Provenance:** Level A property from verified E1 matrix.

### AR-GIT-002 — Git state binding and local review-package truth

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-015`, `FR-069`, `UF-10`, `NEG-EXT-01`
- **Description:** Repository/base/ref/revision and final diff state must be independently reread and bound to evidence; local patch/branch/commit/draft-package outputs must state exactly what occurred, and a draft package must remain explicitly NOT_SUBMITTED unless a separately authorized remote effect is confirmed.
- **Rationale:** A local review artifact is not a remote pull request, and cached command output is not authoritative Git state.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D10_GIT_INTEGRATION`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D21_LOCAL_FIRST_PACKAGING`
- **Required observable property:** Review package carries exact base/head or patch identity, changed-file inventory, checks, limitations, evidence, verification, approval/effect status, and fresh readback.
- **Prohibited architectural outcome:** Draft package presented as remote effect, stale ref evidence, or unauthorized additional Git actions.
- **Evaluation linkage:** EP-CONTRIB-*; EP-GIT-021..030; EP-NEG-EXT-01.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Review-package contract is portable across hosting services without selecting one.
- **Uncertainty:** The one or more review forms a candidate supports must be declared.
- **Provenance:** Level A property.

### AR-SEC-001 — Closed trust and authority precedence

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-004`, `FR-009`, `FC-004`, `NEG-AUTH-01`
- **Description:** Founder/project governance and authenticated user/task authority must be structurally distinguished from admitted narrowing instructions and untrusted repository, issue, document, model, tool, test, web, or connector content; untrusted content cannot grant, widen, override, approve, or prove.
- **Rationale:** Prompt injection is an architecture trust-boundary problem, not only a prompting problem.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D02_CORE_APPLICATION_RUNTIME`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Conflicts yield a typed denial, wait, or blocker under the higher authority with zero prohibited effect.
- **Prohibited architectural outcome:** LLM judgment as the sole authority boundary or repository/tool/model content granting capabilities.
- **Evaluation linkage:** EP-NEG-AUTH-01; EP-WF-003/019; COMP-06/16.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Authority contracts can later accept principal/tenant scopes while v0.1 states its single-user assumptions.
- **Uncertainty:** Authentication mechanism and policy-enforcement topology are candidate-owned.
- **Provenance:** Level A property.

### AR-SEC-002 — Deny-by-default scoped capabilities

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-006`, `FR-037`, `FR-042`, `RR-015`, `NEG-CRED-01`, `NEG-FUTURE-01`
- **Description:** Capabilities must be denied by default and bound to authenticated principal, task, attempt/operation, normalized action/resource, workspace, policy/schema version, limits, time/use, credential, network, Git, and effect scopes; grants do not broaden by implication.
- **Rationale:** Model policy reminders cannot prevent confused-deputy or stale-owner use.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D11_APPROVAL_PERMISSION_SYSTEM`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D20_SECURITY_BOUNDARIES`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`
- **Required observable property:** Wrong task/target/owner/version/endpoint/child/replay uses fail before dispatch and are auditable.
- **Prohibited architectural outcome:** Ambient authority, global mutable grants, grant inheritance without contract, or self-expansion.
- **Evaluation linkage:** EP-APR-004/005/008; EP-NEG-CRED-01; EP-NEG-FUTURE-01.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Explicit scopes prevent cross-task/agent/client reuse and can later add tenant identity.
- **Uncertainty:** Capability token/record representation is unselected.
- **Provenance:** Level A property.

### AR-SEC-003 — Protected-secret recipient boundary

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-046`, `FR-047`, `RR-015`, `NEG-SECRET-01`, `NEG-CRED-01`
- **Description:** Protected-secret classification must override otherwise allowed roots and instructions; raw values may cross only an explicitly authorized protected recipient boundary with least purpose/time/use scope and must not enter model context, chat, general environment, descendant inheritance, commands, logs, screenshots, artifacts, diffs, summaries, approvals, or evidence.
- **Rationale:** Redaction after broad exposure is not a secret boundary.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D09_ISOLATION_SANDBOXING`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D13_MODEL_PROVIDER_GATEWAY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Synthetic marker scans across all twelve observable surface classes find zero unauthorized occurrence; ambiguous locations fail closed without value inspection.
- **Prohibited architectural outcome:** Secret in ordinary state/context/output, allowed-root precedence over secret policy, digest leakage, or revocation ignored.
- **Evaluation linkage:** EP-NEG-SECRET-01; EP-NEG-CRED-01; EP-EVID-005; COMP-06/07.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Protected recipient contracts remain explicit for later connectors/providers.
- **Uncertainty:** Secret store and delivery mechanism are unselected; exhaustive detection is not claimed.
- **Provenance:** Level A property.

### AR-SEC-004 — Explicit network, destination, and credential boundary

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-045`, `RR-013`, `NEG-NET-01`, `NEG-PROVIDER-01`
- **Description:** Network use must be a separately visible, bounded capability tied to effective destination, redirect/DNS/proxy/TLS policy, credential scope, data policy, route/provider authorization, and conservative cost ceiling.
- **Rationale:** Local repository or tool permission does not imply arbitrary egress or provider dispatch.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D08_EXECUTION_PROCESS_CONTROL`, `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Disallowed or unauthorized destinations/routes transmit zero bytes/incur zero calls; effective targets are rechecked after redirection.
- **Prohibited architectural outcome:** Implicit egress, destination substitution, credential forwarding, metadata/private target access, or unknown-cost unbounded dispatch.
- **Evaluation linkage:** EP-NEG-NET-01; EP-NEG-PROVIDER-01; COMP-13/15.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Destination and data-policy contracts can apply equally to future workers/connectors.
- **Uncertainty:** Network enforcement mechanism is unselected.
- **Provenance:** Level A property.

### AR-SEC-005 — Clean-room and source-provenance enforcement

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `RR-015`, `UF-16`
- **Description:** Architecture work and later implementation must preserve source/evidence provenance, exclude reconstructed external code and Level C internals, and keep observed product facts, external patterns, project-derived requirements, and implementation proposals explicitly distinct.
- **Rationale:** Untracked architectural borrowing creates correctness, rights, and audit risk.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`, `D21_LOCAL_FIRST_PACKAGING`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`
- **Required observable property:** Source/dependency/fixture provenance is reviewable; forbidden reconstructed identifiers/artifacts are absent; unknown rights remain blockers.
- **Prohibited architectural outcome:** Importing external implementation, relabeling reconstructed details as requirements, or unsupported rights claims.
- **Evaluation linkage:** OR-CLEANROOM-PROVENANCE; release forbidden-artifact and rights checks.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Versioned provenance supports later extensions and editions without contaminating the shared core.
- **Uncertainty:** Outbound/inbound licensing remains separately unresolved under R-029.
- **Provenance:** Level A project constraint; Level B patterns may inform candidates only.

### AR-APR-001 — Durable exact-scope approval object

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-043`, `FR-044`, `NEG-APR-01`, `NEG-RACE-01`, `UF-09`
- **Description:** Approval must be an authenticated durable record distinct from authorization and conversation, bound to requester/approver/principal/task/attempt/operation/action/capability/schema/target/base/policy/time/use, with denial, expiry, revocation, replay, mutation, display, ownership-transfer, and recovery semantics.
- **Rationale:** A conversational yes or digest cannot safely authorize a consequential action.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D06_EVENT_OPERATION_HISTORY`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Only one exact current inspectable use can be consumed; stale/revoked/mutated/replayed/recovered ambiguity is denied or reconciled.
- **Prohibited architectural outcome:** Boolean/conversational approval, scope substitution, one approval broadening another action, or approval surviving ambiguous dispatch.
- **Evaluation linkage:** EP-APR-001..009; EP-NEG-APR-01; COMP-01/09/16.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Approval binding can later include tenant/client identity without changing semantics.
- **Uncertainty:** Approval storage and UI representation are unselected.
- **Provenance:** Level A property; structured approval records are required, any specific schema is Level B/C.

### AR-APR-002 — External-effect intent, attempt, observation, confirmation, and uncertainty

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-032`, `FR-068`, `RR-003`, `NEG-EXT-01`, `UF-10`
- **Description:** The architecture must distinguish effect intent, authorization/approval, dispatch attempt, observed response, authoritative readback, confirmed effect, known failure/no-start, cancellation, and unknown effect, with stable request and execution identities.
- **Rationale:** Tool success text and external state are different facts.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D17_EVIDENCE_ARTIFACT_SYSTEM`
- **Required observable property:** Every consequential effect ends with authoritative confirmation, known terminal non-success, or explicit uncertainty that blocks completion and blind retry.
- **Prohibited architectural outcome:** Collapsing intent/approval/attempt into success, cached readback, or unknown acknowledgement treated as failure/success.
- **Evaluation linkage:** EP-CTL-019/023; EP-FALSE-008/015; EP-NEG-EXT-01; COMP-02/03/10.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Readback/reconciliation can be supplied by local or remote capability implementations.
- **Uncertainty:** Effect-specific authoritative readback sources must be declared by candidates.
- **Provenance:** Level A property.

### AR-APR-003 — Consequential, destructive, and prohibited action enforcement

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-024`, `FR-037`, `RR-015`, `NEG-DESTRUCT-01`
- **Description:** Action policy must structurally separate allowed read-only/local reversible, constrained local destructive, external-read, remote, approval-required, and prohibited classes; approval cannot enable a prohibited class and user-owned material has stronger protection than task-owned material.
- **Rationale:** LLM classification at dispatch time alone cannot safely control destructive effects.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D08_EXECUTION_PROCESS_CONTROL`, `D10_GIT_INTEGRATION`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** The effective normalized target and ownership are revalidated at dispatch; prohibited actions yield zero effect even after conversational approval.
- **Prohibited architectural outcome:** Approval-as-policy-override, target hiding, or destructive action against ambiguous/pre-existing user material.
- **Evaluation linkage:** EP-GIT-013..030; EP-NEG-DESTRUCT-01; EP-APR-008.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** New capability classes must enter the same explicit policy model.
- **Uncertainty:** Policy engine topology is unselected.
- **Provenance:** Level A property.

### AR-MOD-001 — Provider- and logical-role-neutral product semantics

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-050`, `FR-055`, `FC-009`
- **Description:** Core task, lifecycle, permission, approval, evidence, verification, and completion semantics must not depend on a provider's native state/naming, and logical roles must remain independent of permanent model assignments.
- **Rationale:** Provider behavior is an occupant of a product contract, not the source of product truth.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D16_VERIFICATION_ARCHITECTURE`
- **Required observable property:** Different provider shapes preserve the same core invariants while retaining provider-specific distinctions and provenance.
- **Prohibited architectural outcome:** Provider-native state as canonical product state, provider lock-in hidden in semantics, or E2 role assignment.
- **Evaluation linkage:** EP-ROUTE-001..007; EP-CONTRIB-008; provider-shape fixtures.
- **E3 validation obligation:** `E3V-004`; `E3V-008`
- **Future compatibility impact:** New providers can be added without renaming product truth or gaining automatic eligibility.
- **Uncertainty:** Gateway topology and provider SDKs are unselected.
- **Provenance:** Level A property; provider-router patterns are Level B.

### AR-MOD-002 — Purpose, eligibility, capability discovery, and zero-dispatch denial

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-051`, `FR-053`, `RR-011`, `NEG-PROVIDER-01`, `UF-12`
- **Description:** Every model route must independently declare purpose and eligibility class, required capabilities/policy evidence, class authority/version, authorization, bounds, and route reason; DISALLOWED produces no dispatch, EVALUATION_ONLY cannot serve normal tasks or self-promote, and USER_CONFIGURED_UNVERIFIED requires explicit experimental selection and warning.
- **Rationale:** An unbenchmarked or available model is not automatically eligible for normal product work.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Requested/resolved route, purpose, eligibility, authority, denial/outcome, and zero-dispatch proof are retained for every model operation.
- **Prohibited architectural outcome:** Hidden class elevation, evaluation result as eligibility, or disallowed bytes/call/cost.
- **Evaluation linkage:** EP-ROUTE-001..005; EP-NEG-PROVIDER-01.
- **E3 validation obligation:** `E3V-004`; `E3V-008`
- **Future compatibility impact:** New providers/configurations enter through explicit capability and eligibility contracts.
- **Uncertainty:** No model/provider is assigned or called in E2.
- **Provenance:** Level A property.

### AR-MOD-003 — Explicit fallback and provider-specific semantics

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-052`, `FR-054`, `FC-009`, `NEG-PROVIDER-01`, `UF-12`
- **Description:** Fallback must be off unless explicitly configured for a compatible purpose/class; each fallback is a new attributed route, and provider-specific streaming, refusal, tool, context, cancellation, usage, cost, latency, and failure semantics remain typed and observable.
- **Rationale:** Flattening provider differences creates hidden fallback, false success, and incorrect cost/failure attribution.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D18_OBSERVABILITY_LOGGING`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Provider/model versus transport/policy/capability failures remain distinguishable; fallback parent and resolved route are explicit.
- **Prohibited architectural outcome:** Silent fallback, crediting fallback to requested model, or normalizing refusal/error into success prose.
- **Evaluation linkage:** EP-ROUTE-004..007; EP-NEG-PROVIDER-01; COMP-15.
- **E3 validation obligation:** `E3V-004`; `E3V-008`
- **Future compatibility impact:** Provider evolution preserves semantics while allowing provider-specific adapters.
- **Uncertainty:** Fallback policy and adapter mechanisms are unselected.
- **Provenance:** Level A property.

### AR-EVD-001 — Versioned outcome-profile evidence bundle

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-026`, `FR-064`, `RR-010`, `UF-15`
- **Description:** Every run state, including rejection, active work, wait/block/control/recovery, terminal noncomplete, candidate, and completed outcomes, must produce or update a versioned secret-safe evidence bundle that validates against its profile and preserves canonical state, operations, checks, approvals/effects, routing, actors, verification, limitations, and final disposition.
- **Rationale:** Evidence cannot be reconstructed from a final success summary.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D18_OBSERVABILITY_LOGGING`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Required fields/references are present or explicitly NOT_APPLICABLE under policy; missing/mismatched semantics fail validation and completion.
- **Prohibited architectural outcome:** Silent omission, outcome profile mismatch, evidence generated only after success, or secrets in the bundle.
- **Evaluation linkage:** EP-EVID-001..012; EVR-01..16; six evidence profiles.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Versioned logical evidence can use replaceable serialization/storage.
- **Uncertainty:** Format, large-object storage, and hashing are unselected.
- **Provenance:** Level A property.

### AR-EVD-002 — Stable artifact identity, provenance, references, and redaction

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-063`, `FR-069`, `NEG-EVID-01`
- **Description:** Artifacts and large outputs must have stable identity, task/workspace/revision/type/producer/model/tool provenance, sensitivity/privacy class, integrity/tamper/staleness state, retention rule, inspectable reference, and redaction/exposure status.
- **Rationale:** A path or digest alone does not prove provenance, semantic correctness, or safe disclosure.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`, `D21_LOCAL_FIRST_PACKAGING`
- **Required observable property:** Missing, mutated, stale, wrong-task, forged, or unsafe artifacts are rejected while bounded references retain necessary output.
- **Prohibited architectural outcome:** Self-attested artifact identity, raw secret retention, digest-as-correctness, or unbounded inline output.
- **Evaluation linkage:** EP-EVID-003/005/007; EP-NEG-EVID-01; draft-package checks.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Stable references support later remote artifact storage without selecting it now.
- **Uncertainty:** Identity/integrity mechanism is unselected; content addressing is Level B.
- **Provenance:** Level A property.

### AR-EVD-003 — Evidence integrity distinct from telemetry

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-062`, `RR-014`, `NEG-EVID-01`, `NEG-AUDIT-01`
- **Description:** Operational telemetry may aid diagnosis but cannot grant authority or establish evidence truth; material evidence/history must expose provenance, correlation, completeness, integrity, gaps, tamper state, and independent readback where applicable.
- **Rationale:** Logs can be dropped, forged, reordered, or produced by untrusted tools.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D18_OBSERVABILITY_LOGGING`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Telemetry/evidence disagreements retain both facts and authoritative validation controls the outcome.
- **Prohibited architectural outcome:** Telemetry as source of truth, self-hashing manifest as proof, or unexplained gap ignored.
- **Evaluation linkage:** EP-NEG-EVID-01; EP-NEG-AUDIT-01; OR-EVIDENCE-BUNDLE.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Evidence contracts can be transported without trusting a particular logging backend.
- **Uncertainty:** Integrity mechanism and threat-resistance beyond the declared local boundary are unselected.
- **Provenance:** Level A property.

### AR-VER-001 — Structurally independent verification path

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-065`, `NEG-VER-01`, `UF-14`
- **Description:** Verification must operate against the exact produced state through a separate accountable execution context with no shared mutable author state, obtain durable evidence independently of executor claims, prioritize deterministic oracles, use least privilege, and record verifier identity/configuration/route/independence.
- **Rationale:** Executor self-report or the same running model session is not independent evidence.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Verifier reruns deterministic checks/readbacks from a bounded context manifest and can reject author claims without private chain-of-thought.
- **Prohibited architectural outcome:** Same-session author verification, transcript-only verification, verifier using author approval/credentials for a new effect, or provider diversity treated as proof.
- **Evaluation linkage:** EP-NEG-VER-01; EP-WF-014; OR-INDEPENDENT-VERIFY.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Verifier role remains provider-neutral and separately deployable.
- **Uncertainty:** Verifier model/provider and process topology are unselected.
- **Provenance:** Level A property.

### AR-VER-002 — Deterministic replay, bounded verification context, and adequacy review

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-025`, `FR-026`, `FR-065`, `NEG-VER-02`, `UF-14`
- **Description:** Verification must receive a bounded manifest, rerun deterministic checks where applicable with exact revision/configuration/environment identity, evaluate predicate-set adequacy before crediting passes, preserve ordered repetitions/flakiness, and let deterministic ground truth dominate model judgment.
- **Rationale:** A polished review narrative cannot compensate for missing or irrelevant objective checks.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Check replays and adequacy variants reproduce the expected result without author hidden reasoning or hidden production-only state.
- **Prohibited architectural outcome:** Irreproducible verifier context, one later pass erasing flakiness, or judgment overriding deterministic failure.
- **Evaluation linkage:** VER-ADQ-01..09; EP-FALSE-003/006/010; OR-CHECK-REPLAY.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Portable verifier inputs allow different future verifier occupants.
- **Uncertainty:** Finite rerun/repetition values remain prospectively policy-owned.
- **Provenance:** Level A property.

### AR-VER-003 — Verification lifecycle, error separation, and correction invalidation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-031`, `FR-067`, `RR-009`, `NEG-VER-02`, `UF-14`
- **Description:** Verification runs must be immutable/sequential with at most one active run; infrastructure error, substantive verdict, task failure, and implementation correction remain separate, and changes-required or state mutation supersedes/invalidate prior completion evidence without erasing history.
- **Rationale:** Verifier failure must not fabricate either task failure or success.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D06_EVENT_OPERATION_HISTORY`, `D16_VERIFICATION_ARCHITECTURE`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Verifier crash/timeout yields VERIFICATION_ERROR and aggregate UNVERIFIED; correction creates linked attempt/revision and requires new verification.
- **Prohibited architectural outcome:** Retry hiding prior runs, verifier error as PASS/FAILED task, or stale verdict retained as current.
- **Evaluation linkage:** EP-FALSE-004/005/007/014; EP-WF-014/017; COMP-04/11.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Run identity/configuration supports future independent verifier services.
- **Uncertainty:** Verifier rerun ceiling value is not set here.
- **Provenance:** Level A property.

### AR-OBS-001 — Structured operational observability

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-021`, `FR-051`, `FR-060`, `FR-064`, `MET-003`
- **Description:** The architecture must expose structured inspectable answers for active task/phase/owner, operation, capabilities, files/base/workspace, checks, approvals, effects, routes, recovery, blockers, verification, evidence, limits, and why the task is blocked or unverified.
- **Rationale:** Users and recovery/verifier actors need state facts, not private reasoning.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D18_OBSERVABILITY_LOGGING`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Disconnect/reconnect yields an equivalent axis-qualified view with causal references and visible unknowns/limitations.
- **Prohibited architectural outcome:** Activity prose as canonical state, hidden active capabilities/effects, or a single success/error label erasing causes.
- **Evaluation linkage:** EP-WF-008; EP-EVID-*; MET-003 protocol.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Observable state can be projected to future clients without sharing runtime memory.
- **Uncertainty:** UI and telemetry implementation are unselected.
- **Provenance:** Level A property.

### AR-OBS-002 — Evidence-linked explanations without private reasoning

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-061`, `FR-062`, `RR-014`, `NEG-EVID-01`
- **Description:** User-visible explanations must state decisions, authoritative evidence, uncertainty, limitations, and causal references without exposing or requiring private chain-of-thought; operational telemetry and authoritative evidence remain semantically distinct.
- **Rationale:** Reviewability requires inspectable reasons, not hidden reasoning traces or log volume.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D18_OBSERVABILITY_LOGGING`
- **Required observable property:** A reviewer can trace each material disposition to durable evidence and unknowns while no hidden reasoning is required.
- **Prohibited architectural outcome:** Chain-of-thought dependency, unsupported explanations, or logs presented as completion proof.
- **Evaluation linkage:** EP-WF-014; OR-BOUNDED-RUBRIC limited to explanation clarity; evidence non-claims.
- **E3 validation obligation:** `E3V-005`
- **Future compatibility impact:** Explanation contracts are client/provider neutral.
- **Uncertainty:** Presentation form and judgment rubric are unselected.
- **Provenance:** Level A property.

### AR-FAIL-001 — Structured semantic failure model

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-021`, `FR-031`, `FR-034`, `FR-035`, `FR-052`, `UF-03`, `UF-15`
- **Description:** Failures must preserve semantically useful classes for user/input, repository, capability/policy, process/tool, provider/model, network, Git, verification, approval, effect/reconciliation, persistence/recovery, security, resource/budget, and internal invariant causes, with source layer, retryability, consequence, and resolution path.
- **Rationale:** A generic error cannot safely drive retry, recovery, user action, or completion.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D13_MODEL_PROVIDER_GATEWAY`, `D18_OBSERVABILITY_LOGGING`, `D19_ERROR_FAILURE_MODEL`
- **Required observable property:** Same visible symptom from different layers retains different typed causes and permitted next actions; unknown stays unknown.
- **Prohibited architectural outcome:** Flattening errors into success prose, automatic retry of nonretryable classes, or provider failure confused with task failure.
- **Evaluation linkage:** EP-CTL-*; EP-ROUTE-006/007; EP-WF-005/015.
- **E3 validation obligation:** `E3V-001`; `E3V-004`
- **Future compatibility impact:** Failure contracts can traverse local/remote boundaries without importing an external error registry.
- **Uncertainty:** Exact type hierarchy and codes are E2 candidate details.
- **Provenance:** Level A semantic requirement; a typed-error registry is Level B.

### AR-FAIL-002 — Ceiling exhaustion and bounded safety reserve

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `RR-005`, `RR-013`, `NEG-DOS-01`
- **Description:** Time, output, tool-call, retry, network, cost, cancellation, and reconciliation ceilings must be finite and enforceable where applicable; after productive exhaustion, no new productive work starts and only a separately authorized bounded control/safety/readback/evidence/cleanup reserve may run.
- **Rationale:** A retry storm or evidence task must not bypass the same resource/budget gate it reports.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D08_EXECUTION_PROCESS_CONTROL`, `D19_ERROR_FAILURE_MODEL`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Exhaustion time/reason, consumed limit, blocked productive dispatch, reserve operations, and truthful final state are recorded.
- **Prohibited architectural outcome:** Unbounded recursion/retry/output/spend, silent ceiling changes, or cleanup reserve doing productive work.
- **Evaluation linkage:** EP-NEG-DOS-01; EP-WF-017; BOUND-CORRECTION-EXHAUSTION.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Resource contracts can later include remote/tenant quotas.
- **Uncertainty:** Numeric values are prospectively owned design/configuration/validation parameters, not invented here.
- **Provenance:** Level A property.

### AR-TST-001 — Deterministic test seams and fault injection

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-025`, `FR-026`, `FR-041`, `UF-02`, `NEG-VER-02`
- **Description:** Architecture boundaries must permit deterministic inspection/control of authoritative state, time/order, process interruption, filesystem/Git state, capability policy, provider routes, approvals, effects/readbacks, evidence, verification, and resource ceilings without hidden production-only state.
- **Rationale:** The frozen E1 expected outcomes cannot be implemented if critical boundaries are unobservable or inseparable.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D08_EXECUTION_PROCESS_CONTROL`, `D16_VERIFICATION_ARCHITECTURE`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Clean-room fixtures can inject each declared fault and decisive oracles can read resulting state without changing product semantics.
- **Prohibited architectural outcome:** Untestable singleton/global state, production-only hidden authority, or tests depending on model claims.
- **Evaluation linkage:** All 11 fixture families and 18 oracle classes.
- **E3 validation obligation:** `E3V-001`; `E3V-002`; `E3V-003`; `E3V-004`; `E3V-005`; `E3V-006`
- **Future compatibility impact:** Explicit seams allow alternative local/remote implementations to share the same suite.
- **Uncertainty:** Concrete harness adapters are E3/E4 work.
- **Provenance:** Level A requirement derived from the frozen suite.

### AR-TST-002 — Complete frozen E1 suite materialization

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `RR-008`, `RR-015`, `UF-16`, `NEG-FUTURE-01`
- **Description:** Every candidate must show how its boundaries can later materialize all 170 cases, 18 oracles, 11 fixtures, 23 security-negative families, 16 repository conditions, 30 Git/effect rows, nine adequacy variants, sixteen dangerous compositions, and eight reliability protocols without redefining expected outcomes.
- **Rationale:** An architecture that cannot be tested against the frozen suite cannot establish E1 compliance.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D20_SECURITY_BOUNDARIES`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Candidate trace names the seam, fixture input, decisive oracle/readback, and blocked unsupported condition for every suite family.
- **Prohibited architectural outcome:** Dropping cases as implementation-inconvenient, hidden state, or changing expected outcomes to fit a mechanism.
- **Evaluation linkage:** EP-EVAL-0.2 complete catalog and release checkpoint.
- **E3 validation obligation:** `E3V-001`; `E3V-002`; `E3V-003`; `E3V-004`; `E3V-005`; `E3V-006`; `E3V-007`
- **Future compatibility impact:** The same suite contract can compare future implementations/providers.
- **Uncertainty:** No case is implemented or run in E2-001.
- **Provenance:** Level A testability requirement.

### AR-TST-003 — Measurement-protocol interfaces without invented thresholds

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `SLO-001`, `SLO-002`, `SLO-003`, `SLO-004`, `MET-001`, `MET-002`, `MET-003`, `MET-004`
- **Description:** The architecture must expose stable timestamps, strata, outcomes, costs/usage, interventions, retries/reruns, checks, failures, resource bounds, and candidate/revision identities needed by all eight frozen measurement protocols, while leaving unknown reference-environment and empirical thresholds unknown.
- **Rationale:** SLO/MET outcomes are empirical, but missing measurement seams would make them unmeasurable.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D06_EVENT_OPERATION_HISTORY`, `D13_MODEL_PROVIDER_GATEWAY`, `D18_OBSERVABILITY_LOGGING`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Each PROT-SLO/MET block can derive its numerator, denominator, exclusions, uncertainty, and strata from structured records after future authorized runs.
- **Prohibited architectural outcome:** Fabricated measurements, post-result denominator redefinition, or architecture-only claims of achieved SLOs.
- **Evaluation linkage:** PROT-SLO-001..004; PROT-MET-001..004; OR-METRIC-PROTOCOL.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Measurement contracts compare later providers/workers without renaming metrics.
- **Uncertainty:** Observed values and reference environment are UNKNOWN until E3.
- **Provenance:** Level A measurement seam; primary SLO/MET outcomes are E3 obligations, not architecture guarantees.

### AR-PERF-001 — Finite resource, time, output, network, and cost enforcement

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-034`, `FR-037`, `FR-040`, `RR-005`, `RR-013`, `NEG-DOS-01`
- **Description:** Every applicable task/operation/capability must support prospectively declared finite time, output, tool, retry, network, cost, cancellation, and reconciliation limits, conservative pre-dispatch cost authorization, and truthful unknown usage.
- **Rationale:** Unbounded or unknown-cost execution violates bounded autonomy even when useful.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D08_EXECUTION_PROCESS_CONTROL`, `D13_MODEL_PROVIDER_GATEWAY`, `D20_SECURITY_BOUNDARIES`
- **Required observable property:** Dispatch is denied when required ceilings are missing/exceeded and resource/cost records remain attributed or explicit UNKNOWN.
- **Prohibited architectural outcome:** Unlimited productive work, unknown reporting used as permission, or after-the-fact ceilings.
- **Evaluation linkage:** EP-NEG-DOS-01; EP-ROUTE-005; COMP-15.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Limit contracts can later accept remote/tenant budget scopes.
- **Uncertainty:** No numerical limits are selected by E2-001.
- **Provenance:** Level A property.

### AR-PERF-002 — Latency, cost, responsiveness, and large-output instrumentation

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-021`, `SLO-002`, `SLO-003`, `MET-001`, `MET-002`, `MET-003`, `MET-004`
- **Description:** Structured records must support phase/provider/tool/verification/stall latency, control acknowledgement/effectiveness, restart recovery, component and total cost, ordered check variance, bounded large-output references, and cancellation responsiveness.
- **Rationale:** Performance and cost tradeoffs cannot be compared from narrative estimates.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D08_EXECUTION_PROCESS_CONTROL`, `D13_MODEL_PROVIDER_GATEWAY`, `D18_OBSERVABILITY_LOGGING`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** Future protocols derive raw and aggregate measurements by layer and report unknown/undefined results honestly.
- **Prohibited architectural outcome:** Conflated latency layers, missing cost attribution, unbounded inline outputs, or fabricated zero cost.
- **Evaluation linkage:** PROT-SLO-002/003; PROT-MET-001..004.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Instrumentation supports future remote-provider strata.
- **Uncertainty:** Numerical targets and acceptable local overhead remain E3 evidence or later configuration.
- **Provenance:** Level A measurement property.

### AR-PKG-001 — Local-first packaging and contributor-operable boundary

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-069`, `FC-001`, `UF-16`
- **Description:** The v0.1 system shape must be operable as a local-first single-user product with explicit supported host/persistence/security assumptions, local inspectability/review output, version/migration ownership, and contribution/test/security/reporting boundaries; remote services cannot be required for local truth unless explicitly declared as an unsupported condition.
- **Rationale:** Local-first is the immediate product constraint, not merely a deployment preference.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D02_CORE_APPLICATION_RUNTIME`, `D21_LOCAL_FIRST_PACKAGING`, `D22_FUTURE_REMOTE_EXECUTION`
- **Required observable property:** A contributor/user can identify local components, supported environment, durable boundary, migration/backup/cleanup behavior, and review artifacts without hidden service state.
- **Prohibited architectural outcome:** Undeclared mandatory cloud dependency, opaque local state, or draft-package remote side effect.
- **Evaluation linkage:** EP-CONTRIB-001..008; OR-CONTRIBUTOR-WALKTHROUGH.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Explicit local interfaces preserve a later remote-worker seam without building it now.
- **Uncertainty:** Client, runtime, installer, updater, and packaging technology are unselected.
- **Provenance:** Level A product constraint.

### AR-FUT-001 — Versioned serializable replaceable boundaries

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-050`, `FC-001`, `FC-008`
- **Description:** Durable interchange and cross-component logical contracts must be explicitly versioned, serializable in principle, and owned behind replaceable interfaces; task/workspace/operation truth must not be irreversibly tied to one process, machine path, client, or provider.
- **Rationale:** Future remote execution and schema evolution become prohibitively difficult if logical truth exists only as in-process objects or provider-native state.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D04_DURABLE_STATE_PERSISTENCE`, `D22_FUTURE_REMOTE_EXECUTION`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`
- **Required observable property:** Candidates identify boundaries, versions, compatibility behavior, migration/reversal path, and unsupported assumptions.
- **Prohibited architectural outcome:** Unversioned durable interchange, global path identity, or irreversible provider/process lock-in.
- **Evaluation linkage:** EP-NEG-FUTURE-01; schema-version and migration cases.
- **E3 validation obligation:** `E3V-001`
- **Future compatibility impact:** Directly preserves cloud/remote/provider evolution without implementing distributed operation.
- **Uncertainty:** Transport/serialization mechanism is unselected.
- **Provenance:** Level A compatibility constraint.

### AR-FUT-002 — Explicit ownership scopes without global singleton dependence

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-001`, `FR-008`, `FC-002`, `FC-003`, `FC-004`, `NEG-FUTURE-01`
- **Description:** Agent, task, principal, workspace, capability, approval, operation, artifact, credential, evidence, and resource ownership must be explicit fields/contracts rather than implicit global singletons; v0.1 may enforce one active local user while rejecting cross-scope reuse.
- **Rationale:** A single-user implementation can preserve future concurrency only if ownership is not erased.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D03_TASK_WORKFLOW_ORCHESTRATION`, `D11_APPROVAL_PERMISSION_SYSTEM`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`
- **Required observable property:** Two synthetic principals/workspaces cannot reuse identities, paths, grants, approvals, operations, or artifacts.
- **Prohibited architectural outcome:** Global mutable owner/capability state or path-only cross-task authority.
- **Evaluation linkage:** EP-NEG-FUTURE-01; EP-WF-007.
- **E3 validation obligation:** `E3V-006`
- **Future compatibility impact:** Supports later multiple agents/clients/users/tenants while explicitly not implementing them now.
- **Uncertainty:** No multi-agent or multi-tenant coordination is selected.
- **Provenance:** Level A compatibility constraint.

### AR-FUT-003 — Versionable extension boundary and domain-neutral shared core

- **Class:** `HARD_CONSTRAINT`
- **Source E1 requirement IDs:** `FR-040`, `FR-050`, `FR-055`, `FC-005`, `FC-006`, `FC-007`, `FC-009`
- **Description:** Capabilities, procedures, policies, evaluation contracts, and provenance must be versionable/reviewable behind an explicit extension boundary, while core task/tool/approval/evidence/security semantics remain domain- and provider-neutral.
- **Rationale:** Skills, routines, connectors, and later General/Finance editions must not fork or bypass core authority semantics.
- **Hard constraint:** `YES`
- **Applicable architecture domains:** `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`, `D25_E1_SUITE_TESTABILITY`
- **Required observable property:** A proposed extension declares contracts, authority, provenance, tests, limits, and compatibility without gaining ambient power.
- **Prohibited architectural outcome:** Extension code bypassing policy/evidence, edition-specific core duplication, marketplace/scheduler implementation in v0.1, or finance semantics entering the preview.
- **Evaluation linkage:** EP-CONTRIB-005/008; EP-NEG-FUTURE-01; capability schema cases.
- **E3 validation obligation:** `E3V-004`; `E3V-006`
- **Future compatibility impact:** Directly preserves skills/connectors, General Edition, Finance Edition, and SaaS extension paths.
- **Uncertainty:** No loader, marketplace, routine engine, connector platform, or edition is selected.
- **Provenance:** Level A compatibility constraint.

### AR-PRF-001 — Lower interactive and control latency after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `SLO-002`, `SLO-003`, `MET-001`
- **Description:** Among hard-constraint-passing candidates, prefer lower measured interaction, durable-control, cancellation, and recovery latency in a prospectively fixed reference environment.
- **Rationale:** Responsiveness affects usability but cannot compensate for false completion or unsafe control.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D08_EXECUTION_PROCESS_CONTROL`, `D18_OBSERVABILITY_LOGGING`
- **Required observable property:** Comparable future protocol measurements with uncertainty and layer attribution.
- **Prohibited architectural outcome:** Using estimated latency as evidence or trading a hard failure for speed.
- **Evaluation linkage:** PROT-SLO-002/003; PROT-MET-001.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Remote latency may be a later stratum, not a current requirement.
- **Uncertainty:** Weight and target are unassigned; sensitivity analysis required.
- **Provenance:** Secondary comparative criterion grounded in E1 measurement concerns; no canonical E1 primary disposition is weakened.

### AR-PRF-002 — Lower operational and maintenance complexity after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `FR-040`, `FR-062`, `FC-008`
- **Description:** Among hard-pass candidates, prefer fewer independent failure/upgrade/operational surfaces and clearer component ownership while retaining required semantic separations.
- **Rationale:** Operational simplicity reduces defect and contributor burden but cannot justify collapsing authority boundaries.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D02_CORE_APPLICATION_RUNTIME`, `D04_DURABLE_STATE_PERSISTENCE`, `D19_ERROR_FAILURE_MODEL`, `D21_LOCAL_FIRST_PACKAGING`
- **Required observable property:** Candidate declares components, owners, upgrade/recovery responsibilities, and failure propagation with evidence-based complexity assumptions.
- **Prohibited architectural outcome:** Counting components without correlation review or simplifying away a hard boundary.
- **Evaluation linkage:** E2-003 comparative evidence only; later contributor walkthrough.
- **E3 validation obligation:** `NONE`
- **Future compatibility impact:** Maintainability supports later evolution.
- **Uncertainty:** Weight unassigned; correlated with packaging and migration criteria.
- **Provenance:** E2 comparative preference supported by frozen E1 operability/evolution concerns.

### AR-PRF-003 — Lower migration cost and stronger reversibility after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `FR-048`, `FC-001`, `FC-008`
- **Description:** Among hard-pass candidates, prefer explicit export/migration/reversal paths with smaller irreversible state, provider, process, and packaging commitments.
- **Rationale:** E2 decisions precede empirical validation and should remain reversible where practical.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D04_DURABLE_STATE_PERSISTENCE`, `D13_MODEL_PROVIDER_GATEWAY`, `D21_LOCAL_FIRST_PACKAGING`, `D22_FUTURE_REMOTE_EXECUTION`
- **Required observable property:** Candidate identifies irreversible decisions, migration steps, rollback limits, retained evidence, and reversal triggers.
- **Prohibited architectural outcome:** Assuming zero migration cost or treating lock-in as a hard-compliance substitute.
- **Evaluation linkage:** E2-003 comparison; E3 failure/reversal conditions.
- **E3 validation obligation:** `E3V-001`; `E3V-004`
- **Future compatibility impact:** Directly affects remote/provider evolution.
- **Uncertainty:** Weight unassigned; correlated with extensibility.
- **Provenance:** E2 comparative preference grounded in FC-001/008.

### AR-PRF-004 — Lower future remote/concurrency adaptation cost after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `FC-001`, `FC-002`, `FC-003`, `FC-004`
- **Description:** Among candidates satisfying the minimum versioned/ownership seams, prefer lower evidenced effort to add remote workers, concurrent tasks, multiple clients, or stronger principal scopes without rewriting product truth.
- **Rationale:** Compatibility matters, but v0.1 must not absorb unnecessary distributed-system complexity.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D22_FUTURE_REMOTE_EXECUTION`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`
- **Required observable property:** Candidate names reusable boundaries and concrete assumptions that would change, with a bounded migration profile.
- **Prohibited architectural outcome:** Speculative future feature implementation or vague future-ready claims.
- **Evaluation linkage:** E2-003 scenario comparison; EP-NEG-FUTURE-01 minimum seam remains hard.
- **E3 validation obligation:** `NONE`
- **Future compatibility impact:** Primary comparative future-compatibility criterion.
- **Uncertainty:** Weight unassigned; correlated with migration/reversibility.
- **Provenance:** E2 comparative preference; minimum compatibility remains hard through AR-FUT-001/002.

### AR-PRF-005 — Lower evidence and large-output overhead after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `FR-021`, `FR-063`, `FR-064`, `MET-001`, `MET-002`
- **Description:** Among hard-pass candidates, prefer lower measured storage, serialization, transfer, and review overhead for evidence and large outputs while preserving complete authoritative provenance and bounded references.
- **Rationale:** Evidence must be durable and usable without making ordinary local work needlessly expensive.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D04_DURABLE_STATE_PERSISTENCE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, `D18_OBSERVABILITY_LOGGING`
- **Required observable property:** Comparable size/latency/cost measurements over the same evidence profiles and workloads.
- **Prohibited architectural outcome:** Omitting required evidence or using compression/summary that destroys authority to improve scores.
- **Evaluation linkage:** PROT-MET-001/002; evidence-profile workloads.
- **E3 validation obligation:** `E3V-007`
- **Future compatibility impact:** Efficient references help future remote transport.
- **Uncertainty:** Weight and acceptable overhead are unknown until evidence.
- **Provenance:** E2 comparative preference grounded in E1 measurement and evidence requirements.

### AR-PRF-006 — Lower contributor and local packaging burden after hard compliance

- **Class:** `WEIGHTED_PREFERENCE`
- **Source E1 requirement IDs:** `FR-069`, `FC-005`, `UF-16`
- **Description:** Among hard-pass candidates, prefer clearer setup, diagnosis, migration, test, security-reporting, and local review workflows with fewer hidden prerequisites.
- **Rationale:** The Engineering Preview is intended to be inspectable and open-source-contributor operable.
- **Hard constraint:** `NO`
- **Applicable architecture domains:** `D01_CLIENT_INTERACTION_BOUNDARY`, `D21_LOCAL_FIRST_PACKAGING`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`
- **Required observable property:** A later contributor walkthrough reports prerequisite count, failure clarity, reproducibility, and documentation gaps.
- **Prohibited architectural outcome:** Claiming ease without a reproducible walkthrough or requiring hidden service/account state.
- **Evaluation linkage:** EP-CONTRIB-001..008; OR-CONTRIBUTOR-WALKTHROUGH.
- **E3 validation obligation:** `E3V-003`
- **Future compatibility impact:** Supports extension contributors without implementing an extension marketplace.
- **Uncertainty:** Weight unassigned; correlated with maintainability.
- **Provenance:** E2 comparative preference grounded in UF-16 and local review requirements.

## 5. Cross-cutting invariants

These requirements are jointly non-compensating:

1. **Truthful state and completion:** `AR-COR-003..006`; no executor or UI narration can set completion.
2. **Durability and recovery:** `AR-DUR-001..006`; acknowledgement, restart, ambiguity, control, corruption, and cleanup remain explicit.
3. **Trust and capability boundaries:** `AR-SEC-001..005`, `AR-EXE-001/004`; untrusted content cannot grant authority and LLM judgment cannot replace hard controls.
4. **Approval and effects:** `AR-APR-001..003`; intent, approval, attempt, observed response, authoritative readback, confirmed result, and uncertainty remain distinct.
5. **Original user-state protection:** `AR-WSP-001..005`, `AR-GIT-001/002`; an allowed root is not ownership.
6. **Independent evidence and verification:** `AR-EVD-001..003`, `AR-VER-001..003`; exact revision, deterministic evidence, bounded independent context, and stale invalidation are mandatory.
7. **Provider neutrality:** `AR-MOD-001..003`; product truth and role eligibility do not come from provider-native naming or fallback.
8. **Context safety:** `AR-DAT-001/002`, `AR-CTX-001/002`; compaction cannot delete or upgrade authority.
9. **Clean room:** `AR-SEC-005`; only project-derived Level A properties constrain architecture.
10. **Frozen-suite testability:** `AR-TST-001..003`; no candidate may rely on hidden production-only state.

A candidate that violates any item is ineligible even if it is faster, cheaper, easier to package, or preferred by a reviewer.

## 6. Quality-attribute coverage

| Required category | Architecture requirement coverage | Decision use |
|---|---|---|
| Correctness / false-completion resistance | `AR-COR-001..007`, `AR-VER-001..003` | Hard |
| Durability / restart / recovery / idempotency | `AR-DUR-001..006`, `AR-APR-002` | Hard |
| Security / authority / isolation / secrets | `AR-SEC-001..005`, `AR-WSP-001..005`, `AR-APR-001..003` | Hard |
| Local execution / process / Git control | `AR-EXE-001..004`, `AR-GIT-001/002` | Hard |
| Provider-neutral model abstraction | `AR-MOD-001..003` | Hard |
| Observability / truthful failures | `AR-OBS-001/002`, `AR-FAIL-001/002` | Hard |
| Extensibility / future compatibility | `AR-FUT-001..003`; `AR-PRF-004` beyond floor | Hard floor + preference |
| Performance / resource / cost | `AR-PERF-001/002`, `AR-TST-003`; `AR-PRF-001/005` | Hard instrumentation/bounds + empirical preference |
| Operability / maintainability / reversibility | `AR-PKG-001`; `AR-PRF-002/003/006` | Hard local-first floor + preference |
| E1-suite testability | `AR-TST-001..003`, `AR-EVD-001..003`, `AR-VER-001..003` | Hard |

## 7. Architecture decision-domain ownership

Every domain below is material because it owns at least one frozen-E1-derived requirement. Domain names match the 25-domain E2 plan. A candidate must answer the ownership question; an answer may identify a logical boundary without selecting a separate process.

| Domain ID | Plan domain | Architecture-driving requirements | Required ownership / authority question |
|---|---|---|---|
| `D01_CLIENT_INTERACTION_BOUNDARY` | Client / interaction boundary | `AR-COR-003`, `AR-CTX-001`, `AR-OBS-001`, `AR-OBS-002`, `AR-PKG-001`, `AR-PRF-001`, `AR-PRF-006`, `AR-SEC-001` | Who authenticates user intent, owns durable acknowledgement, and projects reconnect-safe state without becoming authoritative? |
| `D02_CORE_APPLICATION_RUNTIME` | Core application runtime | `AR-EXE-001`, `AR-FUT-001`, `AR-MOD-001`, `AR-PKG-001`, `AR-PRF-002`, `AR-SEC-001`, `AR-TST-001`, `AR-VER-001` | Which boundary owns provider-neutral semantic validation and canonical transition enforcement? |
| `D03_TASK_WORKFLOW_ORCHESTRATION` | Task / workflow orchestration | `AR-APR-001`, `AR-COR-001`, `AR-COR-002`, `AR-COR-003`, `AR-COR-004`, `AR-COR-005`, `AR-COR-007`, `AR-DUR-002`, `AR-DUR-004`, `AR-FAIL-001`, `AR-FAIL-002`, `AR-FUT-002`, `AR-PERF-001`, `AR-VER-003` | Which component may order work, transfer ownership, accept control, and derive terminal disposition? |
| `D04_DURABLE_STATE_PERSISTENCE` | Durable state / persistence | `AR-COR-001`, `AR-COR-007`, `AR-DUR-001`, `AR-DUR-002`, `AR-DUR-005`, `AR-DUR-006`, `AR-FUT-001`, `AR-PRF-002`, `AR-PRF-003`, `AR-PRF-005` | What is the supported acknowledgement boundary, writer authority, recovery unit, migration owner, and failure behavior? |
| `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL` | Canonical task / conversation / evidence model | `AR-COR-001`, `AR-COR-002`, `AR-COR-003`, `AR-COR-006`, `AR-CTX-001`, `AR-CTX-002`, `AR-DAT-001`, `AR-DAT-002`, `AR-DUR-001`, `AR-EVD-001` | Which records are authoritative, which are references/projections, and how are versions and causal links expressed? |
| `D06_EVENT_OPERATION_HISTORY` | Event / operation history | `AR-APR-001`, `AR-APR-002`, `AR-COR-001`, `AR-COR-002`, `AR-COR-006`, `AR-COR-007`, `AR-DAT-001`, `AR-DAT-002`, `AR-DUR-001`, `AR-DUR-002`, `AR-DUR-003`, `AR-DUR-005`, `AR-EVD-002`, `AR-EVD-003`, `AR-EXE-002`, `AR-TST-003`, `AR-VER-003` | How are intent, attempt, ordering, acknowledgement, readback, correction, and gaps retained without making telemetry authoritative? |
| `D07_FILESYSTEM_WORKSPACE_ABSTRACTION` | Filesystem / workspace abstraction | `AR-DUR-005`, `AR-DUR-006`, `AR-WSP-001`, `AR-WSP-002`, `AR-WSP-003`, `AR-WSP-004`, `AR-WSP-005` | How are repository/base/object identity, task ownership, stale detection, protected material, and cleanup boundaries represented? |
| `D08_EXECUTION_PROCESS_CONTROL` | Execution / process control | `AR-APR-003`, `AR-DUR-003`, `AR-DUR-004`, `AR-EXE-001`, `AR-EXE-002`, `AR-EXE-003`, `AR-EXE-004`, `AR-FAIL-002`, `AR-PERF-001`, `AR-PERF-002`, `AR-PRF-001`, `AR-SEC-004`, `AR-TST-001`, `AR-WSP-002` | Who owns dispatch, descendant authority, bounds, cancellation, fencing, output capture, and post-interruption reconciliation? |
| `D09_ISOLATION_SANDBOXING` | Isolation / sandboxing | `AR-EXE-003`, `AR-SEC-003`, `AR-WSP-001`, `AR-WSP-002`, `AR-WSP-003`, `AR-WSP-004`, `AR-WSP-005` | Which structural boundary enforces filesystem/process/secret/network limits and what unsupported assumptions remain? |
| `D10_GIT_INTEGRATION` | Git integration | `AR-APR-003`, `AR-COR-006`, `AR-EXE-004`, `AR-GIT-001`, `AR-GIT-002`, `AR-WSP-001`, `AR-WSP-002`, `AR-WSP-004` | How does each of the thirty actions resolve, what state is reread, and how are local, destructive, external-read, and remote effects kept distinct? |
| `D11_APPROVAL_PERMISSION_SYSTEM` | Approval / permission system | `AR-APR-001`, `AR-APR-002`, `AR-APR-003`, `AR-COR-002`, `AR-EXE-001`, `AR-FUT-002`, `AR-GIT-001`, `AR-SEC-001`, `AR-SEC-002`, `AR-SEC-003` | Which authority issues grants/approvals, how are exact scope and revocation enforced, and where is consumption serialized with dispatch? |
| `D12_EXTERNAL_EFFECT_RECONCILIATION` | External-effect reconciliation | `AR-APR-002`, `AR-DUR-003`, `AR-DUR-004`, `AR-EXE-003`, `AR-GIT-001`, `AR-GIT-002` | What is authoritative readback per effect and how are unknown acknowledgement, duplicate requests, stop, and recovery reconciled? |
| `D13_MODEL_PROVIDER_GATEWAY` | Model / provider gateway | `AR-FAIL-001`, `AR-FUT-003`, `AR-MOD-001`, `AR-MOD-002`, `AR-MOD-003`, `AR-PERF-001`, `AR-PERF-002`, `AR-PRF-003`, `AR-SEC-003`, `AR-SEC-004`, `AR-TST-003` | Where are provider-specific semantics contained and requested/resolved identity, data policy, usage, cost, failure, and cancellation retained? |
| `D14_ROUTING_CAPABILITY_DISCOVERY` | Routing / capability discovery | `AR-EXE-001`, `AR-EXE-004`, `AR-FUT-003`, `AR-MOD-001`, `AR-MOD-002`, `AR-MOD-003`, `AR-SEC-002`, `AR-SEC-004` | Who owns capability evidence, route purpose/eligibility, no-hidden-fallback policy, and zero-dispatch denial? |
| `D15_CONTEXT_MEMORY_COMPACTION` | Context / memory / compaction | `AR-CTX-001`, `AR-CTX-002`, `AR-DAT-001` | What durable manifest reconstructs working context and how are summaries versioned, trusted, invalidated, and prevented from granting authority? |
| `D16_VERIFICATION_ARCHITECTURE` | Verification architecture | `AR-COR-004`, `AR-COR-005`, `AR-COR-006`, `AR-MOD-001`, `AR-TST-001`, `AR-TST-002`, `AR-VER-001`, `AR-VER-002`, `AR-VER-003` | How is verifier execution separated, exact state bound, deterministic evidence rederived, adequacy judged, and infrastructure error represented? |
| `D17_EVIDENCE_ARTIFACT_SYSTEM` | Evidence / artifact system | `AR-APR-002`, `AR-COR-004`, `AR-COR-005`, `AR-COR-006`, `AR-DAT-002`, `AR-DUR-006`, `AR-EVD-001`, `AR-EVD-002`, `AR-EVD-003`, `AR-GIT-002`, `AR-OBS-002`, `AR-PRF-005`, `AR-SEC-005`, `AR-TST-002`, `AR-VER-001`, `AR-VER-002` | Who owns bundle validation, artifact identity, redaction, large-output references, integrity/gap state, and final disposition evidence? |
| `D18_OBSERVABILITY_LOGGING` | Observability / logging | `AR-DAT-001`, `AR-DUR-004`, `AR-EVD-001`, `AR-EVD-003`, `AR-EXE-002`, `AR-FAIL-001`, `AR-MOD-003`, `AR-OBS-001`, `AR-OBS-002`, `AR-PERF-002`, `AR-PRF-001`, `AR-PRF-005`, `AR-TST-003` | Which operational signals answer user/operator questions and how are they prevented from becoming authority or completion evidence? |
| `D19_ERROR_FAILURE_MODEL` | Error / failure model | `AR-COR-003`, `AR-DUR-002`, `AR-DUR-003`, `AR-DUR-005`, `AR-EXE-002`, `AR-FAIL-001`, `AR-FAIL-002`, `AR-MOD-003`, `AR-OBS-001`, `AR-PRF-002`, `AR-VER-003` | Which layer owns a failure, is it retryable, what state consequence follows, and how are unknown/invariant failures preserved? |
| `D20_SECURITY_BOUNDARIES` | Security boundaries | `AR-APR-001`, `AR-APR-003`, `AR-CTX-002`, `AR-DAT-002`, `AR-DUR-006`, `AR-EVD-002`, `AR-EVD-003`, `AR-EXE-001`, `AR-EXE-003`, `AR-EXE-004`, `AR-FAIL-002`, `AR-GIT-001`, `AR-MOD-002`, `AR-PERF-001`, `AR-SEC-001`, `AR-SEC-002`, `AR-SEC-003`, `AR-SEC-004`, `AR-SEC-005`, `AR-TST-002`, `AR-VER-001`, `AR-WSP-001`, `AR-WSP-003`, `AR-WSP-004` | Which controls are structural, what is untrusted, where do secrets/capabilities/effects cross, and what threat boundary is explicitly unsupported? |
| `D21_LOCAL_FIRST_PACKAGING` | Local-first packaging | `AR-EVD-002`, `AR-GIT-002`, `AR-PKG-001`, `AR-PRF-002`, `AR-PRF-003`, `AR-PRF-006`, `AR-SEC-005` | What local components/state/migrations/security assumptions are visible and what can work without an undeclared service? |
| `D22_FUTURE_REMOTE_EXECUTION` | Future remote execution | `AR-FUT-001`, `AR-PKG-001`, `AR-PRF-003`, `AR-PRF-004` | Which versioned identity/control/evidence interfaces remain replaceable across a machine boundary and what remains explicitly unsupported? |
| `D23_FUTURE_CONCURRENCY_MULTI_AGENT` | Future concurrency / multi-agent | `AR-COR-007`, `AR-FUT-002`, `AR-PRF-004`, `AR-WSP-005` | Which ownership/version/scoping contracts prevent singleton lock-in while avoiding v0.1 multi-agent implementation? |
| `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY` | Extension / skill / connector boundary | `AR-FUT-001`, `AR-FUT-002`, `AR-FUT-003`, `AR-PRF-006`, `AR-SEC-002`, `AR-SEC-005` | How must an extension declare authority, contracts, provenance, limits, tests, and compatibility without bypassing core policy? |
| `D25_E1_SUITE_TESTABILITY` | Testability against the E1 suite | `AR-COR-004`, `AR-COR-005`, `AR-EVD-001`, `AR-FUT-003`, `AR-PERF-002`, `AR-TST-001`, `AR-TST-002`, `AR-TST-003`, `AR-VER-002` | Where are deterministic seams, fault controls, readbacks, clocks/counters, fixture adapters, and oracle-visible state for the frozen suite? |

Cross-cutting requirements intentionally appear in several domains. Physical colocation is permitted, but a candidate may not erase the distinct authority, trust, recovery, and verification ownership questions.

## 8. Prospective weighting governance

No weights, candidate scores, rankings, or winner are assigned here. If E2-003 uses weights, it must:

1. reject or quarantine every candidate with a failed hard constraint before scoring;
2. freeze criterion definitions, direction, evidence scale, missing/unknown treatment, weights, and tie/decision rule before candidate-specific scores or a winner are calculated;
3. assign `UNKNOWN_REQUIRING_SPIKE` no favorable/neutral surrogate and route selection-blocking unknowns to E2-004;
4. disclose correlations and avoid accidental double counting, at minimum across:
   - durability, recovery, evidence integrity, and correctness;
   - security, capability scope, approval, effect reconciliation, and isolation;
   - local packaging, maintainability, migration, and contributor burden;
   - remote compatibility, concurrency compatibility, and reversibility;
   - latency, local overhead, evidence overhead, and cost;
5. report sensitivity to plausible alternative weight/group choices and identify any winner instability;
6. use only comparable evidence with explicit confidence/unknowns; and
7. preserve every frozen E1 expected outcome and non-compensating release blocker.

The six weighted preference requirements are `AR-PRF-001..006`. Their weights remain **UNASSIGNED**.

## 9. E3 validation-obligation register

These obligations are postselection validation contracts, not permission to run work and not a place to defer an E2 architecture blocker.

| Obligation ID | Question | Source architecture requirements | Required future evidence | Failure / reversal condition | Unknown owner class |
|---|---|---|---|---|---|
| `E3V-001` | Durability, restart, and ambiguous-effect recovery | AR-COR-001/007; AR-DUR-001/002/003/005; AR-APR-002; AR-TST-001/002 | Interrupt at acknowledgement, persistence, ownership transfer, dispatch, receipt, readback, and partial-write boundaries; verify exact recovery, no duplicate effect, preserved original evidence, and explicit uncertainty. | Any acknowledged loss, stale-writer acceptance, fabricated continuity, duplicate consequential effect, or unreconciled corruption is a hard failure and triggers candidate rejection/reversal. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-002` | Bounded process control and fencing | AR-DUR-004; AR-EXE-002/003; AR-TST-001/002 | Exercise cooperative pause/stop, force termination/fencing, descendant accounting, output bounds, timeout, and interruption across supported host/process classes. | Any permanently unaccountable descendant, post-stop productive dispatch, unbounded STOPPING, or kill-as-completion is a hard failure. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-003` | Workspace isolation, repository conditions, and local packaging | AR-DUR-006; AR-WSP-001..005; AR-GIT-001; AR-PKG-001; AR-PRF-006 | Materialize all sixteen repository conditions, path/link/special-file attacks, dirty/untracked/generated state, stale workspace, cleanup, and contributor setup against the declared local support matrix. | Any original-user-state loss, root escape, premature mutation, cross-task cleanup, or undeclared mandatory service is a hard failure; unsupported conditions must remain explicit. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-004` | Provider gateway, routing, and provider-specific semantics | AR-MOD-001..003; AR-SEC-004; AR-FAIL-001; AR-TST-001/002 | Use offline controlled provider-shape replays first; under separate later authorization, validate capability discovery, purpose/eligibility, zero-dispatch denial, fallback, cancellation, errors, provenance, usage/cost, and data policy. | Hidden fallback/class elevation, unattributed result, disallowed dispatch, or provider-native state replacing product truth is a hard failure. | `E3_EMPIRICAL_VALIDATION; any real/paid call remains separately gated` |
| `E3V-005` | Evidence and independent verification architecture | AR-COR-003..006; AR-DAT-001/002; AR-CTX-001/002; AR-EVD-001..003; AR-VER-001..003 | Materialize evidence profiles, revisions, stale mutation, gap/tamper, bounded verifier context, deterministic replay, predicate adequacy, verifier error, correction, and large-output references. | Any false completion, executor-self-report-only verification, stale pass, missing material evidence, or telemetry-as-authority is a hard failure. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-006` | Security and authority negative suite | AR-EXE-001/004; AR-SEC-001..005; AR-APR-001/003; AR-TST-001/002 | Run all twenty-three security-negative families and sixteen dangerous compositions with synthetic secrets/canaries and structurally enforced zero-effect/readback oracles. | Any unauthorized read/effect, secret marker exposure, approval replay, destructive user-state action, capability escape, or clean-room violation is a hard failure. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-007` | Reliability, latency, resource, and cost protocols | AR-OBS-001; AR-FAIL-002; AR-TST-003; AR-PERF-001/002; AR-PRF-001/005 | Freeze reference environment, populations, strata, finite policy values, and uncertainty handling before runs; execute the eight protocols only under E3 authority and report raw/aggregate values without post-result redefinition. | Missing required instrumentation or ceiling enforcement is an architecture hard failure; observed threshold failure follows the frozen E3 gate/reversal rule and cannot be averaged away. | `E3_EMPIRICAL_VALIDATION` |
| `E3V-008` | Logical-role and configuration eligibility | AR-MOD-001..003 | Under the benchmark plan and separately authorized scope/budget/data/credential policy, benchmark candidate systems/configurations as EVALUATION_ONLY and retain route/model/tool/cost/latency provenance. | Evaluation evidence never self-promotes; DISALLOWED or unauthorized routes dispatch nothing; failure leaves the role unassigned and may reverse a dependent architecture assumption. | `E3_MODEL_OR_CONFIGURATION_BENCHMARK` |

E2-005 must bind each retained obligation to the proposed ADR/reversal package and register the owner/review path for finite verification-rerun, deterministic-check-repetition, and correction-attempt values. E2-006 must independently verify that none is an unresolved preselection architecture question in disguise.

## 10. Frozen-suite testability contract

The resulting design must later materialize, without changing expected outcomes:

| Frozen evaluation asset | Count | Required architecture seam |
|---|---:|---|
| Evaluation cases | 170 | Task/operation/control/routing/effect/evidence/verification state injection and readback |
| Oracle classes | 18 | Deterministic state, Git, repository, policy-zero-effect, effect-stub, check replay, evidence, route, secret-marker, resource, recovery, clean-room, contributor, bounded-judgment, and metric-protocol interfaces |
| Fixture families | 11 | Clean-room deterministic construction with explicit initial state, fault schedule, mutation regions, canaries, and expected end state |
| Security-negative families | 23 | Structural policy boundaries and zero-effect/readback evidence |
| Repository conditions | 16 | Admission matrix identity/disposition and conservative composition |
| Git/effect classifications | 30 | Independent effect/disposition/approval classification and state readback |
| Predicate-adequacy variants | 9 | Hidden harness obligation graph and decisive ground truth |
| Dangerous compositions | 16 | Cross-boundary ordering/fault control without combinatorial expansion |
| Reliability protocols | 8 | Stable populations, timestamps, strata, outcomes, uncertainty, cost/usage, and candidate identity |

Choices that hide authority only inside a model context, expose only a final UI projection, cannot inject failures at acknowledgement/dispatch/readback boundaries, cannot distinguish intent from effect, or require inaccessible production-only state fail `AR-TST-001/002`.

## 11. Performance, resource, cost, and unknown ownership

No new numerical threshold is introduced.

| Unknown class | Items owned by that class |
|---|---|
| `E2_DESIGN_PARAMETER` | Supported local persistence boundary; acknowledged-mutation boundary; supported repository/host/capability classes; operation/control ownership; finite-limit owner and policy interface; evidence large-output/reference contract; migration/reversal declaration. |
| `E3_EMPIRICAL_VALIDATION` | Restart/control/cancellation latency; isolation/process-control feasibility; local resource overhead; evidence/output overhead; provider/tool latency; actual cost/usage; reliability protocol results; SLO threshold satisfaction in a frozen reference environment. |
| `E4_IMPLEMENTATION_CONFIGURATION` | Concrete defaults within independently reviewed finite-ceiling policy; adapter-specific time/output limits; supported build/package configuration; implementation migration tooling, only after authorization. |
| `FUTURE_PRODUCT` | Cloud/multi-tenant SLAs, multi-user quotas, multi-agent scheduling, connector marketplace policy, General/Finance product thresholds, and SaaS operations. |

Interactive responsiveness, cancellation responsiveness, bounded local overhead, and evidence/output size handling are comparative only after the hard bounds and test seams pass.

## 12. Future-compatibility floor

Compatibility is operationalized as explicit identity/ownership fields, versioned serializable logical contracts, replaceable implementation boundaries, visible migration/unsupported assumptions, no irreversible single-process/machine-path/provider truth, and no global mutable authority dependency. This applies to later remote workers, cloud execution, concurrent tasks, multiple agents/clients, skills/routines/connectors, General Edition, Finance Edition, and SaaS.

It does **not** require remote execution, distributed consensus, multiple agents, multiple users, multi-tenancy, connector loaders, schedules, finance schemas, or SaaS operations in v0.1. A candidate satisfies the hard floor by preserving the boundary and rejecting unsupported cross-scope use; comparative ease beyond that floor is `AR-PRF-004`.

## 13. Level A / B / C reconciliation

External-audit evidence is non-authoritative. Level A properties are independently re-derived from E1; Level B patterns may be examined by E2-002; Level C details must not constrain or contaminate E2.

| Audit-derived idea | Level A contribution | Level B candidate pattern | Level C exclusion |
|---|---|---|---|
| Content-addressed canonical state | Stable identity, version, conflict/integrity and recovery properties are Level A. | Content addressing is a Level B candidate pattern only; E1 does not require it. | Any reconstructed manifest/blob layout, hash algorithm, namespace, or module name is Level C and nonbinding. |
| Derived transcript projections | Authoritative-versus-derived separation and rebuildability are Level A. | A derived transcript/projection with recovery is a Level B pattern. | External file routes, projection codecs, and internal identifiers are Level C. |
| Typed error registry | Semantically distinguishable failure layers and consequences are Level A. | A typed registry/hierarchy is a Level B pattern. | Exact external codes, class names, inheritance, and module layout are Level C. |
| Operation journal | Stable operation identity, causal accounting, readback, retry, and gaps are Level A. | A journal is a Level B pattern. | External journal schema, storage engine, and internal operation names are Level C. |
| Provider router | Purpose/eligibility, explicit fallback, provenance, and provider-specific semantics are Level A. | A gateway/router topology is a Level B pattern. | Specific SDKs, provider adapters, routes, and reconstructed identifiers are Level C. |
| Explicit task/execution state | Separate task/operation/verification/effect semantics are Level A. | A particular state-machine or reducer layout is Level B. | External enum names, module boundaries, and implementation files are Level C. |
| Structured approvals | Exact durable approval semantics are Level A. | A particular approval record/service design is Level B. | External schema fields/names or UI implementation are Level C. |
| Local/remote execution abstraction | Stable versioned operation/control/evidence interfaces and no machine-path lock are Level A. | A local/remote executor abstraction is Level B. | Specific worker protocols, transports, cloud lifecycle, and external internal names are Level C. |
| Context summary blocks | Compaction safety, provenance, invalidation, and no authority loss are Level A. | Structured summary blocks are Level B. | Exact block format, memory framework, retrieval stack, and reconstructed names are Level C. |
| Cloud-agent lifecycle patterns | Durable identity, ownership transfer, recovery, control, and effect reconciliation are Level A. | Remote-worker lifecycle patterns are Level B for later comparison. | External cloud orchestration topology, services, statuses, and module names are Level C. |

The architecture adoption matrix therefore supplies questions and pattern hypotheses only. No classification, score, reconstructed name, exact data layout, module boundary, or technology from that matrix is adopted by this task.

## 14. E2-002 candidate-description input contract

E2-002 must generate genuinely different end-to-end candidates. For **each** candidate it must provide one self-contained description with these required fields:

1. **Candidate identity:** stable ID, version, author, date, frozen E1 and `EP-ARCH-REQ-0.1` revisions.
2. **System shape:** components and responsibilities, including what is colocated versus separated and why.
3. **Client/interaction boundary:** authenticated intent, durable acknowledgement, reconnect projection, user control, approval display, and evidence inspection.
4. **Process boundaries:** owner of orchestration, execution, verification, provider calls, persistence, and control/fencing.
5. **Trust boundaries and threat model:** user/founder authority, untrusted repository/tool/model/web/connector input, secrets, filesystem, network, terminal, package/Git surfaces, providers, UI/control, and explicitly unsupported host-compromise assumptions.
6. **Authoritative state ownership:** authoritative/derived/ephemeral/lossy classification, canonical writers, versions, causal history, projections, and stale-writer rules.
7. **Operation model:** intent, validation, dispatch, process tree, bounds, output, cancellation, retryability, effect class, result, and correlation.
8. **Persistence semantics:** acknowledgement boundary, durability scope, versioning, corruption/partial-write behavior, retention, migration, backup/restore assumptions, and evidence preservation.
9. **Recovery model:** client/orchestrator/worker/executor/verifier/machine interruption, acknowledgement loss, duplicate/reordered request, stale workspace, partial write, pause/redirect/stop/force/fence, approval recovery, effect reconciliation, and verification invalidation.
10. **Workspace/execution model:** repository admission, sixteen condition dispositions, base identity, bind-before-mutation isolation, path/link/special/archive defenses, original user-state protection, cleanup, and future task noninterference.
11. **Git model:** all thirty classification semantics, authority scoping, hooks/helpers, exact state readback, local/remote separation, draft-package behavior, and prevention of additional unauthorized actions.
12. **Approval/effect model:** exact durable approval scope/revocation/replay/recovery and distinct intent, approval, attempt, observed response, authoritative readback, confirmed effect, known non-success, and unknown effect.
13. **Model/provider boundary:** provider-neutral core, logical roles, capability discovery, purpose/eligibility, zero-dispatch denial, explicit fallback, provider-specific semantics, routing/model/tool provenance, cost/latency, and offline/EVALUATION_ONLY behavior.
14. **Context/memory model:** bounded invocation context, durable conversation/task/evidence outside it, context-manifest assembly, compaction provenance, invalidation, and resume reconstruction.
15. **Evidence/artifact model:** version/profile, stable identity, exact revision, large-output references, actor/model/tool/command/check/approval/effect/failure/retry/predicate/verifier provenance, integrity/gap/tamper/staleness, redaction, limitations, and final disposition.
16. **Independent-verification path:** exact candidate binding, separate mutable context, deterministic replay/readback, predicate adequacy, verifier identity/configuration, infrastructure-error handling, rerun ceiling ownership, correction, and stale invalidation.
17. **Observability/failure model:** structured answers required by `AR-OBS-001`, telemetry/evidence separation, typed failure layers, recovery reasons, and no chain-of-thought dependency.
18. **Security control ownership:** which protections are structurally enforced outside LLM judgment and where each policy decision is made and validated.
19. **Packaging and local-first behavior:** supported host/runtime assumptions, local components/state, setup/update/migration/cleanup, offline limitations, contribution/test/security workflow, and no hidden mandatory service state.
20. **Future compatibility:** explicit remote, concurrency, multi-agent/client/principal, extension, General/Finance, and SaaS seams plus what is deliberately not implemented.
21. **Requirement trace:** all 127 canonical E1 IDs and all architecture requirement IDs, with `SATISFIED_BY_DESIGN`, `FAILED_HARD`, or `UNKNOWN`; evidence and owner; no missing/waived entry.
22. **Decision-domain trace:** answers for all 25 ownership questions, including cross-cutting interactions.
23. **Testability trace:** seam/fixture/oracle/readback for all frozen suite asset families; any unsupported case is explicit and cannot be called pass.
24. **Known weaknesses and assumptions:** facts, inferences, proposals, unknowns, unsupported environments, security limits, and correlated risks separated.
25. **Selection uncertainties:** paper-resolvable questions, possible `UNKNOWN_REQUIRING_SPIKE` items with why existing evidence is insufficient, and E3 obligations; E2-002 does not run a spike.
26. **Migration and reversibility profile:** irreversible decisions, export/migration path, rollback limits, retained evidence, replacement boundaries, failure/reversal triggers, and estimated evidence confidence without a candidate score.
27. **Level A/B/C record:** each borrowed pattern labeled Level B, independent E1 reason stated, and Level C details excluded.
28. **E3 handoff:** candidate-specific mapping to `E3V-001..008`, validation evidence, failure/reversal consequence, and proposed ADR linkage.

A candidate description is structurally invalid if it omits a hard-constraint mapping, treats an unknown as favorable, uses executor/model self-report as sole proof, lacks credible security/recovery/evidence/verification paths, relies on hidden production-only state, silently changes E1 expected outcomes, or anchors authority in the reconstructed reference. E2-002 may describe mechanisms and weaknesses but may not score, rank, or select a winner.

## 15. Unresolved architecture questions

These are questions for later E2 ownership, not hidden choices and not declared spikes:

| Question ID | Question | Owner / next treatment |
|---|---|---|
| `AQ-001` | What candidate boundary owns canonical writes, durable acknowledgement, and ownership transfer while preserving `AR-DUR-001` and `AR-COR-007`? | E2-002 describes; E2-003 compares; spike only if still selection-blocking. |
| `AQ-002` | What exact local persistence failure boundary is supported across process and machine restart, and what is explicitly unsupported? | Candidate declaration; validate under `E3V-001`. |
| `AQ-003` | What isolation strength and host/repository support matrix can enforce workspace, path, process, secret, and network constraints? | Candidate declaration; E2-003 determines whether feasibility needs E2-004; validate under `E3V-003/006`. |
| `AQ-004` | How are descendant force termination and authority fencing made truthful across supported process classes? | Candidate declaration; possible E2-004 feasibility question; validate under `E3V-002`. |
| `AQ-005` | Which source is authoritative readback for each optional external effect, and which capabilities must remain unsupported when readback is unavailable? | E2-002 capability/effect contract; validate under `E3V-001`. |
| `AQ-006` | How are evidence completeness, integrity/gap detection, large-output references, retention, and migration realized without conflating telemetry with authority? | E2-002 evidence/persistence description; validate under `E3V-005`. |
| `AQ-007` | What local packaging/update/migration shape is contributor-operable and reversible? | E2-002 candidate declaration; compare under weighted preferences; validate under `E3V-003`. |
| `AQ-008` | What finite values and accountable review path govern operation limits, verification reruns, deterministic repetitions, and correction attempts? | Ownership interface in E2; concrete values prospectively registered no later than E2-005/E3 freeze, never inferred from results. |
| `AQ-009` | Which provider/model/configurations are eligible for logical roles? | E3 only under `E3V-008`; E2 assigns none. |

No preselection architecture spike is authorized or run by E2-001. E2-003 owns classification of any candidate-specific unresolved fact; E2-004 owns bounded execution only after that classification.

## 16. Nonselection and governance boundary

This baseline selects no client, language, runtime, database, event store, workflow engine, queue, sandbox, container, virtual machine, cloud, agent/model framework, provider, model, verification occupant, packaging system, or Git invocation strategy. It creates no ADR and accepts none. Content addressing, projection journals, typed-error registries, routers, local/remote executors, summary blocks, and cloud-worker lifecycle patterns remain Level B possibilities only.

The E1 artifacts remain frozen. E2-002 remains BACKLOG until E2-001 is independently VERIFIED. E3 remains NOT_STARTED; all evaluation cases, spikes, benchmarks, and paid calls remain at zero. Architecture remains NOT_SELECTED, application code remains absent, autonomy remains NOT_ELIGIBLE / NOT_AUTHORIZED, and S1-003 remains deferred.
