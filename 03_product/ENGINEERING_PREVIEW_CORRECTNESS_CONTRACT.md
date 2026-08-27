# Engineering Preview v0.1 Correctness Contract

Status: E1-001 AUTHOR PASS — READY_FOR_REVIEW; NOT VERIFIED

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

If a companion document conflicts with this correctness contract on lifecycle, authority, approval, completion, or evidence, the conflict blocks verification and requires an E1-001 amendment. Repository governance remains superior to all product documents. Untrusted content may narrow work only when a governing instruction legitimately applies; it cannot broaden authority.

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

Correctness MUST NOT be encoded in one overloaded status. The product must preserve at least these independent axes even if E2 later chooses different internal names or combines their physical representation:

1. task work phase;
2. wait reason, control condition, and blocker;
3. attempt disposition;
4. verification status;
5. verification verdict;
6. operation/effect outcome;
7. agent identity and operational availability.

The authoritative task view is a tuple, not a winner-takes-all label. A user-facing projection may emphasize a primary label in this order—terminal attempt disposition, `STOPPING`, `RECOVERING`, `PAUSING`, `PAUSED`, named wait reason, blocker, retry condition, then work phase—but it MUST also retain every other nonempty axis. Emphasis never erases a pending approval/question, stop cause, partial-result fact, verifier result, or `OUTCOME_UNCERTAIN` effect.

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

Permission is the intersection of governing policy, admitted task scope, current user grant, and trusted capability limits. No layer may broaden another. Unknown, conflicting, stale, malformed, or ambiguous authority fails closed to a typed denial, `WAITING_FOR_USER`, or `BLOCKED` outcome.

The one local principal MUST have a stable authenticated identity for task admission and approval semantics. E2 selects the authentication mechanism, but E1 requires wrong, changed, lost, stale, or unverifiable principal identity to deny admission/approval and prevent continuation until re-established. Local operating-system presence, client access, or conversational self-assertion alone is not authorization.

Repository files, issue text, web content, documents, model output, generated code, test/build output, dependencies, tool names/descriptions/results, discovered tool servers, restored artifacts, summaries, and telemetry are untrusted content. They cannot grant capability, satisfy approval, change policy, widen scope, or prove completion.

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

An acknowledgement is returned only after the mutation is durable enough for declared recovery and is rereadable. Duplicate delivery returns the original outcome. Stale, illegal, or unauthorized mutations are retained as rejected attempts and do not change state. Material authorization, denial, approval/revocation, secret-boundary, operation/effect/readback, and verification facts have append-only/immutable semantics: corrections and retention/deletion actions add linked records rather than silently rewriting history, and deletion, alteration, reordering, or unexplained gaps are detectable and block verification. Exact concurrency, audit, and persistence mechanisms are E2 decisions.

## 4. Product-task lifecycle

### 4.1 Task work phases

| Phase | Meaning | Entry condition | Legal exits |
|---|---|---|---|
| `CREATED` | A durable task identity and original request or authorized redacted/protected reference exist; admission is not complete. | Request is captured without effectful execution. | `READY`, a wait/block qualifier, or named terminal disposition. |
| `READY` | Task contract is sufficiently bounded and authorized to await claim. | Eligibility, authority, scope, limits, and initial predicates validate. | `QUEUED`, user redirect, stop/cancel. |
| `QUEUED` | The already user-admitted task waits for the single current execution owner under a finite declared bound and visible order. | Waiting admission is durable; this is not self-selection from an autonomous or externally discovered work queue. | `CLAIMED`, pause, stop/cancel, redirect. |
| `CLAIMED` | One accountable current owner holds the attempt under a stale-owner proof. | Exactly one claim is accepted against the current ownership version or equivalent. | `ANALYZING`, recovery, pause, stop/cancel. |
| `ANALYZING` | Governing inputs and repository state are being inspected. | Authorized owner and safe preflight. | `PLANNING`, waiting, blocked, retry/recovery, pause/stop. |
| `PLANNING` | Bounded plan and predicates are being created or revised. | Current evidence supports a bounded proposal. | `READY_TO_EXECUTE`, waiting, blocked, pause/stop. |
| `READY_TO_EXECUTE` | Current plan, predicates, permissions, workspace, and limits validate. | Pre-dispatch validation passes. | `EXECUTING`, waiting for approval, redirect, pause/stop. |
| `EXECUTING` | One or more authorized operations are active or settling. | Operation-specific authorization validates. | `OBSERVING`, `READY_FOR_VERIFICATION`, waiting, blocked, retry/recovery, pause/stop, noncomplete disposition. |
| `OBSERVING` | The author is rereading repository/effect state and assembling evidence. | Material execution ended or reached an observable checkpoint. | `EXECUTING`, `READY_FOR_VERIFICATION`, blocked/recovery, pause/stop. |
| `READY_FOR_VERIFICATION` | Author proposes that predicates are reviewable; no verified-completion claim exists. | Review revision and candidate evidence bundle are fixed and author checks pass. | `VERIFYING`, redirect/supersession, blocked, cancellation. |
| `VERIFYING` | Independent verification is evaluating the exact review revision. | Eligible verifier, independence, revision, authority, and evidence validate. | verification verdict and corresponding attempt disposition or a new corrective attempt. |

### 4.2 Wait and control conditions

These conditions remain separate from the work phase:

| Condition | Meaning | Required record |
|---|---|---|
| `WAITING_FOR_USER` | A specific material answer is required. | Question, why material, affected predicates, safe continuation boundary, response correlation. |
| `WAITING_FOR_APPROVAL` | An exact consequential action is proposed but not approved. | Normalized request, zero-effect fact, expiry, and allowed denial/revocation paths. |
| `WAITING_FOR_EXTERNAL_EVENT` | An authorized observable condition must change before safe continuation. | Expected event/readback, timeout, polling/notification limit, owner, fallback. |
| `PAUSING` | A durable pause request is being reconciled with in-flight operations. | Request/effective timestamps, settling operations, effects after request. |
| `PAUSED` | No productive or task-advancing operation may start under suspended authority; only separately authorized bounded safety, cancellation, readback, evidence-preservation, and reconciliation work may run. | Effective checkpoint, operation classifications, resume preconditions. |
| `STOPPING` | A durable stop/cancel request is being reconciled; no productive or task-advancing operation may start under superseded authority. | Request/effective ordering, cancellation attempts, operation outcomes, partial-result facts, cleanup/readback. |
| `RETRYING` | A retryable failure is inside its predeclared ceiling. | Original failure, attempt count/ceiling, next owner/time, retained costs/effects. |
| `RECOVERING` | Authoritative state and interrupted operations are being validated/reconciled. | Failure boundary, ownership version/equivalent stale-owner proof, integrity/readback results, safe exit. |
| `BLOCKED` | Safe progress cannot continue without a named condition or authority change. | Blocker, owner, attempted safe alternatives, unblock predicate, timeout/escalation. |

`BLOCKED`, a wait, `PAUSING`, `PAUSED`, `STOPPING`, `RETRYING`, and `RECOVERING` qualify a preserved/suspended work phase; they do not overwrite it. A wait can coexist with pause, and an answer/approval received while paused is recorded but launches no work until authorized resume. `DELEGATING` and `WAITING_FOR_AGENT` are unreachable v0.1 states and remain FUTURE_COMPATIBILITY because visible multi-agent delegation is out of scope.

### 4.3 Attempt dispositions and verification verdicts

| Disposition | Meaning | Completion credit |
|---|---|---|
| `COMPLETED` | The common completion gate and every applicable task predicate passed on the exact reviewed revision, with independent verdict `PASSED`. | Full only for that revision. |
| `PARTIALLY_COMPLETED` | The attempt is intentionally terminally closed with useful requested output and at least one unmet required predicate. It is not used while a wait/block remains resumable and does not replace user-stop `CANCELLED`. | None as completed work. |
| `FAILED` | The attempt cannot continue under its current contract after a terminal failure, exhausted authorized recovery, or hard-boundary violation. | None. |
| `CANCELLED` | User or policy ended the attempt; completed effects are preserved, not implicitly rolled back. | None. |
| `SUPERSEDED` | A materially different authorized task/attempt replaced this one with an explicit link. | None for the superseded attempt. |

