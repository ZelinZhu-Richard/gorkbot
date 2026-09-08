# Engineering Preview v0.1 Product Requirements

Status: E1-001 FIXER PASS — READY_FOR_REVIEW; NOT VERIFIED

Authority: D-016, `MASTER_OPERATING_PROMPT.md`, `01_governance/TASK_REGISTRY.yaml` task E1-001, and the independently verified `03_product/ENGINEERING_PREVIEW_CHARTER.md`

Companion contracts:

- `03_product/ENGINEERING_PREVIEW_USER_FLOWS.md`
- `03_product/ENGINEERING_PREVIEW_CORRECTNESS_CONTRACT.md`

Scope: product and correctness requirements only. This document selects no client, programming language, framework, database, event model, workflow engine, queue, sandbox technology, cloud, agent framework, provider, model, or permanent model role. It creates no application code and authorizes no implementation.

## 1. Requirement language and evidence labels

`MUST`, `MUST NOT`, `REQUIRED`, and `SHALL` are normative. `SHOULD` is a requirement that may be waived only by a recorded reason and review. `MAY` is optional.

Normative scope uses these labels:

- **REQUIRED**: an implementation-neutral v0.1 product or correctness constraint.
- **FUTURE_COMPATIBILITY**: v0.1 must preserve a credible extension or migration path, but the future feature is not in v0.1.

Normative classification and epistemic provenance are separate axes. Per the master operating prompt, evidence statements use **VERIFIED FACT** only when directly supported by current authoritative repository evidence or a reproducible observation, **STRONG INFERENCE** when several observations strongly imply but do not directly document the claim, **DESIGN PROPOSAL** for a challengeable recommendation, and **OPEN QUESTION** for material uncertainty requiring research or testing. `UNKNOWN` is the durable state value paired with an `OPEN QUESTION`; it is not permission to infer an answer. A `REQUIRED` behavior is a normative product target, not an observation that an implementation or customer has validated it.

The repository is authoritative. Model prose, a transcript, an activity indicator, a summary, telemetry, a caller-supplied confirmation value, or a self-authored manifest is not proof of authorization, execution, or completion.

## 2. Product definition

### 2.1 Primary user

**REQUIRED — PRODUCT TARGET, NOT VALIDATED CUSTOMER FACT.** The primary user is one developer, open-source contributor, or technical founder operating locally on a real software repository they are authorized to inspect and change.

The user is expected to understand ordinary repository concepts such as a diff, branch, command, and test result. The product must explain its own task state, approvals, failures, and evidence without requiring the user to understand its internal architecture.

### 2.2 User problem

**REQUIRED — PROBLEM DEFINITION, NOT CUSTOMER-RESEARCH EVIDENCE.** The product must address the need for more than a chat answer: a bounded engineering request carried through repository inspection, change isolation, implementation, deterministic checks, independent completion verification, and a reviewable result without silently losing work, overwriting unrelated changes, leaking secrets, or claiming completion from narration alone.

### 2.3 v0.1 product promise

**REQUIRED.** Engineering Preview v0.1 provides one persistent named software-engineering agent for one local user. For an eligible bounded repository task, the product must either:

1. produce an independently verified review package and valid evidence bundle;
2. return an honest canonical status tuple with nine semantic responsibilities: `task.work_phase`; `task.wait_reasons`; `task.control`; `task.reconciliation`; `task.blocker_refs`; terminal `attempt.disposition`; structured `verification` state and runs; per-operation `operation.status`/`operation.outcome`; and separately referenced `agent.identity`/`agent.availability`; or
3. reject the task before execution with a specific eligibility or authorization reason.

Stopping work, exhausting context, generating a plausible answer, passing one check, or creating a diff is never by itself `COMPLETED`.

### 2.4 Primary end-to-end outcome

```text
engineering request or repository issue
→ admit bounded read-only repository inspection and create durable task identity
→ inspect repository, governing instructions, and capture the user working-tree/base state
→ version a bounded plan and completion predicates
→ establish and bind an isolated task workspace
→ reproduce or diagnose there where potentially mutating execution is applicable
→ edit authorized files
→ use authorized filesystem, terminal, Git, and test capabilities
→ persist progress and reconcile interruption or failure
→ produce and freeze a local patch, isolated branch, bounded commit, or draft-PR package plus its exact review revision and candidate evidence bundle
→ independently verify the adequate predicate set against that exact produced state
→ finalize and return the versioned evidence bundle with the bound verification record
→ require human approval before consequential external action
```

The detailed happy path and exception paths are normative in `ENGINEERING_PREVIEW_USER_FLOWS.md`.

## 3. Eligible v0.1 task classes

Every accepted task must declare one primary class before execution. A task may contain subordinate steps, but one completion predicate set owns the final outcome.

| Task class | v0.1 outcome | Required completion basis |
|---|---|---|
| `BOUNDED_CODE_CHANGE` | Implement a scoped source, test, configuration, build, or maintenance change. | Intended behavior, authorized diff, required checks, reread repository state, review package, independent verification. |
| `DEFECT_REPRODUCTION_AND_FIX` | Reproduce a defect through the reported failure or a predeclared alternative failing oracle, implement a bounded correction, and protect against regression. | Pre-fix failing oracle, causal fix evidence, before/after regression check, authorized diff, independent verification. Inability to establish a failing oracle cannot complete this task class as a verified fix. |
| `REPOSITORY_DIAGNOSIS_OR_REVIEW` | Diagnose, explain, or review a bounded repository concern without necessarily modifying application files. | Declared scope/revision, evidence-backed findings or bounded no-finding conclusion, limitations, independent review of the evidence. |
| `DOCUMENTATION_OR_REPOSITORY_METADATA_CHANGE` | Make a bounded documentation or repository-metadata change. | Required content/values, parse/render or other declared checks, source preservation, authorized diff, independent verification. |
| `NO_CHANGE_REQUIRED` | Demonstrate that the requested state already exists or that an authorized no-op is correct. | Current-state readback, predicate-by-predicate evidence, zero unintended diff, independent verification. |

