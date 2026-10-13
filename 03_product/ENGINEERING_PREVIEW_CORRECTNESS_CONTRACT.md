# Engineering Preview v0.1 Correctness Contract

Status: E1-001 FIXER PASS — READY_FOR_REVIEW; NOT VERIFIED

Authority: D-016, `MASTER_OPERATING_PROMPT.md`, task E1-001 in `01_governance/TASK_REGISTRY.yaml`, and the independently verified `ENGINEERING_PREVIEW_CHARTER.md`

Companion specifications:

- `03_product/ENGINEERING_PREVIEW_PRD.md`
- `03_product/ENGINEERING_PREVIEW_USER_FLOWS.md`

This contract defines semantic responsibilities and testable invariants. It does not select a client, language, storage mechanism, database, event model, workflow engine, queue, isolation technology, provider, model, agent framework, tool topology, credential mechanism, or deployment target.

## 1. Normative model and precedence

`MUST`, `MUST NOT`, `REQUIRED`, and `SHALL` are normative. `SHOULD` may be waived only by a versioned reason and independent review. `MAY` is optional.

Requirements are classified as:

- **HARD_INVARIANT**: applies to every relevant occurrence. One violation makes the attempt nonconformant, prevents `COMPLETED`, and is release-blocking.
- **PREVIEW_SLO**: an aggregate preview target. Its population, window, exclusions, threshold, repetition count, and confidence method must be predeclared by E1-002; observations come only from later authorized evaluation.
- **MEASURE_ONLY**: a required reported measurement with no v0.1 pass/fail threshold. Making it a gate requires a prospective E1 amendment/reclassification before scored evaluation.
- **FUTURE_COMPATIBILITY**: preserves an extension or migration path but does not implement the future feature.
- **DESIGN_PROPOSAL**: an explicit, challengeable proposal, not observed capability or selected architecture.
- **UNKNOWN**: information or evidence does not yet exist and must not be inferred.

These normative classes do not turn proposals into observed capability. Evidence records independently classify material claims as fact, inference, proposal, or unknown with source/provenance; a required behavior remains a product contract until later implementation and evaluation evidence shows conformance.

If a companion document conflicts with this correctness contract on lifecycle, authority, approval, completion, or evidence, the conflict blocks verification and requires an E1-001 amendment. Repository governance remains superior to all product documents. Target-repository content may narrow work only through the closed instruction-scope and precedence rules in §3.2; it cannot broaden authority.

## 2. Terms and separate semantic axes

| Term | Normative meaning |
|---|---|
| Governance task | A repository work item such as E1-001. Its `READY_FOR_REVIEW` and `VERIFIED` values are governance states, not product runtime states. |
| Product task | One accepted user engineering request governed by a durable task contract. |
| Agent | The one user-visible persistent v0.1 engineering-agent identity; not a worker, process, model invocation, or logical role. |
| Attempt | A versioned execution effort for a product task. A terminal attempt is never silently reopened or overwritten. |
| Operation | One bounded model, tool, filesystem, terminal, Git, test, control, approval, recovery, or verification action. |
| Effect | A material local or external state change attributable to an operation. |
| Author | The execution path that proposes the result. Author checks are not independent verification. |
| Challenger | An optional adversarial review role only when a task or evaluation policy requires one; absence is recorded as not applicable and E1 selects no occupant. |
| Independent verifier | A separate accountable verification path that evaluates durable evidence and the exact reviewed revision without relying on author narration. |
| Review revision | The exact repository/artifact state to which a verification verdict applies. Any material mutation makes the new state unverified. |
| Approval | An authenticated policy decision authorizing one exact consequential attempt; it is not verification, human patch acceptance, or proof of effect success. |
| Review package | A local patch, isolated branch, bounded commit, draft-PR package, or evidence-backed diagnosis/no-change report. It is not an external pull request. |

Correctness MUST NOT be encoded in one overloaded status. The product preserves exactly these nine semantic responsibilities even if E2 later chooses different internal names or combines their physical representation:

1. `task.work_phase`: one mutually exclusive scalar while an attempt is open; a terminal record retains `last_work_phase` only as history;
2. `task.wait_reasons`: an independent bounded set with zero or more current wait records;
3. `task.control`: one mutually exclusive scalar with values `task.control=NONE`, `task.control=PAUSING`, `task.control=PAUSED`, or `task.control=STOPPING`;
4. `task.reconciliation`: one mutually exclusive scalar with values `task.reconciliation=NONE`, `task.reconciliation=RETRYING`, or `task.reconciliation=RECOVERING`;
5. `task.blocker_refs`: an independent bounded set; nonempty means the open task is blocked;
6. `attempt.disposition`: one mutually exclusive terminal scalar, absent while the attempt is open;
7. `verification`: aggregate `verification.status`, zero or more immutable verification runs, and an authoritative `verification.verdict` only when one applies;
8. per-operation `operation.status` and terminal `operation.outcome`, never collapsed into task disposition; and
9. separately referenced `agent.identity`/`agent.identity_state` and `agent.availability`, neither of which is task authority.

Mutual exclusion applies only inside one scalar domain. Waits and blockers are independent records; `task.reconciliation=RECOVERING` may overlap a control, wait, or blocker where §4.2 permits it. Only `attempt.disposition` is terminal. The authoritative view is the complete tuple, not a winner-takes-all label.

A user-facing primary label is a derived projection only. It may emphasize, in order: `attempt.disposition`; `task.control=STOPPING`; `task.reconciliation=RECOVERING`; `task.control=PAUSING` or `task.control=PAUSED`; a named `task.wait_reasons` entry; nonempty `task.blocker_refs`; `task.reconciliation=RETRYING`; then `task.work_phase`. It MUST expose every other nonempty component and cannot erase a pending approval/question, stop cause, partial-result fact, verification result/error, or `operation.outcome=OUTCOME_UNCERTAIN`.

Axis-qualified notation is normative whenever a token is reused: for example `task.control=PAUSED`, `task.reconciliation=RECOVERING`, `verification.verdict=BLOCKED`, `operation.status=WAITING_FOR_APPROVAL`, `operation.outcome=CANCELLED`, `attempt.disposition=CANCELLED`, and `agent.availability=PAUSED`. A bare value is permitted only inside a table whose header explicitly names its axis.

## 3. Authority and durable-state responsibilities

### 3.1 Required semantic responsibilities

E2 may combine or separate physical representations, but the following responsibilities MUST remain distinguishable, versioned, correlated, recoverable, and independently testable:

| Responsibility | Authoritative content | Material that is not authority over it |
|---|---|---|
| Task | Request, scope, exclusions, owner, limits, dependencies, policy, approvals needed, plan, predicates, current phase, disposition. | Transcript phrasing, model intent, activity indicator, client memory. |
| Conversation/message | Authorship, ordering, original content/reference, trust class, authorization context, corrections, control messages. | A compacted summary or presentation projection. |
| Execution/effect | Operation identity, authorization, dispatch, tool/provider result, retries, cancellations, receipts, readbacks, uncertainty. | Tool success prose, telemetry, author narration. |
| Artifact/evidence | Inputs, patches, diffs, test results, approvals, artifacts, provenance, limitations, verification records. | A digest or self-authored manifest by itself. |
| Causal/history | History sufficient for ordering, audit, recovery, stale-owner rejection, reconciliation, and any selected projection rebuild. | Latest-state display without retained causal facts. |
| Presentation/working context | Transcript view, activity, search, summaries, model context, UI state, optional telemetry. | Any authorization, effect, evidence, or completion record. |

This table does not require six stores or services. D-005 governs project-repository authority and MUST NOT be interpreted as selecting repository files for product runtime persistence.

### 3.2 Admitted authority record

Before the first repository/issue-content read, a minimal preflight grant MUST durably bind the local principal, candidate task/repository or resource, exact allowed root/resource and metadata/path reads, policy version, trust labels, output/resource bounds, and prohibitions on repository code or Git-helper execution, secret locations, and network unless separately granted. It authorizes no write or effectful inspection.

Before later material execution, the expanded product-task authority MUST durably bind:

- authenticated user/principal, task, agent, attempt, workspace, and repository identities;
- original request and admitted governing inputs with identities, versions, precedence, and trust labels;
- task class, requested outcome, allowed and forbidden scope, paths, capabilities, effect classes, data/network/credential scope, and resource limits;
- plan and completion-predicate versions;
- policy and tool-contract versions;
- approval requirements, retry and budget ceilings, and retention/evidence obligations.

Permission is the intersection of governing policy, admitted task scope, current user grant, and trusted capability limits. No layer may broaden another. Unknown, conflicting, stale, malformed, or ambiguous authority fails closed to a typed denial, `task.wait_reasons=WAITING_FOR_USER`, or a `task.blocker_refs` record.

The one local principal MUST have a stable authenticated identity for task admission and approval semantics. E2 selects the authentication mechanism, but E1 requires wrong, changed, lost, stale, or unverifiable principal identity to deny admission/approval and prevent continuation until re-established. Local operating-system presence, client access, or conversational self-assertion alone is not authorization.

Repository files, issue text, web content, documents, model output, generated code, test/build output, dependencies, tool names/descriptions/results, discovered tool servers, restored artifacts, summaries, and telemetry are untrusted content. They cannot grant capability, satisfy approval, change policy, widen scope, or prove completion.

Target-repository instruction influence is a closed, fail-closed contract. File names do not create trust. `AGENTS.md`, `CLAUDE.md`, path-local instruction files, `CONTRIBUTING*`, `README*`, and comparable files may be admitted as `UNTRUSTED_GOVERNING_INPUT` only with content identity/version, applicable repository path, declared role, and precedence. `README*` and `CONTRIBUTING*` are contextual by default and become governing only for an explicitly admitted contribution/workflow purpose. Issue/PR titles, bodies, comments, patches, and attachments are `UNTRUSTED_CONTEXT`; an authenticated user may adopt a material requirement into the task contract, but the source text itself remains untrusted.

The precedence and conflict rule is:

1. nonwaivable platform/runtime boundaries plus this project's repository-authoritative governance and security policy;
2. authenticated founder/user authority within those bounds;
3. the current admitted task contract/amendments and trusted capability contracts, each only within higher authority;
4. applicable `UNTRUSTED_GOVERNING_INPUT`, which may only narrow the first three layers; and
5. `UNTRUSTED_CONTEXT`, which supplies evidence or requested context but no governing power.

Within layer 4, an explicitly recorded repository hierarchy applies; a more path-specific instruction may further narrow only its descendant scope. If applicable sources conflict on a material command, output, ownership, or completion requirement and the recorded hierarchy does not resolve it, the product adds `WAITING_FOR_USER` to `task.wait_reasons` or creates a `task.blocker_refs` record. It never chooses by model preference.

Admitted repository instructions MAY only: propose commands/checks that still require existing execution/network/credential grants; impose formatting/style and contribution/commit/review-package conventions; narrow included paths or identify ownership/no-touch paths; and state source, build, test, verification, or file-handling expectations. They MUST NOT grant or expand roots, capabilities, execution, network, credentials, protected secret locations, budgets, destructive actions, external effects, model routing, trust/evidence classes, or approvals; weaken/add-after-the-fact completion predicates; override founder/user/project/sandbox/security policy; or authorize stage, architecture, release, or autonomous-build changes. A declared check that needs ungranted authority yields a visible unmet precondition or wait/block, never an implicit grant.

### 3.3 Durable mutation contract

Every accepted task, plan, control, approval, effect, artifact, evidence, or verification mutation MUST record:

- stable record and command/operation identities;
- actor/principal and accountable role;
- observed prior version and accepted new version or equivalent stale-mutation proof;
- policy, authority, plan, and predicate versions in force;
- causal parent and correlation identities;
- safe time basis and acceptance/result time;
- prior and resulting semantic state;
- evidence or receipt references and user-visible outcome.

An acknowledgement is returned only after the mutation is durable enough for declared recovery and is rereadable. Duplicate delivery returns the original outcome. Stale, illegal, or unauthorized mutations are retained as rejected attempts and do not change state. Material authorization, denial, approval/revocation, secret-boundary, operation/effect/readback, and verification facts have append-only/immutable semantics: corrections and retention/deletion actions add linked records rather than silently rewriting history, and deletion, alteration, reordering, or unexplained gaps are detectable and block verification.

The v0.1 tamper/gap threat model targets product-caused, concurrent-writer, and accidental mutation or evidence poisoning inside the declared local persistence boundary. It does not claim resistance to the authorized local principal, root/administrator, host compromise, host rollback, or deliberate store deletion. Stronger hostile-local and multi-tenant resistance is a `FUTURE_COMPATIBILITY` concern under `FC-004`. This boundary does not weaken the rule that any detected unexplained material gap blocks verification/completion, and it selects no hash, log, or storage architecture. Exact concurrency, audit, integrity, and persistence mechanisms are E2 decisions.

## 4. Product-task lifecycle

### 4.1 Task work phases

| Phase | Meaning | Entry condition | Legal exits |
|---|---|---|---|
| `CREATED` | A durable task identity and original request or authorized redacted/protected reference exist; admission is not complete. | Request is captured without effectful execution. | `READY`, a wait/block qualifier, or named terminal disposition. |
| `READY` | Task contract is sufficiently bounded and authorized to await claim. | Eligibility, authority, scope, limits, and initial predicates validate. | `QUEUED`, user redirect, stop/cancel. |
| `QUEUED` | The already user-admitted task waits for the single current execution owner under a finite declared bound and visible order. | Waiting admission is durable; this is not self-selection from an autonomous or externally discovered work queue. | `CLAIMED`, pause, stop/cancel, redirect. |
| `CLAIMED` | One accountable current owner holds the attempt under a stale-owner proof. | Exactly one claim is accepted against the current ownership version or equivalent. | `ANALYZING`, recovery, pause, stop/cancel. |
| `ANALYZING` | Admitted governing/context inputs and repository state are inspected read-only before workspace establishment; no potentially mutating reproduction or untrusted code runs there. | Authorized owner and safe preflight. | `PLANNING`, a wait/blocker, retry/recovery, pause/stop. |
| `PLANNING` | Bounded plan, predicate coverage/adequacy map, workspace profile, and controls are being created or revised. | Current evidence supports a bounded proposal. | `READY_TO_EXECUTE`, a wait/blocker, pause/stop. |
| `READY_TO_EXECUTE` | The isolated task workspace has been established/bound from the captured base and current plan, predicates, permissions, repository conditions, route provenance, and limits validate. | Pre-dispatch and non-interference validation pass. | `EXECUTING`, wait for approval, redirect, pause/stop. |
| `EXECUTING` | One or more authorized operations are active or settling. | Operation-specific authorization validates. | `OBSERVING`, `READY_FOR_VERIFICATION`, waiting, blocked, retry/recovery, pause/stop, noncomplete disposition. |
| `OBSERVING` | The author is rereading repository/effect state and assembling evidence. | Material execution ended or reached an observable checkpoint. | `EXECUTING`, `READY_FOR_VERIFICATION`, blocked/recovery, pause/stop. |
| `READY_FOR_VERIFICATION` | Author proposes that predicates are reviewable; no verified-completion claim exists. | Review revision and candidate evidence bundle are fixed and author checks pass. | `VERIFYING`, redirect/supersession, blocked, cancellation. |
| `VERIFYING` | Independent verification is evaluating the exact review revision. | Eligible verifier, independence, revision, authority, and evidence validate. | verification verdict and corresponding attempt disposition or a new corrective attempt. |

### 4.2 Wait, control, reconciliation, and blocker components

These components remain independent from `task.work_phase` and from one another except for the explicit validation rules below.

| `task.wait_reasons` value | Meaning | Required record |
|---|---|---|
| `WAITING_FOR_USER` | A specific material answer is required. | Question, why material, affected predicates, safe continuation boundary, response correlation. |
| `task.wait_reasons=WAITING_FOR_APPROVAL` | An exact consequential action is proposed with `operation.status=WAITING_FOR_APPROVAL` but is not approved/dispatched. | Normalized request, zero-effect fact, expiry, and denial/revocation paths. |
| `WAITING_FOR_EXTERNAL_EVENT` | An authorized observable condition must change before safe continuation. | Expected event/readback, timeout, polling/notification limit, owner, fallback. |

| `task.control` value | Meaning | Required record |
|---|---|---|
| `task.control=NONE` | No current pause/stop control restricts the open attempt. | Current control version. |
| `task.control=PAUSING` | A durable pause request is being reconciled with in-flight operations. | Request/effective timestamps, settling operations, effects after request. |
| `task.control=PAUSED` | No productive/task-advancing operation may start; only separately authorized bounded safety, cancellation, readback, evidence-preservation, and recovery work may run. | Effective checkpoint, operation classifications, resume preconditions. |
| `task.control=STOPPING` | A durable stop/force-stop request is being reconciled; no productive/task-advancing operation may start under superseded authority. | Ordering, cancellation/termination/fencing attempts, deadline, operation outcomes, partial-result facts, cleanup/readback. |

