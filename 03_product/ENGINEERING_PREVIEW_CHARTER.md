# Engineering Preview Charter

Status: AUTHOR DRAFT — READY FOR INDEPENDENT REVIEW
Authority: D-016 (CONFIRMED)
Track: Engineering Preview E0–E5
Scope: governance and product-planning contract only; no application implementation or architecture selection

## 1. Evidence labels and authority

This charter uses the repository's evidence discipline:

- **CONFIRMED DECISION** means a founder decision recorded in `01_governance/DECISION_LOG.md`.
- **VERIFIED EVIDENCE INPUT** means a repository artifact with an independent verification record.
- **PRODUCT REQUIREMENT / REQUIRED PROPERTY** means an implementation-neutral constraint that E1 must make testable before architecture or code begins.
- **ARCHITECTURAL PATTERN TO EVALUATE** means an evidence-supported candidate that E2 must compare against alternatives; it is not selected by this charter or by an external audit label.
- **EXTERNAL IMPLEMENTATION DETAIL** means a reconstruction-specific observation that is neither a product requirement nor an automatically eligible design and must not be copied automatically.
- **PROVISIONAL CONTRACT** means a proposed future operating rule that remains inactive until every named evidence gate and every separately required explicit authorization are satisfied. A verified gate never substitutes for a separate founder authorization when one is required.
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
- Information needed for authorization, resumption, audit, recovery, effect reconciliation, and completion verification remains authoritative, durable, and distinguishable from disposable or rebuildable transcript, activity, summary, telemetry, UI, and model-working-context views. E2 decides the physical and logical boundaries.
- Accepted work survives client or worker restart without silent loss, stale-state overwrite, or unintended duplicate effects.
- Work remains confined to an isolated local workspace with explicit filesystem, terminal, Git, test, model, tool, network, approval, and secret boundaries.
- Every tool boundary uses structured, versioned input/output/action contracts and runtime validation.
- Pause, stop, redirect, resume, retry, recovery, and escalation have persisted semantics.
- Consequential external actions require human approval bound to the exact action and target.
- Failures have structured, machine-distinguishable, bounded, safe semantics that drive retry, recovery, terminal failure, or escalation rather than unbounded repetition.
- Task-specific completion predicates are independently checked through tests, checks, diffs, artifacts, receipts, or external readback.
- A reviewable patch, branch, bounded commit, or draft-pull-request package and a complete evidence bundle are produced.

A model claim, transcript entry, activity event, telemetry event, caller-supplied confirmation flag, or self-authored manifest alone never proves completion or authorization.

## 5. Required v0.1 capabilities

E1 must turn every capability below into functional requirements and objective acceptance evidence.

### 5.1 Identity, conversation, and durable work

- One persistent named agent with a durable identity.
- Durable task state with stable task identity, authority, scope, dependencies, status, limits, and completion predicates.
- Durable conversation and message information needed for ordering, authorship, authorization, resumption, audit, and recovery.
- Execution and effect information whose authority is explicit and cannot be replaced by transcript, UI, activity, summary, telemetry, or model-working-context claims; E2 decides whether these responsibilities use combined or separate stores and services.
- Restart and resume after client, orchestrator, or worker interruption without silent loss or duplicate effects.
- Safe context management: if working context is summarized, compacted, truncated, or rebuilt, the operation may change only derived working context and must not destroy or supersede authoritative records or evidence.

### 5.2 Execution and repository work

- A local execution sandbox with declared isolation and security properties.
- A documented, testable compatibility and migration path for possible future cloud execution without requiring cloud execution or preselecting an execution-provider abstraction or seam in v0.1.
- Filesystem tools with normalized paths, allowed-root enforcement, symlink handling, bounds, and effect receipts.
- Terminal tools with declared working directory, environment, time/output limits, cancellation, exit status, and retained evidence.
- Git tools for inspection, isolated workspace creation, diffing, branching, bounded commits, and review packages.
- Testing and checking tools with exact commands, versions where relevant, exit results, bounded outputs, and artifact references.
- A Git workspace model that prevents unrelated user changes from being silently overwritten or mixed into task output.