**REQUIRED.** A request outside these classes must be rejected, narrowed with the user, or recorded as a user-owned note or suggestion that is not an admitted product task and cannot be claimed or executed without a new authenticated user request. The v0.1 core success path ends with a local review package and does not require remote push, pull-request creation, issue mutation, deployment, release, messaging, purchasing, production operations, or another consequential external effect. If an optional v0.1 capability supports such an effect, the correctness contract's separate task authorization, one-shot approval, receipt, and readback rules apply; unsupported effects return typed failure `UNSUPPORTED_CAPABILITY` and a separate honest task condition/disposition.

## 4. Acceptance and bounded task contract

Before the first repository or issue-content read, the product must durably admit a preflight grant containing the user/principal, candidate task and repository/resource identity, exact root/resource and permitted metadata/path reads, governing policy, output/resource limits, and explicit prohibitions on repository code, Git executable helpers, secret locations, and network unless separately granted. Unknown or ambiguous repository authority stops before content access.

The originally supplied request must be preserved without silent semantic rewriting, except that a probable secret must be stopped before model/general persistence where possible. In that case the ordinary record contains a redacted semantic form and, only when authorized, an opaque protected reference; otherwise the product blocks, requests rotation, and directs protected re-entry. It never publishes a low-entropy digest as a substitute.

Before any write, code execution, dependency action, network request, credential use, or other material operation, the product must expand the preflight grant into a durable task contract containing:

- stable task identity and schema version;
- original request or its authorized redacted form and opaque protected reference;
- primary task class and requested outcome;
- repository identity and observed base state;
- admitted repository instruction/context sources, their trust class, scope, precedence, version, conflicts, and authority references;
- included and excluded paths, effects, and deliverables;
- preconditions, dependencies, assumptions, and unknowns;
- versioned plan and task-specific completion predicates;
- tool, filesystem, terminal, Git, test, network, credential, time, cost, retry, verification-rerun, and output bounds;
- model `route_purpose`, `route_eligibility`, route-class authority/evidence, and prohibited routing;
- required approvals and external-action prohibition or allowance;
- interruption, escalation, and stop conditions;
- evidence-bundle requirements and independent-verification level.

If the request is ambiguous in a way that changes the intended behavior, data boundary, authorization, or consequential effect, the task must enter `WAITING_FOR_USER`; the product must not choose the material interpretation silently.

## 5. MVP scope

### 5.1 Required v0.1 scope

| Scope family | Included requirement |
|---|---|
| User and agent | One local user; one persistent named agent with durable identity and bounded authority. |
| Repository | Real local repositories within the normative repository-condition matrix; instruction/context discovery with closed influence and precedence; base and dirty-state inspection; isolated task workspace before potentially mutating reproduction; unrelated-change protection. |
| Engineering work | Bounded planning, reading, editing, terminal use, local Git operations, tests/checks, review package generation. |
| Durability | Durable task, plan, control, approval, operation, failure, artifact, evidence, and verification state sufficient for restart and recovery. |
| Control | Pause, stop, redirect, resume, approval, denial, revocation, and user-question paths with explicit race semantics. |
| Models | Replaceable provider/model integration requirements, explicit resolved identity, separate route purpose/eligibility provenance, no hidden fallback, provider differences preserved, and no model-role assignment by E1. |
| Tools | Structured, versioned, runtime-validated capabilities with explicit effect and permission metadata. |
| Correctness | Task-specific predicates, independent verification, false-completion prevention, honest partial and failed outcomes. |
| Evidence | Inspectable diff or review package plus the versioned evidence bundle defined in the correctness contract. |
| Security | Least privilege, untrusted-content handling, allowed-root enforcement, secret containment, approval boundaries, network and external-action controls. |
| Observability | User-visible durable status, plan, current operation, approvals, retries, failures, artifacts, verification, budgets, and limitations without private chain-of-thought. |
| Open source | Clean-room, public-source, provenance, isolation, evidence, and review constraints that a later contributor flow must preserve; E1-002 exclusively owns the reproducible setup, contribution, evaluation, maintainer, and release procedure. |

### 5.2 Explicit v0.1 non-goals

The following are outside v0.1 and must not be presented as implemented, required, or authorized:

- multiple users, organizations, tenant administration, billing, subscriptions, or enterprise SSO;
- cloud continuation as a v0.1 requirement or production-scale cloud infrastructure;
- visible multi-agent teams, agent-to-agent delegation, group chat, or group conversations;
- mobile applications or full visual/UI parity with Grok Bot;
- skills marketplace, learned workflows, routines, schedules, event triggers, or every connector;
- production deployment or release automation, and any unapproved or autonomous remote Git/PR/issue mutation; optional human-approved external capabilities are never required for the v0.1 core path;
- customer discovery, outreach, pricing, TAM/SAM/SOM, GTM, sales, fundraising, or customer selection;
- General Edition packaging work beyond compatibility constraints;
- Finance Edition packs, market data, financial analysis products, backtesting, paper trading, live trading, personalized investment advice, portfolio/order state, or real-money execution;
- imported external reconstructed source, schemas, internal names, renderer assets, installers, branding, exact copy, or proprietary implementation material;
- a final architecture, client, language, database, workflow engine, event store, sandbox, cloud, agent framework, provider, model, or permanent logical-role assignment;
- autonomous build execution before independently verified E1, E2, and E3 gates and a separate explicit founder decision recording `AUTONOMOUS_BUILD_AUTHORIZED`.

## 6. Functional requirements

Acceptance evidence in this table is a product-level oracle. The correctness contract supplies the detailed lifecycle, permission, completion, and bundle rules.