| `task.reconciliation` value | Meaning | Required record |
|---|---|---|
| `task.reconciliation=NONE` | No current retry or recovery reconciliation is active. | Current reconciliation version. |
| `task.reconciliation=RETRYING` | A retryable failure is inside its prospectively declared ceiling. | Original failure, attempt count/ceiling, next owner/time, retained costs/effects. |
| `task.reconciliation=RECOVERING` | Authoritative state and interrupted operations are being validated/reconciled. | Failure boundary, ownership proof, integrity/readback results, safe exit. |

Each `task.blocker_refs` item records a stable blocker identity, owner, attempted safe alternatives, unblock predicate, timeout/escalation, affected predicates, and whether it is active, resolved, or carried to a successor. A nonempty active set means progress is blocked; it does not consume another scalar.

The following combination rules are normative and bundle validation MUST reject every invalid combination:

| Combination | Validity | Required consequence |
|---|---|---|
| `task.control=PAUSING` plus `task.reconciliation=RECOVERING` | VALID while open | Recovery may perform only pause/control/safety reconciliation; ordinary execution cannot resume. |
| `task.control=STOPPING` plus `task.reconciliation=RECOVERING` | VALID while open | Stop intent dominates; recovery exits only to continued stopping or `attempt.disposition=CANCELLED`. |
| `task.control=PAUSED` plus `task.reconciliation=RECOVERING` | VALID while open | Pause stays effective while bounded recovery/readback runs. |
| `task.wait_reasons=WAITING_FOR_APPROVAL` plus `task.reconciliation=RECOVERING` | VALID while open | A decision may be received/recorded but cannot be consumed or dispatched until recovery and current pre-dispatch revalidation finish. |
| Active `task.blocker_refs` plus `task.control=PAUSED` | VALID while open | Clearing one does not clear the other; both gates resolve before productive work. |
| `attempt.disposition=CANCELLED` plus `verification.status=UNVERIFIED` or causally compatible `verification.status=FINISHED` and `verification.verdict` | VALID when terminal | Preserve all runs/revision bindings with zero completion credit; `verification.status=IN_PROGRESS` is invalid at terminal close, and a current authoritative `verification.verdict=CHANGES_REQUIRED` requires `attempt.disposition=SUPERSEDED`, not `attempt.disposition=CANCELLED`. |
| `attempt.disposition=COMPLETED` plus a nonterminal operation or `operation.outcome=OUTCOME_UNCERTAIN` | INVALID | Reject transition/bundle as false terminal completion. |
| `task.control=PAUSED` plus `task.control=STOPPING` | STRUCTURALLY IMPOSSIBLE | They are values of one scalar; stop replaces pause through an ordered control mutation. |
| `task.control=PAUSING`, `task.control=PAUSED`, or `task.control=STOPPING` plus `task.reconciliation=RETRYING` | INVALID | Suspend/cancel pending productive retry; only recovery/safety reconciliation may coexist. |
| `task.reconciliation=RETRYING` plus `task.reconciliation=RECOVERING` | STRUCTURALLY IMPOSSIBLE | They are values of one scalar; recovery replaces retry through an ordered mutation. |
| Any terminal `attempt.disposition` plus an active `task.work_phase`, wait, `task.control` other than `task.control=NONE`, `task.reconciliation` other than `task.reconciliation=NONE`, active task blocker, or `verification.status=IN_PROGRESS` | INVALID | Terminal record retains `last_work_phase` and historical/carry-forward references, not active qualifiers. |
| `task.control=PAUSED` plus productive `operation.status=RUNNING` | INVALID | Only separately authorized safety/readback/recovery operations may run. |

A wait may coexist with `task.control=PAUSED`; an answer/approval received while paused is recorded but launches no work until authorized resume. `DELEGATING` and `WAITING_FOR_AGENT` are unreachable v0.1 work states and remain `FUTURE_COMPATIBILITY` only because visible multi-agent delegation is out of scope.

### 4.3 Attempt dispositions and verification verdicts

| `attempt.disposition` value | Meaning | Completion credit |
|---|---|---|
| `attempt.disposition=COMPLETED` | The common completion gate and every applicable task predicate passed on the exact reviewed revision, with independent `verification.verdict=PASSED`. | Full only for that revision. |
| `attempt.disposition=PARTIALLY_COMPLETED` | The attempt is intentionally terminally closed with useful requested output and at least one unmet required predicate. It is not used while a wait/block remains resumable and does not replace user-stop `attempt.disposition=CANCELLED`. | None as completed work. |
| `attempt.disposition=FAILED` | The attempt cannot continue under its current contract after a terminal failure, exhausted authorized recovery, or hard-boundary violation. | None. |
| `attempt.disposition=CANCELLED` | User or policy ended the attempt; completed effects are preserved, not implicitly rolled back. | None. |
| `attempt.disposition=SUPERSEDED` | A materially different authorized task/attempt replaced this one with an explicit link. | None for the superseded attempt. |

The aggregate verification axis accepts `verification.status=UNVERIFIED`, `verification.status=IN_PROGRESS`, or `verification.status=FINISHED`. Each attempt has 0..n immutable verification runs, executed strictly sequentially: a new run cannot start until the preceding run is `verification.run_status=FINISHED` or `verification.run_status=VERIFICATION_ERROR`, and at most one run may have `verification.run_status=IN_PROGRESS`. Aggregate `verification.status=IN_PROGRESS` means exactly one current run is in progress. A run records identity/sequence, verifier identity and exact configuration, route provenance, bounded input-context manifest, independence mechanism, candidate bundle/review revision, `verification.run_status`, predicate evidence, accountable failure layer, and retryability. Run status is `verification.run_status=IN_PROGRESS`, `verification.run_status=FINISHED`, or `verification.run_status=VERIFICATION_ERROR`. Exactly one substantive `verification.verdict`—`verification.verdict=PASSED`, `verification.verdict=CHANGES_REQUIRED`, `verification.verdict=BLOCKED`, or `verification.verdict=INCONCLUSIVE`—exists only when `verification.run_status=FINISHED`.

A verifier crash/timeout, verifier-tool failure, deterministic-check infrastructure failure, or verifier-side evidence-collection failure is `verification.run_status=VERIFICATION_ERROR`; it leaves aggregate `verification.status=UNVERIFIED` and is neither `attempt.disposition=FAILED` nor a pass. Missing/inadequate candidate evidence is instead `verification.verdict=CHANGES_REQUIRED`, `verification.verdict=BLOCKED`, or `verification.verdict=INCONCLUSIVE` according to its evidence; it cannot be disguised as infrastructure error.

The authoritative verification is the latest eligible `verification.run_status=FINISHED` run on the current unchanged revision/contract that has not been invalidated or superseded. When a required later run errors, aggregate status returns to `verification.status=UNVERIFIED` and no old pass is silently current. A same-revision rerun is permitted only after a verifier/provider/check-infrastructure failure recorded as retryable `verification.run_status=VERIFICATION_ERROR`, and only inside a prospectively declared verification ceiling. Every run remains. A substantive `verification.verdict=BLOCKED` or `verification.verdict=INCONCLUSIVE` is not a same-revision retry reason; further verification requires a newly versioned candidate/task-contract/evidence basis after its named unblock or correction. `verification.verdict=CHANGES_REQUIRED` closes the reviewed attempt as `attempt.disposition=SUPERSEDED` with that cause and creates a linked unverified correction attempt; same-revision rerun cannot forum-shop it. `verification.verdict=BLOCKED` is distinct from a task blocker, though it normally creates one.

### 4.4 Legal transition rules

The nominal path is:

```text
CREATED → READY → QUEUED → CLAIMED → ANALYZING → PLANNING
→ READY_TO_EXECUTE → EXECUTING ↔ OBSERVING
→ READY_FOR_VERIFICATION → VERIFYING
→ attempt.disposition=COMPLETED only with verification.verdict=PASSED
```

For every transition, the implementation MUST enforce the authorized actor, exact prior state/version, current-ownership proof, prerequisites, persisted record, affected operations/effects, cancellation behavior, idempotency/reconciliation rule, visible tuple/projection, and recovery path.

| Transition family | Authorized actor | Additional precondition and effect rule |
|---|---|---|
| Admit/queue/claim | User or authorized runtime/controller as applicable | Eligibility and authority validate; only one current owner; stale owners cannot write state or effects. |
| Analyze/plan/execute/observe | Current owner under task contract | Each operation separately validates; evidence and effects stay correlated to current versions. |
| Enter/leave wait | Runtime/controller; user supplies response/decision | Exact wait record exists; response is correlated, current, and authorized; all material constraints revalidate. |
| Pause/resume/stop/redirect | User or an applicable hard policy | Control is durable and ordered; in-flight effects reconcile as specified in §6. |
| Retry/recover | Runtime/controller within declared policy | Retryability, ceiling, authority, ownership, repository state, effect certainty, and budgets validate. |
| Propose verification | Author | Exact review revision is fixed; required author evidence exists; this is not completion. |
| Verify | Independent verifier | Independence, least privilege, exact revision, predicates, and evidence validate; no authority broadening. |
| Complete | Derived correctness gate only | Sole author, model, UI, tool, or controller cannot directly set it. |
| Fail/cancel/supersede | User, hard policy, or runtime under declared terminal rule | Effects and evidence are reconciled/preserved; no silent reopen. |

A terminal `attempt.disposition` is immutable. Further work creates a linked successor or explicit reopen attempt. Terminal records retain `last_work_phase` and historical/carry-forward records, not active wait/control/reconciliation/blocker state. Any post-verification material mutation creates a new revision with `verification.status=UNVERIFIED` while preserving the old run/verdict only for its bound revision.

The complete semantic transition families are below. A destination that is a wait/control/block qualifier updates that axis while preserving the suspended work phase; a destination that is a disposition closes the attempt.

| From | To | Authorized actor | Preconditions, persisted effect, and recovery |
|---|---|---|---|
| `CREATED` | `READY` | Runtime/controller under admitted user request | Eligibility, authority, scope, limits, initial predicates, repository reference, and zero unauthorized effects validate; persist admission version. |
| `CREATED` | `task.wait_reasons=WAITING_FOR_USER` / active `task.blocker_refs` / `attempt.disposition=FAILED` / `attempt.disposition=CANCELLED` | Runtime/controller or user for cancel | Persist the precise ambiguity, missing authority, unsupported/hard denial, or cancel receipt and zero-effect evidence. Only the wait/block path is resumable. |
| `READY` | phase `QUEUED` | Runtime/controller | Current user-admitted task contract validates; persist finite waiting bound and user-visible order without self-selecting other work. |
| `QUEUED` | phase `CLAIMED` | Runtime/controller | Exactly one eligible current owner is accepted under the current ownership version/equivalent stale-owner proof; rejected contenders persist no ownership mutation. |
| `CLAIMED` | phase `ANALYZING` | Current owner | Revalidate authority, repository/workspace identity, and ownership proof; start only authorized inspection. |
| `ANALYZING` | `PLANNING` | Current owner | Governing inputs/read-only preflight are sufficient; persist findings/unknowns and no potentially mutating reproduction before a bound workspace. |
| `PLANNING` | `READY_TO_EXECUTE` | Current owner | Current plan maps every material step/request/class/instruction obligation to scope, capability, limits, and predicates; establish/bind the isolated workspace and validate its carry/exclude profile before entry. |
| Any applicable nonterminal phase | add `task.wait_reasons=WAITING_FOR_APPROVAL` and set referenced `operation.status=WAITING_FOR_APPROVAL` | Current owner/controller | Preserve suspended phase and exact normalized consequential action; launch zero effect before valid receipt. Approval returns through current authorization and pre-dispatch validation; denial/expiry/revocation records zero dispatch and returns to safe replanning/wait/block/cancel. |
| `READY_TO_EXECUTE` | `EXECUTING` | Current owner | Operation-specific authorization and any required approval validate against current versions immediately before dispatch. |
| `EXECUTING` | `OBSERVING` | Current owner | Material operation reaches a known or explicitly uncertain boundary; persist results/effects before readback. |
| `OBSERVING` | `EXECUTING` | Current owner | Fresh evidence justifies another plan-authorized operation and all authority/bounds revalidate. |
| `OBSERVING` | `READY_FOR_VERIFICATION` | Author/current owner | Exact review revision and candidate bundle are fixed; author predicates/checks are fully recorded; no complete claim. |
| `READY_FOR_VERIFICATION` | `VERIFYING` and `verification.status=IN_PROGRESS` | Independent verifier/controller | The §11.3 independence floor, least privilege, bounded context, exact revision, and verification ceiling validate; persist a new run identity/configuration/provenance. |
| `VERIFYING` | `attempt.disposition=COMPLETED` | Derived gate after `verification.verdict=PASSED` | The §11 conjunction is true; persist adequacy/predicate results, verifier/revision, bundle revision, and final disposition as one recoverably consistent gate decision. |
| `VERIFYING` | old `attempt.disposition=SUPERSEDED`; new `task.work_phase=PLANNING` | Verifier returns `verification.verdict=CHANGES_REQUIRED`; user/runtime admits correction attempt | Preserve old verdict/revision with cause; create linked correction attempt with new owner/plan/predicate versions, `verification.status=UNVERIFIED`, and no inherited approval. |
| `VERIFYING` | `verification.verdict=BLOCKED` or `verification.verdict=INCONCLUSIVE` plus applicable `task.blocker_refs` | Independent verifier/controller | Persist failed/unassessed predicates and unblock action, set `verification.status=FINISHED`, and grant no completion credit. |
| `VERIFYING` | `verification.run_status=VERIFICATION_ERROR`; aggregate `verification.status=UNVERIFIED` | Verifier/controller | Persist accountable layer, error evidence, retryability/ceiling, and no task pass/fail inference; unchanged-state rerun is allowed only by §4.3. |
| Any nonterminal work phase | add `task.wait_reasons=WAITING_FOR_USER` or `task.wait_reasons=WAITING_FOR_EXTERNAL_EVENT` | Current owner/controller | Persist response/event correlation, timeout and safe continuation; no work outside current safe boundary. Resume returns only after full revalidation. |
| Any active work phase | `task.control=PAUSING` | User or applicable hard policy | Persist request before acknowledgement; launch no new productive/task-advancing operation; classify in-flight work and allow only the bounded control/safety reserve. |
| `task.control=PAUSING` | `task.control=PAUSED` | Runtime/controller | No productive/pre-pause operation remains running: each is terminal, safely checkpointed/cancelled, or has `operation.outcome=OUTCOME_UNCERTAIN`; bounded safety/readback/recovery may coexist. |
| `task.control=PAUSED` | `task.control=NONE` and recorded resumable phase, optionally with `task.reconciliation=RECOVERING` first | User or applicable policy | Authorized resume plus §6.5 revalidation; recovery never erases the pause before resume is accepted. |
| Any nonterminal work/wait/control phase | `task.control=STOPPING` | User or applicable hard policy | Persist stop/deadline before acknowledgement; launch no productive work; cooperatively cancel, then force-terminate or fence no later than the bound; preserve partial artifacts. |
| `task.control=STOPPING` | `attempt.disposition=CANCELLED` | Runtime/controller after bounded reconciliation | Descendants are terminated/fenced and every operation is terminal or explicitly uncertain; clear active components, preserve verification/effects, and carry unresolved target risk to a successor. Work cessation alone is never completion. |
| Any active work phase with `task.control=NONE` | `task.reconciliation=RETRYING` | Runtime/controller | Failure is retryable, inside declared ceiling/budget, and safe for exact effect; retain original attempt/cost. |
| `task.reconciliation=RETRYING` | `task.reconciliation=NONE` plus prior legal phase / active blocker / `attempt.disposition=FAILED` | Runtime/controller | Revalidate before retry; success returns appropriately, while exhaustion/unsafe retry yields explicit block/failure. |
| Any nonterminal phase after interruption/integrity doubt | `task.reconciliation=RECOVERING` | Runtime/controller | Persist recovery ownership while preserving control/waits/blockers; prevent stale writes/effects and perform §7 reconciliation before work. |
| `task.reconciliation=RECOVERING` | `task.reconciliation=NONE` plus prior legal phase / wait / `task.control=PAUSED` or `task.control=STOPPING` / active blocker / noncomplete disposition | Runtime/controller | Exit reflects current controls, authority, integrity, and effect certainty; never infer completion. |
| Any nonterminal phase | add active `task.blocker_refs` | Current owner/controller or verifier | Persist blocker, owner, alternatives, unblock predicate, timeout/escalation, preserved work/effects. |
| Active `task.blocker_refs` | resolve applicable blocker and return to recorded phase or `task.reconciliation=RECOVERING` | Authorized user/event/controller | Named unblock predicate and all material state revalidate; otherwise remain blocked. |
| Any nonterminal phase | `attempt.disposition=PARTIALLY_COMPLETED` or `attempt.disposition=FAILED` | Runtime/controller under declared terminal predicate/failure rule | Use partial only for intentional terminal close with useful output and no active resumable qualifiers; reconcile effects, preserve artifacts, record failed/missing predicates and next action; zero completion credit. |
| Any nonterminal phase | `attempt.disposition=SUPERSEDED` | User-authorized material redirect/controller | Preserve original contract/evidence, link successor, invalidate changed approvals/verdicts, and perform no silent scope transfer. |
| Any terminal `attempt.disposition` | no in-place exit | None | Correction/continuation creates a linked successor/reopen attempt; terminal history remains immutable. |