### 5.3 Models and capabilities

- Explicit provider and model identity plus provider replaceability across any selected integration design; E2 decides whether router and adapter boundaries exist and how they are arranged.
- Preservation of provider-specific tool, streaming, refusal, usage, cancellation, stop, cost, and error semantics across routing or direct integration.
- No hidden fallback and no permanent task-role assignment without E3 evidence.
- Structured and versioned tool/capability identifiers, input schemas, output schemas, effect classes, side-effect declarations, idempotency rules, limits, cancellation semantics, and runtime validation.
- Portable, authorized, runtime-validated capability integration with explicit credential scope, approval receipts, effect receipts, and independent readback. Direct adapters, an MCP gateway, or an equivalent capability-gateway topology remain E2 alternatives.

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
- A stable structured failure and retry contract with safe user-facing descriptions, internal correlation, retryability/terminal metadata, bounded payloads, and an unknown fallback. A central typed error registry is an E2 pattern to evaluate, not a selected architecture.
- Failure recovery for worker/client restart, stale work, partial effects, cancellation, malformed state, corrupted local records, and interrupted long-running operations.
- Operation recovery with stable operation identity, terminal readback, duplicate-effect prevention, and explicit handling of uncertain outcomes.

## 6. Authority and state invariants

E1 must define the following semantic responsibilities and testable invariants. E2 must decide their authoritative data model, physical boundaries, storage, and projection relationships. This list does not mandate six stores, services, or logs and does not select event sourcing, transactional state, workflow history, content addressing, or any other architecture. E2 may combine responsibilities only where authority, recovery, retention, security, and independent verification remain explicit and testable:

1. Task responsibility: requested outcome, scope, status, limits, dependencies, approvals needed, completion predicates, and final disposition.
2. Conversation/message responsibility: durable ordering, authorship, content references, authorization context, and recovery semantics.
3. Execution/effect responsibility: operations attempted, tools invoked, effects requested, receipts, outputs, retries, cancellations, and uncertain outcomes.
4. Artifact/evidence responsibility: source inputs, patches, logs, test results, manifests, digests, approvals, limitations, provenance, and verification records.
5. Causal/history responsibility: history sufficient for audit, recovery, reconciliation, concurrency safety, and any selected projection-rebuilding design.
6. Presentation/working-context responsibility: transcript displays, activity feeds, search indexes, summaries, model working context, UI state, and telemetry views.

Presentation and working-context material may be rebuildable or explicitly disposable, but it may not overwrite, delete, or become authority over records required for authorization, recovery, effects, audit, evidence, or completion. E2 must document ownership, ordering, versions, correlation/causal identities, retention, recovery, and migration for every chosen boundary.

### 6.1 Context-management invariant

If context is summarized, compacted, truncated, or rebuilt, the operation may alter only a derived model-working projection. It may not delete, overwrite, or become authoritative over durable conversation/message history, task state, execution/effect history, approvals, source and test evidence, artifacts, audit records, or evidence-bundle inputs. Stale working views must not replace newer state, and required source evidence must remain retrievable. Whether compaction or persisted summary blocks exist is an E2 decision.

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

Local read-only inspection and later explicitly authorized bounded local implementation may follow their task contract. E4's provisional contract is a design proposal and does not authorize implementation or external actions. Prompt text, regex matching, tool names, model review, or caller-provided `confirmed: true` values may supplement user experience but may not be primary enforcement.

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
- recovery evidence for the selected persistence mechanism and safe corrupt-state detection/handling without silent use or loss; checkpoint/restore, quarantine, and salvage remain E2 patterns to compare;
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

No bounded task queue or implementation loop is active during E0–E3. The authorization sequence is:

```text
E3 VERIFIED
        ↓
AUTONOMY_ELIGIBLE
        ↓
separate explicit founder authorization
        ↓
AUTONOMOUS_BUILD_AUTHORIZED
```

E3 verification is necessary but not sufficient. It can establish `AUTONOMY_ELIGIBLE` only. No model may automatically activate E4 when E3 passes, and `AUTONOMOUS_BUILD_AUTHORIZED` remains `NO` / `NOT_AUTHORIZED` until a separate founder decision is recorded.

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

v0.1 implements one local user and one persistent agent. E1 requirements and E2 ADRs must demonstrate a credible, testable compatibility and migration path sufficient to add later features below. E2 decides which versioned identities, ownership rules, causal/correlation fields, capability scopes, extension points, and migration mechanisms are necessary rather than treating this list as a preselected schema:

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

The audit is integrated at three separate levels.

#### Level A — verified requirement / property

These implementation-neutral properties are required independently by D-016, the master operating requirements, `SECURITY.md`, and the repository's completion/evidence rules. The external audit corroborates them and may contribute test ideas, but is not their authority:

- durable task and conversation information sufficient for authorization, resumption, audit, recovery, and completion verification;
- safe recovery from restart, interruption, partial failure, stale writers, and uncertain effects without silent loss or duplicate consequential effects;
- explicit, durable approval, refusal, and revocation semantics bound to the exact actor, action, target, scope, policy, and task or operation;
- structured, machine-distinguishable failures with bounded retry, recovery, terminal-failure, and escalation behavior;
- validated tool and provider contracts that preserve provider-specific semantics and never hide fallback or erase failure meaning;
- evidence and artifact provenance sufficient for independent verification, including inputs, actions, outputs, receipts, limitations, and reviewed revision;
- context management that may reduce working context but cannot destroy or supersede authoritative task, conversation, effect, approval, audit, or completion history;
- future concurrency safety that prevents silent lost mutations, stale writers or workers, duplicate effects, and authority amplification while leaving the mechanism open;
- authoritative readback for external-state completion claims, or an explicit unresolved or uncertain outcome.

Level A requires authority and derived claims to remain distinguishable and testable. It does not mandate separate databases, services, logs, projections, or a particular canonical-state implementation.

#### Level B — architectural pattern to evaluate

E2 must compare audit-supported patterns against alternatives before any ADR selects them. Candidate patterns include:

- canonical task or conversation authority with rebuildable transcript or activity projections;
- content-addressed state or artifact referents with versioned roots, retention, privacy, and deletion controls;
- transactional state plus outbox, append-only event history, durable workflow history, or hybrid authority models;
- central typed error registries with stable codes and safe public/internal representations;
- structured long-running or cloud-agent lifecycle and operation-recovery patterns;
- explicit process ports, provider-router/provider-adapter boundaries, and local/remote execution-provider seams;
- direct tool adapters versus an MCP or equivalent capability gateway;
- approval controllers or capability receipts; evidence packets, digest manifests, anchor/closure records, and drift checks;
- provider-aware context-compaction services with persisted summary blocks;
- optimistic concurrency, compare-and-swap/version checks, durable queues, leases/fencing, actors, or workflow-engine ownership;
- separate telemetry, audit, evidence, and presentation stores versus a correlated shared backbone;
- corrupt-state quarantine and bounded salvage patterns.

Only an independently verified E2 ADR may select among these. E3 may test a selected design; an audit classification cannot bypass E1 or E2.

#### Level C — external implementation detail

Reconstruction-specific mechanisms are observations, not requirements and not designs to copy automatically. These include Electron-specific main/preload/renderer/coordinator and IPC boundaries; local SQLite or JSON/JSONL implementations; exact protobuf, hash, schema, table, action, status, error-code, payload, module, adapter, queue, port, authentication, container, selector, renderer, asset, installer, branding, copy, or shipped-compatibility mechanisms; and reconstruction-specific cloud-agent, provider, MCP-bridge, home-directory, or updater behavior.

