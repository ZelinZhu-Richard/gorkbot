# Engineering Preview Charter

Status: AUTHOR DRAFT — READY FOR INDEPENDENT REVIEW
Authority: D-016 (CONFIRMED)
Track: Engineering Preview E0–E5
Scope: governance and product-planning contract only; no application implementation or architecture selection

## 1. Evidence labels and authority

This charter uses the repository's evidence discipline:

- **CONFIRMED DECISION** means a founder decision recorded in `01_governance/DECISION_LOG.md`.
- **VERIFIED EVIDENCE INPUT** means a repository artifact with an independent verification record.
- **PRODUCT REQUIREMENT** means a constraint that E1 must make testable before architecture or code begins.
- **PROVISIONAL CONTRACT** means a future operating rule that remains inactive until its named gate is satisfied.
- **OPEN QUESTION** means no answer has been selected.

The repository is authoritative. A model assertion, chat summary, transcript line, activity event, telemetry event, or self-authored manifest is not by itself evidence that work occurred or completed.

## 2. Founder decision and preserved history

**CONFIRMED DECISION — D-016.** The project is temporarily switching from startup/customer-discovery execution to an engineering-first open-source Developer Preview. The startup/customer track is preserved and deferred, not erased, completed, rejected, or cancelled.

The following state is preserved:

- S1-001 remains independently `VERIFIED`.
- S1-002 remains independently `VERIFIED`.
- S1-003 remains `BLOCKED` with a `DEFERRED` disposition under `PAUSED_BY_D016_ENGINEERING_FIRST_PIVOT`.
- D-012, D-013, D-014, and D-015 remain recorded and unchanged.
- D-015 satisfies the former restricted-storage input, but it did not start S1-003.
- D-013's bounded outreach authorization is preserved but inactive while D-016 is active.
- Customer evidence, outreach, interviews, recruiting posts, and spend remain zero.
- The Stage 1 customer gate remains `NOT_EVALUATED`; no customer wedge or market winner has been selected.

Resuming S1-003 requires a separate founder decision that lifts or supersedes D-016 and a fresh readiness, privacy, storage, consent, channel, spend, and AI-role audit. No outreach is authorized merely because D-013 exists.

## 3. Long-term objective

**CONFIRMED DECISION — D-016.** The long-term objective remains an independently designed, clean-room, model-agnostic, Grok Bot-class persistent-agent platform with functional parity or better. GPT, Claude, DeepSeek, future frontier models, and eventually open or self-hosted models should be usable as interchangeable reasoning engines where benchmark evidence supports them.

This objective is directional. It is not a runtime-parity claim, model-suitability claim, architecture selection, or authorization to import external implementation material.

## 4. Engineering Preview v0.1

### 4.1 Target user

The initial user is a developer, open-source contributor, or technical founder operating the tool locally against a real software repository.

### 4.2 Immediate product outcome

Engineering Preview v0.1 centers on one persistent, named software-engineering agent for one local user. The agent must be able to accept bounded repository work, preserve durable state, survive interruption or restart, use an isolated local workspace, independently verify completion, and return a reviewable change package and evidence bundle.

The product is useful only if its completion claim can be reviewed from durable evidence rather than trusted from prose.

### 4.3 Primary workflow

1. Receive an engineering request or repository issue.
2. Inspect the repository and governing instructions.
3. Establish a durable, bounded task with explicit scope and authority.
4. Understand and, where applicable, reproduce the problem.
5. Create a bounded implementation plan and completion predicates.
6. Create or use an isolated repository workspace.
7. Read and edit files within authorized boundaries.
8. Run authorized terminal, Git, test, and checking operations.
9. Persist progress, effects, failures, and artifacts so work can resume after interruption.
10. Apply bounded retries or escalate according to the error and recovery policy.
11. Independently evaluate the completion predicates.
12. Return a patch, branch, bounded commit, or draft pull-request package for human review.
13. Return an evidence bundle with the relevant diff, commands, exit results, tests, outputs, approvals, limitations, and verification status.
14. Obtain human approval before any consequential external action.

### 4.4 Correctness contract

**PRODUCT REQUIREMENT.** Engineering Preview v0.1 is correct only when all of the following hold:

- An authorized repository task is durably represented with a stable identity, bounded scope, governing inputs, and explicit completion predicates.
- Canonical conversation/message state and durable task state remain distinct from rebuildable transcript, activity, and summary projections and from execution/effect state.
- Accepted work survives client or worker restart without silent loss, stale-state overwrite, or unintended duplicate effects.
- Work remains confined to an isolated local workspace with explicit filesystem, terminal, Git, test, model, tool, network, approval, and secret boundaries.
- Every tool boundary uses structured, versioned input/output/action contracts and runtime validation.
- Pause, stop, redirect, resume, retry, recovery, and escalation have persisted semantics.
- Consequential external actions require human approval bound to the exact action and target.
- Failures are typed and drive bounded retry, recovery, or escalation rather than unbounded repetition.
- Task-specific completion predicates are independently checked through tests, checks, diffs, artifacts, receipts, or external readback.
- A reviewable patch, branch, bounded commit, or draft-pull-request package and a complete evidence bundle are produced.

A model claim, transcript entry, activity event, telemetry event, caller-supplied confirmation flag, or self-authored manifest alone never proves completion or authorization.

## 5. Required v0.1 capabilities

E1 must turn every capability below into functional requirements and objective acceptance evidence.

### 5.1 Identity, conversation, and durable work

- One persistent named agent with a durable identity.
- Durable task state with stable task identity, authority, scope, dependencies, status, limits, and completion predicates.
- Canonical conversation and message state, including ordering, authorship, content references, and durable recovery semantics.
- Execution and effect state separate from canonical conversation state and from transcript, UI, activity, or summary projections.
- Restart and resume after client, orchestrator, or worker interruption without silent loss or duplicate effects.
- Context compaction that changes only derived working context and does not destroy authoritative records or evidence.

### 5.2 Execution and repository work

- A local execution sandbox with declared isolation and security properties.
- A provider-neutral abstraction for a future cloud sandbox without requiring cloud execution in v0.1.
- Filesystem tools with normalized paths, allowed-root enforcement, symlink handling, bounds, and effect receipts.
- Terminal tools with declared working directory, environment, time/output limits, cancellation, exit status, and retained evidence.
- Git tools for inspection, isolated workspace creation, diffing, branching, bounded commits, and review packages.
- Testing and checking tools with exact commands, versions where relevant, exit results, bounded outputs, and artifact references.
- A Git workspace model that prevents unrelated user changes from being silently overwritten or mixed into task output.

### 5.3 Models and capabilities

- A model-provider abstraction with explicit provider and model identity.
- Model routing that preserves provider-specific tool, streaming, refusal, usage, cancellation, stop, cost, and error semantics.
- No hidden fallback and no permanent task-role assignment without E3 evidence.
- Structured and versioned tool/capability identifiers, input schemas, output schemas, effect classes, side-effect declarations, idempotency rules, limits, cancellation semantics, and runtime validation.
- A future-compatible MCP or equivalent capability gateway with explicit authorization, credential scope, approval receipts, effect receipts, and independent readback.

### 5.4 Control, safety, and visibility

- Structured human approval requests and durable approval/refusal/revocation receipts.
- Pause, stop, redirect, and resume controls with persisted state and defined race behavior.
- Visible task, agent, operation, tool, approval, artifact, retry, and recovery activity.
- Activity/telemetry views that remain separate from authoritative domain, audit, and completion evidence.
- Explicit secret boundaries for acquisition, injection, use, redaction, logging, persistence, rotation/revocation, and evidence generation.
- Bounded autonomy across eligible tasks, paths, capabilities, network/credential policy, time, cost, tool calls, retries, and external effects.

### 5.5 Completion, evidence, and recovery

- Durable artifacts with identity, provenance, ownership, retention, and stale-detection rules.
- Evidence bundles defined by the contract in Section 10.
- Task-specific completion predicates defined before execution.
- Independent completion verification distinct from the sole author/model's assertion.
- A stable typed error and retry taxonomy with safe user-facing descriptions, internal correlation, retryability/terminal metadata, bounded payloads, and an unknown fallback.
- Failure recovery for worker/client restart, stale work, partial effects, cancellation, malformed state, corrupted local records, and interrupted long-running operations.
- Operation recovery with stable operation identity, terminal readback, duplicate-effect prevention, and explicit handling of uncertain outcomes.