## 5. Agent lifecycle

Agent identity and operational availability MUST be separate from product-task, worker, model, role, and client lifecycle.

### 5.1 Durable identity state

| `agent.identity_state` value | Meaning |
|---|---|
| `agent.identity_state=REGISTERED` | Stable named identity exists. |
| `agent.identity_state=ENABLED` | Identity may accept eligible work under policy. |
| `agent.identity_state=DISABLED` | Identity accepts no new work; in v0.1 active tasks are safely paused or cancelled and ownership is released only after reconciliation. No other visible agent is selected. |
| `agent.identity_state=RETIRED` | Identity no longer operates; history and evidence remain addressable. Retirement is explicit and does not delete tasks. |

### 5.2 Operational availability

| `agent.availability` value | Meaning |
|---|---|
| `agent.availability=OFFLINE` | No eligible runtime/worker is available; agent identity and tasks remain durable. Client-only disconnection does not make the agent offline while a healthy owner continues. |
| `agent.availability=IDLE` | Enabled and owns no active execution. |
| `agent.availability=BUSY` | Owns one active task/attempt under one current ownership version or equivalent stale-owner proof. |
| `agent.availability=WAITING` | Owned task awaits a named input, approval, or event. |
| `agent.availability=PAUSED` | Agent/task control prevents new material work. |
| `agent.availability=RECOVERING` | New or returning owner is reconciling durable state. |
| `agent.availability=DEGRADED` | A bounded capability is unavailable; limitations and eligible work are explicit. |
| `agent.availability=STOPPED` | Runtime work has stopped, but identity and task history persist. |

v0.1 exposes one persistent agent and at most one current execution owner per task. Logical author/verifier roles and model calls do not become additional persistent user-visible agents. An already user-admitted task may wait in `QUEUED` only under a finite declared bound and visible order; v0.1 does not self-discover or self-select a continuous/autonomous queue. The user may cancel or redirect a queued task, and queue saturation rejects or waits visibly. “Stop task,” “pause agent,” “disable agent,” “worker stopped,” and “client disconnected” are distinct controls/events.

Agent identity survives model replacement, process or worker restart, client closure, repository change, and task completion. A worker loss changes availability and moves affected tasks to recovery; it never deletes the agent or implies task completion.

Legal agent transitions are fully axis-qualified because the table contains two distinct agent axes:

| Qualified source state | Qualified destination state | Actor and gate |
|---|---|---|
| `agent.identity_state=REGISTERED` | `agent.identity_state=ENABLED` | User/governance enables the durable identity under current policy. |
| `agent.identity_state=ENABLED` | `agent.identity_state=DISABLED` | User or hard policy prevents new claims and durably reconciles current work; disabling does not delete tasks. |
| `agent.identity_state=DISABLED` | `agent.identity_state=ENABLED` | Authorized user action after policy, credentials, limits, and affected task state revalidate. |
| `agent.identity_state=REGISTERED`, `agent.identity_state=ENABLED`, or `agent.identity_state=DISABLED` | `agent.identity_state=RETIRED` | Explicit authorized retirement; active tasks are first safely paused/cancelled, ownership is released, and history remains. |
| `agent.availability=OFFLINE` or `agent.availability=STOPPED` | `agent.availability=RECOVERING` | A worker returns and validates identity, policy, ownership, and tasks before availability. |
| `agent.availability=RECOVERING` | `agent.availability=IDLE`, `agent.availability=BUSY`, `agent.availability=WAITING`, `agent.availability=PAUSED`, or `agent.availability=DEGRADED` | Authoritative task ownership and capability state determine the truthful projection. |
| `agent.availability=IDLE` | `agent.availability=BUSY` | An eligible user-admitted product task is claimed under one current ownership version/equivalent stale-owner proof. |
| `agent.availability=BUSY` | `agent.availability=WAITING`, `agent.availability=PAUSED`, `agent.availability=RECOVERING`, or `agent.availability=DEGRADED` | The corresponding task/control/capability record is durable; agent state alone does not change task truth. |
| `agent.availability=WAITING`, `agent.availability=PAUSED`, or `agent.availability=DEGRADED` | `agent.availability=BUSY` | Named resume/unblock and full revalidation succeed for the currently owned task. |
| `agent.availability=BUSY`, `agent.availability=WAITING`, `agent.availability=PAUSED`, or `agent.availability=DEGRADED` | `agent.availability=IDLE` | Current task reaches a reconciled terminal/ownership-release point and no other task is silently claimed. |
| Any operational availability except `agent.availability=STOPPED` | `agent.availability=OFFLINE` | Eligible worker/runtime loss; durable identity/tasks remain and affected active tasks enter recovery. A client-only disconnect changes presentation connectivity only. |
| Any operational availability except `agent.availability=OFFLINE` | `agent.availability=STOPPED` | Explicit authorized runtime stop; no new task is claimed, active work follows stop/pause reconciliation, and restart enters `agent.availability=RECOVERING`. |

Every agent transition inherits the mutation fields and stale/duplicate/recovery rules in §§3.3 and 4.4. Agent pause stops new claims and applies the declared pause policy to its active task; disable stops new claims and requires an explicit pause-or-cancel choice for active work; retirement is terminal for identity operation but never deletes history.

### 5.3 Bounded-autonomy limits

Execution authority ends at the current user-admitted task contract and plan. The product MUST NOT self-create or self-select a new task, delegate to another visible agent, recursively turn an observation into authorized work, expand paths/capabilities/network/credentials/budgets/effects, weaken predicates, or exceed declared time, cost, output, tool-call, and retry ceilings. An authenticated task amendment may change admitted authority; a separate exact approval is still required for any consequential action. Ceiling exhaustion launches no new productive work and yields the narrowest truthful wait, block, or noncomplete result, except for a separately preauthorized bounded cancellation/readback/evidence/safety reserve.

## 6. Pause, stop, redirect, and resume

### 6.1 Operation/effect lifecycle

Every material operation has a stable identity and separate `operation.status`/`operation.outcome`:

```text
operation.status=PROPOSED → operation.status=WAITING_FOR_APPROVAL (when required)
→ operation.status=AUTHORIZED
→ operation.status=DISPATCHED → operation.status=RUNNING → operation.status=RECONCILING (when needed)
→ terminal operation.outcome
```

Terminal outcomes are `operation.outcome=KNOWN_NOT_STARTED`, `operation.outcome=KNOWN_SUCCEEDED`, `operation.outcome=KNOWN_FAILED`, `operation.outcome=CANCELLED`, or `operation.outcome=OUTCOME_UNCERTAIN`. They are not `attempt.disposition` values. Approval authorizes an operation attempt but does not establish success. A consequential `operation.outcome=KNOWN_SUCCEEDED` requires the declared authoritative readback when observable.

| Qualified source operation state | Qualified destination operation state | Actor, precondition, persisted result, and recovery |
|---|---|---|
| `operation.status=PROPOSED` | `operation.status=AUTHORIZED` | Controller validates exact current authority; no separate approval is required; persist normalized operation and bounds. |
| `operation.status=PROPOSED` | `operation.status=WAITING_FOR_APPROVAL` | Controller persists exact inspectable approval request and zero-dispatch fact; task wait reason references it without erasing suspended phase. |
| `operation.status=WAITING_FOR_APPROVAL` | `operation.status=AUTHORIZED` | Authenticated current approval exactly matches; authorization is independently revalidated. |
| `operation.status=PROPOSED`, `operation.status=WAITING_FOR_APPROVAL`, or `operation.status=AUTHORIZED` | terminal `operation.outcome=KNOWN_NOT_STARTED` | Denial, expiry, revocation, stop, redirect, invalidation, or cancellation occurs before dispatch; persist reason and zero-dispatch evidence. |
| `operation.status=AUTHORIZED` | `operation.status=DISPATCHED` | Immediately revalidate task/policy/tool/approval/target/current ownership; persist dispatch intent before or with the declared recoverable boundary. |
| `operation.status=DISPATCHED` | `operation.status=RUNNING`, `operation.status=RECONCILING`, or terminal `operation.outcome` | Correlated provider/tool evidence establishes start, known non-start, or uncertainty; response loss never implies non-effect. |
| `operation.status=RUNNING` | terminal `operation.outcome=KNOWN_SUCCEEDED`, `operation.outcome=KNOWN_FAILED`, or `operation.outcome=CANCELLED` | Declared terminal oracle validates; persist bounded result/effect/receipt and required readback. |
| `operation.status=RUNNING` or `operation.status=DISPATCHED` | `operation.status=RECONCILING` | Cancellation, timeout, crash, invalid/mismatched result, lost response, or uncertain effect requires receipt/idempotency/readback analysis; no blind replay. |
| `operation.status=RECONCILING` | any terminal `operation.outcome` | Authoritative evidence establishes the narrowest truthful outcome; unresolved consequential uncertainty remains `operation.outcome=OUTCOME_UNCERTAIN` and blocks replay/completion. |

Approval denial/expiry/revocation and cancellation before dispatch are idempotent zero-effect terminal results. Cancellation after dispatch is a request, not an outcome, until reconciliation. Duplicate or stale transition attempts are rejected and recorded under §3.3. Recovery never converts an operation outcome into a task disposition without evaluating the task predicates.

### 6.2 Pause

The product MUST persist `PAUSE_REQUESTED` before acknowledging acceptance, set `task.control=PAUSING`, stop launching productive/task-advancing operations ordered after acceptance, and classify every in-flight operation. Cooperative cancellation/checkpointing occurs first. `UNTRUSTED_CODE_EXECUTION` and its descendants can never declare themselves non-interruptible; the capability is inadmissible unless bounded termination/fencing/accounting is available. Only a trusted product-internal effect-crossing operation may be temporarily indivisible, and it has a declared maximum settle bound. `task.control=PAUSING` remains while productive work is running. `task.control=PAUSED` becomes effective only when every such operation is terminal, safely checkpointed/cancelled, or has `operation.outcome=OUTCOME_UNCERTAIN`; separately authorized bounded safety/cancellation/readback/evidence/recovery operations may coexist.

The user sees requested/effective time, preserved work, current operation state, and every effect after the request. Pause promises neither rollback nor immediate process termination. `task.control=PAUSED` may coexist with `task.reconciliation=RECOVERING` or active `task.blocker_refs`, but not with `task.reconciliation=RETRYING` or productive `operation.status=RUNNING`.

### 6.3 Stop or cancel

The product MUST implement this bounded stop sequence without selecting an operating-system or process architecture:

1. persist `STOP_REQUESTED`, set `task.control=STOPPING`, and record the accepted order plus a prospectively declared finite stop-reconciliation deadline;
2. launch no productive/task-advancing operation under superseded authority; only separately bounded cancellation, readback, evidence, exact task-owned cleanup, and safety work may start;
3. request cooperative tool/process cancellation and descendant termination, retaining every response and already-completed effect;
4. reconcile dispatched effects during the finite window using idempotency evidence, receipts, and authoritative readback;
5. accept a user `FORCE_STOP_REQUESTED` after stop acceptance and automatically escalate no later than the deadline; force-terminate when safe/available and otherwise fence/revoke further product authority so the operation cannot continue as authorized work;
6. at the deadline, classify every unresolved operation `operation.outcome=OUTCOME_UNCERTAIN` instead of extending `task.control=STOPPING` indefinitely; and
7. after descendants are terminated or fenced and every material operation is terminal or explicitly uncertain, clear active task components and set `attempt.disposition=CANCELLED`, carrying unresolved target risk as a blocker on any successor that could duplicate or conflict with it.

`task.control=STOPPING` may coexist with `task.reconciliation=RECOVERING`; it cannot coexist with `task.reconciliation=RETRYING`. The stop record preserves partial outputs, workspace/effect readback, cleanup gaps, every verification run/revision, and current `verification.status`. A material stop mutation makes the changed revision `verification.status=UNVERIFIED` but never erases a prior run bound to an older revision. Killing/fencing a process is not rollback, predicate proof, or `attempt.disposition=COMPLETED`. A capability that executes untrusted repository code is nonconformant if it can permanently resist bounded termination/fencing/accounting.

### 6.4 Redirect

A redirect is ordered against the current task version. The product quiesces incompatible work and records the old and new request, plan, predicate, and authority versions. An in-scope clarification may revise the current task; a scope, path, capability, credential, spend, network, external-effect, or outcome expansion first requires an authenticated versioned task-authorization amendment. If the resulting exact action is consequential, it then requires a separate approval receipt. One-shot action approval alone cannot add a capability/root/provider or rewrite the task contract. A materially different outcome creates a linked `SUPERSEDED` task/attempt rather than silently mutating history.

Redirect invalidates any approval, operation, artifact, check, or verification whose bound material changed. Prior valid work and evidence remain preserved. A redirect cannot weaken a failed predicate after the fact without recording a new contract and leaving the prior attempt noncomplete.

### 6.5 Resume

Resume is permitted only from resumable `task.control=PAUSED`, `task.wait_reasons`, or active `task.blocker_refs` by an authorized actor or correlated response/event. A `task.wait_reasons=WAITING_FOR_EXTERNAL_EVENT` response must be authenticated or authoritatively read back, correlate to the current wait identity/version, reject stale/duplicate events, honor the recorded timeout, and return only to the suspended legal phase after the checks below. Before new work, the product revalidates:

- task, request, plan, predicate, policy, schema, and capability versions;
- current ownership version or equivalent stale-owner proof and absence of stale writers;
- repository identity, base/head, branch/ref, workspace, dirty state, and concurrent user changes;
- credentials, network/data policy, budgets, limits, and tool availability;
- approval validity, expiry, use count, revocation, and exact action binding;
- every incomplete or uncertain operation by receipt and authoritative readback.

An otherwise valid unconsumed approval binds to principal/task/attempt/operation/action/target/base/policy/use/expiry, not a worker instance. It survives recovery-installed successor ownership only when ownership installation and the exact tuple are recorded/revalidated and no dispatch ambiguity exists; otherwise the receipt is invalidated/reconciled with a reason.

Terminal `attempt.disposition=CANCELLED`, `attempt.disposition=FAILED`, `attempt.disposition=SUPERSEDED`, or `attempt.disposition=COMPLETED` requires an explicit linked successor/reopen attempt. Stop has precedence over stale resume or approval. Concurrent controls use deterministic causal/version ordering; losing and duplicate commands remain visible.

## 7. Restart and recovery

Client disappearance does not pause, stop, or complete a task and does not make a healthy execution owner recover. Reconnect reconstructs only the presentation view from authoritative state rather than from client transcript memory.

After supported orchestrator or worker loss, affected nonterminal tasks set `task.reconciliation=RECOVERING` before execution while preserving any `task.control`, waits, or blockers. A client restart joins this recovery only when it also caused owner/runtime loss. Recovery MUST validate:

1. record schema, integrity, causal order, and latest acknowledged versions;
2. task, plan, predicates, policy, approvals, limits, budgets, and current ownership version/equivalent stale-owner proof;
3. repository/workspace identity, base/head/dirty state, concurrent changes, and artifacts;
4. checkpoints or other recovery evidence without assuming a specific mechanism;
5. each interrupted operation's identity, dispatch state, idempotency/reconciliation rule, receipt, and readback;
6. provider, tool, environment, credential, network, and data-policy availability without hidden fallback.

Interrupted operations receive `operation.outcome=KNOWN_NOT_STARTED`, `operation.outcome=KNOWN_SUCCEEDED`, `operation.outcome=KNOWN_FAILED`, `operation.outcome=CANCELLED`, or `operation.outcome=OUTCOME_UNCERTAIN`. Consequential uncertainty blocks blind replay and `attempt.disposition=COMPLETED` until authoritative reconciliation or explicit noncomplete escalation. A new owner may continue only after stale-owner state writes/effects are prevented.

Tasks with `task.control=PAUSED`/`task.control=STOPPING`, current waits, or terminal `attempt.disposition=CANCELLED`/`attempt.disposition=SUPERSEDED` do not auto-resume. Recovery during `task.control=STOPPING` continues bounded stop reconciliation before anything else; recovery during `task.control=PAUSING` preserves the pause. Corrupt, malformed, incompatible, or incomplete authority/evidence is preserved and isolated from use; any salvage is itemized and independently checked. Unsafe recovery adds a task blocker or ends with `attempt.disposition=FAILED`, never silent reset.

Required fault evidence injects interruption at every declared acknowledgement and material-effect boundary and proves: zero lost acknowledged mutations, zero accepted stale writes, zero unintended duplicate consequential effects, no authority amplification, and one explicit outcome for every operation. Device or media loss beyond a declared v0.1 persistence boundary remains an explicit unknown/non-guarantee until E2 and E5 define and test it.

## 8. Repository, workspace, and capability contract

### 8.1 Repository and workspace invariants

The repository-condition vocabulary is normative:

- `SUPPORTED`: required v0.1 behavior with no condition-specific restriction beyond the general contract;
- `SUPPORTED_WITH_CONSTRAINTS`: required v0.1 behavior only when every listed constraint is admitted and evidenced;
- `REJECTED_V0_1`: typed admission rejection for task work under that condition, with zero mutation/reproduction effect; and
- `UNKNOWN_E2_E3`: not admitted for mutation or potentially mutating reproduction until a prospective requirements decision and later authorized E2/E3 evidence resolves it. E2 cannot silently promote it.

