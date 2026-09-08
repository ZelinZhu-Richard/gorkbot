# Engineering Preview Stage E2 architecture plan

Status: **AUTHOR planning artifact — PLANNED, NOT EXECUTED, NOT INDEPENDENTLY VERIFIED**
Mode: `PLAN_STAGE_E2`
Recorded: 2026-08-28
Base commit: `c2f70931ce13d0619a0dff4f48951e9278bb0c1c`
Authority: D-016, the independently verified E1 gate, and the repository governance records
Architecture status: **NOT_SELECTED**

This artifact defines the work required to select and verify an Engineering Preview architecture. It does not perform any E2 task, recommend a candidate, create or accept an ADR, choose a technology, run a spike or evaluation case, make a provider call, or authorize implementation.

## 1. Frozen input and decision question

The frozen E1 input is the independently verified charter, PRD, user flows, correctness contract, contribution workflow, evaluation suite `EP-EVAL-0.2`, release-acceptance specification, and E1 gate record. E2 answers implementation **how** against that frozen **what**.

E2 decision question:

> What architecture should implement the independently verified Engineering Preview specification, and what evidence is required before that architecture may be considered selected?

E2 must transform the frozen product, correctness, evaluation, security, and reliability requirements into:

```text
architecture requirements and decision criteria
  -> credible end-to-end alternatives
  -> hard-constraint and trade-off comparison
  -> bounded closure of selection-blocking uncertainty
  -> proposed ADR set and architecture baseline
  -> independent architecture verification
  -> independent E2 stage gate and explicit E3 obligations
```

Any candidate that cannot satisfy E1 loses. E2 may choose mechanisms; it may not weaken, reinterpret, average away, or silently amend E1 semantics.

## 2. Architecture-driving quality attributes

The following properties are derived requirements, not observed implementation results. No new quantitative threshold is introduced here.

| Attribute | Architecture-driving properties | Decision consequence |
|---|---|---|
| Correctness | False-completion prevention; exact candidate and repository-revision binding; adequate predicates; independent verification; evidence integrity; distinct task, control, reconciliation, attempt, operation, verification, and agent responsibilities. | A design must make invalid completion structurally rejectable and independently checkable. An ambiguous fused status or executor-self-report-only design is a hard failure. |
| Durability | Stable task and request identity; recoverable acknowledgement; restart/resume after orchestrator or worker loss; partial-write handling; idempotency; duplicate-request replay; lost-acknowledgement and uncertain-effect reconciliation. | A candidate without an explicit persistence boundary, mutation protocol, recovery owner, and no-blind-replay rule is ineligible. |
| Security | Repository, issue, tool, model, connector, and web content remain untrusted; deny by default; least privilege; protected-secret precedence; path/symlink isolation; process-descendant and Git-hook/package-script control; network policy; exact approval semantics; destructive-action boundaries. | Threat and capability boundaries are evaluated before selection. Prompt instructions, names, descriptions, or caller assertions cannot grant authority. |
| Execution | Local-first repository work; isolated workspace; filesystem, terminal, process, Git, and test lifecycle; pause/stop/redirect/resume; timeouts; force termination or fencing; effect accounting and readback. | The design must explain ownership and safe endpoints through interruption and recovery, not only the happy path. |
| Model abstraction | Provider-neutral logical roles; separate `route_purpose` and `route_eligibility`; capability discovery; explicit unsupported behavior; visible fallback; exact configuration and routing provenance. | Core state and authority cannot depend on a permanent vendor or model assignment. Model and configuration eligibility remains an E3 decision. |
| Observability | Truthful task and operation state; approvals; recovery; artifacts; evidence; failures; routes; resource/cost attribution; distinct telemetry, audit, evidence, and presentation responsibilities. | Evidence cannot be reduced to logs, and telemetry cannot be sole proof of an effect or completion. |
| Extensibility | Local-to-remote execution seam; identities and versions that do not permanently assume one writer, agent, or client; bounded extension/skill/connector boundary; shared-core compatibility with General and Finance Editions and later SaaS. | Compatibility is a constraint, not authorization to implement cloud, multi-agent, multi-tenant, Finance, or SaaS features in v0.1. |
| Performance and cost | Interactive control where E1 requires it; bounded local resource use; measurable provider/tool/infrastructure cost; diagnosable overhead; future scaling path. | Candidates must expose measurement and budget boundaries. This plan invents no latency, throughput, or cost target. |
| Operability and maintainability | Inspectable state, typed failures, migration/reversal path, contributor-accessible local setup, debuggability, bounded operational burden. | Complexity and lock-in are weighted preferences after every hard constraint passes. |
| Testability | Deterministic seams for the 170 specified cases, 18 oracles, 11 fixture families, 9 predicate-adequacy variants, 16 compositions, and 8 measurement protocols. | A candidate that cannot be exercised against the frozen suite is ineligible even if its prose design sounds compliant. |