## 6. Authority and state invariants

E1 must define the exact records and lifecycle semantics; E2 must compare implementations. At minimum, the following logical authorities may not be collapsed merely for convenience:

1. Durable task state: requested outcome, scope, status, limits, dependencies, approvals needed, completion predicates, and final disposition.
2. Canonical conversation/message state: ordered durable messages and referenced content required to reconstruct the conversation.
3. Execution/effect state: operations attempted, tools invoked, effects requested, receipts, outputs, retries, cancellations, and uncertain outcomes.
4. Artifact/evidence state: source inputs, patches, logs, test results, manifests, digests, approvals, limitations, and verification records.
5. Event/history state: durable causal history needed for audit, recovery, reconciliation, and projection rebuilding.
6. Derived projections: transcript displays, activity feeds, search indexes, summaries, working context, UI state, and telemetry views.

Derived projections must be rebuildable or explicitly disposable and may not overwrite authoritative state. E2 must document ownership, ordering, versions, correlation/causal identities, retention, recovery, and migration for every chosen boundary.

### 6.1 Compaction invariant

Context compaction may alter only the model's working projection. It may not delete, overwrite, or become authoritative over durable conversation/message history, task state, execution/effect history, approvals, source and test evidence, artifacts, audit records, or evidence-bundle inputs. Stale summaries must not replace newer state, and required source evidence must remain retrievable.

### 6.2 Content identity caveat

Content-addressed state and artifacts are E2 alternatives, not a v0.1 technology mandate. A content hash does not by itself establish authorization, confidentiality, tenant isolation, deduplication safety, retention compliance, or physical erasure. Equality and known-content-presence leakage, key/namespace boundaries, holds, garbage collection, and deletion evidence must be evaluated if such an alternative is considered.

## 7. Task and agent lifecycle requirements

E1 must define a complete transition table rather than relying on transcript wording. The final names remain an E1 decision, but the lifecycle must represent at least:

- task creation and readiness;
- bounded claim and ownership;
- planning and execution;
- waiting for approval or user input;
- voluntary pause and user stop;
- redirect with preserved prior state;
- blocked, retryable failure, terminal failure, and uncertain-effect recovery;
- ready-for-review and independently verified completion;
- cancellation or supersession without erasing evidence;
- safe restart and resumption from every nonterminal state.

The agent lifecycle must represent at least durable identity, availability, active task ownership, paused/stopped state, recovery, bounded failure, and resume. A stopped client process must not imply that the durable task or agent identity was deleted.

For every transition, E1 must specify authorized actor, preconditions, persisted record, operation/effect behavior, cancellation semantics, idempotency expectations, visible projection, and recovery path.

## 8. Completion predicates and independent verification

Each task must declare completion predicates before implementation. Applicable predicates include:

- required files or artifacts exist at the authorized locations;
- the diff stays inside allowed scope and excludes unrelated user changes;
- reproduction evidence exists where the task began from a defect;
- required commands and tests ran with acceptable exit results;
- lint, type, build, security, or domain checks meet declared thresholds;
- required negative tests behave safely;
- no forbidden artifacts, secrets, private data, or unapproved effects are present;
- external state is reread when an approved external effect was requested;
- approval receipts match the exact consequential actions performed;
- evidence-bundle required fields are complete and internally consistent;
- known limitations and remaining failures are stated;
- an independent verifier reproduces or checks the declared predicates.

Independent verification must use durable inputs and effects, not the author's narrative alone. The verifier may return verified, changes required, blocked, or another E1-defined outcome. High-risk work may not be self-verified by its sole author.

## 9. Approval boundaries

Approval is a policy-enforced record, not conversational assent inferred from wording.

An approval request and receipt must bind at least the actor, normalized action, exact resource or target, capability/effect class, governing policy/version, scope, expiry or one-shot use, task/operation identity, and outcome. E1 must define refusal, revocation, deduplication, replay protection, mutation detection, stale approval handling, and terminal readback.

Human approval is required before consequential external actions, including as applicable:

- pushing a branch or commit to a remote;
- opening, modifying, commenting on, merging, or closing an external pull request or issue;
- deploying, publishing, releasing, or changing production/cloud state;
- messaging or contacting another person;
- spending money, purchasing services, or creating paid usage beyond an authorized budget;
- using a privileged credential or broadening credential/network scope;
- destructive migration, irreversible deletion, force update, or other difficult-to-recover effect;
- changing a release, stage, security, architecture, or autonomous-build gate.

Local read-only inspection and later explicitly authorized bounded local implementation may follow their task contract. E4's provisional contract does not authorize external actions. Prompt text, regex matching, tool names, model review, or caller-provided `confirmed: true` values may supplement user experience but may not be primary enforcement.

## 10. Evidence-bundle contract

E1 must define a versioned, runtime-validated evidence-bundle schema. A valid bundle must contain or reference, as applicable:

- bundle schema version and bundle identity;
- task and persistent-agent identities;
- author, challenger, and verifier identities or explicitly recorded unknowns;
- repository identity, base revision, workspace identity, branch/head revision, and dirty-state facts;
- request, governing instructions, scope, dependencies, limits, and authorization references;
- bounded plan and task-specific completion predicates;
- relevant source/input identities and digests where useful;
- files created, modified, deleted, and unchanged invariants;
- reviewable diff or patch plus branch, bounded commit, or draft-PR package reference;
- every material command with working directory, exit result, bounded stdout/stderr or artifact reference, and execution time where material;
- tests/checks with exact result, skipped checks and reasons, failures, and retries;
- provider, model, tool/capability, environment, and configuration identities needed to interpret the work, with unknowns explicit;
- tool effect records, approval requests/receipts, cancellations, uncertain outcomes, and external-state readbacks;
- artifacts with provenance, ownership, content identity where appropriate, retention, and stale/regeneration rules;
- error codes, recovery actions, escalation events, and remaining blockers;
- limitations, unverified claims, remaining failures, and out-of-scope observations;
- independent verification method, predicate-by-predicate results, verdict, and reviewed revision;
- final task status and human-review requirements.

Outputs must be bounded and secret-safe. Evidence digests and manifests aid integrity and traceability but do not themselves prove correctness. Every generated evidence record needs an authoritative input, owner, regeneration trigger, stale-detection rule, automation policy, and defined consequence when it cannot be produced or verified.

## 11. Reliability requirements

E1 must define measurable requirements for:

- durable acknowledgement and recovery after client, orchestrator, or worker restart;
- idempotent or explicitly reconciled re-entry after uncertain effects;
- stale-writer and stale-summary rejection;
- operation identity, progress, cancellation, timeout, retry ceilings, terminal status, and readback;
- repository-workspace isolation and protection of unrelated changes;
- checkpoint/restore evidence and corrupt-state quarantine or salvage;
- bounded output, history, artifact, and evidence retention;
- deterministic completion-predicate evaluation where possible;
- surfaced partial completion, skipped checks, degradation, and limitations;
- no silent fallback across models, tools, execution providers, credentials, or approval scopes;
- observability that diagnoses behavior without becoming completion authority.

E1 must specify reliability service levels or preview-grade thresholds without representing them as production evidence before E3/E5 tests run.

## 12. Security requirements

Repository files, web pages, documents, issue text, MCP/tool descriptions and outputs, model output, generated code, and retrieved content are untrusted data. They cannot broaden authority or override repository governance.

E1 must define security requirements and negative tests for:

- allowed-root, path traversal, symlink, hard-link, device-file, archive, and workspace escape behavior;
- terminal command, environment, process, resource, output, and cancellation boundaries;
- network egress, domain/endpoint, redirect, DNS, download, and credential boundaries;
- secret discovery, least-scope injection, redaction, log/evidence exclusion, persistence, revocation, and rotation;
- structured schema validation for malformed, oversized, unknown, duplicated, stale, incompatible, or adversarial inputs and outputs;
- prompt injection and authority-confusion attempts from repositories, pages, documents, tools, models, comments, tests, and artifacts;
- approval replay, mutation, target substitution, expiry bypass, race, and stale-worker behavior;
- duplicate side effects, interrupted effects, cancellation races, and uncertain terminal outcomes;
- cross-workspace, future tenant, and future multi-writer isolation assumptions;
- malicious dependency/test/build output and evidence poisoning;
- forbidden customer evidence, credentials, private artifacts, external code, and reconstructed assets in public output;
- safe error payloads and correlation without leaking internal secrets or sensitive paths;
- cleanup, retention, legal hold, garbage collection, and verifiable deletion where applicable.