### 6.1 Identity, task, plan, and authority

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-001` | The agent has a stable durable identity distinct from a process, model session, task, workspace, or client window. | Restart fixture preserves agent identity while process/session identity changes. |
| `FR-002` | Every accepted request creates one stable task identity before execution. | Acknowledgement resolves to a readable durable task record; crash-after-ack does not lose it. |
| `FR-003` | Original request, governing instructions, task class, scope, exclusions, authority, limits, predicates, and status are versioned and inspectable. | Schema validation and history show the initial and current versions without destructive overwrite. |
| `FR-004` | Target-repository instruction files are recorded as `UNTRUSTED_GOVERNING_INPUT` only when their identity, applicable path, and precedence are admitted under the closed influence rules in the correctness contract. They may narrow workflow details but cannot broaden founder/user/project authority or override sandbox, secret, network, approval, destructive-action, model-routing, or evidence policy; issue/PR text and non-admitted documentation remain `UNTRUSTED_CONTEXT`. | Conflicting root/local instruction and issue/PR fixtures preserve the higher-authority contract, apply only permitted narrowing, and enter `task.wait_reasons` or `task.blocker_refs` rather than silently selecting a material interpretation. |
| `FR-005` | The plan is bounded, versioned, mapped to completion predicates, and revised when evidence changes. | Each executed material step resolves to a current plan item; superseded versions remain inspectable. |
| `FR-006` | A material scope or outcome change requires user clarification or a versioned authorized redirect. | Mutation test cannot add paths, capabilities, credentials, spend, or external effects silently. |
| `FR-007` | Task status is the canonical multi-component tuple defined in the correctness contract. Each scalar axis is mutually exclusive only within itself; independent waits/blockers and `task.reconciliation` may overlap `task.control`; terminal `attempt.disposition` and any emphasized primary label are derived from durable facts, never model narration or client presence. | Required legal combinations reconstruct exactly; illegal combinations are schema/semantic failures; misleading-model and reconnect fixtures cannot set `attempt.disposition=COMPLETED` or erase a companion axis. |
| `FR-008` | The task records one current accountable owner and prevents silent concurrent ownership. | Two-worker fixture has one accepted owner; stale owner cannot persist a state or effect. |
| `FR-009` | A minimal durable preflight grant limits the first repository/issue read before any untrusted content is opened; it authorizes no code/helper execution, secret-location access, or implicit network. | Pre-admission malicious repository, Git-helper, secret-file, and remote-issue fixtures produce zero ungranted access/effect and a typed denial. |

### 6.2 Repository and workspace behavior

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-010` | Preflight records repository identity, observed revision, branch/ref, all applicable repository-condition-matrix rows, worktree/common-repository topology, tracked/untracked/ignored/generated state, submodule/nested/LFS facts, and governing instruction/context sources before any task work. Each condition receives exactly one current disposition and composed constraints. | Preflight bundle matches an independent repository readback and rejects or waits on every `REJECTED_V0_1`/unresolved `UNKNOWN_E2_E3` condition before mutation or reproduction. |
| `FR-011` | Existing tracked, untracked, ignored, generated, nested-repository, shared-ref, and other user material is user-owned and is neither overwritten nor silently included, transported, installed, staged, committed, stashed, restored, reset, cleaned, or removed. | Supported dirty-state fixtures preserve unrelated byte/ref identities and report every included, excluded, carried, and unavailable class. |
| `FR-012` | After read-only admission/base capture and before any potentially mutating reproduction, diagnosis command, dependency/test/build hook, or edit, the product establishes and binds an isolated task-identified workspace or another E2-selected mechanism with equivalent non-interference evidence. Unisolated mutating reproduction requires an explicit product rule and authenticated authorization; repository text cannot grant it. | Concurrent task/user-change and reproduction-location evidence show no unintended overlap, a separable task diff, and no potentially mutating oracle run in an unisolated user working tree. |
| `FR-013` | Every filesystem operation is confined to normalized authorized roots and handles links, special files, archives, sizes, and traversal safely. | Allowed-root and malicious-path negative suite fails closed with no out-of-root effect. |
| `FR-014` | Reads and writes preserve file identity, encoding, permissions, line endings, and any declared all-or-detectably-interrupted update semantics; partial writes are detected. | Before/after evidence and interrupted-write fixture show either valid new content or retained/recoverable prior content, never silent corruption. |
| `FR-015` | The final repository state and changed files are reread after edits and before completion. | Evidence bundle contains post-change identities generated after the last write. |