Verification status is `UNVERIFIED`, `IN_PROGRESS`, or `FINISHED`. A finished verification has exactly one verdict: `PASSED`, `CHANGES_REQUIRED`, `BLOCKED`, or `INCONCLUSIVE`; before it is finished the verdict is absent. `verification.BLOCKED` is distinct from a task blocker, though it normally creates one. A `CHANGES_REQUIRED` verdict closes the reviewed attempt as `SUPERSEDED` with cause `CHANGES_REQUIRED` and creates a linked unverified correction attempt; it does not erase the reviewed result. `BLOCKED` or `INCONCLUSIVE` leaves the attempt noncomplete.

### 4.4 Legal transition rules

The nominal path is:

```text
CREATED → READY → QUEUED → CLAIMED → ANALYZING → PLANNING
→ READY_TO_EXECUTE → EXECUTING ↔ OBSERVING
→ READY_FOR_VERIFICATION → VERIFYING
→ COMPLETED only with independent PASSED verdict
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

A terminal disposition is immutable. Further work creates a linked successor or explicit reopen attempt. Any post-verification material mutation creates a new unverified revision while preserving the old verdict.

The complete semantic transition families are below. A destination that is a wait/control/block qualifier updates that axis while preserving the suspended work phase; a destination that is a disposition closes the attempt.

| From | To | Authorized actor | Preconditions, persisted effect, and recovery |
|---|---|---|---|
| `CREATED` | `READY` | Runtime/controller under admitted user request | Eligibility, authority, scope, limits, initial predicates, repository reference, and zero unauthorized effects validate; persist admission version. |
| `CREATED` | `WAITING_FOR_USER` / `BLOCKED` / `FAILED` / `CANCELLED` | Runtime/controller or user for cancel | Persist the precise ambiguity, missing authority, unsupported/hard denial, or cancel receipt and zero-effect evidence. Only the applicable wait/block path is resumable. |
| `READY` | phase `QUEUED` | Runtime/controller | Current user-admitted task contract validates; persist finite waiting bound and user-visible order without self-selecting other work. |
| `QUEUED` | phase `CLAIMED` | Runtime/controller | Exactly one eligible current owner is accepted under the current ownership version/equivalent stale-owner proof; rejected contenders persist no ownership mutation. |
| `CLAIMED` | phase `ANALYZING` | Current owner | Revalidate authority, repository/workspace identity, and ownership proof; start only authorized inspection. |
| `ANALYZING` | `PLANNING` | Current owner | Governing inputs and preflight evidence are sufficient; persist findings/unknowns and bounded plan work. |
| `PLANNING` | `READY_TO_EXECUTE` | Current owner | Current plan maps every material step to scope, capability, limits, and predicates; required workspace/preconditions validate. |
| Any applicable nonterminal phase | wait reason `WAITING_FOR_APPROVAL` | Current owner/controller | Preserve suspended phase and persist exact normalized consequential action; launch zero effect before valid receipt. Approval returns through current authorization and pre-dispatch validation; denial/expiry/revocation records zero dispatch and returns to safe replanning/wait/block/cancel. |
| `READY_TO_EXECUTE` | `EXECUTING` | Current owner | Operation-specific authorization and any required approval validate against current versions immediately before dispatch. |
| `EXECUTING` | `OBSERVING` | Current owner | Material operation reaches a known or explicitly uncertain boundary; persist results/effects before readback. |
| `OBSERVING` | `EXECUTING` | Current owner | Fresh evidence justifies another plan-authorized operation and all authority/bounds revalidate. |
| `OBSERVING` | `READY_FOR_VERIFICATION` | Author/current owner | Exact review revision and candidate bundle are fixed; author predicates/checks are fully recorded; no complete claim. |
| `READY_FOR_VERIFICATION` | `VERIFYING` | Independent verifier/controller | Verifier eligibility/independence, least privilege, evidence completeness, and exact reviewed revision validate. |
| `VERIFYING` | `COMPLETED` | Derived gate after independent verifier `PASSED` | The §11 conjunction is true; persist predicate results, verifier/revision, bundle revision, and final disposition as one recoverably consistent gate decision. |
| `VERIFYING` | old disposition `SUPERSEDED`; new phase `PLANNING` | Verifier returns `CHANGES_REQUIRED`; user/runtime admits correction attempt | Preserve old verdict/revision with cause; create linked correction attempt with new owner/plan/predicate versions, verification status `UNVERIFIED`, and no inherited approval. |
| `VERIFYING` | verification verdict `BLOCKED` / `INCONCLUSIVE` plus applicable task blocker | Independent verifier/controller | Persist failed/unassessed predicates, owner/unblock action, verification status `FINISHED`, and no completion credit. |
| Any nonterminal work phase | `WAITING_FOR_USER` / `WAITING_FOR_EXTERNAL_EVENT` | Current owner/controller | Persist exact wait reason, response/event correlation, timeout and safe continuation; no work outside current safe boundary. Resume returns only to the recorded legal phase after full revalidation. |
| Any active work phase | `PAUSING` | User or applicable hard policy | Persist request before acknowledgement; launch no new productive/task-advancing operation under suspended authority; classify in-flight work and allow only the separately bounded control/safety reserve. |
| `PAUSING` | control `PAUSED` | Runtime/controller | No productive/task-advancing or pre-pause in-flight operation remains actively running: each is terminal, safely checkpointed/cancelled, or classified `OUTCOME_UNCERTAIN`; separately authorized bounded safety/readback reconciliation may coexist with pause. |
| `PAUSED` | recorded resumable phase or `RECOVERING` | User or applicable policy | Authorized resume plus §6.5 revalidation; use `RECOVERING` whenever state/effect certainty is insufficient. |
| Any nonterminal work/wait/control phase | control `STOPPING` | User or applicable hard policy | Persist stop before acknowledgement; launch no new productive/task-advancing work under superseded authority after its accepted order; cancel/settle/classify every operation and preserve partial artifacts using only the separately bounded control/safety reserve. |
| `STOPPING` | disposition `CANCELLED` | Runtime/controller after bounded reconciliation | Preserve termination reason, partial-result facts, verification status, failures, and effect certainty separately. If bounded reconciliation cannot finish, `STOPPING` coexists with `BLOCKED`/`RECOVERING`; work cessation alone is never completion. |
| Any active work phase | `RETRYING` | Runtime/controller | Failure is retryable, inside predeclared ceiling/budget, and safe for the exact effect; retain original attempt and cost. |
| `RETRYING` | prior legal phase / `BLOCKED` / `FAILED` | Runtime/controller | Revalidate before attempt; success returns to the appropriate phase, while exhaustion/unsafe retry yields explicit block/failure. |
| Any nonterminal phase after interruption/integrity doubt | `RECOVERING` | Runtime/controller | Persist recovery ownership; prevent stale writes/effects; perform §7 validation and reconciliation before work. |
| `RECOVERING` | prior legal phase / wait / `PAUSED` / `BLOCKED` / `FAILED` / `CANCELLED` | Runtime/controller | Exit reflects current controls, authority, state integrity, and operation certainty; never infer completion. |
| Any nonterminal phase | `BLOCKED` | Current owner/controller or verifier | Persist blocker, owner, alternatives, unblock predicate, timeout/escalation, preserved work/effects. |
| `BLOCKED` | recorded legal phase or `RECOVERING` | Authorized user/event/controller | Named unblock predicate is satisfied and all material state revalidates; otherwise remain blocked. |
| Any nonterminal phase | disposition `PARTIALLY_COMPLETED` / `FAILED` | Runtime/controller under declared terminal predicate/failure rule | Use partial only for an intentional terminal close with useful output and no active resumable wait; reconcile effects, preserve artifacts, record failed/missing predicates and next action; zero completion credit. |
| Any nonterminal phase | `SUPERSEDED` | User-authorized material redirect/controller | Preserve original contract/evidence, link successor task/attempt, invalidate changed approvals/verdicts, and perform no silent scope transfer. |
| Any terminal disposition | no in-place exit | None | Correction/continuation creates a linked successor/reopen attempt; terminal history remains immutable. |

## 5. Agent lifecycle

Agent identity and operational availability MUST be separate from product-task, worker, model, role, and client lifecycle.

### 5.1 Durable identity state

| State | Meaning |
|---|---|
| `REGISTERED` | Stable named identity exists. |
| `ENABLED` | Identity may accept eligible work under policy. |
| `DISABLED` | Identity accepts no new work; in v0.1 active tasks are safely paused or cancelled and ownership is released only after reconciliation. No other visible agent is selected. |
| `RETIRED` | Identity no longer operates; history and evidence remain addressable. Retirement is explicit and does not delete tasks. |

### 5.2 Operational availability

| State | Meaning |
|---|---|
| `OFFLINE` | No eligible runtime/worker is available; agent identity and tasks remain durable. Client-only disconnection does not make the agent offline while a healthy owner continues. |
| `IDLE` | Enabled and owns no active execution. |
| `BUSY` | Owns one active task/attempt under one current ownership version or equivalent stale-owner proof. |
| `WAITING` | Owned task awaits a named input, approval, or event. |
| `PAUSED` | Agent/task control prevents new material work. |
| `RECOVERING` | New or returning owner is reconciling durable state. |
| `DEGRADED` | A bounded capability is unavailable; limitations and eligible work are explicit. |
| `STOPPED` | Runtime work has stopped, but identity and task history persist. |

v0.1 exposes one persistent agent and at most one current execution owner per task. Logical author/verifier roles and model calls do not become additional persistent user-visible agents. An already user-admitted task may wait in `QUEUED` only under a finite declared bound and visible order; v0.1 does not self-discover or self-select a continuous/autonomous queue. The user may cancel or redirect a queued task, and queue saturation rejects or waits visibly. “Stop task,” “pause agent,” “disable agent,” “worker stopped,” and “client disconnected” are distinct controls/events.

Agent identity survives model replacement, process or worker restart, client closure, repository change, and task completion. A worker loss changes availability and moves affected tasks to recovery; it never deletes the agent or implies task completion.

Legal agent transitions are:

| From | To | Actor and gate |
|---|---|---|
| `REGISTERED` | `ENABLED` | User/governance enables the durable identity under current policy. |
| `ENABLED` | `DISABLED` | User or hard policy prevents new claims and durably reconciles current work; disabling does not delete tasks. |
| `DISABLED` | `ENABLED` | Authorized user action after policy, credentials, limits, and affected task state revalidate. |
| `REGISTERED` / `ENABLED` / `DISABLED` | `RETIRED` | Explicit authorized retirement; active tasks are first safely paused/cancelled, ownership is released, and history remains. |
| `OFFLINE` / `STOPPED` | `RECOVERING` | A worker returns and validates identity, policy, ownership, and tasks before availability. |
| `RECOVERING` | `IDLE` / `BUSY` / `WAITING` / `PAUSED` / `DEGRADED` | Authoritative task ownership and capability state determine the truthful projection. |
| `IDLE` | `BUSY` | An eligible user-admitted product task is claimed under one current ownership version/equivalent stale-owner proof. |
| `BUSY` | `WAITING` / `PAUSED` / `RECOVERING` / `DEGRADED` | The corresponding task/control/capability record is durable; agent state alone does not change task truth. |
| `WAITING` / `PAUSED` / `DEGRADED` | `BUSY` | Named resume/unblock and full revalidation succeed for the currently owned task. |
| `BUSY` / `WAITING` / `PAUSED` / `DEGRADED` | `IDLE` | Current task reaches a reconciled terminal/ownership-release point and no other task is silently claimed. |
| Any operational availability except `STOPPED` | `OFFLINE` | Eligible worker/runtime loss; durable identity/tasks remain and affected active tasks enter recovery. A client-only disconnect changes presentation connectivity only. |
| Any operational availability except `OFFLINE` | `STOPPED` | Explicit authorized runtime stop; no new task is claimed, active work follows stop/pause reconciliation, and restart enters `RECOVERING`. |

Every agent transition inherits the mutation fields and stale/duplicate/recovery rules in §§3.3 and 4.4. Agent pause stops new claims and applies the declared pause policy to its active task; disable stops new claims and requires an explicit pause-or-cancel choice for active work; retirement is terminal for identity operation but never deletes history.

### 5.3 Bounded-autonomy limits

Execution authority ends at the current user-admitted task contract and plan. The product MUST NOT self-create or self-select a new task, delegate to another visible agent, recursively turn an observation into authorized work, expand paths/capabilities/network/credentials/budgets/effects, weaken predicates, or exceed declared time, cost, output, tool-call, and retry ceilings. An authenticated task amendment may change admitted authority; a separate exact approval is still required for any consequential action. Ceiling exhaustion launches no new productive work and yields the narrowest truthful wait, block, or noncomplete result, except for a separately preauthorized bounded cancellation/readback/evidence/safety reserve.

## 6. Pause, stop, redirect, and resume

### 6.1 Operation/effect lifecycle

Every material operation has a stable identity and separate status/outcome:

```text
PROPOSED → operation.WAITING_FOR_APPROVAL (when required) → AUTHORIZED
→ DISPATCHED → RUNNING → RECONCILING (when needed)
→ terminal outcome
```

Terminal operation outcomes are `KNOWN_NOT_STARTED`, `KNOWN_SUCCEEDED`, `KNOWN_FAILED`, `CANCELLED`, or `OUTCOME_UNCERTAIN`. They are not attempt dispositions. Approval authorizes an attempt but does not establish success. A consequential `KNOWN_SUCCEEDED` outcome requires the declared authoritative readback when observable.

| From | To | Actor, precondition, persisted result, and recovery |
|---|---|---|
| `PROPOSED` | `AUTHORIZED` | Controller validates exact current authority; no separate approval is required; persist normalized operation and bounds. |
| `PROPOSED` | operation `WAITING_FOR_APPROVAL` | Controller persists exact inspectable approval request and zero-dispatch fact; task wait reason references it without erasing suspended phase. |
| operation `WAITING_FOR_APPROVAL` | `AUTHORIZED` | Authenticated current approval exactly matches; authorization is independently revalidated. |
| `PROPOSED` / `WAITING_FOR_APPROVAL` / `AUTHORIZED` | terminal `KNOWN_NOT_STARTED` | Denial, expiry, revocation, stop, redirect, invalidation, or cancellation occurs before dispatch; persist reason and zero-dispatch evidence. |
| `AUTHORIZED` | `DISPATCHED` | Immediately revalidate task/policy/tool/approval/target/current ownership; persist dispatch intent before or with the declared recoverable boundary. |
| `DISPATCHED` | `RUNNING` / `RECONCILING` / terminal outcome | Correlated provider/tool evidence establishes start, known non-start, or uncertainty; response loss never implies non-effect. |
| `RUNNING` | terminal `KNOWN_SUCCEEDED` / `KNOWN_FAILED` / `CANCELLED` | Declared terminal oracle validates; persist bounded result/effect/receipt and required readback. |
| `RUNNING` / `DISPATCHED` | `RECONCILING` | Cancellation, timeout, crash, invalid/mismatched result, lost response, or uncertain effect requires receipt/idempotency/readback analysis; no blind replay. |
| `RECONCILING` | any terminal operation outcome | Authoritative evidence establishes the narrowest truthful outcome; unresolved consequential uncertainty remains `OUTCOME_UNCERTAIN` and blocks replay/completion. |

Approval denial/expiry/revocation and cancellation before dispatch are idempotent zero-effect terminal results. Cancellation after dispatch is a request, not an outcome, until reconciliation. Duplicate or stale transition attempts are rejected and recorded under §3.3. Recovery never converts an operation outcome into a task disposition without evaluating the task predicates.

### 6.2 Pause

The product MUST persist `PAUSE_REQUESTED` before acknowledging acceptance, stop launching any productive or task-advancing operation under suspended authority ordered after that acceptance, and classify every in-flight operation. Interruptible work is safely cancelled or checkpointed; an unsafe-to-interrupt operation may settle only within its predeclared boundary. The control remains `PAUSING` while productive work is actively running. `PAUSED` becomes effective only when every such operation is terminal, safely checkpointed/cancelled, or classified `OUTCOME_UNCERTAIN`; separately authorized bounded safety/cancellation/readback/evidence/reconciliation operations may then coexist with pause.

The user sees requested time, effective time, preserved work, current operation state, and every effect that landed after the request. Pause promises neither rollback nor immediate process termination.

### 6.3 Stop or cancel

The product MUST persist `STOP_REQUESTED`, enter control `STOPPING`, launch no productive or task-advancing operation under superseded authority ordered after acceptance, best-effort cancel interruptible operations, reconcile dispatched effects, preserve partial outputs, and invalidate stale approvals/owners as policy requires. Only separately authorized bounded cancellation/readback/evidence/cleanup/safety operations may start. Once every material operation has a terminal or explicit uncertain classification, the attempt disposition is `CANCELLED`; result-completeness facts, existing verifier result/revision, current verification status, blockers/failures, and effect certainty remain separate. A material stop mutation invalidates any verdict for the changed revision but does not erase the prior verdict. If bounded reconciliation cannot finish, `STOPPING` coexists with `BLOCKED` or `RECOVERING` until the narrowest truthful classification is possible. Work cessation never maps to `COMPLETED`, and completed effects are never represented as rolled back without authoritative readback.

### 6.4 Redirect

A redirect is ordered against the current task version. The product quiesces incompatible work and records the old and new request, plan, predicate, and authority versions. An in-scope clarification may revise the current task; a scope, path, capability, credential, spend, network, external-effect, or outcome expansion first requires an authenticated versioned task-authorization amendment. If the resulting exact action is consequential, it then requires a separate approval receipt. One-shot action approval alone cannot add a capability/root/provider or rewrite the task contract. A materially different outcome creates a linked `SUPERSEDED` task/attempt rather than silently mutating history.

Redirect invalidates any approval, operation, artifact, check, or verification whose bound material changed. Prior valid work and evidence remain preserved. A redirect cannot weaken a failed predicate after the fact without recording a new contract and leaving the prior attempt noncomplete.

### 6.5 Resume

Resume is permitted only from a resumable paused/waiting/blocked condition by an authorized actor or correlated response/event. A `WAITING_FOR_EXTERNAL_EVENT` response must be authenticated or authoritatively read back, correlate to the current wait identity/version, reject stale/duplicate events, honor the recorded timeout, and return only to the suspended legal phase after the checks below. Before new work, the product revalidates:

- task, request, plan, predicate, policy, schema, and capability versions;
- current ownership version or equivalent stale-owner proof and absence of stale writers;
- repository identity, base/head, branch/ref, workspace, dirty state, and concurrent user changes;
- credentials, network/data policy, budgets, limits, and tool availability;
- approval validity, expiry, use count, revocation, and exact action binding;
- every incomplete or uncertain operation by receipt and authoritative readback.

`CANCELLED`, `FAILED`, `SUPERSEDED`, or terminal `COMPLETED` work requires an explicit linked successor/reopen attempt. Stop has precedence over stale resume or approval. Concurrent controls use deterministic causal/version ordering; losing and duplicate commands remain visible rather than disappearing.

## 7. Restart and recovery

Client disappearance does not pause, stop, or complete a task and does not make a healthy execution owner recover. Reconnect reconstructs only the presentation view from authoritative state rather than from client transcript memory.

After supported orchestrator or worker loss, affected nonterminal tasks enter `RECOVERING` before execution. A client restart joins this recovery only when it also caused owner/runtime loss. Recovery MUST validate:

1. record schema, integrity, causal order, and latest acknowledged versions;
2. task, plan, predicates, policy, approvals, limits, budgets, and current ownership version/equivalent stale-owner proof;
3. repository/workspace identity, base/head/dirty state, concurrent changes, and artifacts;
4. checkpoints or other recovery evidence without assuming a specific mechanism;
5. each interrupted operation's identity, dispatch state, idempotency/reconciliation rule, receipt, and readback;
6. provider, tool, environment, credential, network, and data-policy availability without hidden fallback.

Interrupted operations are classified `KNOWN_NOT_STARTED`, `KNOWN_SUCCEEDED`, `KNOWN_FAILED`, `CANCELLED`, or `OUTCOME_UNCERTAIN`. Consequential uncertainty blocks blind replay and `COMPLETED` until authoritative reconciliation or explicit noncomplete escalation. A new owner may continue only after stale-owner state writes and effects are prevented.

`PAUSED`, waiting, `STOPPING`, `CANCELLED`, and `SUPERSEDED` tasks do not auto-resume. A recovered `STOPPING` task continues stop reconciliation before any other work. Corrupt, malformed, incompatible, or incomplete authority/evidence is preserved and isolated from use; any salvage is itemized and independently checked. Unsafe recovery becomes `BLOCKED` or `FAILED`, never silent reset.

Required fault evidence injects interruption at every declared acknowledgement and material-effect boundary and proves: zero lost acknowledged mutations, zero accepted stale writes, zero unintended duplicate consequential effects, no authority amplification, and one explicit outcome for every operation. Device or media loss beyond a declared v0.1 persistence boundary remains an explicit unknown/non-guarantee until E2 and E5 define and test it.

## 8. Repository, workspace, and capability contract

### 8.1 Repository and workspace invariants

Before mutation, the product MUST record repository identity, observed base revision/tree, branch/ref, head, dirty and untracked state, relevant nested repository/submodule facts, governing instructions, workspace identity, and allowed/excluded paths. Pre-existing user changes remain user-owned.

Task work MUST occur in an identified isolated workspace or an E2-selected equivalent that objectively proves non-interference. The product MUST:

- prevent task work from overwriting, deleting, staging, committing, or silently including unrelated user changes;
- reauthorize the effective target at operation time and again during cleanup;
- detect concurrent user or task changes and fail or reconcile visibly rather than silently merge/overwrite;
- reread final repository state, changed-file inventory, base/head/dirty facts, and review package after the last mutation;
- bind every artifact, command, test, diff, and verification verdict to the exact workspace and revision;
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

The contract distinguishes:

1. local inspection (`status`, `diff`, declared history/ref inspection);
2. task-authorized isolated preparation (workspace, branch, patch, bounded local commit, draft-PR package);
3. destructive/history-changing actions;
4. remote or externally consequential actions.

Local preparation is allowed only when admitted by the task contract. Existing-branch deletion, amend/rebase/history rewrite, reset/clean of user material, force update, remote push, external PR/issue mutation, merge, deploy, publish, and release require their stricter authority; consequential actions require one-shot human approval and readback.

Repository/local/global Git configuration, aliases, hooks, credential helpers, text-conversion or external-diff drivers, clean/smudge or large-file filters, submodules, signing helpers, filesystem monitors, and SSH/transport commands are untrusted executable surfaces. A Git permission does not implicitly authorize those surfaces, network, or credentials. Tests MUST show no unapproved ref movement, helper execution, secret access, or remote effect.

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

Both requests and results are runtime-validated. A malformed, oversized, duplicated, unknown, stale, incompatible, adversarial, or ambiguously normalized request/contract/target, or a schema change after approval, MUST fail before dispatch. An invalid, mismatched, or oversized result MUST fail before consumption or any downstream operation; because the dispatched capability may already have acted, its effect becomes `OUTCOME_UNCERTAIN` until receipt/readback reconciliation. Best-effort repair may not widen authority, change targets/effect class, fabricate semantics, conceal provider/tool loss, or claim that invalid output proves zero effect.

Dynamically discovered tools or servers are non-executable until admitted by trusted policy. Tool names, descriptions, schemas supplied only by an untrusted server, model classification, prompt content, and caller Booleans do not grant permission. E2 chooses the capability topology.

### 9.2 Action/effect classes

The following vocabulary is a **DESIGN_PROPOSAL** for challenge; equivalent E2 names are allowed only if these boundaries remain testable:

| Class | Boundary |
|---|---|
| `LOCAL_INSPECTION` | Read admitted repository/workspace data without code execution, secret use, or network. |
| `ISOLATED_LOCAL_MUTATION` | Reversible edits and review-package preparation within admitted paths. |
| `UNTRUSTED_CODE_EXECUTION` | Terminal, tests, builds, generators, packages, and descendants under hard bounds. |
| `EXTERNAL_READ` | Network/API/model read request; still an egress, data-policy, credential, budget, and provenance event. |
| `EXTERNAL_MUTATION` | Remote Git, PR/issue, deploy, publish, release, message, purchase, or other external state change. |
| `PRIVILEGED_OR_DESTRUCTIVE` | Privileged credential, system/global mutation, irreversible or difficult-to-recover deletion/history change. |
| `GOVERNANCE_PROHIBITED` | Self-expanding authority or architecture, security, release, stage, or autonomous-build gate mutation by ordinary product execution. |

Task admission may authorize bounded local inspection, isolated mutation, checks, and review-package generation. Network, dependency acquisition/execution, named credential use, and other added-risk actions require explicit task grants and any policy-required approval. An optional supported external mutation, privileged credential, destructive/global action, or spend within admitted authority but at or above a declared approval threshold requires one-shot human approval; scope, egress, capability, credential, or budget expansion first requires an authenticated task amendment and then any applicable approval. None is required for the v0.1 core local-review outcome. `GOVERNANCE_PROHIBITED` actions cannot be enabled by ordinary runtime approval; they require a separately authorized governance task/decision.

### 9.3 Network and provider egress

Network is deny-by-default for agent tools and every descendant process. A grant binds protocol, normalized destination/port and material path/method, purpose, data class, credential identity/scope, limits, expiry, task, and operation. Loopback, private, link-local, metadata, local socket, proxy, and redirect targets are not implicitly trusted.

Every connection and redirect MUST re-resolve and reauthorize its effective target. DNS rebinding, redirect substitution, proxy bypass, TLS/authentication downgrade, and cross-target credential forwarding fail closed. Repository content may leave the workspace only under an approved data classification and provider/account/region/retention/training policy. A read-only web or model request can disclose data and incur cost and therefore remains an accountable external operation.

### 9.4 Approval request, receipt, and consumption

Approval is a durable authenticated policy decision, never inferred from conversational wording, repository text, prompt instructions, tool output, UI availability, regex, model review, tests, a tool name, or `confirmed: true`.

The human-visible request and executable normalized action MUST derive from the same authoritative representation. Untrusted target/action/content is rendered inert, escaped and visually separated from trusted actor/policy/risk fields; bidirectional/control characters, markup, terminal escapes, leading options, and truncation cannot conceal the effective target or effect. Every material input must be fully inspectable before decision, either inline or through an immutable content reference whose full bytes are accessible from the approval surface and whose digest binds those bytes. A digest alone cannot authorize. The representation binds:

- actor/user, task, attempt, operation, capability/schema version, and effect class;
- normalized action and every material argument;
- exact target/resource/ref and before-state preconditions;
- credential identity/scope without its value, network/data/budget scope, and policy/version;
- issue/expiry time, one-shot or explicit count limit, revocation rule, and decision/outcome.

Mutation, substitution, policy/capability/schema/base-state change, expiry, revocation, replay, duplicate consumption, stale worker, or widened batch invalidates approval. One-shot is the default. A narrower user decision creates and re-presents a newly normalized action before consumption; it does not mutate or consume the original unchanged. A standing grant, if supported, MUST expose exact action/resource/count/time/budget ceilings and remaining/revocable scope and cannot cover materially different future actions.

Refusal, timeout, revocation, pause, redirect, cancellation, stale ownership, and task-scope change are persisted and reconciled before dispatch. If already dispatched, the operation is cancelled where safe and read back. Approval permits an attempt; execution receipt plus authoritative terminal readback establishes the known effect. The verifier cannot reuse author approval or credentials for a new consequential effect.

### 9.5 Consequential external actions

The following require exact human approval when an optional capability is separately admitted and supported: remote branch/commit push; PR or issue create/edit/comment/merge/close; deploy/publish/release; message/contact; purchase or paid use within admitted authority that crosses a declared approval threshold; privileged credential use; remote deletion or force update; destructive/global/system mutation; and any difficult-to-recover external state change. Spend beyond the admitted budget first requires an authenticated task/budget amendment and then any applicable approval. None is required to satisfy the v0.1 core local-review workflow.

Every consequential operation MUST have stable identity, declared replay/idempotency or reconciliation semantics, execution receipt, and authoritative readback method. On timeout or response loss, the product reads external state before retry; it never blindly repeats a non-idempotent or uncertain effect. A changed action may require fresh approval. Partial/wrong/unreadable external state records the truthful operation outcome and prevents completion; the attempt disposition, task blocker, and verification status remain separate axes.

Unsupported capabilities report typed failure `UNSUPPORTED_CAPABILITY`, perform no effect, and separately select the truthful task qualifier/disposition. Producing a local draft-PR package cannot be described as opening an external PR.

### 9.6 Secret handling

Raw secrets MUST NOT enter ordinary chat, model context, repository source, task summaries, tool descriptions, approval text, general/inherited environment, general logs or telemetry, shell history/command text, process arguments/listings, screenshots, crash/core data, diffs, fixtures, caches, artifacts, or evidence bundles. Secrets are referenced only by stable identity and scope. An authorized operation may receive/use a raw value only through an E2-selected protected recipient boundary, for the exact capability, endpoint/resource, task/operation, use count, and minimum duration; this is the only test exception, descendants cannot inherit it, and the raw value is never returned to the model, UI, or general tool output.

Human secret acquisition MUST use a protected path distinct from conversation and repository files. During protected entry, agent/model/tool observation and capture of keystrokes, clipboard, screen/screenshot, accessibility state, terminal stream, and the secret value stop; only a non-secret outcome/receipt returns, followed by full resume revalidation. Secret files and account/operating-system credential locations are denied by default. Unavoidable absence of such a protected boundary yields `WAITING_FOR_USER` or `BLOCKED`; conversational approval cannot authorize raw reveal.

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
| Verification/evidence | predicate failure, missing/stale/cross-task evidence, revision mismatch, independence failure, false completion. |
| Clean room/security | unauthorized effect/read, forbidden artifact, private/external code, provenance/license or hard-boundary violation. |
| Unknown layer | accountable layer cannot safely be established; the uncertainty remains explicit and cannot be credited as success. |

Exact error codes and registry representation remain E2 decisions; external reconstructed error names/counts are not imported.

### 10.3 Retry and status rules

Retries require a predeclared ceiling and safe eligibility for the exact failure/effect class. Each attempt, failure, delay, cost, output, and effect remains visible. Authorization/policy denial, invalid/malicious schema, secret or hard-boundary violation, stale approval, non-idempotent uncertain effect, exhausted budget, and known terminal failure do not auto-retry.

`WAITING_*` names one expected input/approval/event. `BLOCKED` names an unblock predicate and owner. `PAUSED` is user control. `RETRYING` is bounded recovery. `PARTIALLY_COMPLETED` is an intentional terminal disposition preserving useful output with zero completed credit. `FAILED` is terminal for the attempt. `CANCELLED` records stop/cancel. Verification status `UNVERIFIED` means independent verification has not passed. These facts remain axis-qualified and none may be projected or summarized as `COMPLETED`.

## 11. Completion predicates and independent verification

### 11.1 Common completion gate

`COMPLETED` is a derived result only when this conjunction is true:

```text
every applicable required predicate PASS on the exact reviewed revision
AND independent verification verdict is PASSED
AND evidence-bundle schema and semantic validation PASS
AND repository/artifact/effect state was freshly reread where required
AND every performed consequential effect matches current authority and approval
AND zero material effect is OUTCOME_UNCERTAIN
AND every success-required effect is authoritatively KNOWN_SUCCEEDED with required readback
AND every other material effect has a known terminal outcome
    (KNOWN_NOT_STARTED, KNOWN_SUCCEEDED, KNOWN_FAILED, or CANCELLED) consistent with predicates