These are product dispositions, not claims that implementation or tests exist. Multiple observed conditions compose using the most restrictive disposition and the union of all constraints. Unknown/unrecognized condition identity fails closed.

| Repository condition | v0.1 disposition | Required behavior/constraint |
|---|---|---|
| Clean working tree | `SUPPORTED` | Capture exact base/head/ref and proceed only under the ordinary workspace contract. |
| Dirty tracked files | `SUPPORTED_WITH_CONSTRAINTS` | Record each pre-existing change as user-owned; isolate task work; exact overlap needs authenticated user resolution; preserve bytes/refs. |
| Untracked files | `SUPPORTED_WITH_CONSTRAINTS` | Record identity/class and explicit include/exclude/carry rule; default is user-owned and not silently copied, deleted, staged, or attributed. |
| Ignored files/directories | `SUPPORTED_WITH_CONSTRAINTS` | Workspace profile declares carried/excluded/unavailable classes; default is no implicit content availability, execution, or reinstall. Protected-secret policy overrides any carriage. |
| Detached `HEAD` | `SUPPORTED_WITH_CONSTRAINTS` | Anchor exact commit. Read/diagnosis/patch work may proceed; any branch/commit review form requires a separately admitted task-owned ref and no existing-ref mutation. |
| No configured remote | `SUPPORTED` for the local core | Local review outcome remains available; remote predicates/actions are unavailable and cannot be simulated or silently configured. |
| Shallow clone | `SUPPORTED_WITH_CONSTRAINTS` | Record available/missing history boundary; do not auto-fetch; history-dependent predicates wait/block or remain noncomplete. |
| Submodules present | `SUPPORTED_WITH_CONSTRAINTS` | Record populated/unpopulated/dirty state; each submodule root is excluded by default or separately admitted as its own repository boundary; no automatic init/update/network. |
| Git LFS present | `SUPPORTED_WITH_CONSTRAINTS` | Record pointer versus hydrated-object state; no automatic filter execution/fetch/network; missing required content waits/blocks. |
| Checkout is a linked worktree | `SUPPORTED_WITH_CONSTRAINTS` | Record common repository directory, worktree identities, shared refs/config, and user ownership; prove non-interference and deny destructive shared-ref/worktree actions. |
| Nested repository | `SUPPORTED_WITH_CONSTRAINTS` | Record each repository identity/root and separately admit any crossing; outer-root authority does not enter or mutate the nested repository implicitly. |
| Monorepo | `SUPPORTED_WITH_CONSTRAINTS` | Bind exact repository root, task subpath, applicable instruction hierarchy, and check/read/execute scope; subpath scope does not imply repo-wide execution. |
| Merge, rebase, cherry-pick, revert, apply/am, or bisect in progress | `REJECTED_V0_1` | Reject task work before mutation or potentially mutating reproduction with the exact operation state; no automatic abort/continue/stash/reset. A separately admitted read-only diagnosis may report it without changing state. |
| Bare repository | `REJECTED_V0_1` | Core workspace/change tasks require a working tree; preflight records and rejects with zero task mutation. |
| Pre-existing generated/build-output files | `SUPPORTED_WITH_CONSTRAINTS` | Treat as user-owned regardless of ignored status; profile declares include/exclude/carry; cleanup cannot delete them unless exact task ownership is proven. |
| Sparse/partial checkout or another material repository extension not otherwise classified | `UNKNOWN_E2_E3` | Record the condition and deny mutation/reproduction that depends on omitted/ambiguous state until prospectively resolved; no implicit expansion/fetch. |

Before task work, the product MUST record repository identity, observed base revision/tree, branch/ref, head, every applicable matrix row, tracked/untracked/ignored/generated state, relevant shared-worktree/nested/submodule/LFS facts, applicable instruction/context sources, and allowed/excluded paths. Pre-existing material remains user-owned.

The lifecycle is: bounded read-only admission and base capture; establish and bind the isolated task workspace; run any potentially mutating reproduction/diagnosis there; then implement. Read-only preflight may precede isolation. Any mutation or `UNTRUSTED_CODE_EXECUTION`—including the first failing oracle after workspace establishment—requires the bound isolated workspace first unless an explicit product rule and authenticated task authorization permit a named unisolated operation. Repository content cannot supply that rule or authorization.

Task work MUST occur in an identified isolated workspace or an E2-selected equivalent that objectively proves non-interference. The product MUST:

- prevent task work from overwriting, deleting, staging, committing, or silently including unrelated user changes;
- reauthorize the effective target at operation time and again during cleanup;
- detect concurrent user or task changes and fail or reconcile visibly rather than silently merge/overwrite;
- reread final repository state, changed-file inventory, base/head/dirty facts, and review package after the last mutation;
- bind every artifact, command, reproduction/test run, diff, and verification verdict to the exact workspace/revision and prove that no potentially mutating oracle ran in the unisolated user checkout;
- treat local-process, operating-system-user, worktree, container, or machine boundaries as implementation claims that require later evidence, not automatic security proof.

### 8.2 Filesystem operations

Read, write, create, rename, link, and delete permissions are distinct. Effective targets MUST be normalized and authorized at use time against declared roots, including:

- relative and absolute paths, `..`, path encoding, case and Unicode aliases;
- symbolic links, hard links, link swaps and other time-of-check/time-of-use changes;
- mount points and targets, archive entries, nested archives, size/resource bombs;
- device files, FIFOs, sockets, and other special files;
- cleanup after workspace identity or path topology changes.

Unknown target identity or an unverifiable boundary denies the operation. Creating a link does not confer later authority. Tests MUST use synthetic canaries and prove zero access or mutation outside authorized roots and byte-identical preservation of unrelated material.

### 8.3 Terminal and descendant execution

Each terminal operation MUST bind the exact task/attempt/workspace, working directory, command/action representation, environment and secret policy, resource/time/output/tool/network ceilings, cancellation class, process-tree ownership, expected effect class, and evidence rule before dispatch.

Shells, scripts, package managers, build tools, test runners, Git hooks/helpers, generated programs, children, detached processes, and local services inherit the same or narrower authority. Command text or regex analysis is never the primary permission boundary. Background/detached work is unsupported unless it becomes its own durably tracked operation. Cancellation/terminal status MUST kill or account for every descendant and leave no unexplained orphan.

Results MUST distinguish successful exit, nonzero exit, signal/termination, timeout, cancellation, output truncation, resource limit, transport loss, and uncertain effect. Bounded stdout/stderr is untrusted data and cannot approve an action or prove a predicate without the declared oracle and provenance.

### 8.4 Git operations

Git classification has independent columns: `primary_effect_class`, `v0_1_disposition`, and `approval_rule`. Approval-rule values are `NO_SEPARATE_APPROVAL`, `POLICY_CONDITIONAL_APPROVAL`, `APPROVAL_REQUIRED`, and `NOT_APPLICABLE_PROHIBITED`. A task/network/credential grant is still required where stated even when no separate human approval applies. `APPROVAL_REQUIRED` is a gate, never an effect class or a way to enable `PROHIBITED_V0_1`. `OPTIONAL_WITH_CONSTRAINTS` means the core preview need not implement the capability; when absent it returns `UNSUPPORTED_CAPABILITY`, and when present it obeys every listed requirement.

| Git or repository action | Primary effect class | v0.1 disposition | Approval rule | Required grant and evidence |
|---|---|---|---|---|
| Status, safe local config and remote-configuration inspection without remote contact, history/ref/object inspection | `READ_ONLY` | `SUPPORTED_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Exact repository/read scope; executable helpers/filters disabled or separately admitted; no network/credential. |
| Diff generation | `READ_ONLY` | `SUPPORTED_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Exact base/target/path; no external diff/text-conversion helper unless separately admitted; result bound to revision. |
| Local edit | `LOCAL_REVERSIBLE` | `SUPPORTED` in admitted isolated paths | `NO_SEPARATE_APPROVAL` | Task authorization; before/after reread; no user-material overlap. |
| Stage | `LOCAL_REVERSIBLE` | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Task-owned isolated index only; exact changed-file readback; no pre-existing user change. |
| Unstage without working-tree mutation | `LOCAL_REVERSIBLE` | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Task-owned isolated index and exact before/after readback; any user/shared-index target escalates to prohibited destructive action. |
| Local branch creation | `LOCAL_REVERSIBLE` | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Exact task-owned name/base, collision check, no existing-ref movement, task authorization. |
| New bounded local commit | `LOCAL_REVERSIBLE` | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Task contract explicitly allows; exact tree/parent/message/identity and post-commit readback; signing helper separately authorized. |
| Local remote-configuration mutation without remote contact | `LOCAL_REVERSIBLE` configuration mutation | `OPTIONAL_WITH_CONSTRAINTS` | `POLICY_CONDITIONAL_APPROVAL` | Exact task-owned isolated config/name/URL, no credential value, no shared/global config, before/after readback; task and policy must explicitly admit it. |
| Remote contact/read without local ref update, such as `ls-remote` | `EXTERNAL_READ_EFFECT` | `OPTIONAL_WITH_CONSTRAINTS` | `POLICY_CONDITIONAL_APPROVAL` | Explicit network/source/data/credential grant; record effective endpoint, helpers, receipt/result, cost, and zero local ref update. |
| Fetch | `EXTERNAL_READ_EFFECT` plus local ref mutation | `OPTIONAL_WITH_CONSTRAINTS` | `POLICY_CONDITIONAL_APPROVAL` | Explicit network/destination/data/credential grant; record ref namespace before/after and helper/filter behavior. |
| Clone into a new task-owned destination | `EXTERNAL_READ_EFFECT` plus local creation | `OPTIONAL_WITH_CONSTRAINTS` | `POLICY_CONDITIONAL_APPROVAL` | Explicit network/source/credential/destination/size grant; destination is empty/task-owned and becomes separately admitted; no implicit code/filter execution. |
| Submodule or Git LFS fetch/update/hydration | `EXTERNAL_READ_EFFECT` plus local mutation | `OPTIONAL_WITH_CONSTRAINTS` | `POLICY_CONDITIONAL_APPROVAL` | Separately admitted repository/LFS object boundary, network/data/credential grant, exact target/readback; no implicit helpers or execution. |
| Pull | `EXTERNAL_READ_EFFECT` plus local integration mutation | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Composite fetch+merge/rebase is denied; approval cannot enable it. |
| Stash | `LOCAL_DESTRUCTIVE` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied for user and task work; no implicit workaround for dirty state. |
| Checkout/switch/restore that may discard or replace working-tree/index material | `LOCAL_DESTRUCTIVE` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied; read-only object inspection and explicit bounded edits use their own rows. |
| Reset, clean, reflog expiry/prune, or equivalent history/index/worktree discard | `LOCAL_DESTRUCTIVE` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied, including inside the allowed root; approval cannot enable it. |
| Worktree create | `LOCAL_REVERSIBLE` | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Exact task-owned path/ref/common-dir topology, collision and user-material checks, task authorization, creation readback. |
| Worktree remove/prune of the exact task-owned isolated workspace | `LOCAL_DESTRUCTIVE` cleanup | `OPTIONAL_WITH_CONSTRAINTS` | `NO_SEPARATE_APPROVAL` | Prospectively admitted task-owned cleanup; terminal operations, no user material, no hold, exact identity/topology check and post-removal readback. |
| Worktree remove/prune of a user/shared/unknown worktree | `LOCAL_DESTRUCTIVE` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied. |
| Local branch deletion, including task branch | `LOCAL_DESTRUCTIVE` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied in v0.1; preservation is preferred over unproven cleanup. |
| Push without force | `REMOTE_EFFECT` | `OPTIONAL_WITH_CONSTRAINTS` | `APPROVAL_REQUIRED` | Exact task/remote/ref/object, one-shot approval, execution receipt, and fresh remote readback. |
| Force push/update | `REMOTE_EFFECT` plus destructive history change | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied; approval cannot enable it. |
| Pull-request create or update | `REMOTE_EFFECT` | `OPTIONAL_WITH_CONSTRAINTS` | `APPROVAL_REQUIRED` | Exact remote/base/head/title/body/content, one-shot approval, receipt, and fresh external record readback. |
| Local draft-PR package | `LOCAL_REVERSIBLE` | `SUPPORTED_WITH_CONSTRAINTS` as one selectable review form | `NO_SEPARATE_APPROVAL` | Task authorization; minimum package below; explicit `NOT_SUBMITTED`; zero remote effect. |
| Local merge, rebase, or cherry-pick | `LOCAL_DESTRUCTIVE` integration/history change | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied. |
| Remote PR merge | `REMOTE_EFFECT` plus difficult-to-recover change | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied; approval cannot enable it. |
| Remote branch deletion | `REMOTE_EFFECT` plus destructive deletion | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied; approval cannot enable it. |
| Local tag creation | `LOCAL_REVERSIBLE` shared-ref mutation | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied, including signed tags. |
| Local tag deletion | `LOCAL_DESTRUCTIVE` shared-ref deletion | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied. |
| Remote tag creation or deletion | `REMOTE_EFFECT` | `PROHIBITED_V0_1` | `NOT_APPLICABLE_PROHIBITED` | Denied; deletion remains destructive and approval cannot enable either. |

Target/ownership escalation is deterministic: an otherwise reversible action becomes `LOCAL_DESTRUCTIVE` when it can overwrite/remove user material, a shared ref/index/worktree, or ambiguous ownership; ambiguity denies the action. Local task-workspace permission never implies remote, credential, helper, filter, signer, submodule, LFS, or cleanup authority.

A draft-PR package is a local artifact, not a pull request. It MUST contain:

- package/schema identity and version plus an explicit `NOT_SUBMITTED` marker;
- repository identity, exact base ref/revision, and proposed head/ref/commit list or immutable patch/diff reference;
- changed-file inventory, title, summary/body, and source request/issue reference or justified `NOT_APPLICABLE`;
- applicable contribution checklist with each instruction source identity/version/trust class;
- checks/tests with exact results, including skips, failures, retries, and `FLAKY` outcomes;
- known limitations, unmet predicates, unresolved effects, and no-merge/no-release caveats;
- evidence-bundle reference and current verification status/run reference; and
- external capability and human-approval status showing that no PR was created.

Repository/local/global Git configuration, aliases, hooks, credential helpers, text-conversion/external-diff drivers, clean/smudge/LFS filters, submodules, signing helpers, filesystem monitors, and SSH/transport commands are untrusted executable surfaces. A Git permission does not implicitly authorize them, network, or credentials. Required review must show no unapproved ref movement, helper execution, secret access, user-material loss, or remote effect.

### 8.5 Tests, builds, dependencies, and downloads

Tests, linters, builds, generators, dependency resolvers, and package lifecycle scripts are untrusted code execution, not read-only inspection. They run only within the declared filesystem, process, resource, output, network, data, credential, and time bounds.

Retrieval does not authorize installation or execution. Downloads, archives, packages, binaries, caches, and generated artifacts require declared provenance, version/source, size/type/resource limits, target containment, and separate applicable network/execution grants. Unsupported safe execution returns typed failure `UNSUPPORTED_CAPABILITY`; the task separately waits, blocks, partially closes, or fails under its predicates rather than simulating success.

## 9. Tool, permission, approval, secret, and external-effect boundaries

### 9.1 Trusted capability contract

Every executable capability MUST have trusted, versioned metadata outside untrusted model/tool prose:

- stable capability and provider/server identities;
- runtime input and output schemas and compatible versions;
- action/effect class, reversibility, idempotency/reconciliation, and cancellation semantics;
- normalized-target rules and filesystem, process, network, data, credential, cost, and resource needs;
- hard limits, approval requirements, receipt/readback rules, and safe error contract.

Both requests and results are runtime-validated. A malformed, oversized, duplicated, unknown, stale, incompatible, adversarial, or ambiguously normalized request/contract/target, or a schema change after approval, MUST fail before dispatch. An invalid, mismatched, or oversized result MUST fail before consumption or any downstream operation; because the dispatched capability may already have acted, its effect becomes `operation.outcome=OUTCOME_UNCERTAIN` until receipt/readback reconciliation. Best-effort repair may not widen authority, change targets/effect class, fabricate semantics, conceal provider/tool loss, or claim that invalid output proves zero effect.

Dynamically discovered tools or servers are non-executable until admitted by trusted policy. Tool names, descriptions, schemas supplied only by an untrusted server, model classification, prompt content, and caller Booleans do not grant permission. E2 chooses the capability topology.

### 9.2 Action/effect classes

Equivalent E2 names are allowed only if these independent dimensions remain testable. They MUST NOT be collapsed into one permissive label.