E2-001 must trace every one of the 127 canonical E1 requirement IDs to a hard architecture constraint, a weighted preference, or a justified non-architecture-driving disposition. A non-architecture-driving disposition does not waive the requirement.

## 3. External-audit Level A / B / C discipline

| Level | E2 treatment | Prohibition |
|---|---|---|
| A — required system property | Treat as a constraint only where independently authoritative E1/D-016/security/evidence rules require it. The verified audit may corroborate or suggest tests. | Do not cite the reconstruction as the authority for the property. |
| B — pattern worth evaluating | Admit as one input to alternative generation and compare against genuinely different patterns. | An audit label such as ADOPT or ADAPT cannot become an ADR decision or substitute for comparison. |
| C — reconstruction-specific detail | Retain only as bounded research context or a negative clean-room check. | Do not copy source, schemas, names, module boundaries, file layouts, client machinery, renderer compatibility, local-store choices, assets, copy, or provider integrations. |

No choice may be justified solely by “Grok Bot did it this way.”

## 4. Required architecture decision domains

Every end-to-end candidate, matrix, selected baseline, and independent verification must explicitly cover all 25 domains below.

| # | Domain | Required E2 question and evidence |
|---:|---|---|
| 1 | Client / interaction boundary | Which client responsibilities are authoritative or derived, and how do authentication, control acknowledgement, reconnect, and multiple future clients cross the boundary? |
| 2 | Core application runtime | Which process or service owns policy and domain invariants, and what is the local lifecycle and crash boundary? |
| 3 | Task / workflow orchestration | Who owns dispatch, transition legality, retries, control, deadlines, leases or equivalent ownership, and terminal disposition? |
| 4 | Durable state / persistence | What is durably acknowledged, how are atomicity, versions, migration, corruption, backup/restore, and the declared persistence boundary handled? |
| 5 | Canonical task / conversation / evidence model | Which responsibilities are authoritative, how are they correlated, and which combinations may share a transaction without becoming semantically fused? |
| 6 | Event / operation history | What immutable or append-only history exists, what is reconstructible, and how are causality, ordering, retention, gaps, and schema evolution handled? |
| 7 | Filesystem / workspace abstraction | How are admitted repository state, task workspace, artifacts, temporary data, paths, symlinks, cleanup, stale workspaces, and future remote storage represented? |
| 8 | Execution / process control | How are commands and descendants launched, observed, timed out, paused, stopped, forcibly fenced, reconciled, and accounted for? |
| 9 | Isolation / sandboxing | What isolation properties and limitations are declared and testable for local v0.1, without claiming a stronger tier or selecting a technology prematurely? |
| 10 | Git integration | How are repository admission, dirty state, work isolation, hooks/helpers, refs, commits, review packages, prohibited operations, and exact revision binding enforced? |
| 11 | Approval / permission system | How are capability, action class, actor, target, scope, policy/version, expiry, revocation, and one-shot approval bound to execution? |
| 12 | External-effect reconciliation | How are idempotency, dispatch ambiguity, lost acknowledgement, receipts, fresh readback, duplicate prevention, and uncertain outcomes represented? |
| 13 | Model / provider gateway | What provider-neutral contract exists, which provider semantics remain explicit, and how are exact identity, streaming, tool calls, refusal, failures, usage, and fallback preserved? |
| 14 | Routing / capability discovery | How are route purpose, route eligibility, capability availability, cost/latency limits, unsupported behavior, and provenance evaluated without choosing role occupants? |
| 15 | Context / memory / compaction | How are lossy working context, durable conversation, memory, execution history, and authoritative evidence separated, versioned, invalidated, and recovered? |
| 16 | Verification architecture | How can a verifier independently obtain the exact candidate, predicates, deterministic results, state readbacks, and failure evidence rather than trusting executor narration? |
| 17 | Evidence / artifact system | How are bundles, artifacts, receipts, checks, approvals, routes, verifier identity, integrity, retention, privacy, and final disposition bound and validated? |
| 18 | Observability / logging | What belongs in operational telemetry, durable audit, evidence, user presentation, and cost accounting; how are drops and redaction visible? |
| 19 | Error / failure model | How are stable error identity, accountable layer, retryability, user-safe detail, internal correlation, unknown failures, and escalation represented? |
| 20 | Security boundaries | Where are trust, identity, secret, network, process, path, provider, connector, policy, and evidence-integrity boundaries, and what fails closed? |
| 21 | Local-first packaging | How is a contributor-accessible local system installed, started, updated, migrated, recovered, and removed with bounded overhead and no selected packaging technology in this plan? |
| 22 | Future remote execution | Which contract seam permits later remote workers or cloud execution without forcing cloud infrastructure into v0.1? |
| 23 | Future concurrency / multi-agent | Which identities, versions, causality, ownership, fencing, and conflict rules avoid permanent singleton assumptions without implementing visible multi-agent features now? |
| 24 | Extension / skill / connector boundary | How can later skills, routines, connectors, clients, and vertical packs be governed, versioned, least-privileged, revoked, migrated, and kept outside the shared core? |
| 25 | Testability against the E1 suite | Which seams, deterministic substitutes, fault points, state inspectors, readbacks, and evidence outputs allow every applicable frozen case and protocol to be implemented later? |