AND every material operation has a terminal outcome and is accounted consistently with close
AND no current wait reason, control condition, blocker, or pending approval/question/event remains
AND every accepted pause was explicitly resumed/released
AND every accepted stop resolves the attempt only to CANCELLED
AND every redirect is verified against its current revision
AND no unresolved required failure, skipped check, blocker, completion-blocking limitation,
    security violation, secret/provenance violation, or stale/missing evidence remains
```

Executor/model prose, a transcript/activity signal, client closure, plan exhaustion, a diff, one passing test, tool success, approval, receipt, manifest, digest, score, or sole-author assertion cannot satisfy this gate alone.

Any author/model/tool `COMPLETED` assertion is evaluated and retained. If the gate rejects it before it becomes authoritative, record `UNSUPPORTED_COMPLETION_ASSERTION`; that is correct defensive behavior and a measured event, not a failed scenario. If a projection or durable disposition actually admits `COMPLETED` while the conjunction is false, record `FALSE_TERMINAL_COMPLETION`; this is the zero-tolerance hard failure that cannot be averaged away. Missing/stale evidence, required-check skip/failure, revision mismatch, author-only proof, mock-only evidence for a real task, unapproved effect, unknown outcome, or contradictory readback MUST prevent the authoritative terminal transition.

### 11.2 Task-type predicates

All task types inherit the common gate and add the following predicates:

| Task type | Required operational predicates |
|---|---|
| `BOUNDED_CODE_CHANGE` | Requested observable behavior exists; allowed files contain intended change; diff is scoped and excludes unrelated work; declared build/lint/type/security/domain/tests pass or unmet results prevent completion; repository is reread; artifacts are inspectable. |
| `DEFECT_REPRODUCTION_AND_FIX` | Reported failure or a predeclared alternative failing oracle demonstrates the defect before the fix; fix is bounded; the same relevant oracle demonstrates before/after regression protection; specified negative and affected checks pass; no unrelated diff. Mere inability/contradiction cannot complete this class and requires redirect/reclassification to diagnosis or another honest noncomplete outcome. |
| `REPOSITORY_DIAGNOSIS_OR_REVIEW` | Exact inputs/scope/revision are enumerated; material claims cite authoritative evidence; fact, inference, proposal, and unknown are separated; commands are reproducible; no unauthorized mutation; limitations and unanswered questions remain explicit. |
| `DOCUMENTATION_OR_REPOSITORY_METADATA_CHANGE` | Artifact exists and opens/parses/renders as declared; required sections/fields/traceability exist; sources and cross-file terminology reconcile; exact config/status behavior validates; no premature governance or release gate changes. |
| `NO_CHANGE_REQUIRED` | Fresh current-state readback satisfies every predicate; zero unintended diff/effect exists; independent verifier confirms the no-op against the exact state. |
| Approved external effect, when a task explicitly supports one | Exact approval matches payload/target/policy; stable receipt exists; fresh authoritative target readback matches expected state; duplicate absence or reconciliation is proven. |

Mixed tasks use the conjunction of all applicable predicates. Optional or not-applicable criteria must be predeclared with an objective reason. Every limitation records affected scope/predicate, evidence, owner, and completion consequence. An unresolved required, supported-case, or security limitation blocks completion; an explicit out-of-scope or nonblocking preview limitation remains visible but does not itself prevent an otherwise valid completion. Post-failure scope reduction is a visible redirect/new predicate version and cannot relabel the earlier attempt successful.

### 11.3 Independent verification

The author may run self-checks and propose `READY_FOR_VERIFICATION`; only an eligible independent path may produce a verification verdict. Independence requires:

- a separate accountable verifier identity/path from the sole author for consequential or high-risk work;
- the exact task contract, authority/policy versions, review revision, diff/artifacts, operations, predicates, and candidate evidence bundle as inputs;
- independent repository/artifact/effect readback and reproduction of deterministic checks where applicable; verifier-generated build/test outputs are isolated or declared and MUST NOT mutate the review revision/package;
- least privilege; author approvals or credentials cannot authorize verifier-created effects;
- predicate-by-predicate `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, or `INCONCLUSIVE` results with evidence;
- retention of disagreements, failures, and changes-required results.