### 6.3 Terminal, Git, and test capabilities

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-020` | A terminal operation declares task, workspace, working directory, normalized command/action, environment policy, timeout, output bound, cancellation class, and expected effect before launch. | Operation record validates before execution; malformed or unauthorized fields are denied. |
| `FR-021` | Terminal results retain start/end, exit or termination state, bounded stdout/stderr or artifact references, timeout/cancel facts, and uncertain effects. | Success, nonzero exit, timeout, cancellation, and truncated-output fixtures remain distinguishable. |
| `FR-022` | Commands are not authorized merely because their text appears read-only; their declared capability/effect class and runtime policy control execution. | Adversarial command/tool description cannot change its permission class. |
| `FR-023` | Every Git action is classified by the normative matrix as `READ_ONLY`, `LOCAL_REVERSIBLE`, `LOCAL_DESTRUCTIVE`, `EXTERNAL_READ_EFFECT`, or `REMOTE_EFFECT`, with an independent v0.1 disposition and approval rule. Only admitted supported actions may run; local Git permission never implies helpers, credentials, network, remote effects, or destructive cleanup. | The matrix covers every named action and an exact review package is produced without unclassified ref/worktree/user-material or remote mutation. |
| `FR-024` | Local commits and optional remote actions occur only under their matrix row. `APPROVAL_REQUIRED` never enables `PROHIBITED_V0_1`; destructive user-material/shared-ref actions, force updates, remote deletion, and prohibited merge/tag actions remain denied even if conversationally approved. | Target/ownership-sensitive permission review denies every prohibited action, requires approval/readback for each supported consequential action, and records zero undeclared state change. |
| `FR-025` | Required tests/checks are derived from the admitted request, task-class minimums, explicit agreement, or applicable repository instructions under `FR-004`; a declared command is not an execution/network/credential grant. Checks are recorded before execution and cannot be silently weakened, removed, skipped, or rescued by one later pass after flakiness is known or detected. | Comparison exposes deleted/relaxed/uncovered checks; ungranted requirements wait/block; skipped and `FLAKY` checks have their required status consequence. |
| `FR-026` | Test results identify exact check/run identity, command, workspace, reviewed revision, tool/version/configuration/environment, ordered repetitions, exit/result, bounded output/artifact, duration, and predicate relationship. Mixed results on the same revision/configuration/environment remain classified `FLAKY`, never `PASS`; only the associated predicate may receive pass credit when a prospectively declared repetition rule is satisfied. | Evidence validator rejects unattributed “tests passed” prose, reclassification of mixed outcomes as `PASS`, and a single-pass claim after mixed outcomes. |
| `FR-027` | Installing or executing untrusted dependencies, build hooks, test hooks, or downloaded binaries is a separately classified operation subject to policy, network, and approval rules. | Malicious-dependency fixture cannot execute by being named in repository text. |

### 6.4 Durable execution and user control

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-030` | An accepted state/control mutation is acknowledged only after durable recording sufficient for recovery. | Crash immediately after acknowledgement retains exactly one mutation. |
| `FR-031` | Orchestrator/worker interruption resumes every affected nonterminal task from authoritative state or moves it to an honest `task.reconciliation=RECOVERING`/blocked state. Client-only disconnect/reconnect rebuilds presentation and does not interrupt a healthy execution owner; a verifier-layer interruption becomes a separately attributed verification-run error rather than automatic task failure or pass. | Fault review distinguishes client, orchestrator, worker, executor, and verifier loss across every applicable lifecycle class with no false completion. |
| `FR-032` | Before replaying an operation after uncertainty, the product checks idempotency evidence, receipt, target readback, and current authority; unresolved consequential effects are never retried blindly. | Crash-around-effect fixture produces one effect or an explicit `operation.outcome=OUTCOME_UNCERTAIN`, never an unrecorded duplicate. |
| `FR-033` | Pause, stop, force-stop, redirect, and resume are durable ordered commands with the semantics in the user-flow and correctness contracts. Stop proceeds through cooperative cancellation, a finite reconciliation window, safe/available force termination or authority fencing, and final workspace/effect reconciliation; process death alone never implies completion. | Race and bounded-control review reproduces the declared winner, preserves every request/outcome, and proves no untrusted operation can make itself permanently non-interruptible. |
| `FR-034` | Retry ceilings are defined by failure class before execution; authorization, policy, malformed-input, unknown-effect, and terminal failures do not auto-retry. | Injected failures stop at the configured ceiling and retain every attempt. |
| `FR-035` | Corrupt, incompatible, or incomplete durable state is not silently accepted or overwritten. | Corruption fixture preserves original evidence and enters a typed recovery, blocked, or failed state. |
| `FR-036` | Context compaction may change only derived model-working context and may not destroy or supersede task, conversation, operation, approval, artifact, audit, or completion evidence. | Long-context/restart test retrieves authoritative facts omitted from a lossy summary and rejects a stale summary. |
| `FR-037` | Autonomy is bounded to one user-admitted task contract and its current plan. The product cannot discover/select new work, delegate to visible peer agents, widen paths/capabilities/network/credentials/budgets/effects, weaken predicates, or continue past time, cost, tool, output, and retry ceilings without the applicable authenticated task amendment; a consequential action additionally requires its applicable approval. | Scope, queue, recursive-work, retry, budget, stale-plan, and capability-expansion checks show no operation outside the admitted task; exhaustion yields a truthful wait/block/noncomplete result plus only the separately bounded safety reserve. |