## 5. Registered E2 task graph

`01_governance/TASK_REGISTRY.yaml` is authoritative for the executable task contracts. This table is a planning projection.

| Task | Responsibility | Planning status | Selection authority |
|---|---|---|---|
| `E2-001` | Derive and independently verify architecture requirements, traceability, quality attributes, and decision-criterion governance. | `READY`; not executed | None |
| `E2-002` | Generate at least three credible, materially different, end-to-end candidate architectures covering all 25 domains. | `BACKLOG` on `E2-001` | None |
| `E2-003` | Compare candidates using the frozen hard/preference/unknown matrix and classify every uncertainty. | `BACKLOG` on `E2-002` | None; no winner may be named |
| `E2-004` | Close every pre-selection architecture blocker through bounded analysis or a prospectively contracted E2 spike; record a verified no-spike disposition if none is required. | `BACKLOG` on `E2-003` | None |
| `E2-005` | Produce a challenged ADR set, proposed architecture baseline, and E3 validation-obligation plan. | `BACKLOG` on `E2-004` | Proposed only; ADRs remain pending independent architecture verification |
| `E2-006` | Independently re-derive E1 compliance, verify the selected baseline, threat/recovery/evidence models, ADR coherence, and E3 readiness. | `BACKLOG` on `E2-005` | May establish a verified architecture baseline; cannot pass the E2 stage gate itself |
| `VERIFY_STAGE_E2` | Separate mode-level stage-gate verification, following the E1 gate precedent; not a normal task ID. | Not eligible until `E2-001..006` are `VERIFIED` | May pass or reject E2; may not redesign the baseline |

Dependency graph:

```text
E0-001 VERIFIED + E1-001 VERIFIED + E1-002 VERIFIED + E1 GATE VERIFIED
  -> E2-001
  -> E2-002
  -> E2-003
  -> E2-004
  -> E2-005
  -> E2-006
  -> VERIFY_STAGE_E2
  -> E3 planning/execution may become eligible only under its separate prerequisites
```