If verification mutates the review revision/package or observes a material concurrent mutation, it stops, records the new state as unverified, and cannot issue `PASSED` for that state. Provider/model diversity alone neither proves nor is required for independence. E3 later determines eligible role occupants; E1 selects none. High-risk work cannot be verified by its sole author. Human review or action approval does not substitute for a technical verification verdict, and a technical verdict does not authorize merge, release, or external effect.

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
| `work_phase` | enumerated phase, 0..1 | Nonterminal profiles; terminal bundle retains last phase. |
| `wait_reasons` | list of enumerated values, 0..many | When present / authoritative wait records. |
| `control_condition` | enumerated value, 0..1 | When present / pause/stop/recovery control record. |
| `blocker_refs` | blocker references, 0..many | When present / authoritative blocker records. |
| `attempt_disposition` | enumerated disposition, 0..1 | Terminal profiles; absent while attempt open. |
| `verification_status` | `UNVERIFIED`/`IN_PROGRESS`/`FINISHED`, exactly 1 after acceptance | Accepted-task profiles / verification authority. |
| `verification_verdict` | enumerated finished verdict, 0..1 | Exactly 1 only when verification status is `FINISHED`. |
| `agent_availability_ref` | versioned reference, 0..1 | Accepted task / agent authority; never substitutes for task status. |
| `operation_outcome_refs` | operation references, 0..many | As operations exist / execution-effect authority. |
| `repository_ref` | repository identity object, 0..1 | Repository task profiles / preflight and fresh reread. |
| `workspace_ref` | workspace identity object, 0..1 | Once workspace exists / workspace authority. |
| `review_revision_ref` | immutable revision/package reference, 0..1 | Candidate and completed profiles. |
| `authority_refs` | versioned references, 1..many after acceptance | Task/policy/principal/tool-contract authority. |
| `plan_ref` | versioned reference, 0..1 | After planning. |
| `predicate_results` | predicate result objects, 0..many | Candidate/completed and applicable noncomplete profiles. |
| `section_refs` | typed evidence-section references, 0..many | As evidence sections exist; all refs resolve within allowed task/profile. |
| `persistence_boundary` | bounded support object, exactly 1 after acceptance | Declared client/orchestrator/worker/device/media failure classes, exclusions, acknowledgement point, recovery-point objective, recovery oracle, and candidate configuration identity. |
| `final_validation_ref` | validation-attestation reference, 0..1 | Exactly 1 for completed; applicable candidate/noncomplete bundle failures. |