| Primary effect class | Boundary |
|---|---|
| `READ_ONLY` | Read admitted local data without mutation, code/helper execution, secret use, or network. |
| `LOCAL_REVERSIBLE` | Bounded local mutation in task-owned isolated state whose exact prior state remains recoverable and whose target is not user/shared material. |
| `LOCAL_DESTRUCTIVE` | Local deletion, discard, shared-ref/index/worktree mutation, or another action difficult to recover without user-material risk. |
| `EXTERNAL_READ_EFFECT` | Network/API/model/Git read or retrieval: data egress, credentials, cost, provenance, and any local cache/ref mutation remain accountable effects. |
| `REMOTE_EFFECT` | Remote Git, PR/issue, deploy, publish, release, message, purchase, or other external state mutation. |

Independent execution/risk overlays include `UNTRUSTED_CODE_EXECUTION`, `PRIVILEGED`, and `GOVERNANCE_PROHIBITED`. Independent v0.1 dispositions include `SUPPORTED`, `SUPPORTED_WITH_CONSTRAINTS`, `OPTIONAL_WITH_CONSTRAINTS`, `PROHIBITED_V0_1`, and `UNKNOWN_E2_E3`. Independent approval rules are `NO_SEPARATE_APPROVAL`, `POLICY_CONDITIONAL_APPROVAL`, `APPROVAL_REQUIRED`, and `NOT_APPLICABLE_PROHIBITED`. Target ownership or uncertainty may escalate the primary class/disposition but can never downgrade it based on model/tool prose.

Task admission may authorize bounded local reads, isolated reversible mutation, checks, and review-package generation. Network, dependency acquisition/execution, named credential use, and other added-risk actions require explicit task grants and any policy-required approval. A supported optional remote effect, privileged action, or spend within admitted authority at/above a declared approval threshold requires one-shot human approval. `LOCAL_DESTRUCTIVE`, `PROHIBITED_V0_1`, and `GOVERNANCE_PROHIBITED` are not enabled by ordinary approval; the latter requires a separately authorized governance task/decision. None of these optional effects is required for the v0.1 core local-review outcome.

### 9.3 Network and provider egress

Network is deny-by-default for agent tools and every descendant process. A grant binds protocol, normalized destination/port and material path/method, purpose, data class, credential identity/scope, limits, expiry, task, and operation. Loopback, private, link-local, metadata, local socket, proxy, and redirect targets are not implicitly trusted.

Every connection and redirect MUST re-resolve and reauthorize its effective target. DNS rebinding, redirect substitution, proxy bypass, TLS/authentication downgrade, and cross-target credential forwarding fail closed. Repository content may leave the workspace only under an approved data classification and provider/account/region/retention/training policy. A read-only web or model request can disclose data and incur cost and therefore remains an accountable external operation.

Model routing uses two independent required fields:

| `route_eligibility` | Meaning and allowed use |
|---|---|
| `PRODUCTION_OR_NORMAL_ELIGIBLE` | Configuration has current independently verified qualification evidence and governing authorization for normal/default use. E1 assigns none; only a later gate may establish it. |
| `EVALUATION_ONLY` | Candidate may run only for a separately authorized E3/evaluation purpose under its exact task, data, credential, cost, and provider policy. The run produces candidate evidence and never promotes itself. |
| `USER_CONFIGURED_UNVERIFIED` | User explicitly selected/configured this experimental route for the current task. It is visibly unverified, never default/fallback/release evidence, never silently promoted, and obeys every other bound. |
| `DISALLOWED` | Configuration conflicts with provider/account/region/retention/training/legal/data/security/capability/cost policy or lacks an enforceable required ceiling. It never dispatches for any purpose. |

| `route_purpose` | Permitted `route_eligibility` | Required rule |
|---|---|---|
| `NORMAL_PRODUCT_TASK` | `PRODUCTION_OR_NORMAL_ELIGIBLE` only | Default/recommended/ordinary task routing; current eligibility evidence and authorization revalidate before dispatch. |
| `E3_EVALUATION` | `EVALUATION_ONLY` and eligible comparison controls | Requires a separately registered/authorized E3 evaluation task and all budget/data/credential/provider approvals. Results remain evaluation evidence until an independent governance decision changes class. |
| `USER_EXPERIMENTAL` | `USER_CONFIGURED_UNVERIFIED` only | Requires an explicit authenticated user selection for the exact task/configuration plus visible nonqualification warning; never autonomous/default/fallback routing. |

Every model operation/evidence record binds requested/resolved provider/model/configuration, both fields, class authority/evidence version, route reason/policy, applicable E3 or user authorization reference, fallback parent, task/data/capability/network/credential/cost bounds, timing/usage/cost when exposed, and explicit unknowns. A purpose/class mismatch is denied before any repository byte is transmitted or cost incurred. Merely unbenchmarked is not synonymous with `DISALLOWED`; only a matching authorized evaluation/user-experimental purpose can route it. This routing model authorizes no E3 run, paid call, model role, or qualification decision.

### 9.4 Approval request, receipt, and consumption

Approval is a durable authenticated policy decision, never inferred from conversational wording, repository text, prompt instructions, tool output, UI availability, regex, model review, tests, a tool name, or `confirmed: true`.

The human-visible request and executable normalized action MUST derive from the same authoritative representation. Untrusted target/action/content is rendered inert, escaped and visually separated from trusted actor/policy/risk fields; bidirectional/control characters, markup, terminal escapes, leading options, and truncation cannot conceal the effective target or effect. Every material input must be fully inspectable before decision, either inline or through an immutable content reference whose full bytes are accessible from the approval surface and whose digest binds those bytes. A digest alone cannot authorize. The representation binds:

- actor/user, task, attempt, operation, capability/schema version, and effect class;
- normalized action and every material argument;
- exact target/resource/ref and before-state preconditions;
- credential identity/scope without its value, network/data/budget scope, and policy/version;
- issue/expiry time, one-shot or explicit count limit, revocation rule, and decision/outcome.

Mutation, substitution, policy/capability/schema/base-state change, expiry, revocation, replay, duplicate consumption, stale-worker consumption, widened batch, or possible prior dispatch invalidates or reconciles approval. One-shot is the default. Approval binds to principal/task/attempt/operation/normalized action/capability/schema/target/base/policy/time/use, not the ephemeral worker instance. Ownership turnover alone does not invalidate an otherwise exact unexpired/unconsumed receipt: a recovery-installed successor may consume it once only after recording the successor identity/ownership version, revalidating the complete binding, and proving no dispatch/effect ambiguity. A narrower user decision creates and re-presents a new action; it does not mutate or consume the original. A standing grant, if supported, exposes exact action/resource/count/time/budget ceilings and remaining/revocable scope and cannot cover materially different future actions.

Refusal, timeout, revocation, pause, redirect, cancellation, stale ownership, and task-scope change are persisted and reconciled before dispatch. If already dispatched, the operation is cancelled where safe and read back. Approval permits an attempt; execution receipt plus authoritative terminal readback establishes the known effect. The verifier cannot reuse author approval or credentials for a new consequential effect.

### 9.5 Consequential external actions

The Git matrix in §8.4 is controlling: supported optional non-force push and PR create/update require exact one-shot approval/readback; force push, pull, local/remote merge, remote branch deletion, tag mutation, and the listed destructive local actions are `PROHIBITED_V0_1`, and approval cannot enable them. Other separately admitted/supported external effects—such as issue create/edit/comment/close, deploy/publish/release, message/contact, purchase or paid use at/above a declared threshold, privileged credential use, or another difficult-to-recover external state change—require exact human approval and readback under their own future capability contract. Spend beyond admitted budget first requires a task/budget amendment and then applicable approval. None is required for the core local-review workflow.

Every consequential operation MUST have stable identity, declared replay/idempotency or reconciliation semantics, execution receipt, and authoritative readback method. On timeout or response loss, the product reads external state before retry; it never blindly repeats a non-idempotent or uncertain effect. A changed action may require fresh approval. Partial/wrong/unreadable external state records the truthful operation outcome and prevents completion; the attempt disposition, task blocker, and verification status remain separate axes.

Unsupported capabilities report typed failure `UNSUPPORTED_CAPABILITY`, perform no effect, and separately select the truthful task qualifier/disposition. Producing a local draft-PR package cannot be described as opening an external PR.

### 9.6 Secret handling

Raw secrets MUST NOT enter ordinary chat, model context, repository source, task summaries, tool descriptions, approval text, general/inherited environment, general logs or telemetry, shell history/command text, process arguments/listings, screenshots, crash/core data, diffs, fixtures, caches, artifacts, or evidence bundles. Secrets are referenced only by stable identity and scope. An authorized operation may receive/use a raw value only through an E2-selected protected recipient boundary, for the exact capability, endpoint/resource, task/operation, use count, and minimum duration; this is the only test exception, descendants cannot inherit it, and the raw value is never returned to the model, UI, or general tool output.

Protected-location policy is non-exhaustive and covers at minimum:

| Protected location family | Examples/signals that do not by themselves constitute exhaustive detection |
|---|---|
| Repository/runtime secret configuration | `.env*`, repo-local token/secret files, designated private config, local overrides, vault exports/backups. Public templates such as examples require an explicit nonsecret classification rather than a filename assumption. |
| Private/signing and SSH material | Private/signing keys, SSH configuration containing sensitive routes or identities, agent sockets, key stores, and passphrase material. |
| Git credentials | Credential stores/helpers, askpass material, credential-bearing remote URLs, signing credentials, and helper outputs. |
| Package-registry credentials | Registry/auth config such as `.npmrc`, `.pypirc`, `.netrc`, and analogous Maven/Gradle/Cargo/NuGet or package-manager credentials. |
| Cloud/provider/orchestrator credentials | Provider CLI configs, token/session caches, service-account files, kubeconfigs, cloud profiles, and API-token config. |
| Operating-system credential stores | Keychains, credential managers, keyrings, secure-store databases/sockets/APIs, and protected account material. |
| Browser/session material | Browser profiles, cookies, session/local-storage databases, saved passwords, and authentication caches. |
| Shell/process/user-session material | Shell histories/profiles with exported credentials, inherited secret environments, clipboard/session caches, process dumps/listings. |
| Diagnostic/remnant material | Crash/core dumps, diagnostic archives, temp/cache files, swap-like remnants, and logs known or suspected to contain secret bytes. |

Protected-secret classification overrides repository/workspace-root, path, task, Git, terminal, tool, and instruction-file allowance. Being inside an allowed workspace never implies permission to read, copy, execute, display, hash for publication, or send secret content. The override follows aliases/links and applies to descendants, helpers, filters, tools, model/provider transmission, and cleanup.

If a location/content classification is `UNKNOWN` or ambiguous, the product denies content read, egress, use, and model transmission. It may inspect only already-authorized nonrevealing metadata strictly needed to identify the family, then requests protected user resolution or records a blocker. It cannot content-sniff by first exposing the bytes. The classification mechanism is an E2 decision and no exhaustive detection claim is made; any false negative that causes exposure is a hard secret-boundary failure.

Human secret acquisition MUST use a protected path distinct from conversation and repository files. During protected entry, agent/model/tool observation and capture of keystrokes, clipboard, screen/screenshot, accessibility state, terminal stream, and the secret value stop; only a non-secret outcome/receipt returns, followed by full resume revalidation. Unavoidable absence of such a protected boundary adds `WAITING_FOR_USER` to `task.wait_reasons` or creates a task blocker; conversational approval cannot authorize raw reveal.

Revocation or rotation invalidates queued and stale use and cancels/reconciles active use, recording possible exposure when termination cannot be proven. Descendants and unrelated tools do not inherit credentials. If a probable secret is encountered, the product stops propagation, safely quarantines/redacts derived output, records a security blocker without echoing or publishing a low-entropy digest, and directs revocation/rotation where applicable. If bytes may already have reached any provider, tool, process, log, or artifact, it records a safe possible/confirmed exposure with destination class, time/scope, cleanup and rotation actions; it makes no false containment claim and cannot complete until the applicable security predicate is reconciled. Required evidence retains only the safe incident fact, not the raw secret.

Redaction is defense in depth, not authorization. Safe errors/evidence use allowlisted bounded fields. Marker tests cover encoded, split-stream, exception/stack, general/inherited environment, process, screenshot, temp/cache, diff, summary, approval, and evidence surfaces and require zero raw marker occurrences outside the exact authorized recipient boundary.

### 9.7 Retention, legal hold, cleanup, and deletion claims

Every authority, audit, artifact, evidence, workspace, temporary credential, and process class has an explicit retention/cleanup policy and owner. A declared legal hold, when applicable, prevents destructive cleanup and remains visible; if v0.1 does not support holds for a class, that limitation is explicit and no contrary deletion promise is made. Garbage collection or cleanup cannot silently remove material needed for authorization, recovery, reconciliation, review, verification, or security investigation.

A deletion claim MUST bind the exact identity, scope, policy/hold state, known locations/replicas/caches, link-safe cleanup method, result, failures, and authoritative reread. Logical inaccessibility and physical erasure are distinct; unknown physical erasure remains `UNKNOWN`. Retention/deletion adds a historical action/result record and never rewrites the fact that prior authorized activity occurred.

## 10. Structured failure and honest partial-result contract

Every failure MUST be machine-distinguishable, bounded, secret-safe, correlated to task/attempt/operation, and preserve the accountable layer without false precision.

### 10.1 Required failure fields

- stable failure identity and contract/schema version;
- failure class, accountable layer, safe code, and safe user message;
- task, attempt, operation, capability/provider/tool, and causal correlation identities;
- observed state/version, effect certainty, and evidence reference;
- retryability (`RETRYABLE`, `TERMINAL`, `POLICY_DENIED`, or `UNKNOWN`), attempt count/ceiling, and retained cost/time;
- user or operator action, recovery/escalation path, resulting lifecycle condition/disposition, and limitations;
- bounded internal diagnostic reference, never raw secret/private payload.

### 10.2 Required failure classes and accountable layers

At minimum, contracts distinguish:

| Family | Examples that remain distinguishable |
|---|---|
| Admission/precondition | invalid request, unsupported task, missing governing input, repository mismatch, missing dependency. |
| Authority/policy/permission | out-of-scope, policy conflict, unknown capability, untrusted-content escalation, budget gate. |
| Approval | required, denied, expired, revoked, replayed, mutated, stale, already consumed. |
| Workspace/filesystem | dirty-state conflict, path/link/archive/special-file denial, isolation failure, concurrent mutation. |
| Terminal/process/resource | invalid command contract, nonzero exit, timeout, cancellation, output/resource ceiling, orphan/uncertain descendant. |
| Git/test/build/dependency | Git precondition/ref/helper denial, reproduction failure, check failure/skip, unsafe dependency, generated-artifact drift. |
| Network/credential/secret | egress denial, destination/redirect/TLS failure, missing/revoked credential, possible leakage. |
| Provider/model | transport, capacity/rate limit, policy/refusal, unsupported semantics, context limit, cancellation, wrong model/configuration. |
| Tool/environment | unavailable/incompatible tool, malformed input/output, unknown schema, host/platform/dependency failure. |
| Recovery/concurrency | corrupt/incompatible state, stale owner/writer/summary, duplicate operation, unreconciled or uncertain effect. |
| Verification/evidence | predicate or predicate-adequacy failure, verifier crash/timeout, verifier-tool/check-infrastructure failure, missing/stale/cross-task evidence, revision mismatch, independence failure, post-verification mutation, false completion. |
| Clean room/security | unauthorized effect/read, forbidden artifact, private/external code, provenance/license or hard-boundary violation. |
| Unknown layer | accountable layer cannot safely be established; the uncertainty remains explicit and cannot be credited as success. |

Exact error codes and registry representation remain E2 decisions; external reconstructed error names/counts are not imported.

### 10.3 Retry and status rules

Execution retries require a prospectively declared ceiling and safe eligibility for the exact failure/effect class. Each attempt, failure, delay, cost, output, and effect remains visible. Authorization/policy denial, invalid/malicious schema, secret or hard-boundary violation, stale approval, non-idempotent uncertain effect, exhausted budget, and known terminal failure do not auto-retry. `task.reconciliation=RETRYING` cannot coexist with `task.control=PAUSING`, `task.control=PAUSED`, or `task.control=STOPPING`.

Verification reruns are separate from execution retries. A verifier crash/timeout, verifier-tool failure, deterministic-check infrastructure failure, or verifier-side collection failure records `verification.run_status=VERIFICATION_ERROR`, accountable layer, and retryability; aggregate status becomes `verification.status=UNVERIFIED`. Runs are sequential. A same-revision run may be created only after such an error is explicitly retryable, within the prospectively declared verification ceiling, and when no candidate/task-contract/predicate material changed. It is neither `attempt.disposition=FAILED` nor `verification.verdict=PASSED`. If the error is nonretryable or the ceiling is exhausted, `verification.status=UNVERIFIED` remains, the task adds a named wait/blocker or intentionally closes with an honest noncomplete disposition under the existing task rules, and the verifier error alone never implies task failure or pass. A candidate evidence defect receives a substantive verdict instead; `verification.verdict=BLOCKED`, `verification.verdict=INCONCLUSIVE`, or `verification.verdict=CHANGES_REQUIRED` is not an infrastructure-rerun basis. Concrete ceilings/repetition counts belong to E1-002/E3.