Worker threads, process boundaries, containers, and encryption are not automatically security boundaries; E2 must evaluate and document the actual threat model and isolation evidence of any alternative.

## 13. Bounded autonomy

v0.1 autonomy is bounded by eligible task state, declared scope, allowed repository/workspace paths, capabilities, network and credential policy, time/cost/tool/retry ceilings, approvals, completion predicates, and stop/escalation conditions. It may not broaden its own authority.

The user must be able to pause, stop, redirect, and resume work. The system must persist the requested control, reconcile in-flight operations, show whether an effect may already have occurred, and require readback or escalation where terminal state is uncertain.

No bounded task queue or implementation loop is active during E0–E3. `FULL_AUTONOMOUS_BUILD_MODE` remains `NOT_AUTHORIZED` until E3 is independently verified.

## 14. Explicit v0.1 non-goals

The following are not required for v0.1 and are not authorized by this charter:

- multi-tenant SaaS;
- billing or subscriptions;
- organizations or multi-user administration;
- enterprise controls, enterprise SSO, or enterprise administration;
- mobile applications;
- full visual or UI parity with Grok Bot;
- visible multi-agent teams;
- group chat or group conversations;
- a skills marketplace;
- every connector;
- production-scale cloud infrastructure;
- Finance Edition strategy packs;
- backtesting, paper trading, live trading, or real-money finance;
- startup customer discovery, pricing, TAM/SAM/SOM, GTM, sales, outreach, or fundraising.

## 15. Future compatibility without premature scope

v0.1 implements one local user and one persistent agent. E1 requirements and E2 ADRs must preserve versioned identities, ownership, causal/correlation fields, capability scopes, extension points, and migration paths sufficient to add later:

- multiple persistent agents;
- agent-to-agent messaging;
- group conversations;
- skills and vertical packs;
- routines and scheduled or event-triggered work;
- cloud execution;
- multiple devices and multi-writer state;
- multi-user organizations and multi-tenant operation;
- the General Edition;
- the Finance Edition.

This is a compatibility obligation, not authorization to implement those features in v0.1. General and Finance remain extensions of one shared core rather than duplicated platforms.

E2 must explicitly examine future ordering, expected versions, causal identities, idempotency, duplicate or reordered delivery, reconnect, revocation, leases/fencing where applicable, conflict reconciliation, schema/event evolution, retention, and migration. A global singleton or single-process assumption may not be made permanent merely because v0.1 is local and single-user.

## 16. Clean-room and verified research inputs

### 16.1 Grok Bot capability baseline

**VERIFIED EVIDENCE INPUT.** `02_research/GROK_BOT_BASELINE_2026-08-21.md` is a verified official-documentation baseline. It had zero installed-build or black-box runs. It does not prove runtime reliability, rollout, internal architecture, stop/recovery semantics, production isolation, or parity.

### 16.2 Reconstructed architecture audit

**VERIFIED EVIDENCE INPUT.** The corrected reconstructed-architecture audit and its verifier review are verified static research against the pinned unofficial reconstruction identified in those artifacts. They are not original or production Grok Bot architecture, security, behavior, deployment, or tenancy evidence. Their `ADOPT`, `ADAPT`, `REJECT`, and similar labels are research recommendations, not project decisions.

E1/E2 must evaluate, without automatically adopting:

- canonical conversation state distinct from transcript projection;
- content-addressed state and artifact concepts with authorization, privacy, retention, and erasure caveats;
- structured long-running/cloud-agent lifecycle concepts and operation recovery;
- stable typed errors and bounded safe error identity;
- context summarization/compaction with authoritative-evidence preservation;
- structured approvals bound to exact effects;
- local/remote execution-provider abstraction;
- provider/model routing that preserves provider semantics;
- MCP or equivalent capability gateway;
- typed and runtime-validated boundaries;
- evidence manifests and lineage;
- multi-writer and multi-device concerns;
- security-negative testing.

No external source code, translated schema, exact internal name, renderer/minified asset, installer, selector/hash, UI copy, branding, consumer-session authentication integration, undocumented endpoint, or private implementation material may be imported. All product and implementation work must be independently designed.