No external source code, translated schema, exact internal name, renderer/minified asset, installer, selector/hash, UI copy, branding, consumer-session authentication integration, undocumented endpoint, or private implementation material may be imported. All product and implementation work must be independently designed.

## 17. E0–E5 program

| Phase | Purpose | Current status | Gate to proceed |
|---|---|---|---|
| E0 | Engineering pivot and governance reconciliation | `READY_FOR_REVIEW` | Independent review and verification of the initialization artifacts |
| E1 | Engineering Preview product and correctness specification | `NOT_STARTED`; E1-001 and E1-002 are `BACKLOG` | E0-001 independently verified before E1-001 can become `READY`; all required E1 artifacts independently verified before E2 |
| E2 | Architecture alternatives and ADR selection | `NOT_STARTED` | E1 gate independently verified |
| E3 | Technical spikes and model-role benchmarks | `NOT_STARTED` | E2 gate independently verified; verified Engineering Preview task/evaluation suite and external inputs/approvals satisfied |
| E4 | Autonomous implementation of Engineering Preview | `NOT_STARTED`; autonomous build `NOT_AUTHORIZED` | E3 independently verified, then a separate explicit founder decision records `AUTONOMOUS_BUILD_AUTHORIZED` and its limits |
| E5 | Reliability, open-source packaging, and release verification | `NOT_STARTED` | Eligible E4 implementation independently verified and release gate opened |

E0-001 must be independently verified before E1-001 can become `READY`. No downstream authoring task is released during this fixer pass.

While D-016 engineering-first mode is active, the E-track reconciles to the preserved master stage model as follows: E1 supplies the immediate product-definition work analogous to Stage 2; E2 is the Stage 3 architecture decision; E3 covers Stage 4 technical evidence plus model-role benchmarks; E4 is analogous to bounded Stage 5 implementation only after separate founder authorization; and E5 is a bounded Stage 6 reliability/open-source release subset. This mapping does not erase the startup track. E1 Engineering Preview requirements replace customer-wedge selection as the current workflow-definition input, and the E3 suite depends on verified E1/E2 engineering artifacts rather than completion of paused S1-003. If a separate founder decision resumes the startup track, its preserved Stage 1 customer gate applies again.

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

E1-001 and E1-002 remain `BACKLOG`. E1-001 covers items 1–12 and may become `READY` only after E0-001 is independently verified. E1-002 covers items 13–15 and remains blocked until both E0-001 and E1-001 are independently verified. Challenge, fix, and verify operations apply the repository's author/challenger/verifier protocol to each task; no author may mark their own high-risk work verified.

The E1 gate must answer what correctness means before architecture or code begins.

## 19. E2 architecture and ADR gate

E2 is not authorized during this operation. The questions below are comparison subjects, not preselected components, stores, services, or topology. E2 must later compare alternatives and record evidence-backed ADRs for:

- workflow durability and ownership: a dedicated workflow engine, explicit task-state loop, or another bounded mechanism;
- authority relationships among task, conversation/message, execution/effect, artifact/evidence, and causal/history responsibilities, including combined transactional, event-history, workflow-history, content-addressed, and hybrid alternatives;
- whether transcript/activity/search/summary/UI/telemetry views are derived, stored, rebuilt, or combined with an authoritative backbone;
- local persistence and migration alternatives, without assuming a database type or separate store;
- sandbox and local-execution alternatives, their declared isolation tier, and the compatibility path to possible future cloud execution;
- direct provider integration versus router/adapter boundaries, while preserving provider identity and semantics;
- direct capability adapters versus gateway, MCP, or equivalent integration topology;
- approval-policy enforcement and durable receipt alternatives;
- secrets acquisition, storage, injection, redaction, revocation, and evidence boundaries;
- artifact/evidence representation, provenance, retention, integrity, and its relationship to other authority;
- Git workspace isolation and review-package alternatives;
- separate telemetry, audit, evidence, and presentation stores versus a correlated shared backbone;
- structured error and recovery alternatives, including whether a central registry exists;
- concurrency, ordering, version/CAS, queues, leases/fencing, actors, workflow ownership, idempotency, and conflict-handling alternatives;
- recovery, migration, and schema/event evolution;
- plugin and vertical-pack boundaries;
- CLI, web, desktop, or another client surface.