### 6.5 Tool permissions, approvals, and secrets

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-040` | Every capability has a stable versioned identity; input/output schemas; owner; effect, reversibility, idempotency, network, credential, Git-action, approval, and v0.1-disposition classes; limits; cooperative cancellation, force-termination/fencing, and maximum settle semantics. | Registry/contract validation rejects missing/incompatible material metadata and denies untrusted-code execution without bounded descendant termination/fencing/accounting. |
| `FR-041` | Inputs and outputs are runtime-validated at every trust boundary with size, type, enum, version, unknown-field, correlation, and adversarial-content handling. Invalid requests fail before dispatch; invalid results fail before consumption or downstream effect and trigger reconciliation of any already-dispatched effect. | Malformed/oversized/unknown-version/mismatched-result suite proves zero dispatch for invalid requests and an explicit `operation.outcome=OUTCOME_UNCERTAIN`/readback path for invalid effectful results. |
| `FR-042` | Authorization is deny-by-default and bound to the user/task, capability, normalized action, resource, workspace, policy version, limits, and time/use scope. | Wrong task/target/actor/version/replay fixtures hard-fail. |
| `FR-043` | Human approval is distinct from authorization and is required for the consequential classes in the correctness contract. | A conversational “yes,” prompt instruction, regex, tool name, or caller Boolean cannot create a valid receipt. |
| `FR-044` | Approval, denial, expiry, and revocation are durable and historically tamper-detectable. Approval binds to principal/task/attempt/operation/action/target/base/policy/use/expiry rather than an ephemeral worker; it may survive crash and successor-owner installation only after exact revalidation and recorded ownership change. Mutation, substitution, ambiguity, expiry, revocation, replay, or possible prior dispatch invalidates or reconciles it. | Post-approval restart, mutation/replay, crash-around-dispatch, and audit gap/tamper checks produce at most one authorized effect and block verification on unexplained history. |
| `FR-045` | Network access is separately visible, bounded, and policy-controlled; local repository permission does not imply arbitrary egress. | Unapproved DNS/redirect/domain/download and Git-remote fixtures are denied and recorded. |
| `FR-046` | Secrets are never requested or stored in ordinary chat, repository files, model working context, command text, inherited/general environment, general logs, screenshots, artifacts, diffs, or evidence bundles. Protected-location policy covers the minimum families in the correctness contract and overrides an otherwise allowed repository/workspace root. Unknown or ambiguous secret-location content is denied read/egress/use pending protected resolution; detection is explicitly non-exhaustive. | Marker-secret, in-root protected-location, alias/descendant, and accidental-paste review finds zero marker occurrences outside the explicitly authorized recipient boundary and retains a safe exposure/rotation record without echo or digest leakage. |
| `FR-047` | Secret use is least-scope, purpose-bound, time-bounded, auditable, and revocable. A protected operation may receive a raw value only through the selected recipient boundary; the value is never returned to model/UI/general tool output or inherited by descendants. Revocation cancels/reconciles in-flight use. | Wrong task/tool/endpoint/child/stale use and queued or active post-revocation use fail or reconcile visibly; marker scans and receipts expose no secret value. |
| `FR-048` | Every authority, audit, artifact, evidence, workspace, temporary credential, and process class has an explicit retention/cleanup owner and policy. Holds prevent conflicting cleanup; deletion claims distinguish logical inaccessibility from physical erasure and require exact-scope readback or explicit uncertainty without erasing historical activity. | Retention, hold, expiry, cleanup, cache/replica, link-swap, and deletion-readback checks preserve required evidence, leave unrelated/user data unchanged, and reject unsupported erasure claims. |

### 6.6 Model-provider abstraction and routing

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-050` | Core task, lifecycle, permission, approval, evidence, and completion semantics do not depend on one provider's native state or naming. | Recorded fixtures for two provider shapes map to the same product invariants while retaining differences. |
| `FR-051` | Every model operation records requested/resolved provider/model/configuration identity, logical role, `route_purpose`, `route_eligibility`, class authority/evidence version, route reason/policy, E3-or-user authorization reference when applicable, fallback parent, timing, usage/cost when exposed, bounds, and unknowns. | Evidence validator rejects an unattributed or purpose/class-incompatible model result. |
| `FR-052` | Provider-specific tool, streaming, refusal, fallback, usage, cost, cancellation, stop, context, and error semantics remain observable and are not fabricated or flattened into success prose. | Transport/refusal fixtures preserve exact supported/unsupported distinctions and typed outcomes. |
| `FR-053` | Routing uses separate `route_purpose` and `route_eligibility` values. `NORMAL_PRODUCT_TASK` admits only `PRODUCTION_OR_NORMAL_ELIGIBLE`; `E3_EVALUATION` may admit `EVALUATION_ONLY` candidates only under separately authorized E3 scope/budget/data/credential policy and does not itself promote them; `USER_EXPERIMENTAL` may admit only an explicitly selected `USER_CONFIGURED_UNVERIFIED` route with a visible warning and no default/fallback/release-evidence credit. `DISALLOWED` never dispatches for any purpose. Every class still obeys task/data/capability/cost/network/credential policy. This requirement assigns no model role and authorizes no E3 or paid call. | Route-policy review shows evaluation candidates can produce attributed candidate evidence without normal eligibility, user experiments are never silently promoted, and disallowed routes transmit zero bytes/incur zero call cost. |
| `FR-054` | Fallback is off unless explicitly configured for a compatible route purpose/class. Each fallback is a new recorded route/configuration, never silently crosses into evaluation/user-experimental eligibility, and its result is not credited to the requested model. | Provider-failure review shows either no fallback or a complete separately attributed and class-compatible fallback record. |
| `FR-055` | Logical roles remain provider-neutral and no permanent model assignment is made by E1. | Specification and governance scans find no vendor/model selected as controller, planner, executor, coder, verifier, or security reviewer. |

### 6.7 Observability, artifacts, verification, and outcomes

| ID | REQUIRED behavior | Objective acceptance evidence |
|---|---|---|
| `FR-060` | The user can inspect every canonical status component using axis-qualified names, plan/predicate version and adequacy map, current operations, workspace/base and repository conditions, approvals, retries/recovery, blockers, budgets, route provenance, artifacts, verification runs/errors, and limitations. | Disconnect/reconnect produces an equivalent view without collapsing `task.control`, `task.reconciliation`, `attempt.disposition`, `verification`, or `agent.availability`. |
| `FR-061` | User-visible explanations expose concise decisions, evidence, and uncertainty without exposing or requiring private chain-of-thought. | Review confirms decisions are understandable and evidence-linked without hidden reasoning traces. |
| `FR-062` | Operational telemetry, activity views, audit facts, and completion evidence remain distinguishable even if E2 later correlates or combines their storage. Material authorization, denial, approval/revocation, secret-boundary, operation/effect/readback, and verification history has append-only/immutable semantics and product-caused, concurrent-writer, or accidental alteration/deletion/reordering/gaps are detectable. v0.1 does not claim resistance to the authorized local principal, root, or host compromise. | Dropped/spoofed telemetry cannot change task outcome or authorize an action; detected material audit/evidence poisoning blocks verification without selecting a hash or storage mechanism. |
| `FR-063` | Artifacts have stable identity, task/workspace/revision provenance, type, producer, sensitivity, integrity/staleness facts, retention rule, and inspectable location/reference. | Mutated, stale, missing, or wrong-task artifact is rejected by evidence validation. |
| `FR-064` | Every run, including open wait/block/control/reconciliation combinations, terminal noncomplete disposition, verifier error, flaky check, or uncertain effect, produces or updates a secret-safe evidence bundle whose canonical status components, route provenance, author/executor/verifier/challenger provenance, and 0..n sequential verification runs remain intact; at most one verification run is active. | Conditional-field review proves no projection collapses control/recovery, cancellation/verification, partial result, blocker, route class, or effect certainty or admits concurrent active verification runs. |
| `FR-065` | `attempt.disposition=COMPLETED` requires an evidence-backed `PREDICATE_SET_ADEQUATE` result, all applicable predicates, and independent verification against the exact reviewed revision. The verifier maps every material request/class/governing/scope obligation to an objective predicate or justified `NOT_APPLICABLE`; executor self-report and passing weak/irrelevant predicates are insufficient. | Misleading executor, weak predicate set, missing requested behavior, stale/post-verification-mutated diff, skipped/flaky check, and verifier-error review cannot reach `attempt.disposition=COMPLETED`. |
| `FR-066` | Completion assertions rejected before authoritative admission are recorded as `UNSUPPORTED_COMPLETION_ASSERTION`; an admitted `COMPLETED` disposition while the gate is false is `FALSE_TERMINAL_COMPLETION`, a zero-tolerance blocking failure. Both retain claimed state, observed state, causal evidence, and correction path. | Evaluation distinguishes correctly rejected assertions from escaped false terminal completion and blocks release on every latter occurrence. |
| `FR-067` | Partial success and useful artifacts are preserved without upgrading the outcome. `attempt.disposition=PARTIALLY_COMPLETED` is used only for an intentional terminal close with useful requested output and unmet predicates; resumable waits/blocks remain open; verifier infrastructure errors leave `verification.status=UNVERIFIED`; and user stop closes only as `attempt.disposition=CANCELLED` with separate partial-result/verification/effect facts. | Late failure, resumable blocker, verifier error, cancellation, and useful partial-output review each retain artifacts while producing the correct distinct components. |
| `FR-068` | When a separately authorized optional capability performs a consequential external effect, completion requires fresh authoritative readback or an explicit unresolved/unknown effect outcome. | Cached model/tool output alone cannot satisfy the external-state predicate; absent capability returns `UNSUPPORTED_CAPABILITY` with zero effect and a separate honest task condition/disposition. |
| `FR-069` | The product generates at least one inspectable local review form: patch, isolated branch, bounded commit, draft-PR package, or evidence-backed diagnosis/no-change report. A draft-PR package contains package/schema identity, explicit `NOT_SUBMITTED`, repository/base and proposed head/commit-or-patch references, changed-file inventory, title, summary/body, request/issue reference or reason `NOT_APPLICABLE`, applicable contribution checklist with instruction provenance, checks including skipped/flaky results, known limitations/unmet predicates/outstanding effects, evidence-bundle/current-verification references, and external capability/approval status. | Independent user can inspect/apply/review the selected form and a draft package cannot be mistaken for an externally created PR. |