`task.wait_reasons` names expected input/approval/event. Active `task.blocker_refs` name unblock predicates/owners. `task.control=PAUSED` is user control. `task.reconciliation=RETRYING` is bounded retry. `attempt.disposition=PARTIALLY_COMPLETED` is intentional terminal useful-output closure with zero completion credit; `attempt.disposition=FAILED` is terminal failure; `attempt.disposition=CANCELLED` records stop/cancel. `verification.status=UNVERIFIED` means no current authoritative independent pass. None may be projected as `attempt.disposition=COMPLETED`.

## 11. Completion predicates and independent verification

### 11.1 Common completion gate

`attempt.disposition=COMPLETED` is a derived result only when this conjunction is true:

```text
PREDICATE_SET_ADEQUATE has predicate.result = PASS with evidence-backed request/class/instruction/scope coverage
AND every applicable required predicate has predicate.result = PASS on the exact reviewed revision
AND current authoritative verification.verdict=PASSED
AND evidence-bundle schema and semantic validation result = PASS
AND repository/artifact/effect state was freshly reread where required
AND every performed consequential effect matches current authority and approval
AND zero material operation.outcome=OUTCOME_UNCERTAIN
AND every success-required effect is authoritatively operation.outcome=KNOWN_SUCCEEDED with required readback
AND every other material effect has a known terminal outcome
    (operation.outcome=KNOWN_NOT_STARTED, operation.outcome=KNOWN_SUCCEEDED,
     operation.outcome=KNOWN_FAILED, or operation.outcome=CANCELLED) consistent with predicates
AND every material operation has a terminal outcome and is accounted consistently with close
AND task.control=NONE and task.reconciliation=NONE
AND no current task.wait_reasons, active task.blocker_refs, or pending approval/question/event remains
AND verification.status=FINISHED with no required later verification.run_status=VERIFICATION_ERROR
AND every accepted pause was explicitly resumed/released
AND every accepted stop resolves the attempt only to attempt.disposition=CANCELLED
AND every redirect is verified against its current revision
AND no unresolved required failure, skipped/failed/stale/FLAKY check, blocker, completion-blocking limitation,
    security violation, secret/provenance violation, or stale/missing evidence remains
```

Executor/model prose, a transcript/activity signal, client closure, plan exhaustion, a diff, one passing or once-retried flaky test, tool success, approval, receipt, manifest, digest, score, or sole-author assertion cannot satisfy this gate alone.

Any author/model/tool `COMPLETED` assertion is evaluated and retained. If the gate rejects it before it becomes authoritative, record `UNSUPPORTED_COMPLETION_ASSERTION`; that is correct defensive behavior and a measured event, not a failed scenario. If a projection or durable `attempt.disposition` actually admits `COMPLETED` while the conjunction is false, record `FALSE_TERMINAL_COMPLETION`; this is the zero-tolerance hard failure that cannot be averaged away. Missing/stale evidence, inadequate predicates, required-check skip/failure/unresolved flakiness, verifier error, revision mismatch, author-only proof, mock-only evidence for a real task, unapproved effect, unknown outcome, or contradictory readback MUST prevent the authoritative terminal transition.

### 11.2 Task-type predicates

All task types inherit the common gate and mandatory predicate `PREDICATE_SET_ADEQUATE`. Before any individual predicate can support completion, the verifier maps every material clause of the original request, applicable task-class minimum, admitted scope/exclusion, applicable `UNTRUSTED_GOVERNING_INPUT`, and security/correctness obligation to an objective predicate or evidence-backed `NOT_APPLICABLE`. Each mapping records source clause/reference, predicate/oracle, coverage evidence, and any gap. An uncovered requested behavior, irrelevant or weak oracle, or omitted class minimum makes adequacy fail and yields `verification.verdict=CHANGES_REQUIRED`; passing the author's listed predicates is insufficient. Deterministic structural/behavioral coverage evidence is preferred over unsupported model judgment.

Task types add the following operational predicates:

| Task type | Required operational predicates |
|---|---|
| `BOUNDED_CODE_CHANGE` | Requested observable behavior exists; allowed files contain intended change; diff is scoped and excludes unrelated work; declared build/lint/type/security/domain/tests pass or unmet results prevent completion; repository is reread; artifacts are inspectable. |
| `DEFECT_REPRODUCTION_AND_FIX` | Reported failure or a predeclared alternative failing oracle demonstrates the defect before the fix; fix is bounded; the same relevant oracle demonstrates before/after regression protection; specified negative and affected checks pass; no unrelated diff. Mere inability/contradiction cannot complete this class and requires redirect/reclassification to diagnosis or another honest noncomplete outcome. |
| `REPOSITORY_DIAGNOSIS_OR_REVIEW` | Exact inputs/scope/revision are enumerated; material claims cite authoritative evidence; fact, inference, proposal, and unknown are separated; commands are reproducible; no unauthorized mutation; limitations and unanswered questions remain explicit. |
| `DOCUMENTATION_OR_REPOSITORY_METADATA_CHANGE` | Artifact exists and opens/parses/renders as declared; required sections/fields/traceability exist; sources and cross-file terminology reconcile; exact config/status behavior validates; no premature governance or release gate changes. |
| `NO_CHANGE_REQUIRED` | Fresh current-state readback satisfies every predicate; zero unintended diff/effect exists; independent verifier confirms the no-op against the exact state. |
| Approved external effect, when a task explicitly supports one | Exact approval matches payload/target/policy; stable receipt exists; fresh authoritative target readback matches expected state; duplicate absence or reconciliation is proven. |

Mixed tasks use the conjunction of all applicable predicates. Optional/not-applicable criteria are prospectively declared with an objective reason. For one check identity, review revision, configuration, and environment, mixed ordered outcomes are `FLAKY`, never `PASS`; one later pass is insufficient once flakiness is known or detected. The check satisfies its predicate only if a prospectively declared repetition rule is met; otherwise it blocks completion and all outcomes report under `MET-004`. E1-002 owns concrete repetition rules/cases and E3 owns observations. Every limitation records affected scope/predicate, evidence, owner, and consequence. An unresolved required, supported-case, or security limitation blocks completion; an explicit out-of-scope/nonblocking preview limitation remains visible. Post-failure scope reduction is a visible redirect/new predicate version and cannot relabel the earlier attempt successful.

### 11.3 Independent verification

The author may run self-checks and propose `READY_FOR_VERIFICATION`; only an eligible independent path may produce `verification.verdict`. Every verification run satisfies this floor where applicable:

- it operates on the exact produced repository/artifact state and immutable review revision, not a recreated state or executor assertion;
- it has a separate accountable verifier identity and execution context, with no shared mutable author working state; the same running model session cannot author and verify one attempt;
- its bounded input-context manifest contains the exact task contract, authority/policy and instruction versions, review revision, diff/artifacts, operations, predicate coverage map, and candidate bundle. Author transcript/reasoning is excluded or supplied only as `UNTRUSTED`, and every conclusion cites durable evidence rather than relying solely on executor self-report;
- it independently reads repository/artifact/effect state and reproduces deterministic checks/readbacks where applicable. Deterministic oracle evidence is authoritative over conflicting LLM judgment for the same predicate; disagreement is recorded rather than averaged;
- verifier outputs are isolated/declared and MUST NOT mutate the review revision/package;
- it has least privilege; author approvals/credentials cannot authorize verifier-created effects;
- verifier identity, exact configuration, `route_purpose`/`route_eligibility`, context manifest, independence basis, reviewed state, timing, and tool/check infrastructure are recorded;
- it evaluates `PREDICATE_SET_ADEQUATE` before individual predicates and records each as `predicate.result=PASS`, `predicate.result=FAIL`, `predicate.result=BLOCKED`, `predicate.result=NOT_APPLICABLE`, or `predicate.result=INCONCLUSIVE` with evidence; and
- it retains disagreements, errors, failures, reruns, and changes-required results.

Same-model/configuration verification MAY be permitted only for policy-defined low-risk tasks and only with the full separation above. It is never the same running session. Stronger process, provider, family, human, or other independence strategies are E3 comparison variables, not universal E1 requirements; provider/model diversity alone neither proves nor is required for independence. E3 later benchmarks strategies and determines eligible role occupants; E1 selects none.

If verification mutates the candidate or observes a material concurrent/post-verification mutation, it stops, preserves the old run/verdict for the old revision, sets the new state to `verification.status=UNVERIFIED`, denies `attempt.disposition=COMPLETED`, and requires a new candidate/reverification. High-risk work cannot be verified by its sole author. Human review/action approval does not substitute for technical verification, and technical verification does not authorize merge, release, or external effect.

## 12. Evidence-bundle contract

### 12.1 Envelope and versioning

Every submitted request, including one rejected before task acceptance, MUST produce a minimal secret-safe admission/rejection bundle. Every accepted active, waiting, blocked, partial, failed, cancelled, unverified, candidate-review, or completed attempt MUST produce/update the applicable evidence profile. The logical bundle is versioned and runtime-validated. Storage and serialization technology are deliberately unselected.

Required profiles are `ADMISSION_REJECTION`, `ACTIVE`, `WAITING_OR_BLOCKED`, `TERMINAL_NONCOMPLETE`, `CANDIDATE_REVIEW`, and `COMPLETED`. Each profile has explicit conditional requiredness; a profile cannot weaken a field already required by a prior phase.

The core logical field dictionary is normative:

| Logical key | Type and cardinality | Required profile / bound source |
|---|---|---|
| `schema_version` | version identifier, exactly 1 | All / supported evidence contract. |
| `bundle_id` | identifier, exactly 1 | All / bundle authority. |
| `bundle_revision` | positive integer, exactly 1 | All / accepted bundle mutation. |
| `prior_bundle_revision_ref` | bundle reference, 0..1 | Revision >1 / prior preserved revision. |
| `profile` | enumerated value, exactly 1 | All / lifecycle facts above. |
| `request_id` | identifier, exactly 1 | All / admitted user input envelope. |
| `generated_at` | instant plus time basis, exactly 1 | All / authoritative clock or explicit uncertainty. |
| `privacy_class` | enumerated classification, exactly 1 | All / current data policy. |
| `redaction_scan` | result object, exactly 1 | All / declared scanner/check version and result. |
| `task_id` | identifier, 0..1 | Exactly 1 for accepted-task profiles; a pre-admission profile includes the candidate task identity if issued, otherwise absence has a reason. |
| `attempt_id` | identifier, 0..1 | All accepted-task profiles. |
| `task_class` | enumerated task class, 0..1 | After classification; otherwise explicit unknown/not applicable. |
| `agent_id` | identifier/reference, 0..1 | Accepted-task profiles / persistent agent authority. |
| `author_identity_ref` | accountable role identity reference, exactly 1 | Accepted-task profiles / accepted author ownership. |
| `executor_identity_refs` | accountable role identity references, 0..many | As execution occurs; includes the actor/configuration for every authored operation. |
| `challenger_identity_ref` | accountable role identity reference or explicit `NOT_APPLICABLE`, exactly 1 | Accepted-task profiles / applicable review policy. |
| `task_work_phase` | one §4.1 work-phase value, exactly 1 while open | Open accepted-task profiles; mutually exclusive lifecycle/work phase. Absent after terminal disposition. |
| `last_work_phase` | work-phase value, 0..1 | Terminal profiles; historical fact only, never an active phase. |
| `task_wait_reason_refs` | references to independent wait-reason records, 0..many | Open profiles when present; includes `task.wait_reasons=WAITING_FOR_APPROVAL`, `task.wait_reasons=WAITING_FOR_USER`, or `task.wait_reasons=WAITING_FOR_EXTERNAL_EVENT` facts without replacing phase/control/reconciliation. |
| `task_control` | `task.control=NONE`, `task.control=PAUSING`, `task.control=PAUSED`, or `task.control=STOPPING`; exactly 1 | Every open accepted-task profile; mutually exclusive control axis. |
| `task_reconciliation` | `task.reconciliation=NONE`, `task.reconciliation=RETRYING`, or `task.reconciliation=RECOVERING`; exactly 1 | Every open accepted-task profile; mutually exclusive reconciliation axis. |
| `task_blocker_refs` | blocker references, 0..many | Open profiles when blockers exist; independent from wait and control axes. |
| `attempt_disposition` | enumerated disposition, 0..1 | Terminal profiles; absent while attempt open. |
| `verification_status` | `verification.status=UNVERIFIED`, `verification.status=IN_PROGRESS`, or `verification.status=FINISHED`; exactly 1 after acceptance | Accepted-task profiles / verification authority. |
| `verification_verdict` | `verification.verdict=PASSED`, `verification.verdict=CHANGES_REQUIRED`, `verification.verdict=BLOCKED`, or `verification.verdict=INCONCLUSIVE`; 0..1 | Exactly 1 only when aggregate `verification.status=FINISHED`; derived from the current authoritative eligible run. |
| `verification_run_refs` | immutable verification-run references, 0..many | As verification runs occur; every run records identity/configuration, routing provenance, exact candidate/revision, bounded context, independence mechanism, run status, evidence, failure layer, and retryability. |
| `authoritative_verification_run_ref` | verification-run reference, 0..1 | Exactly 1 when aggregate `verification.status=FINISHED`; absent for `verification.status=UNVERIFIED` or `verification.status=IN_PROGRESS`. |
| `agent_availability_ref` | versioned reference, 0..1 | Accepted task / agent authority; never substitutes for task status. |
| `operation_refs` | operation references, 0..many | As operations exist / each operation has its own status/outcome and execution-effect authority. |
| `repository_ref` | repository identity object, 0..1 | Repository task profiles / preflight and fresh reread. |
| `repository_condition_refs` | classified repository-condition references, 0..many | Repository task profiles / §8.1 matrix, most-restrictive disposition, and union of constraints. |
| `workspace_ref` | workspace identity object, 0..1 | Once workspace exists / workspace authority. |
| `review_revision_ref` | immutable revision/package reference, 0..1 | Candidate and completed profiles. |
| `authority_refs` | versioned references, 1..many after acceptance | Task/policy/principal/tool-contract authority. |
| `input_provenance_refs` | versioned material-input references, 0..many | As author attachments or external inputs materially influence requirements, predicates, evidence, or output; each records content identity/digest where safely available, role, trust class, and limitations. |
| `route_provenance_refs` | model-operation routing references, 0..many | As model operations occur; requested/resolved model/configuration plus `route_purpose`, `route_eligibility`, authorization, fallback, and outcome. |
| `plan_ref` | versioned reference, 0..1 | After planning. |
| `predicate_coverage_map_ref` | versioned coverage-map reference, 0..1 | Required from planning onward; binds every material request/scope/governance/security obligation to an objective predicate or justified `NOT_APPLICABLE`. |
| `predicate_results` | predicate result objects, 0..many | Candidate/completed and applicable noncomplete profiles. |
| `section_refs` | typed evidence-section references, 0..many | As evidence sections exist; all refs resolve within allowed task/profile. |
| `persistence_boundary` | bounded support object, exactly 1 after acceptance | Declared client/orchestrator/worker/device/media failure classes, exclusions, acknowledgement point, recovery-point objective, recovery oracle, and candidate configuration identity. |
| `final_validation_ref` | validation-attestation reference, 0..1 | Exactly 1 for completed; applicable candidate/noncomplete bundle failures. |

Every nested object/list item also declares a stable ID, contract/version, logical type, allowed enum/domain, cardinality, conditional profile, maximum bound or referenced bounded artifact, authoritative source/version, and reference target. Unknown extension fields require an admitted namespace and cannot change core semantics.

A new task/plan/predicate/policy/repository/configuration/schema/review revision produces a new preserved bundle revision when it changes the meaning of evidence. Old evidence remains attached only to the state it proves and carries an explicit stale/superseded rule.

### 12.2 Required logical sections