Each comparison must consider correctness, durability, recovery, isolation, security, local-first usability, future cloud/multi-writer extension, operability, testability, migration, open-source contributor burden, cost, and lock-in. No client, language, framework, workflow engine, queue, database, sandbox/container/VM, artifact store, event model, schema library, MCP topology, secret store, provider, model, or permanent model role is selected by this charter.

## 20. E3 benchmark/spike and autonomy-eligibility gate

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

The benchmark must determine which available system or model, if any, may occupy each logical role for each eligible task class: `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER`, and `SECURITY_REVIEWER`. Codex, Terra, Luna, Claude Code, DeepSeek, open/self-hosted models, and future systems remain candidates; none is selected by E0. The benchmark must also determine when escalation is required. Provider access, paid calls, live technical spikes, or final suitability claims remain subject to S0-005, budget, credential, data-policy, and approval constraints.

E3 verification can establish `AUTONOMY_ELIGIBLE`; it cannot activate E4 or authorize implementation. D-016 establishes engineering-first mode, eventual bounded autonomous-task capability, and the requirement to avoid implementation until specification, architecture, and spike gates are verified. It does not authorize autonomous build execution. After E3, a separate explicit founder decision must record `AUTONOMOUS_BUILD_AUTHORIZED` before any E4 loop can run. That future decision may define allowed systems/models, cost limits, task classes, escalation conditions, branch/worktree policy, commit policy, and stop conditions. Current authorization remains `NO` / `NOT_AUTHORIZED`.

## 21. Provisional E4 autonomous build contract

**PROVISIONAL CONTRACT — DESIGN PROPOSAL, INACTIVE.** Only after both (a) E3 is independently verified and records `AUTONOMY_ELIGIBLE` and (b) a separate explicit founder decision records `AUTONOMOUS_BUILD_AUTHORIZED`, a benchmark-approved `AUTONOMOUS_CONTROLLER` may coordinate occupants of the logical `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER`, and `SECURITY_REVIEWER` roles for eligible task classes. A system/model may occupy a role only when the E3 evidence and founder decision allow it. Subject to those still-future conditions, the controller may repeat the following only while eligible `READY` engineering tasks exist:

1. Read `01_governance/PROJECT_STATE.yaml`.
2. Claim the highest-priority unblocked eligible engineering task.
3. Assign only benchmark-approved, founder-authorized role occupants for that task class.
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

This design proposal is not itself an authorization. It does not authorize implementation, external push, pull-request creation, merge, release, deployment, messaging, spending, or any other consequential external action without every separately required approval. It is not active during E0, E1, E2, or E3, and E3 verification alone cannot activate it.

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
- E0-001 is `READY_FOR_REVIEW` and not verified, while E1-001 and E1-002 are `BACKLOG` pending their verified dependencies;
- E2, E3, E4, and E5 are not started, and autonomous build is not authorized;
- this charter and a factual initialization handoff exist;
- D-016, verified customer artifacts, customer evidence, model candidate evidence, role hypotheses, and benchmark-run counts are unchanged;
- YAML, task dependency/status, Markdown, scope, secret, no-source-code, and whitespace checks pass;
- no architecture, model role, customer wedge, pricing, application code, technical spike, benchmark, outreach, external action, or autonomous build mode is created or activated.

E0-001 remains `READY_FOR_REVIEW` until an independent verifier checks these criteria. This charter does not claim verification or production readiness.