## 7. Reliability requirements

The detailed contract is `ENGINEERING_PREVIEW_CORRECTNESS_CONTRACT.md`, Section 14. These are **HARD_INVARIANTS**, not observed results or production claims. One relevant breach prevents `COMPLETED` and blocks release:

| ID | Preview correctness requirement |
|---|---|
| `RR-001` | Recover 100% of acknowledged authoritative mutations needed for task/message/plan/control/approval/effect/artifact/evidence/verification recovery within the declared supported local persistence boundary; lose zero acknowledged records. |
| `RR-002` | Every affected task after supported orchestrator/worker interruption resumes from the latest valid acknowledged state or reaches an explicit recovery/block/failure/uncertain state; client-only reconnect does not interrupt healthy work. |
| `RR-003` | Produce zero unintended duplicate material non-idempotent or consequential local/external effects; every uncertain effect is read back or escalated and none is called complete. |
| `RR-004` | Accept zero stale authoritative owner/writer mutations; let zero stale projections/summaries influence newer authority; preserve 100% of authority/evidence through context reduction. |
| `RR-005` | Enforce finite declared ceilings, including cooperative/force-stop and stop-reconciliation bounds; after productive exhaustion start zero new productive/task-advancing work, allowing only a preauthorized separately bounded control/safety/cancellation/readback/evidence/cleanup reserve. |
| `RR-006` | Reconcile every accepted pause/stop/force-stop/redirect; start zero material operation ordered after durable control acceptance under superseded authority; within the declared stop bound terminate or fence descendants, classify unresolved effects explicitly, and never let repository code claim permanent non-interruptibility. |
| `RR-007` | Across every supported task, lose, overwrite, stage, commit, delete, or silently mix zero unrelated user changes and reconcile initial/final repository/diff facts. |
| `RR-008` | Produce zero `FALSE_TERMINAL_COMPLETION` outcomes and zero `attempt.disposition=COMPLETED` results without adequate/all predicates, valid evidence, every operation terminal/accounted, zero uncertain effect, required readback, `task.control=NONE`, `task.reconciliation=NONE`, no current wait/blocker/pending event, any pause resumed, any stop resolved only to `attempt.disposition=CANCELLED`, redirect verification on the current revision, and current authoritative `verification.verdict=PASSED`. |
| `RR-009` | Give a noncomplete result to every required missing/skipped/failed/stale/unverifiable or unresolved `FLAKY` check and every verification error; account for every operation, execution/verification attempt, and bundle failure without converting verifier infrastructure failure to task failure or pass. |
| `RR-010` | Validate every required bundle revision against its outcome profile; completed bundles additionally have zero unresolved mandatory reference/revision/semantic mismatch. |
| `RR-011` | Execute zero malformed/incompatible/oversized/stale/unknown executable contracts and use zero hidden fallback or route-class elevation; every model operation records requested/resolved provenance, `route_purpose`, `route_eligibility`, authorization, and fallback, and evaluation/user-experimental results never establish normal eligibility. |
| `RR-012` | Silently prune zero needed records; bind every retention/hold/cleanup/deletion action to authoritative readback or explicit uncertainty and preserve historical evidence. |
| `RR-013` | Dispatch zero cost-bearing operations without an enforceable conservative authorized ceiling, including when live usage is unavailable; incur zero budget-gate violations. |
| `RR-014` | Correlate every material operation and verification run from intent to result/readback or explicit uncertainty/error; detect/account for accidental and product-boundary adversarial loss, gaps, truncation, delay, reordering, substitution, retries, and cancellation; telemetry or a digest alone proves neither authority nor completion. |
| `RR-015` | Across every relevant occurrence, permit zero unauthorized effect/read, destructive action against user-owned material, protected-secret/private-data disclosure even inside an allowed root, workspace/root escape, approval replay/mutation, post-verification mutation presented under stale evidence, or clean-room/provenance violation. |

The correctness contract defines stable `SLO-001`–`SLO-004` `PREVIEW_SLO` families and `MET-001`–`MET-004` `MEASURE_ONLY` families. Aggregate thresholds are **UNKNOWN** at E1-001. E1-002 must predeclare thresholds/populations only for the SLO families; E3/E5 later observe them. Measure-only families remain report-only unless prospectively reclassified. No aggregate score may compensate for a hard-invariant failure.