## 17. E0–E5 program

| Phase | Purpose | Current status | Gate to proceed |
|---|---|---|---|
| E0 | Engineering pivot and governance reconciliation | `READY_FOR_REVIEW` | Independent review and verification of the initialization artifacts |
| E1 | Engineering Preview product and correctness specification | `ACTIVE`; E1-001 is `READY` | All required E1 artifacts and E0-001 independently verified |
| E2 | Architecture alternatives and ADR selection | `NOT_STARTED` | E1 gate independently verified |
| E3 | Technical spikes and model-role benchmarks | `NOT_STARTED` | E2 gate independently verified; external inputs and approvals satisfied |
| E4 | Autonomous implementation of Engineering Preview | `NOT_AUTHORIZED` | E3 independently verified under the provisional contract and its recorded limits |
| E5 | Reliability, open-source packaging, and release verification | `NOT_STARTED` | Eligible E4 implementation independently verified and release gate opened |

E0 being ready for review does not block authoring E1-001 because D-016 is already confirmed and E1-001 depends only on verified research tasks. E0-001 must nevertheless be independently verified before E1 can be gate-verified or E2 can activate.

## 18. E1 product-specification gate

E1 must eventually produce independently verified artifacts for:

1. Engineering Preview PRD.
2. User flows.
3. MVP scope.
4. Explicit non-goals.
5. Functional requirements.
6. Reliability requirements.
7. Security requirements.
8. Task lifecycle.
9. Agent lifecycle.
10. Completion predicates.
11. Approval boundaries.
12. Evidence-bundle contract.
13. Open-source contribution workflow.
14. Evaluation suite.
15. Release acceptance criteria.

E1-001 is the sole READY authoring task and covers items 1–12. E1-002 remains BACKLOG and covers items 13–15 after E1-001 and E0-001 are independently verified. Challenge, fix, and verify operations apply the repository's author/challenger/verifier protocol to each task; no author may mark their own high-risk work verified.

The E1 gate must answer what correctness means before architecture or code begins.

## 19. E2 architecture and ADR gate

E2 is not authorized during this operation. It must later compare alternatives and record evidence-backed ADRs for:

- durable workflow engine;
- canonical task state;
- canonical conversation/message state;
- event/history log;
- projections and indexes;
- local database;
- sandbox provider and declared isolation tier;
- local execution;
- future cloud execution;
- model router;
- provider adapters;
- tool/capability gateway;
- MCP integration;
- approval engine;
- secrets handling and storage;
- artifact/evidence store;
- Git workspace model;
- observability and audit separation;
- error taxonomy and recovery policy;
- concurrency, ordering, leases/fencing, idempotency, and conflict handling;
- recovery, migration, and schema/event evolution;
- plugin and vertical-pack boundary;
- CLI, web, desktop, or other client surface.

Each comparison must consider correctness, durability, recovery, isolation, security, local-first usability, future cloud/multi-writer extension, operability, testability, migration, open-source contributor burden, cost, and lock-in. No client, language, framework, workflow engine, queue, database, sandbox/container/VM, artifact store, event model, schema library, MCP topology, secret store, provider, model, or permanent model role is selected by this charter.

## 20. E3 automation-unlock gate

E3 is not authorized during this operation. Future E3 work must test the riskiest product and architecture assumptions and benchmark candidate execution models on representative task classes.

At minimum, E3 must evaluate:

- durable execution;
- restart and recovery;
- Git workspace isolation;
- repository inspection and editing;
- test execution;
- user interruption, pause, stop, redirect, and resume;
- completion-predicate evaluation and independent verification;
- evidence generation;
- filesystem, terminal, Git, testing, and broader tool-use reliability;
- provider/model routing and semantic preservation;
- inexpensive-model execution reliability;
- difficult-task escalation;
- security-negative cases;
- cost;
- latency.

Security-negative cases must include untrusted repository/web/document/MCP/model content, secret leakage, path/symlink escape, egress, malformed or oversized schemas, approval replay or mutation, stale workers, duplicate effects, cancellation races, and isolation failure.