Every nested object/list item also declares a stable ID, contract/version, logical type, allowed enum/domain, cardinality, conditional profile, maximum bound or referenced bounded artifact, authoritative source/version, and reference target. Unknown extension fields require an admitted namespace and cannot change core semantics.

A new task/plan/predicate/policy/repository/configuration/schema/review revision produces a new preserved bundle revision when it changes the meaning of evidence. Old evidence remains attached only to the state it proves and carries an explicit stale/superseded rule.

### 12.2 Required logical sections

| Section | Required content or references |
|---|---|
| Authority and request | Original request identity/content or safe authoritative reference; user/principal; admitted governing inputs and precedence; dependencies; task class; allowed/forbidden scope; paths; capabilities; data/network/credential/effect limits; budgets; policy and authorization references. |
| Repository/workspace | Repository identity; base revision/tree; workspace identity/profile; initial branch/head/dirty/untracked state; separately identified pre-existing changes; final branch/head/dirty state and reread time. |
| Plan and predicates | Plan identity/version/amendments; each predicate's identity, applicability, oracle, mandatory status, acceptance rule, evidence references, actual result, and unresolved reason; reproduction predicate or explicit applicability decision. |
| Inputs/provenance | Source/input identities, safe locations/references, trust and evidence labels, versions/dates, freshness/staleness and integrity facts where useful; fact/inference/proposal/unknown separation. |
| Change/review package | Created, modified, deleted, renamed, and protected-unchanged files; diff/patch identity and integrity; local branch/bounded commit/draft-PR package reference as applicable; prepared local package distinguished from actual external state. |
| Operations | Operation and attempt IDs; task authority, policy, plan and predicate versions; capability and input/output schema versions plus validation results; provider identities; effect class; secret-safe normalized arguments; working directory; start/end/time basis; bounds; cancellation; exit/signal/outcome; bounded output or artifact refs; idempotency/reconciliation; retry links; failure/effect refs. |
| Tests/checks | Check identity and type; exact secret-safe command/action; tool/version/configuration; reviewed revision; predicate mapping; result/exit; bounded output evidence; retries; skipped/not-applicable reason and consequence. |
| Provider/model/tool/environment | Requested and resolved provider/model/configuration, logical role, route/fallback reason, refusal/stop/error semantics, capability/tool/server and environment/dependency identities, usage/cost/latency when exposed, and explicit unknowns. |
| Approvals/effects/readbacks | Exact approval request/receipt binding; decision, denial/expiry/revocation/consumption; operation/effect receipt; before/after identity; authoritative readback; cancellation, duplicate, partial, or uncertain outcome. |
| Artifacts | Stable identity, kind, safe inspectable location/reference, owner/producer, lineage, reviewed revision, integrity fact, sensitivity, retention rule, regeneration trigger, stale rule, automation policy, and failure consequence. |
| Failures/recovery | Failure identity/class/layer/retryability/terminal metadata; all attempts and retained costs/effects; recovery/reconciliation/escalation; resulting state; blockers, uncertain effects, and next safe action. |
| Verification | Method, verifier identity and independence basis, immutable candidate-bundle and reviewed-revision references, predicate-by-predicate results and evidence refs, reproduced checks/readbacks, disagreements, verification status/verdict, corrective action. |
| Final disposition | Preserved work phase, wait/control/blocker tuple, attempt disposition, verification status/verdict, agent-availability reference, operation/effect outcomes, completed/unmet predicates, limitations with blocking consequence, unverified claims, remaining failures/blockers, out-of-scope observations, user review and human-approval requirements. |
| Final validation | Validator/rule-set/schema versions, exact final bundle revision and content identity, validation time, structural/type/bound/reference/semantic results, candidate/review-revision binding, failure refs, and attestation identity. |