## 8. Security requirements

The security and approval matrices in the correctness contract are normative. At minimum v0.1 must:

1. treat repository content, issues, comments, documentation, web content, dependencies, test output, tools, MCP metadata/results, model output, generated code, and artifacts as untrusted data;
2. deny unregistered capabilities and unapproved scope by default;
3. enforce allowed workspace/filesystem, command, process, resource, network, Git, credential, and external-effect boundaries outside model judgment;
4. prevent content from changing its own trust, side-effect, permission, approval, or evidence class;
5. keep secret values out of model context and general product records;
6. bind approvals to exact normalized actions and reject replay, mutation, substitution, expiry, revocation, ambiguous post-dispatch reuse, and stale-owner consumption while allowing only exact successor-owner revalidation;
7. preserve evidence of malicious inputs and denials without executing their instructions or leaking sensitive payloads;
8. require negative coverage for traversal/link/archive escape, in-root user-material destruction, command injection, prompt injection/instruction escalation, malicious dependencies, network redirects, protected secret locations, approval restart/replay, duplicate effects, cancellation/force-stop races, stale workers, post-verification mutation, evidence poisoning, and forbidden external material;
9. distinguish a local single-user preview boundary from future tenant or hostile-workload isolation claims; and
10. make any selected isolation class and known gap explicit after E2/E3 rather than treating a process, thread, container, or encryption mechanism as sufficient by name.

## 9. E1-002 contribution-workflow handoff constraints

E1-001 does not author the open-source contribution workflow. That procedure, including setup steps, commands, environment matrix, templates, review sequence, and maintainer actions, is exclusively an E1-002 deliverable after E1-001 verification.

E1-002 may not weaken these product constraints: clean source plus public repository specifications must be sufficient without private chat, customer data, production credentials, or external reconstructed material; contributor changes remain isolated and evidence-backed under the same security/correctness rules; independent review and maintainer approval remain distinct; and secret/private/forbidden/provenance/license gaps or weakened controls fail closed. These are handoff constraints, not a contributor procedure.

## 10. E1-002 evaluation-suite handoff constraints

E1-001 does not define cases, fixtures, seeds, harnesses, executable oracles/graders, repetitions, scoring, aggregate thresholds, or an evaluation artifact. E1-002 must trace every `FR-*`, `RR-*`, `SLO-*`, `MET-*`, `FC-*`, lifecycle transition, completion predicate, evidence profile/field, and `NEG-*` requirement to concrete reproducible coverage with an independent oracle and expected status tuple. Positive, adversarial/negative, interruption/fault, and unsupported-case coverage is required where applicable. E1-002 instantiates rather than replaces these invariants.

## 11. E1-002 release-gate handoff constraints

E1-001 does not create a release checklist or checkpoint. The later E1-002 gate may not waive a hard invariant; it must predeclare/pass every `PREVIEW_SLO`, report every `MEASURE_ONLY` metric, require independently verified E0/E1/E2/E3 and authorized/verified applicable E4 work, require E5 independent release verification against the exact candidate, preserve clean-room/secret/provenance/security/evidence blockers, state preview limitations, and require accountable human release approval. E1-002 owns the executable criteria and checkpoint.

## 12. Future compatibility constraints

These constraints do not add future features to v0.1.

| ID | FUTURE_COMPATIBILITY constraint | v0.1 evidence required |
|---|---|---|
| `FC-001` | Cloud execution | Local task/workspace/operation identities and contracts are not permanently tied to one process or machine path; E2 documents migration and unsupported assumptions. |
| `FC-002` | Multiple devices and writers | Mutations carry stable identities/versions sufficient for a later explicit ordering, conflict, dedupe, and reconciliation design; v0.1 tests stale-state rejection. |
| `FC-003` | Multiple persistent agents | Agent identity, task ownership, capability scope, and workspace scope are not global singletons; no agent-to-agent behavior is implemented. |
| `FC-004` | Multi-user and multi-tenant SaaS | Authority, ownership, resource, credential, artifact, and audit contracts can later accept organization/tenant/principal scopes; v0.1 makes its single-user trust assumptions explicit. |
| `FC-005` | Skills, routines, and vertical packs | Capabilities, procedures, policies, evaluations, and provenance are versionable and reviewable; no loader, marketplace, schedule, or event trigger is required. |
| `FC-006` | General Edition | Shared core product semantics remain domain-neutral; General-specific packaging is deferred. |
| `FC-007` | Finance Edition | Finance can later add a governed pack without duplicating core task, tool, approval, evidence, or security semantics; no finance schema or feature enters v0.1. |
| `FC-008` | Schema and event evolution | Every durable interchange or record has an explicit version and incompatible data fails or migrates visibly; the storage/event mechanism remains an E2 decision. |
| `FC-009` | Provider evolution | New providers can preserve core invariants and provider-specific semantics without renaming product truth or granting automatic eligibility. |

## 13. Requirements traceability matrix

This matrix traces requirement families to authoritative or bounded evidence inputs. The external audit may corroborate Level A properties; Level B material is reserved for E2 comparison and is not evidence for E1 requirements or selections; Level C details are excluded.