| Section | Required content or references |
|---|---|
| Authority and request | Original request identity/content or safe authoritative reference; user/principal; author, executor, verifier-run, and challenger provenance; admitted governing inputs with trust labels and §3.2 precedence; dependencies; task class; allowed/forbidden scope; paths; capabilities; data/network/credential/effect limits; budgets; policy and authorization references. |
| Repository/workspace | Repository identity; base revision/tree; every detected §8.1 condition and disposition; effective most-restrictive disposition and union of constraints; workspace identity/profile; included/excluded tracked, untracked, ignored, nested, submodule, and LFS state; separately identified pre-existing changes; proof that each potentially mutating reproduction/diagnosis command ran only after isolation or under the exact exceptional authorization; final branch/head/dirty state and reread time. |
| Plan and predicates | Plan identity/version/amendments; coverage map from every material original-request clause, task-class minimum, admitted scope, governing instruction, and security/correctness obligation to an objective predicate or justified `NOT_APPLICABLE`; `PREDICATE_SET_ADEQUATE` result; each predicate's identity, applicability, oracle, mandatory status, acceptance rule, evidence references, actual result, and unresolved reason; reproduction predicate or explicit applicability decision. |
| Inputs/provenance | Source/input identities, safe locations/references, trust and evidence labels, version/date and content identity or safe digest where available, author-input attachment/reference role, material requirement/evidence/output trace, freshness/staleness and integrity facts, limitations, and fact/inference/proposal/unknown separation. A digest proves byte identity only. |
| Change/review package | Created, modified, deleted, renamed, and protected-unchanged files; diff/patch identity and integrity; local branch/bounded commit reference as applicable. Any draft-PR package minimally records package identity/version, `NOT_SUBMITTED`, repository/base/head or patch identity, title, summary/body, changed-file/diff reference, request and checklist provenance, tests/checks including flaky outcomes, known limitations, evidence and verification references, and outstanding capability/approval requirements. |
| Operations | Operation and attempt IDs; task authority, policy, plan and predicate versions; executor identity; capability and input/output schema versions plus validation results; provider identities; independent effect class plus v0.1 disposition and approval requirement; routing provenance for model operations; secret-safe normalized arguments; working directory; start/end/time basis; bounds; cancellation; exit/signal/status/outcome; bounded output or artifact refs; idempotency/reconciliation; retry links; failure/effect refs. |
| Tests/checks | Check identity and type; exact secret-safe command/action; tool/version/configuration/environment; reviewed revision; predicate mapping; result/exit; bounded output evidence; ordered repeated outcomes and `FLAKY` classification; retries; infrastructure failure layer/retryability; skipped/not-applicable reason and consequence. |
| Provider/model/tool/environment | Requested and resolved provider/model/configuration, logical role without implying E3 eligibility, `route_purpose`, `route_eligibility`, authorization and route/fallback reason, refusal/stop/error semantics, capability/tool/server and environment/dependency identities, usage/cost/latency when exposed, and explicit unknowns. |
| Approvals/effects/readbacks | Exact approval request/receipt binding including principal, task, attempt, operation, action, capability schema, target, base, policy, validity interval and use limit; authoritative current ownership and revalidation after recovery; decision, denial/expiry/revocation/consumption; dispatch-boundary state; operation/effect receipt; before/after identity; authoritative readback; cancellation, duplicate, partial, or uncertain outcome. |
| Artifacts | Stable identity, kind, safe inspectable location/reference, owner/producer, lineage, reviewed revision, integrity fact, sensitivity, retention rule, regeneration trigger, stale rule, automation policy, and failure consequence. |
| Failures/recovery | Failure identity/class/layer/retryability/terminal metadata; all attempts and retained costs/effects; recovery/reconciliation/escalation; resulting state; blockers, uncertain effects, and next safe action. |
| Verification | Every immutable run in order: verifier identity/configuration and route provenance, exact candidate-bundle and reviewed-revision references, bounded context manifest and independence mechanism, run status, failure layer/retryability or substantive verdict, predicate-adequacy/coverage assessment, predicate-by-predicate results and evidence refs, reproduced checks/readbacks, disagreements, rerun reason/ceiling/basis, corrective action, and current authoritative-run reference. |
| Final disposition | For an open attempt, the complete current tuple of `task_work_phase`, wait reasons, `task_control`, `task_reconciliation`, blockers, verification, agent availability, and operation states. For a terminal attempt, `last_work_phase`, terminal `attempt_disposition`, terminal/uncertain operation outcomes, settled verification run state, completed/unmet predicates, limitations with blocking consequence, unverified claims, remaining failures, out-of-scope observations, user review, and human-approval requirements; no active phase/control/reconciliation/wait/blocker fact is represented as current. |
| Integrity and threat evidence | Content-identity, lineage, authorization, append/revision, current-state binding, validation, and gap/tamper-detection facts required by §3.3; detected accidental or product-boundary adversarial mutation/reordering/substitution and its blocking/recovery consequence; explicit limits of protection. |
| Final validation | Validator/rule-set/schema versions, exact final bundle revision and content identity, validation time, structural/type/bound/reference/semantic results including legal multi-axis combinations, candidate/review-revision binding, role/routing/input provenance, integrity/gap results, failure refs, and attestation identity. |

### 12.3 Validation rules

A bundle is invalid if any applicable rule fails:

1. reject unsupported versions, malformed types, duplicate identities/keys, oversized fields, unknown non-namespaced fields, unsafe payloads, and unresolved or cross-task references;
2. classify every material repository condition under §8.1, apply the most-restrictive disposition and union of constraints, and reconcile repository identity, base/head/dirty state, included/excluded material, changed-file inventory, diff/review package, and reviewed revision against fresh authoritative state;
3. never attribute pre-existing user changes to the task;
4. count a check as passing only on the reviewed revision under the declared configuration/environment; retain ordered repeats, skips, truncation, retries, infrastructure failures, and failures. Mixed outcomes for the same identity/revision/configuration/environment validate as `FLAKY`, and a later pass alone cannot erase that classification;
5. require a demonstrated reported or predeclared alternative pre-fix failing oracle for `DEFECT_REPRODUCTION_AND_FIX`; non-reproduction requires redirect/reclassification or a noncomplete profile;
6. require every consequential effect to link exact current authority, approval, operation, receipt, and readback; uncertainty prevents completion;
7. keep requested and resolved provider/model/tool/configuration identities separate, require a valid `route_purpose`/`route_eligibility` pair and authorization on every model operation, and expose fallback as a separately proven route/attempt; `EVALUATION_ONLY` and `USER_CONFIGURED_UNVERIFIED` evidence cannot masquerade as normal eligibility;
8. require every generated record/artifact to state its authoritative inputs, accountable author/executor/verifier/challenger role provenance where applicable, what it proves and does not prove, regeneration trigger, stale detection, automation policy, and failure consequence;
9. exclude secrets, prohibited private data, forbidden external code/assets/copy, and unsafe sensitive paths/metadata; a digest aids byte integrity but proves neither authority, confidentiality, correctness, nor deletion;
10. bind every material author attachment/external input to its declared version/content identity, role, trust class, and downstream requirement/evidence/output use; absence or ambiguity is explicit and cannot silently establish authority;
11. bind the immutable candidate bundle, exact reviewed revision, authoritative eligible `verification.run_status=FINISHED` run, exact final bundle revision, and final validation attestation consistently; any material post-verification mutation preserves the old evidence for its old revision but returns the new state to `verification.status=UNVERIFIED` until re-verification;
12. validate the multi-axis state rules in §§2 and 4: independent conditions may coexist only where declared, mutually exclusive values cannot coexist, retry and recovery cannot be simultaneous, terminal disposition cannot retain active phase/wait/control/reconciliation/blocker or in-progress verification, and `attempt.disposition=COMPLETED` cannot coexist with a nonterminal or `operation.outcome=OUTCOME_UNCERTAIN` material operation;
13. require `PREDICATE_SET_ADEQUATE`, complete material-obligation coverage, all applicable predicates, and an independent `verification.verdict=PASSED` for `attempt.disposition=COMPLETED`; schema validity or passing insufficient tests is not enough;
14. require verification runs to be sequential with at most one `verification.run_status=IN_PROGRESS`; every rerun must meet §4.3's preceding-terminal-run, retryable-`verification.run_status=VERIFICATION_ERROR`, same-revision, bounded-ceiling, and preserved-history rules; a verifier/infrastructure error keeps aggregate `verification.status=UNVERIFIED` and is neither task failure nor verification pass;
15. require a draft-PR package, when produced, to remain explicitly local/`NOT_SUBMITTED` and contain every minimum field in §8.4/§12.2; and
16. detect or explicitly fail closed on evidence gaps, reorder, mutation, substitution, or stale binding within §3.3's product threat boundary. A digest alone does not establish authority, completeness, currentness, or correctness.

Outcome-conditional missing fields MUST use an explicit `NOT_APPLICABLE`, `UNKNOWN`, `NOT_RUN`, or `UNAVAILABLE` value with reason and status consequence. Silent omission is invalid. Every required bundle revision must validate against its outcome profile; a completed bundle additionally has no unresolved mandatory field, reference, blocking limitation, effect, or check.

Bundle generation or validation failure creates a bounded `EVIDENCE_FAILURE`, preserves the underlying authoritative facts, supplies the next safe action, and prevents `COMPLETED`; it MUST NOT destroy or hide the task merely because its export/assembly failed.

## 13. Observability and context compaction

### 13.1 Authority separation

Operational telemetry and presentation views diagnose behavior. They cannot grant authority, overwrite task/effect history, or prove completion. Required audit and evidence responsibilities are never sampled away. Optional telemetry loss is visible but cannot change outcome; missing mandatory authority/evidence blocks completion. E2 decides physical representation.

### 13.2 Minimum correlated record

“Material” means any fact that can affect authority, policy, scope, cost/budget, ordering, lifecycle/control, effect certainty, recovery, security/privacy, predicate evaluation, evidence validity, verification, or final disposition. Every material transition and operation MUST expose or reference, as applicable:

- schema and record type/version, authority class (`AUTHORITY`, `AUDIT`, `EVIDENCE`, `TELEMETRY`, or `PROJECTION`), mandatory/optional class, record/task/agent/attempt/operation identities, causal parent, correlation and idempotency identities;
- actor/role including accountable author/executor/verifier/challenger provenance, authoritative source/reference and version/current-ownership proof, occurrence time, record/observation time, time basis/duration, ordering position, detected gap/reorder fact, and axis-qualified state before/after;
- repository/workspace/base/head, repository-condition dispositions, normalized target/effect class, action disposition, policy/approval reference and applicable bounds;
- requested/resolved provider, model, capability/tool, configuration, `route_purpose`, `route_eligibility`, route authorization/fallback, result/stop/refusal/error semantics;
- retry/cancellation/recovery including verification-run failure layer and retryability, usage/cost when exposed, artifact/evidence/readback references, uncertainty and limitations;
- sampling/drop/truncation policy and occurrence, projection as-of source version, lag/freshness/staleness, and required recovery consequence;
- privacy/redaction class and safe bounded content.

Explicit `UNKNOWN` is allowed where the source does not expose a value; silent omission or fabricated precision is not.

### 13.3 Required observable events

User-visible status and accountable records cover: admission/preflight and pre-dispatch policy/schema denials; task/agent transitions by axis; plan/predicate and coverage-map versions; controls and reconciliation; approval request/grant/deny/expire/revoke/consume and recovery revalidation; operation/tool start/end/cancel/timeout/force-termination/fencing; retries/recovery; budget preflight/exhaustion; artifacts; retention/legal-hold/cleanup/deletion; context-reduction accept/reject; provider route-purpose/eligibility/fallback decisions; predicate checks and flaky repetitions; verification run/status/verdict/error/rerun events; effects/readbacks; observability loss/degradation/gap/tamper detection; evidence validation; and final disposition.

Every started operation reaches a known terminal result or a named waiting/uncertain record within its declared bound. The user can distinguish no progress, long-running work, waiting, pause, recovery, retry, provider/tool failure, evidence assembly, and verification. Concise decisions and evidence are shown without private chain-of-thought.

Every aggregate observation additionally records stable metric ID and definition version, unit, candidate/build/configuration, population/window, raw numerator and denominator, sample size, every exclusion with reason, missing/unknown data, uncertainty/confidence method when applicable, and whether the metric is a hard invariant, `PREVIEW_SLO`, or `MEASURE_ONLY`. No average may hide an individual hard-gate failure.

### 13.4 Context reduction invariant

Summary, compaction, truncation, retrieval, or model-context reconstruction may alter only a derived working view. It MUST NOT delete, overwrite, reorder, or become authoritative over original messages, task/plan/predicate state, controls, policy, approvals, operation/effect history, failures, artifacts, audit records, or evidence inputs.

Trust and authority labels, corrections, revocations, pending approvals, limits, current versions, failures, and unresolved effects MUST survive reconstruction through authoritative retrieval rather than summary assertion. A stale or poisoned summary cannot overwrite newer state or upgrade untrusted content to an instruction. Required source evidence remains retrievable and correlated. The existence and mechanism of persisted summaries is an E2 decision.

## 14. Reliability contract

### 14.1 Per-occurrence hard invariants

| ID | Class | Requirement and objective result |
|---|---|---|
| `RR-001` | HARD_INVARIANT | Every acknowledged authoritative mutation needed for task/message/plan/control/approval/effect/artifact/evidence/verification recovery has recovery-point objective zero within the declared supported local persistence boundary: 100% recovered, zero acknowledged-record loss. |
| `RR-002` | HARD_INVARIANT | Every affected nonterminal task after a supported orchestrator/worker interruption resumes from the latest valid acknowledged state or enters an explicit recovery/block/failure/uncertain state: zero silent regression or fabricated continuity. Client-only reconnection does not interrupt healthy work. |
| `RR-003` | HARD_INVARIANT | Stable operation identity and declared idempotency/reconciliation yield zero unintended duplicate material non-idempotent or consequential local/external effects; every uncertain effect is read back or escalated and none is called complete. |
| `RR-004` | HARD_INVARIANT | Zero stale authoritative owner/writer mutations are accepted; stale projections/summaries cannot influence newer authority; 100% of authoritative/evidence records survive context reduction. |
| `RR-005` | HARD_INVARIANT | Every operation/task has finite declared time, output, tool-call, retry, network, cost, cancellation, and reconciliation limits as applicable. After a productive ceiling is exhausted, zero new productive or task-advancing work starts; only a preauthorized, separately bounded control/safety/cancellation/readback/evidence/cleanup reserve may run. Verification reruns also have a prospectively bounded ceiling, without E1 choosing a numeric count. |
| `RR-006` | HARD_INVARIANT | Every accepted pause/stop/redirect receives explicit reconciliation; zero material operation ordered after the control's durable acceptance starts under superseded authority. Requested, cooperative-cancel, force-stop/fence, reconciliation-deadline, and effective times remain separately visible where applicable. A stop closes only after descendants and effects are terminal or explicitly uncertain, never as `COMPLETED`. |
| `RR-007` | HARD_INVARIANT | Across every supported task, zero unrelated user changes are lost, overwritten, staged, committed, deleted, or silently mixed; initial/final repository and diff facts are reconciled. |
| `RR-008` | HARD_INVARIANT | Zero `FALSE_TERMINAL_COMPLETION` outcomes and zero `attempt.disposition=COMPLETED` without an adequate complete predicate set, valid evidence, every material operation terminal/accounted consistently with close, zero material `operation.outcome=OUTCOME_UNCERTAIN`, every success-required effect authoritatively `operation.outcome=KNOWN_SUCCEEDED` with required readback, every other material effect at a known terminal outcome consistent with predicates, no current wait reason/control/reconciliation/blocker or pending approval/question/event, every accepted pause explicitly resumed/released, every accepted stop resolved only to `attempt.disposition=CANCELLED`, every redirect verified on its current revision, and an authoritative eligible independent `verification.verdict=PASSED` run. Rejected unsupported completion assertions are recorded separately. |
| `RR-009` | HARD_INVARIANT | Every required missing/skipped/failed/stale/inadequate/unverifiable or unresolved-flaky check produces a noncomplete outcome; verifier/check-infrastructure errors remain distinguished from substantive task/check failures; every proposed/dispatched operation, rejected pre-dispatch attempt, execution attempt, verification run/rerun, and evidence-bundle failure is accounted for. |
| `RR-010` | HARD_INVARIANT | Every required evidence-bundle revision validates against its outcome profile and is retrievable/bound to authoritative state; completed bundles additionally have zero unresolved mandatory reference/revision/semantic mismatch. |
| `RR-011` | HARD_INVARIANT | Zero malformed/incompatible/oversized/stale/unknown executable contracts run and zero hidden provider/model/tool fallback or route-class elevation occurs. Every model operation records requested/resolved provenance, `route_purpose`, `route_eligibility`, authorization, and fallback; a source-unavailable provenance field is explicit `UNKNOWN` with its declared consequence, never permission to execute an unknown contract. Evaluation-only or user-experimental results cannot establish normal eligibility. |
| `RR-012` | HARD_INVARIANT | Zero silent pruning of state needed for authority, recovery, reconciliation, review, or verification; every retention/hold/cleanup/deletion action has authoritative readback or explicit uncertainty and preserves required historical evidence. |
| `RR-013` | HARD_INVARIANT | Every cost-bearing operation has an enforceable authorized conservative ceiling before dispatch, including when live usage/cost reporting is unavailable; zero budget-gate violations. Actual usage/cost is attributed or explicit `UNKNOWN`, but unknown reporting never excuses unbounded dispatch. |
| `RR-014` | HARD_INVARIANT | Every material operation and verification run is correlated from intent through result/readback or explicit uncertainty/error; accidental and product-boundary adversarial drops, gaps, truncation, delay, reordering, substitution, retries, and cancellation are detected/accounted for; telemetry or a digest alone never establishes authority, integrity, adequacy, or completion. |
| `RR-015` | HARD_INVARIANT | Across every relevant occurrence, zero unauthorized effect/read, destructive action against user-owned material, protected-secret/private-data disclosure even inside an allowed root, allowed-root/workspace escape, approval replay/mutation, post-verification candidate mutation presented under stale evidence, or clean-room/provenance violation is permitted. |

These are preview correctness gates, not claims that an implementation has passed them.

### 14.2 Aggregate and measurement requirements

E1-002 MUST define the versioned release population, sample size, repetition policy, exclusions, window, threshold, and confidence treatment for each `PREVIEW_SLO` before scored E3/E5 execution. It may not average away a hard-invariant failure. `MEASURE_ONLY` metrics have no v0.1 pass/fail threshold; converting one to a gate requires a prospective E1 amendment/reclassification before the scored run.