### 12.3 Validation rules

A bundle is invalid if any applicable rule fails:

1. reject unsupported versions, malformed types, duplicate identities/keys, oversized fields, unknown non-namespaced fields, unsafe payloads, and unresolved or cross-task references;
2. reconcile repository identity, base/head/dirty state, changed-file inventory, diff/review package, and reviewed revision against fresh authoritative state;
3. never attribute pre-existing user changes to the task;
4. count a check as passing only on the reviewed revision under the declared configuration; retain skips, truncation, retries, and failures;
5. require a demonstrated reported or predeclared alternative pre-fix failing oracle for `DEFECT_REPRODUCTION_AND_FIX`; non-reproduction requires redirect/reclassification or a noncomplete profile;
6. require every consequential effect to link exact current authority, approval, operation, receipt, and readback; uncertainty prevents completion;
7. keep requested and resolved provider/model/tool/configuration identities separate and expose fallback as a separate attempt;
8. require every generated record/artifact to state its authoritative inputs, owner, what it proves and does not prove, regeneration trigger, stale detection, automation policy, and failure consequence;
9. exclude secrets, prohibited private data, forbidden external code/assets/copy, and unsafe sensitive paths/metadata; a digest aids byte integrity but proves neither authority, confidentiality, correctness, nor deletion;
10. bind the immutable candidate bundle, exact reviewed revision, finished verification result, exact final bundle revision, and final validation attestation consistently; any material mutation invalidates the verdict until re-verification;
11. require all applicable predicates and an independent `PASSED` verdict for `COMPLETED`; schema validity alone is insufficient.