| Requirement family | IDs | Primary authority | Bounded evidence input | Required verification evidence |
|---|---|---|---|---|
| Local-first one-user/one-agent target | `FR-001`–`FR-009`, MVP scope | D-016; Charter §§4–5; D-003 | Baseline GBF-001 is documented target context only, not customer or runtime evidence | Identity/restart/task-schema tests; no multi-agent implementation. |
| Repository workflow and change isolation | `FR-010`–`FR-027` | D-016 workflow; Charter §5.2; master completion standard | External audit Level A evidence/provenance principles; no external workspace design | Dirty-repo, allowed-diff, terminal/Git/test, review-package scenarios. |
| Durable lifecycle, bounded autonomy, and recovery | `FR-030`–`FR-037`, `RR-001`–`RR-006` | Charter §§4.4, 5.1, 6–7, 11; master runtime requirements | Baseline GBF-010/011/015 are documented but untested; external audit Level A restart/effect properties | Lifecycle transition review and deterministic fault matrix. |
| Permission, approval, secrets, and retention | `FR-040`–`FR-048`, `RR-012`, `RR-015` | `SECURITY.md`; Charter §§9, 12; master security principles | Baseline GBF-009/022–024 is documented, enforcement untested; external audit Level A counterexamples only | Approval/security negative-case matrix with zero hard violations. |
| Model abstraction and routing | `FR-050`–`FR-055` | D-004; Charter §§5.3, 19–20; model registry/benchmark policy | Baseline GBF-031 is reference behavior only; Level B material is reserved for E2 and not used here | Route-purpose/eligibility matrix coverage; two-shape conformance; no provider/role selected; only later authorized E3 can produce qualification evidence. |
| Observability and evidence | `FR-060`–`FR-069`, `RR-008`–`RR-014` | D-003/D-016; Charter §§5.4–5.5, 8, 10; master completion standard | Baseline GBF-013/014 encourages artifacts but does not prove verification; external audit Level A evidence-closure property only | Bundle schema validation, reconnect projection, false-completion and stale-artifact tests. |
| Reliability invariants and metric families | `RR-001`–`RR-015`, `SLO-001`–`SLO-004`, `MET-001`–`MET-004` | Charter §11; E1-001 objective/acceptance criteria | Benchmark-plan thresholds are unrun design inputs; no reliability claim imported | Hard-invariant challenge; E1-002 aggregate thresholds; later E3/E5 results and confidence reporting. |
| Clean room and open source | Non-goals; §9 handoff constraints | D-002/D-016; Charter §16; `SECURITY.md` | Verified external-audit review establishes research limits, not code rights | E1-002 provenance/license/forbidden-artifact coverage and independent review. |
| Evaluation and release boundary | §§10–11 handoff constraints | D-016; task E1-001/E1-002 ownership; Charter §§18, 20, 22 | No external or benchmark result derives the gate | E1-002 owns suite/release artifacts; E3/E5 later supply observations. |
| Future compatibility | `FC-001`–`FC-009` | D-001, D-003, D-004, D-016; Charter §15 | Level B alternatives are reserved E2 inputs and are not E1 evidence | E2 ADR comparison and migration/compatibility review; no future feature in v0.1. |

### 13.1 Operational crosswalk

Every functional requirement's acceptance interpretation has seven distinct facets even when the table abbreviates them: user/actor, trigger and preconditions, expected behavior, failure behavior, permissions, returned evidence, and measurable acceptance. Unless a row narrows them, §2.1 and the listed user flow supply the user and trigger/preconditions; the FR behavior column supplies expected behavior; the applicable user-flow exception plus correctness-contract §10 supplies failure behavior; contract §§3, 8, and 9 supply permissions; the applicable §12 evidence profile/sections supply returned evidence; and the FR acceptance-evidence column supplies the measurable product-level oracle. E1-002 later instantiates executable cases and oracles.

| Requirement IDs | Primary user-flow coverage | Correctness-contract coverage |
|---|---|---|
| `FR-001`–`FR-009` | UF-01, UF-02, UF-07, UF-08 | §§2–5, especially admitted authority and agent/task identity. |
| `FR-010`–`FR-015` | UF-01, UF-02, UF-08 | §§3, 7, 8.1–8.2. |
| `FR-020`–`FR-027` | UF-02, UF-08, UF-10, UF-12 | §§6.1, 8.3–8.5, 9.1–9.3, 10. |
| `FR-030`–`FR-037` | Global invariants; UF-01, UF-02, UF-04–UF-08, UF-12, UF-13, UF-15 | §§3.3–7, 10, 13.4, 14. |
| `FR-040`–`FR-048` | UF-01, UF-06, UF-09–UF-11, UF-15 | §§3.2–3.3, 6, 9, 10, 12, 15. |
| `FR-050`–`FR-055` | UF-02, UF-07, UF-08, UF-12 | §§3, 7, 9.1–9.3, 10, 12–14. |
| `FR-060`–`FR-069` | UF-02, UF-08–UF-10, UF-13–UF-15 | §§4, 6, 10–15. |
| `RR-001`–`RR-015`; `SLO-001`–`SLO-004`; `MET-001`–`MET-004` | Global invariants; UF-04–UF-15 emphasize control, recovery, evidence, and truthful outcomes | §§3–16, with the normative reliability and measurement contracts in §14. |
| All 23 stable `NEG-*` IDs defined in contract §15 | Global invariants; UF-01–UF-15 | §15 defines required stimulus/outcome families; E1-002 owns concrete cases and fixtures. |
| `FC-001`–`FC-009` | Global non-goals and UF-16 ownership boundary | §§1, 5, 16–18, 20. |

## 14. Preserved unknowns and prohibited inference

The following remain **UNKNOWN** until later authorized work:

- final client surface and interaction form;
- state, storage, history, event, projection, and compaction architecture;
- local isolation mechanism and demonstrated isolation class;
- supported host platforms, repository sizes, languages, build systems, and tool catalog;
- funded model/API access, exact provider configurations, route-class assignments/qualification evidence, thresholds, and role occupants;
- benchmark and implementation budget;
- final preview latency/cost envelopes by repository/task class;
- distribution, packaging, update, migration, and rollback implementation;
- customer demand, willingness to pay, market size, pricing, or production suitability;
- reference-product runtime reliability, stop/recovery behavior, account rollout, and parity.

No unknown may be filled from model reputation, external reconstruction details, or a single unverified run.

## 15. E1-001 completion boundary

This corrected fixer draft is ready for independent post-fix verification when the three E1-001 artifacts, governance records, original-handoff addendum, and fixer handoff exist; their identifiers and terms reconcile; and required fixer validations pass. It remains unverified until an independent verifier checks the corrected bytes and every challenger finding.

E1-001 does not activate E1-002. E1-002 remains `BACKLOG` until E1-001 is independently `VERIFIED`. E2, E3, E4, E5, customer work, architecture, application implementation, model benchmarks, paid calls, external actions, and autonomous build remain unauthorized or not started according to current governance.