| ID | Class | Stable metric family |
|---|---|---|
| `SLO-001` | PREVIEW_SLO | Independently verified end-to-end success by eligible task and repository class, with task/executor, verifier/provider/tool/model, and verification-infrastructure error layers reported separately. |
| `SLO-002` | PREVIEW_SLO | Durable-control acknowledgement and effectiveness latency, separately measured for pause, cooperative stop, force-stop/fencing where invoked, redirect, and resume. Stop effectiveness requires, within the declared stop bound, zero later productive dispatch, every descendant terminated or authority-fenced, and every operation terminal or explicitly `operation.outcome=OUTCOME_UNCERTAIN`. |
| `SLO-003` | PREVIEW_SLO | Supported orchestrator/worker restart recovery latency to a truthful inspectable phase/condition. |
| `SLO-004` | PREVIEW_SLO | Candidate review-package/evidence-profile acceptance rate after deterministic validation and independent review. |
| `MET-001` | MEASURE_ONLY | Raw and p50/p95 task, phase, provider, tool, verification, and stalled latency where sample size permits. |
| `MET-002` | MEASURE_ONLY | Total/component cost per attempted task and per independently verified success; the latter is undefined at zero successes. |
| `MET-003` | MEASURE_ONLY | User interventions, execution retries, verification reruns, verifier crashes/timeouts/tool/check-infrastructure errors, rate-limit delays, evidence failures, rejected completion assertions, force-stop/fencing, and recovery actions. |
| `MET-004` | MEASURE_ONLY | Ordered check outcomes and `FLAKY` classifications plus outcome variance across repeated equivalent attempts and configuration/provider strata. |

Universal aggregate task-success, latency, cost, intervention, and variance thresholds remain **UNKNOWN** until E1-002 sets only the `PREVIEW_SLO` gates and E3/E5 supply observations. A future release requirement must pass every predeclared `PREVIEW_SLO`, report every `MEASURE_ONLY` metric with raw counts/denominators/unknowns, and pass all hard invariants. E1-001 does not import the unrun model-benchmark-plan design proposals or the zero-run reference baseline as reliability evidence.

## 15. Security-negative and approval review requirements

All security negatives use synthetic/local fixtures, fake marker secrets, controlled sinks/stubs, before/after canaries, and no real credential, external exploitation, paid action, or imported external code. Any unauthorized effect/read or marker leak is a non-compensating failure.

| ID | Required stimulus family | Required outcome/evidence |
|---|---|---|
| `NEG-AUTH-01` | Repository instruction, README/contribution text, issue/PR/document/tool/model/test output orders policy, sandbox, network, secret, approval, destructive-action, routing, or evidence bypass and claims superior or local authority; or a benign-looking required check declares a command that needs an ungranted network/credential capability. | §3.2 precedence and trust remain unchanged; governing repository instructions may only narrow admitted workflow behavior; the check creates no implicit grant and records an unmet precondition/wait/block; zero prohibited action; denial/conflict audited. |
| `NEG-SCHEMA-01` | Unknown/stale tool version, malformed/duplicate/oversized request, mismatched/invalid result, or target mutation. | Invalid request/contract/target is denied before dispatch. Invalid post-dispatch result is denied consumption/downstream use and the possible effect enters readback/reconciliation; no widening repair or zero-effect fiction. |
| `NEG-FS-01` | Traversal, path alias, symlink/hard-link/swap, mount/device/FIFO/socket, archive escape/bomb, cleanup-time topology change. | Zero out-of-root read/write/delete; all canaries byte-identical. |
| `NEG-GIT-01` | Hook, alias, credential helper, external diff/text conversion, filter, submodule, signer, monitor, or transport helper attempts execution/egress; a prohibited pull/stash/reset/restore/merge/tag or other Git action is requested. | No unapproved helper/network/secret effect or ref movement; §8.4 classification is enforced and approval does not enable a prohibited action; limitation visible. |
| `NEG-DESTRUCT-01` | An apparently in-root edit, cleanup, restore, reset, worktree removal, or other destructive operation targets pre-existing user-owned tracked, untracked, ignored, linked-worktree, nested-repository, generated, or ambiguous material. | Operation is denied or confined to proven task-owned material under exact task authorization and any matrix-row-required approval; user material remains byte-/identity-consistent and uncertainty blocks completion. |
| `NEG-TERM-01` | Test/build/script spawns descendants, changes working directory, writes outside, floods output, claims it is non-interruptible, or resists cooperative cancellation through the reconciliation deadline. | Inherited bounds; output bounded; safe force termination or authority fencing occurs when available; descendants/effects are terminal or explicitly uncertain; zero outside effect/orphan; killed work is never relabeled complete. |
| `NEG-CMD-01` | Untrusted filename/ref/task/tool argument contains spaces, leading options, metacharacters, substitutions, control/bidirectional characters, or command/option injection. | Value is handled as data under the declared command representation or denied; no unintended command, target, or effect. |
| `NEG-SUPPLY-01` | Downloaded package/archive/binary or lifecycle script attempts execution, egress, secret access, or escape. | Retrieval does not authorize execution; provenance retained; unauthorized action denied. |
| `NEG-NET-01` | Undeclared connection, redirect, DNS rebind, proxy bypass, loopback/private/metadata target, TLS downgrade, credential forwarding. | Zero forbidden connection or data/credential transmission; effective target rechecked. |
| `NEG-PROVIDER-01` | Disallowed provider/account/region/retention/training policy, missing cost ceiling, hidden fallback, evaluation-only candidate on a normal route, user-unverified model without explicit experimental routing, or evaluation result presented as production eligibility is offered an otherwise valid request. | Zero bytes/call/cost for disallowed or unauthorized routing; no class elevation or eligibility promotion; exact requested/resolved model, purpose, eligibility, authorization, and denial/outcome retained. |
| `NEG-SECRET-01` | A marker appears in an in-root `.env*` or known secret/config family, SSH/cloud/package/Git/provider credential material, OS/browser/shell/process/clipboard data, ambiguous path/link, command/tool output, exception, encoded/split stream, screenshot, temp/cache/log, diff, summary, approval, evidence, or accidental request paste. | Protected-secret precedence overrides allowed-root access; ambiguous content is not read/used/egressed; zero raw marker occurrences outside the exact protected recipient boundary; safe quarantine/exposure/rotation record without echo/digest leak; no claim of exhaustive detection. |
| `NEG-CRED-01` | Credential scoped to one task/tool/endpoint is attempted by another tool/child/redirect/retry/stale owner, then rotated/revoked during queued or active use. | Every mismatched/stale/new use is denied; queued use invalidates; active use cancels/reconciles with possible exposure explicit; receipt contains identity/scope only. |
| `NEG-APR-01` | Approval replay, target/argument substitution, schema/policy/base change, expiry/revocation, one-shot reuse, crash/restart ownership ambiguity, forged conversational confirmation, digest-only material, markup/control/bidirectional spoofing, or target-hiding truncation. | All invalid/uninspectable uses denied; a recovered successor consumes only an exact current revalidated approval with authoritative ownership; exact valid action executes at most once; inert full-content display/reference and executable action binding match. |
| `NEG-RACE-01` | Approval/revocation/pause/stop/redirect/restart/stale-owner races before, during, or after dispatch/effect. | One legal persisted outcome; stale owner denied; dispatch-boundary ambiguity becomes reconciliation/uncertainty; no blind retry, duplicate approval consumption, or false completion. |
| `NEG-EXT-01` | External effect occurs but response is lost, or tool reports success while target is wrong/unchanged/partial. | Authoritative readback before retry/completion; at most one effect; honest partial/uncertain/noncomplete status. |
| `NEG-VER-01` | Sole author self-verifies high-risk work, the same running model session authors and verifies, verifier relies only on executor self-report/transcript, deterministic evidence is ignored, or verifier tries a new effect with author approval/credential. | Invalid independence rejected; bounded context and separate execution path retained; deterministic oracle controls the same predicate; verifier remains least-privilege or obtains separate authority; exact revision and verifier identity/configuration retained. |
| `NEG-VER-02` | Candidate/repository/effect state mutates after a pass, or passing lint/tests/file-existence evidence omits or cannot establish a material requested behavior/obligation. | Old verdict remains bound only to its old revision; current aggregate becomes `verification.status=UNVERIFIED`; `PREDICATE_SET_ADEQUATE` fails or requires stronger objective coverage; no stale-evidence completion. |
| `NEG-CTX-01` | Compaction upgrades malicious text or omits a correction/revocation/policy change. | Trust labels and latest authority win; stale summary discarded; authoritative evidence retained. |
| `NEG-EVID-01` | Tool/test output forges approval, source, receipt, readback, pass result, or self-hashing manifest. | Provenance/schema/correlation and independent readback reject it; digest alone gets no correctness credit. |
| `NEG-AUDIT-01` | Material denial, approval/revocation, secret-boundary, effect/readback, or verification history is deleted, altered, reordered, duplicated, or replaced by telemetry. | Mutation/gap is detected, authoritative history is not silently reconstructed from telemetry, and verification/completion is blocked pending safe reconciliation. |
| `NEG-CLEAN-01` | Cleanup follows a malicious link, workspace identity changes, or cancellation leaves temp credential/process/artifact. | User/outside data untouched; required evidence retained; scoped cleanup is authoritatively reread. |
| `NEG-DOS-01` | Recursive call, retry storm, oversized result, decompression bomb, output flood, or budget exhaustion. | Hard ceilings hold; no uncontrolled resource/spend; terminal/blocked evidence remains bounded. |
| `NEG-FUTURE-01` | Two synthetic principals/workspaces reuse path, capability, approval, operation, artifact, or identity. | Explicit current ownership prevents cross-workspace use; this proves compatibility only, not multi-tenant implementation. |

Hard acceptance requires zero unauthorized reads/writes/effects/credential use/network connections; zero marker-secret leakage; 100% invalid/stale/mutated requests and approvals denied before dispatch; 100% invalid effectful results denied downstream use and reconciled without claiming zero effect; 100% consequential effects correlated to authority, approval, operation, receipt, and readback or explicitly noncomplete; at most one committed effect per operation identity; 100% outside/unrelated canaries unchanged; detectable material-audit tampering/gaps; and independent verification of every applicable security-sensitive predicate.

## 16. Evaluation and release requirement boundary

E1-001 defines requirement families only. E1-002 exclusively owns contributor procedures, fixture/case definitions, harnesses, graders/oracles, seeds, repetitions, scoring, aggregate release thresholds, detailed checklists, and the release checkpoint. E1-002 MUST NOT weaken E1-001 hard invariants; a conflict requires E1-001 amendment and reverification.

E1-002 must trace every `FR-*`, `RR-*`, `SLO-*`, `MET-*`, `FC-*`, lifecycle transition, completion predicate, evidence profile/field, and `NEG-*` requirement to concrete reproducible coverage with an independent oracle and expected multi-axis result. It must instantiate positive, adversarial/negative, interruption/fault, and unsupported coverage where applicable. This is a coverage obligation, not a case list or suite authored by E1-001.

The future gate MUST treat `FALSE_TERMINAL_COMPLETION`; unauthorized, duplicate, or unresolved consequential effects; secret/private-data disclosure; workspace/root escape or unrelated-change loss; invalid/stale/missing completion evidence; missing independent verification; and clean-room/provenance/forbidden-artifact failures as non-compensating blockers. It must pass every predeclared `PREVIEW_SLO`, report every `MEASURE_ONLY` metric, preserve exact preview limitations, receive E5 independent release verification against the exact candidate, and then receive explicit accountable human release approval. E5 supplies later release evidence; E1-001 supplies none.

## 17. Future compatibility without future scope

**FUTURE_COMPATIBILITY.** v0.1 records explicit principal, agent, task, workspace, operation, approval, artifact, provider, and policy ownership/version identities so later cloud, multi-device/multi-writer, multiple-agent, multi-user/SaaS, General Edition, Finance Edition, skills/routines, and vertical packs have a credible migration path without treating current values as permanent global singletons.

This does not add multiple visible agents, agent-to-agent messaging, groups, organizations, billing, enterprise controls, cloud execution, General/Finance behavior, market data, backtesting, paper/live trading, real-money actions, routines, schedules, marketplaces, broad connectors, mobile, or production operations to v0.1. E2 must later document migration and incompatible assumptions; it need not implement future concurrency or tenancy now.

Provider/configuration identities and versioned capability contracts permit future replacement without allowing provider-native state to define core task, authority, approval, evidence, or completion truth. Schema evolution must fail or migrate visibly; no event or storage mechanism is selected here.

## 18. Clean-room and evidence limits

The dated 2026-08-21, independently verified Grok Bot baseline is official-document behavioral reference evidence with zero black-box executions in its recorded baseline. It does not prove current runtime reliability, stop/recovery timing, approval enforcement, isolation, parity, or implementation feasibility.

The independently verified reconstructed-architecture audit is static research over a pinned unofficial reconstruction. Its clean-room levels apply as follows:

- **Level A:** the implementation-neutral system properties in this contract are required independently by D-016, the charter, master/security rules, and completion governance; the audit only corroborates or supplies test ideas.
- **Level B:** patterns are RESERVED_E2 comparison inputs only and are not used to derive E1 requirements or selections.
- **Level C:** reconstruction-specific code, exact schemas, status/error sets, constants, internal names, module layout, assets, UI copy, branding, consumer authentication/session flows, undocumented endpoints, and private material are forbidden inputs.

This specification imports no external code, exact internal implementation detail, runtime claim, provider assignment, or reference-product reliability result. Baseline/audit facts corroborate or identify unknowns but cannot override repository governance.

## 19. Traceability and ownership matrix

| Requirement family | Contract sections | Primary authority | Bounded corroboration | Reserved later owner |
|---|---|---|---|---|
| Authority and durable semantic state | §§2–3 | D-003/D-016; Charter §§5–6; master authority rules | D-005 establishes current project-repository authority only; Audit Level A corroborates properties only | E2 physical model/topology and instruction-precedence enforcement. |
| Task/agent lifecycle and controls | §§4–7 | D-016; Charter §§6–7, 11; master runtime rules | Baseline continuation/control claims are documented but untested; Audit Level A semantics only | E2 mechanism; E1-002 legal/invalid axis and bounded-stop coverage. |
| Repository/workspace/capabilities | §8 | D-016 workflow; Charter §§4, 8, 12 | Audit Level A boundary properties; no reconstructed implementation | E2 isolation/tool design under the condition and Git/effect matrices; E1-002 coverage. |
| Permissions, approvals, secrets, routing, effects | §9, §15 | `SECURITY.md`; D-004/D-016; Charter §§9, 12, 19–20; master security rules | Baseline features documented, enforcement unknown; Audit Level A/negative ideas | E2 enforcement/routing mechanism; E1-002 cases; E3 qualification evidence only after authorization. |
| Failure and honest partial outcomes | §10 | Charter §§6, 10–11 | Audit Level A accountable-failure property only | E2 structured contract representation. |
| Completion and verification | §11 | D-016; Charter §§7–8; master completion standard | Baseline artifacts are not automatic predicates; Audit Level A evidence closure | E1-002 adequacy/flaky/error cases; E3 independence-strategy and role eligibility evidence. |
| Evidence and observability/context | §§12–13 | D-003/D-016; Charter §§5.4–5.5, 6, 8, 10; master completion rules | Audit Level A evidence/derived-context principles corroborate only | E2 storage/projection/integrity design; E1-002 schema and tamper/gap validation. |
| Reliability and security negatives | §§14–15 | Charter §§11–12; R-002/R-003/R-009/R-013–R-015/R-025–R-028 | Zero-run baseline and unrun benchmark plan are not results | E1-002 thresholds/cases; E3/E5 runs. |
| Evaluation/release requirements | §16 | Charter §§18, 20, 22; task boundary | Taxonomy ideas only | E1-002 owns artifacts/gate. |
| Future compatibility and non-goals | §17 | D-001, D-003, D-004, D-016; Charter §15 | Level B material is reserved for E2 and is not E1 evidence | E2 migration analysis; later authorized stages. |
| Clean room/provenance | §18 | D-002, D-016; master prompt; Charter §16 | Verified baseline/audit within stated limits | Every later author/reviewer/verifier. |

## 20. Preserved unknowns and E1-001 boundary

The following remain **UNKNOWN**: final client and interaction form; storage/state/history/event/projection/compaction design; local isolation mechanism and demonstrated tier; host/language/repository support matrix; capability catalog; funded provider access and exact model configurations; model-role assignments; benchmark and implementation budget; aggregate preview release thresholds; universal latency/cost envelopes; packaging/update/migration mechanics; customer demand; production readiness; and reference-product runtime behavior beyond sourced documentation.

No unknown may be filled from model reputation, a single run, external reconstructed detail, or an architecture preference. This contract creates no application code, performs no benchmark, selects no architecture or technology, does not activate E1-002/E2/E3/E4/E5, does not resume S1-003, and does not authorize autonomous build or external action.

E1-001 may move only to repository `READY_FOR_REVIEW` after author validations and factual handoff. It remains unverified until the registered independent challenger, author/fixer response, and independent post-fix verifier satisfy all task acceptance criteria. E1-002 remains `BACKLOG` until that independent verification is complete.