Outcome-conditional missing fields MUST use an explicit `NOT_APPLICABLE`, `UNKNOWN`, `NOT_RUN`, or `UNAVAILABLE` value with reason and status consequence. Silent omission is invalid. Every required bundle revision must validate against its outcome profile; a completed bundle additionally has no unresolved mandatory field, reference, blocking limitation, effect, or check.

Bundle generation or validation failure creates a bounded `EVIDENCE_FAILURE`, preserves the underlying authoritative facts, supplies the next safe action, and prevents `COMPLETED`; it MUST NOT destroy or hide the task merely because its export/assembly failed.

## 13. Observability and context compaction

### 13.1 Authority separation

Operational telemetry and presentation views diagnose behavior. They cannot grant authority, overwrite task/effect history, or prove completion. Required audit and evidence responsibilities are never sampled away. Optional telemetry loss is visible but cannot change outcome; missing mandatory authority/evidence blocks completion. E2 decides physical representation.

### 13.2 Minimum correlated record

“Material” means any fact that can affect authority, policy, scope, cost/budget, ordering, lifecycle/control, effect certainty, recovery, security/privacy, predicate evaluation, evidence validity, verification, or final disposition. Every material transition and operation MUST expose or reference, as applicable:

- schema and record type/version, authority class (`AUTHORITY`, `AUDIT`, `EVIDENCE`, `TELEMETRY`, or `PROJECTION`), mandatory/optional class, record/task/agent/attempt/operation identities, causal parent, correlation and idempotency identities;
- actor/role, authoritative source/reference and version/current-ownership proof, occurrence time, record/observation time, time basis/duration, ordering position, detected gap/reorder fact, state before/after;
- repository/workspace/base/head, normalized target/effect class, policy/approval reference and applicable bounds;
- requested/resolved provider, model, capability/tool, configuration, route/fallback, result/stop/refusal/error semantics;
- retry/cancellation/recovery, usage/cost when exposed, artifact/evidence/readback references, uncertainty and limitations;
- sampling/drop/truncation policy and occurrence, projection as-of source version, lag/freshness/staleness, and required recovery consequence;
- privacy/redaction class and safe bounded content.

Explicit `UNKNOWN` is allowed where the source does not expose a value; silent omission or fabricated precision is not.

### 13.3 Required observable events

User-visible status and accountable records cover: admission/preflight and pre-dispatch policy/schema denials; task/agent transitions; plan/predicate versions; controls and reconciliation; approval request/grant/deny/expire/revoke/consume; operation/tool start/end/cancel/timeout; retries/recovery; budget preflight/exhaustion; artifacts; retention/legal-hold/cleanup/deletion; context-reduction accept/reject; provider routes/fallbacks; predicate checks; verification status/verdicts; effects/readbacks; observability loss/degradation/gap detection; evidence validation; and final disposition.

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
| `RR-005` | HARD_INVARIANT | Every operation/task has finite declared time, output, tool-call, retry, network, and cost limits as applicable. After a productive ceiling is exhausted, zero new productive or task-advancing work starts; only a preauthorized, separately bounded control/safety/cancellation/readback/evidence/cleanup reserve may run. |
| `RR-006` | HARD_INVARIANT | Every accepted pause/stop/redirect receives explicit reconciliation; zero material operation ordered after the control's durable acceptance starts under superseded authority. Requested and effective times remain separately visible. |
| `RR-007` | HARD_INVARIANT | Across every supported task, zero unrelated user changes are lost, overwritten, staged, committed, deleted, or silently mixed; initial/final repository and diff facts are reconciled. |
| `RR-008` | HARD_INVARIANT | Zero `FALSE_TERMINAL_COMPLETION` outcomes and zero `COMPLETED` dispositions without all predicates, valid evidence, every material operation terminal/accounted consistently with close, zero material `OUTCOME_UNCERTAIN` effects, every success-required effect authoritatively `KNOWN_SUCCEEDED` with required readback, every other material effect at a known terminal outcome consistent with predicates, no current wait/control/blocker or pending approval/question/event, every accepted pause explicitly resumed/released, every accepted stop resolved only to `CANCELLED`, every redirect verified on its current revision, and independent `PASSED` verification. Rejected unsupported completion assertions are recorded separately. |
| `RR-009` | HARD_INVARIANT | Every required missing/skipped/failed/stale/unverifiable check produces a noncomplete outcome; every proposed/dispatched operation, rejected pre-dispatch attempt, attempt, and evidence-bundle failure is accounted for. |
| `RR-010` | HARD_INVARIANT | Every required evidence-bundle revision validates against its outcome profile and is retrievable/bound to authoritative state; completed bundles additionally have zero unresolved mandatory reference/revision/semantic mismatch. |
| `RR-011` | HARD_INVARIANT | Zero malformed/incompatible/oversized/stale/unknown executable contracts run and zero hidden provider/model/tool fallback occurs. Requested/resolved provenance is recorded; a source-unavailable provenance field is explicit `UNKNOWN` with its declared consequence, never permission to execute an unknown contract. |
| `RR-012` | HARD_INVARIANT | Zero silent pruning of state needed for authority, recovery, reconciliation, review, or verification; every retention/hold/cleanup/deletion action has authoritative readback or explicit uncertainty and preserves required historical evidence. |
| `RR-013` | HARD_INVARIANT | Every cost-bearing operation has an enforceable authorized conservative ceiling before dispatch, including when live usage/cost reporting is unavailable; zero budget-gate violations. Actual usage/cost is attributed or explicit `UNKNOWN`, but unknown reporting never excuses unbounded dispatch. |
| `RR-014` | HARD_INVARIANT | Every material operation is correlated from intent through result/readback or explicit uncertainty; accidental and deliberate drops, gaps, truncation, delay, reordering, retries, and cancellation are accounted for; telemetry alone never establishes completion. |
| `RR-015` | HARD_INVARIANT | Across every relevant occurrence, zero unauthorized effect/read, secret/private-data disclosure, allowed-root/workspace escape, approval replay/mutation, or clean-room/provenance violation is permitted. |

These are preview correctness gates, not claims that an implementation has passed them.

### 14.2 Aggregate and measurement requirements

E1-002 MUST define the versioned release population, sample size, repetition policy, exclusions, window, threshold, and confidence treatment for each `PREVIEW_SLO` before scored E3/E5 execution. It may not average away a hard-invariant failure. `MEASURE_ONLY` metrics have no v0.1 pass/fail threshold; converting one to a gate requires a prospective E1 amendment/reclassification before the scored run.