The benchmark must determine which task classes, if any, can safely use Luna, Terra, Sol, Claude/Fable, DeepSeek, open/self-hosted models, or other candidates, and when escalation is required. No permanent role is assigned now. Provider access, paid calls, live technical spikes, or final suitability claims remain subject to S0-005, budget, credential, and approval constraints.

`FULL_AUTONOMOUS_BUILD_MODE` is not authorized until E3 has been independently verified. D-016 conditionally authorizes the provisional E4 loop after that gate, subject to eligible READY task state and all approval, budget, stage, release, and stop/escalation rules below.

## 21. Provisional E4 autonomous build contract

**PROVISIONAL CONTRACT — INACTIVE.** After E3 is independently verified, Codex may repeat the following only while eligible READY engineering tasks exist:

1. Read `01_governance/PROJECT_STATE.yaml`.
2. Claim the highest-priority unblocked eligible engineering task.
3. Select a benchmark-approved execution model for that task class.
4. Create or use an isolated branch or worktree.
5. Read the task's required specifications and governing records.
6. Implement only the allowed scope.
7. Run the required tests and checks.
8. Evaluate the acceptance criteria and completion predicates.
9. Generate the evidence bundle and factual handoff.
10. Commit the bounded local changes when the task contract allows it.
11. Proceed to the next eligible task.

The loop must stop and escalate on:

- architecture conflict;
- ambiguous requirement;
- security-sensitive decision;
- destructive migration;
- failed acceptance criteria;
- repeated implementation failure;
- missing credential or approval;
- budget threshold;
- out-of-scope change;
- stage or release gate;
- unsupported model capability;
- uncertain consequential effect that cannot be resolved by safe readback.

This contract does not authorize external push, pull-request creation, merge, release, deployment, messaging, spending, or other consequential external action without the separately required human approval. It is not active during E0, E1, E2, or E3.

## 22. E5 reliability, packaging, and release gate

E5 must independently establish that a candidate release is reliable enough for its stated Developer Preview limits and can be built, inspected, tested, and contributed to from clean source.

E1-002 must make the release criteria testable. At minimum, the future E5 gate must require:

- end-to-end primary workflow success on declared representative repositories and task classes;
- restart/recovery, interruption, duplicate-effect, workspace-isolation, and failure-path evidence;
- completion-predicate and independent-verification evidence;
- security-negative tests and resolution of release-blocking findings;
- evidence-bundle schema and content validation;
- deterministic declared build/test/package outputs where applicable;
- forbidden-artifact, secret, private-data, external-code, branding, and clean-room checks;
- provider/model/configuration limits and known unsupported cases;
- open-source license, provenance, setup, contribution, test, security-reporting, and release documentation;
- exact known limitations and preview-grade, not production-grade, claims;
- independent release verification and human release approval.

E5 does not imply a particular packaging technology or client surface.

## 23. Open questions preserved for E1–E3

The following remain open and may not be silently selected during E0:

- exact E1 functional, reliability, security, lifecycle, and release thresholds;
- final state-machine vocabulary and data authority map;
- architecture and technology choices listed in Section 19;
- prototype and benchmark budget;
- funded provider/API access and account quotas;
- candidate model suitability, routing policy, escalation policy, and cost/latency thresholds;
- local sandbox security tier and future cloud-execution contract;
- final client surface;
- release scope and explicit preview limitations.

## 24. E0 completion boundary

This E0 authoring operation is complete for review when:

- project state and the task registry consistently preserve and defer the startup track;
- the Engineering Preview track is active with unique E0–E5 identifiers;
- S1-003 is preserved, blocked, and deferred by D-016 with zero execution;
- E0-001 is `READY_FOR_REVIEW`, E1-001 is the sole `READY` task, and E1-002 is `BACKLOG`;
- E2 and E3 are not started and E4 is not authorized;
- this charter and a factual initialization handoff exist;
- D-016, verified customer artifacts, customer evidence, and the model registry are unchanged;
- YAML, task dependency/status, Markdown, scope, secret, no-source-code, and whitespace checks pass;
- no architecture, model role, customer wedge, pricing, application code, technical spike, benchmark, outreach, external action, or autonomous build mode is created or activated.

E0-001 remains `READY_FOR_REVIEW` until an independent verifier checks these criteria. This charter does not claim verification or production readiness.