The serial graph is deliberate: alternatives cannot race requirements, comparison cannot race alternative generation, spikes cannot be chosen before unknowns are classified, and ADR selection cannot precede uncertainty closure. A dependency is satisfied only by independent `VERIFIED`, not by author completion or `READY_FOR_REVIEW`.

## 6. Lifecycle and independence

For material authoring tasks `E2-001` through `E2-005`:

```text
AUTHOR -> READY_FOR_REVIEW -> independent CHALLENGER
       -> FIXER when findings require change
       -> independent post-fix VERIFIER -> VERIFIED or returned for correction
```

The E2-005 author may recommend one candidate and draft ADRs only as `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`. The author, challenger, fixer, and author-side assistants cannot perform E2-006. E2-006 must be a fresh architecture verifier that independently reconstructs the compliance case from the frozen E1 baseline and underlying artifacts. `VERIFY_STAGE_E2` must be a separate stage-gate session from E2-006.

The E2-005 challenger must aggressively inspect hidden E1 violations, hard constraints disguised as preferences, premature vendor/model lock-in, security and recovery gaps, evidence circularity, evaluation incompatibility, unjustified complexity, speculative future scope, poor reversibility, and clean-room contamination.

## 7. Alternative-generation strategy

E2-002 must construct at least three coherent end-to-end architectures. The alternatives must differ in consequential system shape across several axes such as client/runtime boundary, authority and persistence model, orchestration ownership, execution/isolation boundary, and local control-plane/execution-plane relationship. Merely swapping languages, frameworks, libraries, databases, or vendors inside the same shape does not create another candidate.

Each candidate must:

- cover all 25 decision domains and every E2-001 hard constraint;
- include authority, process, trust, data, control, effect, recovery, and verification boundaries;
- describe local v0.1 and compatibility seams separately;
- distinguish required now, interface reserved now, and deferred later;
- state assumptions, unknowns, migration/reversal boundaries, contributor burden, and E3 validation obligations;
- identify Level B inputs used and Level C details explicitly rejected; and
- avoid naming a winner or using an audit classification as a decision.

E2-002 may generate better candidate shapes than any examples in prior prompts or research.

## 8. Decision matrix contract

E2-001 defines the criterion semantics before candidate scoring; E2-003 applies them. This plan assigns no final weights.

| Class | Treatment |
|---|---|
| `HARD_CONSTRAINT` | Pass/fail against frozen E1 semantics. Any failure eliminates the candidate. No score, weight, simplicity benefit, or future promise can compensate. |
| `WEIGHTED_PREFERENCE` | Compared only among candidates that pass every hard constraint. Includes implementation complexity, local-first experience, operability/debugging, resource overhead, portability, maintainability, contributor accessibility, future adaptation, and reversibility. |
| `UNKNOWN_REQUIRING_SPIKE` | A decision-relevant fact that cannot responsibly be established on paper. It is neither a zero score nor a favorable assumption and blocks selection until E2-004 closes it. |
| `E3_VALIDATION_OBLIGATION` | An empirical question that does not change which architecture is coherent and can be tested only after a baseline exists. It must have an owner, contract, failure consequence, reversal trigger, and ADR linkage. |

The matrix must compare at least: E1 correctness, false-completion resistance, recovery/durability, security isolation, approval/effect safety, evidence integrity, implementation complexity, local-first developer experience, debugging/observability, E1-suite testability, provider neutrality, performance, resource overhead, portability, maintainability, contributor accessibility, future remote execution, future SaaS and Finance compatibility, and migration/reversibility risk.

Every cell needs a claim class (`FACT`, `INFERENCE`, `PROPOSAL`, or `UNKNOWN`), source/evidence reference, rationale, and consequence. Correlated criteria and any weights must be disclosed and challenged before use. Sensitivity analysis cannot rescue a hard-constraint failure.

## 9. ADR plan

No ADR is created or accepted by this plan. E2-005 must use separate records for independently reviewable decision boundaries rather than one giant ADR. The provisional decomposition is:

| Planned record | Decision boundary | Current status |
|---|---|---|
| `ADR-E2-001` | System, client, and core-runtime boundary | `NOT_CREATED` |
| `ADR-E2-002` | Canonical state, persistence, causal/operation history, projections, and migration | `NOT_CREATED` |
| `ADR-E2-003` | Task/execution orchestration, ownership, recovery, idempotency, and future concurrency | `NOT_CREATED` |
| `ADR-E2-004` | Workspace, filesystem/process execution, isolation tier, Git, and local/remote execution seam | `NOT_CREATED` |
| `ADR-E2-005` | Capability, permission, approval, secret, external-effect, and reconciliation boundary | `NOT_CREATED` |
| `ADR-E2-006` | Model/provider abstraction, routing/capability discovery, and context/compaction boundary | `NOT_CREATED` |
| `ADR-E2-007` | Verification, evidence, artifact, provenance, and integrity architecture | `NOT_CREATED` |
| `ADR-E2-008` | Observability, audit, logging, metering, and typed failure architecture | `NOT_CREATED` |
| `ADR-E2-009` | Local packaging plus future remote, multi-client, extension, General, Finance, and SaaS compatibility boundaries | `NOT_CREATED` |

E2-001 or E2-005 may split or combine records only with a traceable rationale that preserves reviewability and covers every domain. Each ADR must record status, context, constraints, options, evidence, decision, trade-offs, rejected alternatives, consequences, reversibility, migration/reversal cost, E1 mapping, missing evidence, and E3 validation obligations. Before E2-006 passes, every ADR status remains `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`.

## 10. Cross-cutting security architecture contract

Security is a hard constraint at every E2 node:

- E2-001 produces a threat-boundary checklist and negative architecture criteria.
- E2-002 gives each candidate a trust-boundary model covering authenticated authority, untrusted repository/web/tool/model/connector content, secrets, filesystem and symlink handling, processes/descendants, Git hooks/helpers, package scripts, network/egress, approvals, destructive actions, effects, evidence integrity, and provider boundaries.
- E2-003 rejects any candidate with an unresolved hard security violation.
- E2-004 may test a mechanism but cannot select a sandbox or weaken policy to make a spike pass.
- E2-005 maps every security boundary into ADRs and E3 negative-test obligations.
- E2-006 independently traces the content-to-capability-to-effect path and verifies fail-closed behavior is structurally possible.

No sandbox, container, VM, secret store, network product, or cloud provider is selected here.

## 11. Cross-cutting recovery architecture contract

Every candidate and selected baseline must provide a failure/recovery matrix for:

- durable task identity and restart/resume;
- acknowledged mutation loss and partial writes;
- tool, process, model, worker, and orchestrator timeout or loss;
- duplicate requests and reordered delivery;
- external effect before lost acknowledgement;
- stale workspace, writer, worker, approval, evidence, and verification;
- pause, cooperative stop, force termination or authority fencing, redirect, and resume;
- recovery reconciliation, explicit uncertainty, and no blind replay; and
- verification invalidation after candidate mutation.

The matrix must name authoritative state, recovery owner, idempotency boundary, readback, legal endpoint, bounded stop/escalation condition, and evidence. A candidate lacking a credible recovery model fails selection.

## 12. Cross-cutting evidence and verification architecture contract

The architecture must make these independently obtainable and correlatable:

- exact repository, workspace, candidate, policy, route, tool, environment, and schema versions;
- operation, causal, actor, authorization, approval, effect, receipt, readback, and recovery provenance;
- artifact identity and provenance;
- required check/test identity, scope, raw outcome, repetition/flakiness, and adequacy result;
- verifier identity, session independence, run status, verdict, and authoritative run reference;
- integrity/gap/tamper status within the E1 threat boundary; and
- truthful final disposition and known limitations.

Evidence is not logging. The verifier must be able to inspect the exact candidate and independently replay deterministic checks or read authoritative state. Any architecture in which verification depends only on executor narration is invalid.

## 13. Bounded technical-spike boundary

E2-003 must classify each uncertainty before any spike exists:

- `PAPER_RESOLVABLE` — close with cited analysis;
- `E2_PRESELECTION_SPIKE_REQUIRED` — mechanism feasibility could change the architecture choice;
- `E3_POSTSELECTION_TECHNICAL_VALIDATION` — test the selected interface/mechanism after the baseline exists;
- `E3_MODEL_OR_CONFIGURATION_BENCHMARK` — evaluate a system/model/configuration for a logical role; or
- `DEFERRED_OUT_OF_SCOPE` — not needed for v0.1 selection.

E2-004 executes only `E2_PRESELECTION_SPIKE_REQUIRED` items from the independently verified E2-003 register. If there are none, it produces an independently verified `NO_PRESELECTION_SPIKE_REQUIRED` closure record and runs nothing. Every actual spike must have a question, hypothesis, real alternatives, minimal prototype, workload, success and failure criteria, security checks, finite local resource/time budget, USD 0 paid/provider/cloud default unless separately authorized, stop condition, artifacts, decision rule, ADR linkage, and challenger/verifier evidence. A spike that cannot remain bounded requires a prospective task split or escalation before execution.

The verified `SP-C01..SP-C10` contracts are a reusable research library, not a mandatory portfolio. E2 should adapt only the contract relevant to a selection blocker. In particular, state/effect/projection recovery, ownership/concurrency, capability/approval/readback, execution lifecycle, and workspace recovery contracts may be relevant; provider/model comparisons belong to E3, the security harness generally requires an implementation, and Finance-specific work remains deferred. No spike is run by this plan.

## 14. E2 / E3 boundary and provider neutrality

E2 selects architectural interfaces and records what E3 must test. E3 later supplies technical and model/configuration evidence against the verified E1 suite and selected E2 baseline.

E2 must not:

- assign Luna, Terra, Sol, Fable, DeepSeek, or any other system permanently;
- infer role eligibility from reputation, availability, the authoring surface, or prior reviewer use;
- benchmark providers or models, make paid calls, or promote an evaluation-only route;
- let a preferred model dictate an architecture change; or
- authorize implementation or autonomous build.

Logical roles remain `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER`, and `SECURITY_REVIEWER`. E2 defines role-facing capabilities and provenance contracts; E3 determines eligible occupants by task class under separate access, budget, credential, region, data-policy, and run authorization.

E2-005 must enumerate E3 technical obligations and E3 model-benchmark obligations separately. It must also assign an accountable future qualification-policy task/authority and independent-review path for finite verification-rerun, deterministic-check-repetition, and correction-attempt ceiling values before any scored freeze. Until that owner and finite value are prospectively recorded, the affected E3 run remains `BLOCKED`.

## 15. Local-first and future compatibility

The immediate design target remains one local user, one persistent software-engineering agent, real repositories, and a local review package. Candidates must preserve seams for later remote workers, multiple tasks/agents/clients, skills/routines/connectors, General Edition, Finance Edition, and SaaS without implementing those features now.

The comparison must reject both forms of failure:

- permanent local-only identities, boundaries, or state assumptions that make later extension needlessly destructive; and
- speculative cloud, tenancy, multi-agent, billing, enterprise, Finance, or marketplace machinery that increases v0.1 complexity without satisfying a current E1 requirement.

## 16. E2 stage gate

The future mode-level gate question is:

> Do we have an independently verified architecture baseline that satisfies the frozen E1 product, correctness, evaluation, security, and reliability specification; results from a genuine comparison of at least three end-to-end alternatives; has no failed hard constraint or unresolved architecture-blocking uncertainty; records its major decisions and reversibility in a coherent ADR set; provides credible security, recovery, evidence, and independent-verification architectures; preserves provider neutrality and bounded future compatibility; and supplies a stable, explicitly bounded E3 validation plan without beginning application implementation?

Following the E1 precedent, the future `VERIFY_STAGE_E2` session is mode-level rather than a task-registry entry and must record its independent result in `10_checkpoints/stage_checkpoints/ENGINEERING_PREVIEW_E2_ARCHITECTURE_GATE_VERIFICATION.yaml`. That record must pin the exact reviewed commit and artifact identities, methods, results, findings, limitations, gate verdict, and resulting state transition.

The E2 gate may pass only when:

1. `E2-001..E2-006` are independently `VERIFIED` and no material challenger/verifier finding remains unresolved.
2. The frozen E1 artifact set is byte-preserved or any prospective amendment has completed the full E1 challenge/reverification path.
3. All 127 canonical requirements and all 25 architecture domains resolve in traceability.
4. At least three genuinely different end-to-end alternatives were compared.
5. Every hard constraint passes; no weighted average masks a failure.
6. Every selection-blocking unknown is resolved, or the gate is `BLOCKED`; E3 deferrals are demonstrably post-selection validation, not hidden architecture blockers.
7. The ADR set is complete, mutually coherent, independently verified, and tied to E1 and E3 obligations.
8. Threat, capability, secret, isolation, recovery, reconciliation, evidence, and verifier-independence models are credible and testable.
9. Provider/model roles remain unassigned and E3 obligations, owners, ceilings, stop conditions, budgets/authorization gates, and reversal triggers are explicit.
10. Architecture is the only E2 selection: application code, evaluation-case execution, E3 benchmark execution, paid calls, autonomy eligibility, autonomous-build authorization, and S1-003 resumption remain absent.

`VERIFY_STAGE_E2` must independently re-derive these conditions. It cannot rely on the E2-005 recommendation, E2-006 summary, or author assertions alone.

## 17. Author-side task-graph challenge

This planning pass checked the graph for the required defects:

- **Overlapping decision authority:** none; only E2-005 proposes and only E2-006 independently verifies the architecture.
- **Premature irreversible decision:** none; requirements, alternatives, comparison, and blocker closure precede ADR proposal.
- **Evidence from a later task required too early:** none; E2-003 may identify E3 obligations but cannot treat missing E3 empirical results as favorable evidence.
- **Tasks too broad for review:** the six irreversible boundaries are separated; E2-004 must split prospectively if a spike portfolio is not bounded.
- **Security/recovery/evidence as afterthoughts:** no; each is a hard cross-cutting contract from E2-001 through E2-006.
- **E2 spikes confused with E3 benchmarks:** no; the uncertainty taxonomy and route/model prohibitions are explicit.
- **ADR and gate points explicit:** yes; proposed ADRs in E2-005, independent baseline verification in E2-006, separate `VERIFY_STAGE_E2` gate.
- **E3 begins only after E2:** yes; E3 execution remains blocked until the mode-level E2 gate is independently verified and all separate authorizations hold.

This is AUTHOR-side evidence only. It does not challenge or verify the plan independently.

## 18. Current state and unresolved questions

After this planning pass:

- E1 gate remains `VERIFIED / E1_GATE_PASSED`.
- E2 is `PLANNED`; only `E2-001` is `READY` and it has not been claimed or executed.
- E2-002 through E2-006 remain `BACKLOG` behind verified dependencies.
- architecture is `NOT_SELECTED`; no ADR exists or is accepted.
- E3 through E5 remain `NOT_STARTED`.
- application code remains absent; evaluation cases implemented/run remain `0 / 0`; technical spikes, model benchmarks, paid calls, and external actions remain `0`.
- `AUTONOMY_ELIGIBLE=NOT_ELIGIBLE`, `AUTONOMOUS_BUILD_AUTHORIZED=NO`, and S1-003 remains deferred and not executed.

Unresolved questions are intentionally assigned to future tasks:

- E2-001: exact hard-constraint normalization, criterion definitions, prospective weighting governance, and full E1 traceability.
- E2-002: the actual end-to-end candidates and their boundary models.
- E2-003: comparative results and which unknowns, if any, block selection.
- E2-004: results of any bounded pre-selection spike or a verified no-spike disposition.
- E2-005: the proposed choice, ADR consequences, reversibility, migration path, and E3 obligations.
- E2-006: independent compliance verdict and whether the baseline may be considered verified.
- E3: empirical technical behavior, role/model/configuration eligibility, exact costs/latencies, reference environment, and prospectively frozen finite rerun/repetition/correction values.

Next command after founder review and commit:

```text
MODE: EXECUTE_TASK_E2-001
```

That command authorizes architecture-requirements work only. It does not authorize alternative generation, architecture selection, a spike, a benchmark, application code, or autonomous build.