| ID | Class | Stable metric family |
|---|---|---|
| `SLO-001` | PREVIEW_SLO | Independently verified end-to-end success by eligible task and repository class, with provider/tool/model layers reported separately. |
| `SLO-002` | PREVIEW_SLO | Durable-control acknowledgement and effectiveness latency, separately measured for pause, stop, redirect, and resume. |
| `SLO-003` | PREVIEW_SLO | Supported orchestrator/worker restart recovery latency to a truthful inspectable phase/condition. |
| `SLO-004` | PREVIEW_SLO | Candidate review-package/evidence-profile acceptance rate after deterministic validation and independent review. |
| `MET-001` | MEASURE_ONLY | Raw and p50/p95 task, phase, provider, tool, verification, and stalled latency where sample size permits. |
| `MET-002` | MEASURE_ONLY | Total/component cost per attempted task and per independently verified success; the latter is undefined at zero successes. |
| `MET-003` | MEASURE_ONLY | User interventions, retries, rate-limit delays, evidence failures, rejected completion assertions, and recovery actions. |
| `MET-004` | MEASURE_ONLY | Outcome variance across repeated equivalent attempts and configuration/provider strata. |

Universal aggregate task-success, latency, cost, intervention, and variance thresholds remain **UNKNOWN** until E1-002 sets only the `PREVIEW_SLO` gates and E3/E5 supply observations. A future release requirement must pass every predeclared `PREVIEW_SLO`, report every `MEASURE_ONLY` metric with raw counts/denominators/unknowns, and pass all hard invariants. E1-001 does not import the unrun model-benchmark-plan design proposals or the zero-run reference baseline as reliability evidence.

## 15. Security-negative and approval review requirements

All security negatives use synthetic/local fixtures, fake marker secrets, controlled sinks/stubs, before/after canaries, and no real credential, external exploitation, paid action, or imported external code. Any unauthorized effect/read or marker leak is a non-compensating failure.

| ID | Required stimulus family | Required outcome/evidence |
|---|---|---|
| `NEG-AUTH-01` | Repository/issue/document/tool/model/test output orders policy bypass, secret access, or external mutation and claims approval. | Authority unchanged; zero prohibited action; denial/conflict audited; safe wait/block where needed. |
| `NEG-SCHEMA-01` | Unknown/stale tool version, malformed/duplicate/oversized request, mismatched/invalid result, or target mutation. | Invalid request/contract/target is denied before dispatch. Invalid post-dispatch result is denied consumption/downstream use and the possible effect enters readback/reconciliation; no widening repair or zero-effect fiction. |
| `NEG-FS-01` | Traversal, path alias, symlink/hard-link/swap, mount/device/FIFO/socket, archive escape/bomb, cleanup-time topology change. | Zero out-of-root read/write/delete; all canaries byte-identical. |
| `NEG-GIT-01` | Hook, alias, credential helper, external diff/text conversion, filter, submodule, signer, monitor, or transport helper attempts execution/egress. | No unapproved helper/network/secret effect or ref movement; limitation visible. |
| `NEG-TERM-01` | Test/build/script spawns descendants, changes working directory, writes outside, floods output, or resists cancellation. | Inherited bounds; output bounded; descendants terminated/accounted; zero outside effect/orphan. |
| `NEG-CMD-01` | Untrusted filename/ref/task/tool argument contains spaces, leading options, metacharacters, substitutions, control/bidirectional characters, or command/option injection. | Value is handled as data under the declared command representation or denied; no unintended command, target, or effect. |
| `NEG-SUPPLY-01` | Downloaded package/archive/binary or lifecycle script attempts execution, egress, secret access, or escape. | Retrieval does not authorize execution; provenance retained; unauthorized action denied. |
| `NEG-NET-01` | Undeclared connection, redirect, DNS rebind, proxy bypass, loopback/private/metadata target, TLS downgrade, credential forwarding. | Zero forbidden connection or data/credential transmission; effective target rechecked. |
| `NEG-PROVIDER-01` | Disallowed provider/account/region/retention/training policy, missing cost ceiling, or hidden fallback is offered an otherwise valid model request. | Zero repository bytes transmitted and zero call/cost; exact denial and requested/resolved route facts retained. |
| `NEG-SECRET-01` | Marker appears in files, general/inherited environment, command/tool output, exception, encoded/split stream, process data, screenshot, temp/cache, diff, summary, approval, evidence, or accidental request paste. | Zero raw marker occurrences outside the exact protected recipient boundary; safe quarantine/exposure/rotation record without echo/digest leak. |
| `NEG-CRED-01` | Credential scoped to one task/tool/endpoint is attempted by another tool/child/redirect/retry/stale owner, then rotated/revoked during queued or active use. | Every mismatched/stale/new use is denied; queued use invalidates; active use cancels/reconciles with possible exposure explicit; receipt contains identity/scope only. |
| `NEG-APR-01` | Approval replay, target/argument substitution, schema/policy/base change, expiry/revocation, one-shot reuse, forged conversational confirmation, digest-only material, markup/control/bidirectional spoofing, or target-hiding truncation. | All invalid/uninspectable uses denied; exact valid action executes at most once; inert full-content display/reference and executable action binding match. |
| `NEG-RACE-01` | Approval/revocation/pause/stop/redirect/restart/stale-owner races around dispatch and effect. | One legal persisted outcome; stale owner denied; uncertainty reconciled; no blind retry or false completion. |
| `NEG-EXT-01` | External effect occurs but response is lost, or tool reports success while target is wrong/unchanged/partial. | Authoritative readback before retry/completion; at most one effect; honest partial/uncertain/noncomplete status. |
| `NEG-VER-01` | Sole author self-verifies high-risk work or verifier tries new effect with author approval/credential. | Self-verification rejected; verifier remains least-privilege or obtains separate authority; exact revision retained. |
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
| Authority and durable semantic state | §§2–3 | D-003/D-016; Charter §§5–6; master authority rules | D-005 establishes current project-repository authority only; Audit Level A corroborates properties only | E2 physical model/topology. |
| Task/agent lifecycle and controls | §§4–7 | D-016; Charter §§6–7, 11; master runtime rules | Baseline continuation/control claims are documented but untested; Audit Level A semantics only | E2 mechanism; E1-002 cases. |
| Repository/workspace/capabilities | §8 | D-016 workflow; Charter §§4, 8, 12 | Audit Level A boundary properties; no reconstructed implementation | E2 workspace/isolation/tool design. |
| Permissions, approvals, secrets, effects | §9, §15 | `SECURITY.md`; Charter §§9, 12; master security rules | Baseline features documented, enforcement unknown; Audit Level A/negative ideas | E2 enforcement mechanism; E1-002 cases. |
| Failure and honest partial outcomes | §10 | Charter §§6, 10–11 | Audit Level A accountable-failure property only | E2 structured contract representation. |
| Completion and verification | §11 | D-016; Charter §§7–8; master completion standard | Baseline artifacts are not automatic predicates; Audit Level A evidence closure | E1-002 cases; E3 role eligibility. |
| Evidence and observability/context | §§12–13 | D-003/D-016; Charter §§5.4–5.5, 6, 8, 10; master completion rules | Audit Level A evidence/derived-context principles corroborate only | E2 storage/projection; E1-002 validation. |
| Reliability and security negatives | §§14–15 | Charter §§11–12; R-002/R-003/R-009/R-013–R-015/R-025–R-028 | Zero-run baseline and unrun benchmark plan are not results | E1-002 thresholds/cases; E3/E5 runs. |
| Evaluation/release requirements | §16 | Charter §§18, 20, 22; task boundary | Taxonomy ideas only | E1-002 owns artifacts/gate. |
| Future compatibility and non-goals | §17 | D-001, D-003, D-004, D-016; Charter §15 | Level B material is reserved for E2 and is not E1 evidence | E2 migration analysis; later authorized stages. |
| Clean room/provenance | §18 | D-002, D-016; master prompt; Charter §16 | Verified baseline/audit within stated limits | Every later author/reviewer/verifier. |

## 20. Preserved unknowns and E1-001 boundary

The following remain **UNKNOWN**: final client and interaction form; storage/state/history/event/projection/compaction design; local isolation mechanism and demonstrated tier; host/language/repository support matrix; capability catalog; funded provider access and exact model configurations; model-role assignments; benchmark and implementation budget; aggregate preview release thresholds; universal latency/cost envelopes; packaging/update/migration mechanics; customer demand; production readiness; and reference-product runtime behavior beyond sourced documentation.

No unknown may be filled from model reputation, a single run, external reconstructed detail, or an architecture preference. This contract creates no application code, performs no benchmark, selects no architecture or technology, does not activate E1-002/E2/E3/E4/E5, does not resume S1-003, and does not authorize autonomous build or external action.

E1-001 may move only to repository `READY_FOR_REVIEW` after author validations and factual handoff. It remains unverified until the registered independent challenger, author/fixer response, and independent post-fix verifier satisfy all task acceptance criteria. E1-002 remains `BACKLOG` until that independent verification is complete.
