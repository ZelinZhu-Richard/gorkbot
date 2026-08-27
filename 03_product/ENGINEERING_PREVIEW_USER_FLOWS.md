# Engineering Preview v0.1 User Flows

Status: E1-001 AUTHOR PASS — READY_FOR_REVIEW; NOT VERIFIED

Normative scope: user-visible workflow and control semantics for the product defined in `ENGINEERING_PREVIEW_PRD.md`. Lifecycle states, completion predicates, approval rules, and evidence fields are defined in `ENGINEERING_PREVIEW_CORRECTNESS_CONTRACT.md`.

This document selects no client surface or technology. A “view,” “control,” or “notification” means a product capability available through whichever surface E2 later selects.

## 1. Actors and shared terms

| Actor or object | Meaning |
|---|---|
| User | The one local authenticated principal who owns or is authorized to work on the repository and controls the task; authentication mechanism is an E2 decision. |
| Agent | One persistent named software-engineering agent. Its identity survives model, process, client, and task changes. |
| Author execution | The bounded implementation/analysis path producing the proposed result. It cannot independently declare verified completion. |
| Independent verifier | A logically separate verification path that reads the exact task contract, authoritative repository state, artifacts, and evidence for the reviewed revision. Exact eligible role occupants are decided only after E3 evidence. |
| Task contract | The durable versioned request, scope, authority, plan, limits, predicates, approvals, and outcome rules. |
| Workspace | The task-identified isolated repository work area or an E2-selected equivalent that proves non-interference. |
| Operation | One versioned model, tool, filesystem, terminal, Git, test, approval, recovery, or verification action. |
| Review package | An inspectable patch, isolated branch, bounded commit, draft-PR package, or evidence-backed diagnosis/no-change report created locally under the task contract. |
| Evidence bundle | The versioned, secret-safe record defined in the correctness contract. |

## 2. Global flow invariants

The following apply to every flow:

1. The product does not acknowledge an accepted request or control mutation until recovery-sufficient durable state exists.
2. Every user command has a stable identity, observed task version, acceptance sequence, actor, time, and result. Duplicate delivery returns the first result rather than repeating the effect.
3. A stale command that would overwrite newer scope, state, or authority is rejected or reconciled visibly; it is never applied as silent last-write-wins.
4. No model, tool, file, issue, comment, test output, or retrieved content can grant authority, approve an action, or change the task's permission class.
5. A task may move to `COMPLETED` only after independent verification passes against the exact final review revision.
6. Every exit path preserves useful artifacts, failures, limitations, approvals, uncertain effects, and current repository state in the evidence bundle.
7. The user may inspect status and issue pause or stop while work is active; the client disappearing is not a stop request.
8. A consequential external action is not dispatched without matching admitted authorization and human approval. After dispatch, only fresh authoritative readback may establish `KNOWN_SUCCEEDED` and satisfy completion; missing or contradictory readback yields `OUTCOME_UNCERTAIN` and a noncomplete task result rather than a claim that no effect occurred.
9. The user-visible status is a tuple: work phase, wait/control/blocker, attempt disposition, verification status/verdict, effect certainty, and agent availability remain separate even when one label is emphasized.
10. Autonomy ends at the current user-admitted task contract and finite limits; observations cannot create new tasks, widen scope/capability, weaken predicates, select continuous work, or authorize another visible agent.
11. Cleanup, retention, hold, and deletion behavior preserves required authority/evidence and user data; a deletion claim requires exact-scope readback or explicit uncertainty and never erases the historical action record.
12. `COMPLETED` cannot coexist with any current wait/control/blocker, pending approval/question/event, or proposed/authorized/dispatched/running/reconciling material operation; every material operation is terminal and accounted consistently with close. Historical records remain evidence, not active axes. Pause must be explicitly resumed/released; an accepted stop closes only as `CANCELLED`; a redirect requires verification of its current revision.

## 3. UF-01 — Accept or reject an engineering request

### Trigger

The user submits natural-language work, a repository issue reference, or both, and identifies or confirms the target repository.

### Preconditions

- The user's local principal identity is established under current policy, and the user identifies a repository they are authorized to inspect.
- The product can identify the repository without executing repository-provided code.
- No prior task is silently reused merely because the request text resembles it.

### Flow

| Step | Product behavior | Durable evidence |
|---:|---|---|
| 1 | Capture the original request and repository reference without semantic rewriting. If probable secret material is present, stop it before model/general persistence where possible and retain only an authorized redacted form plus opaque protected reference; otherwise block and request rotation/protected re-entry. | Request identity, safe content/reference, received time, principal, repository candidate, secret-handling outcome. |
| 2 | Before opening repository/issue content, persist a candidate task identity and the minimal preflight grant: exact root/resource and allowed metadata/path reads, policy, bounds, no repository code/Git-helper execution, no secret locations, and no network unless separately granted. | Candidate task and preflight-grant identities/versions and accepted/denied scope. |
| 3 | Perform the bounded preflight: repository identity, revision/ref, dirty/untracked state, nested repository/submodule facts where relevant, governing instructions, and obvious sensitivity or authorization conflicts. | Preflight observations and bounded command/read results. |
| 4 | Classify the request as an eligible v0.1 task class or record why it is ineligible/ambiguous. | Classification, eligibility rule, unknowns. |
| 5 | Identify material ambiguities, unavailable prerequisites, possible external effects, secret needs, untrusted dependency execution, and destructive actions. | Question/approval/risk list; no effect yet. |
| 6A | If safely bounded, expand the grant into the durable task contract and acknowledge the same stable task identity. | Stable task ID, full axis tuple/schema/version, complete contract. |
| 6B | If a material choice is missing, set wait reason `WAITING_FOR_USER` and continue no unauthorized write/execution work. | Question IDs, suspended phase, affected predicates, response effect. |
| 6C | If unauthorized, unsupported, unsafe, or out of v0.1 scope, reject before execution and preserve the reason in the admission/rejection evidence profile. | Named failure/rejection reason and zero-effect proof; never `COMPLETED`. |

### Acceptance

- A crash immediately after task acknowledgement restores the exact task identity and request once.
- Dirty user work and governing instructions are visible before the first write.
- Rejection or waiting is not represented as successful completion.

## 4. UF-02 — Primary bounded repository change

### Trigger

UF-01 produced an eligible durable task contract.

### Flow

| Phase | Required behavior | Exit condition |
|---|---|---|
| `ANALYZING` | Read governing instructions and the smallest relevant repository surface; map requested behavior, constraints, affected components, risks, and unknowns. Untrusted text is data, not authority. | Evidence supports a bounded understanding or a wait/block qualifier is recorded. |
| `ANALYZING` — defect observation | Run the least invasive authorized failing oracle. Record non-reproduction, unsafe/flaky/environmental conditions, or not-applicable as observations, not verifier verdicts. | A reported/alternative failing oracle is established for a fix, or the task redirects/reclassifies to diagnosis/noncomplete. |
| `PLANNING` | Create a versioned plan with allowed paths, operations, tests/checks, approvals, retry/stop rules, review-package form, and task-specific predicates. | Plan is internally consistent and any material user decision is resolved. |
| `READY_TO_EXECUTE` | Revalidate authority, repository/base/dirty state, workspace isolation, tool contracts, model route eligibility, budgets, and required approvals before mutation. | Pre-dispatch validation passes or a named qualifier/disposition applies. |
| `EXECUTING` | Make only authorized changes. Record every material read/write/command/tool operation, result, failure, retry, and artifact. Reread changed files after writes. | Planned edits end, a control/wait/block occurs, or redirect returns to planning. |
| `OBSERVING` — checks | Run the declared checks against the task workspace and record exact exit/results. A failed or skipped required check cannot be converted to pass in prose. | All applicable author-side predicates are evaluated. |
| `OBSERVING` — package | Reinspect repository status/diff; separate unrelated changes; create the selected local review package and candidate evidence bundle. | Immutable candidate bundle and exact review revision/package identity exist. |
| `VERIFYING` | A logically separate verifier reads authoritative state and evaluates each predicate without relying on author narration or mutating the review revision. | Verification status `FINISHED` with verdict `PASSED`, `CHANGES_REQUIRED`, `BLOCKED`, or `INCONCLUSIVE`. |
| Close | Map the separate verifier result, predicates, disposition, qualifiers, and effects to the final tuple; present evidence, limitations, and required human actions. | Only independently passed all-gate work is disposition `COMPLETED`. |

### Success view

The user receives:

- the exact requested outcome and task status;
- an inspectable review package and changed-file summary;
- checks run, checks skipped, failures, and exact results;
- independent verification verdict and reviewed revision;
- approvals and external-state readbacks, if any;
- known limitations and unresolved questions; and
- no claim that a local package was pushed, merged, deployed, or released.

## 5. UF-03 — Reproduction unavailable or contradictory

### Trigger

A defect-oriented task cannot reproduce the reported behavior, reproduces only intermittently, or reveals that the request's stated cause is wrong.

### Flow

1. Preserve the reported conditions and the exact attempted conditions.
2. Record environment/revision/configuration differences and each attempt result.
3. Do not invent a reproduction or causal explanation.
4. If a safe change remains justified by other evidence, amend the plan and predicates visibly; a change in intended behavior may require user input.
5. Otherwise preserve the work phase and record the applicable wait reason/blocker, or intentionally close with disposition `PARTIALLY_COMPLETED`/`FAILED`; verification status remains separately `UNVERIFIED` until an eligible diagnosis result is checked.
6. A non-reproduced defect can be `COMPLETED` only when the agreed task itself was a bounded diagnosis and its diagnosis predicates independently pass; it cannot be called a verified fix.

## 6. UF-04 — Pause

### User intent

Temporarily stop starting new work while preserving a resumable task.

### Semantics

| Step | Required behavior |
|---:|---|
| 1 | Persist the pause command with the user's observed task version before acknowledging it. |
| 2 | Move the task to `PAUSING`; start no new productive or task-advancing operation under superseded authority after acceptance. Separately authorized bounded control, cancellation, safety, readback, evidence-preservation, and reconciliation operations may run. |
| 3 | Request cancellation of an interruptible in-flight operation. An operation declared indivisible or non-interruptible by its trusted capability contract may settle, but its status and possible effect must be visible. |
| 4 | Reconcile receipts/readback for any operation that might have crossed an effect boundary. |
| 5 | Persist a checkpoint containing current plan step, repository/workspace state, pending questions/approvals, in-flight outcomes, budgets, artifacts, and resume preconditions. |
| 6 | Remain `PAUSING` while productive/task-advancing or pre-pause in-flight work runs. Enter `PAUSED` only after each such operation is terminal, safely checkpointed/cancelled, or classified `OUTCOME_UNCERTAIN`; a blocker/recovery qualifier and separately authorized bounded safety/readback/reconciliation operation may coexist with pause. |

### Acceptance

- Pause does not undo completed effects.
- A client disconnect before the pause receipt does not imply the pause was accepted.
- Restart during `PAUSING` resumes reconciliation, not ordinary execution.

An agent-level pause stops new task claims and applies this pause flow to its active task. Disabling the agent stops new claims and requires an explicit pause-or-cancel policy for active work. Retirement is explicit, reconciles/releases active ownership, and preserves all history; it is not a task deletion or transfer to another visible v0.1 agent.

## 7. UF-05 — Stop or cancel

### User intent

End the current task attempt and prevent further planned work.

### Semantics

1. Persist a stop command before acknowledgement and move the task to `STOPPING`.
2. Launch no new work other than cancellation, readback, cleanup, evidence finalization, and safety-preserving recovery.
3. Request cancellation for interruptible operations. Do not claim already completed effects were undone.
4. Reconcile every in-flight operation as `KNOWN_NOT_STARTED`, `CANCELLED`, `KNOWN_SUCCEEDED`, `KNOWN_FAILED`, or `OUTCOME_UNCERTAIN`.
5. Preserve task changes and artifacts unless cleanup was already authorized and proven safe; never delete user work to make cancellation look clean.
6. Remain `STOPPING` while bounded cancellation/reconciliation is active; a blocker or recovery qualifier may coexist when progress needs another condition.
7. Once every operation is terminal or explicitly uncertain, finalize the attempt disposition as `CANCELLED`. Preserve any finished verification result and its bound revision; the current cancellation revision is `UNVERIFIED` when no finished verdict exists or when stop/material mutation invalidated that binding. Record useful partial-result facts, failures/cleanup gaps, and effect `OUTCOME_UNCERTAIN` separately rather than changing the stop cause into `PARTIALLY_COMPLETED` or `COMPLETED`.
8. Resuming a terminally cancelled task requires an explicit linked reopen/new attempt; reconnect alone cannot revive it.

## 8. UF-06 — Redirect

### User intent

Change priority, approach, requested output, or scope while preserving prior work.

### Semantics

| Redirect kind | Behavior |
|---|---|
| Non-material clarification | Version the task/plan, preserve the prior wording, and continue from the earliest affected step. |
| Plan/priority change within existing authority | Stop starting superseded steps, reconcile in-flight work, version the plan, and continue only after preconditions pass. |
| Requested-behavior or completion-predicate change | Return to `ANALYZING`/`PLANNING`; invalidate affected checks and verifier results. |
| Path, capability, credential, network, budget, destructive action, or external-effect expansion | Do not infer permission. First enter `WAITING_FOR_USER` and obtain an authenticated versioned task-authorization amendment. If the resulting exact action is consequential, separately enter `WAITING_FOR_APPROVAL`; action approval alone cannot broaden the task contract. |
| Redirect conflicting with higher-authority repository/project rules | Reject the conflicting portion, explain the evidence, and preserve both commands. |

### Race behavior

- Redirect and stop/pause are ordered by durable acceptance sequence.
- An earlier operation already past its declared cancellation boundary is reconciled before the redirect continues.
- Work from a superseded plan cannot be credited without reevaluation against the new predicates.

## 9. UF-07 — Resume after pause or user wait

### Preconditions

- The user explicitly resumes/answers/approves, or a recorded `WAITING_FOR_EXTERNAL_EVENT` condition receives a current authenticated/read-back event as required.
- The task is nonterminal and the responding command references a current or safely reconcilable task version.

### Resume validation

Before ordinary work resumes, the product must recheck:

1. task and agent identity and current ownership;
2. repository identity, base/ref, dirty state, workspace availability, and unexpected user changes;
3. governing instructions and task/plan versions;
4. pending operations, receipts, uncertain effects, and cancellation results;
5. approval validity, revocation, scope, and expiry;
6. capability schema/version and permission policy;
7. selected model/provider eligibility and configuration;
8. time, cost, tool, output, retry, network, and credential budgets; and
9. whether completion predicates or tests became stale.

If any recheck fails, resume enters `WAITING_FOR_USER`, `WAITING_FOR_APPROVAL`, `RECOVERING`, or `BLOCKED`; it does not silently continue from stale context.

An external event must correlate to the current wait identity/version, pass authoritative readback, and reject stale/duplicate delivery. Timeout follows the recorded noncomplete/escalation rule. An answer, approval, or event received while `PAUSED` is recorded but launches no work until authorized resume.

## 10. UF-08 — Restart and recovery

### Trigger

The orchestration process, execution owner/worker, model/tool/terminal operation, or local runtime support process ends unexpectedly or is intentionally restarted. A client-only disconnect/reload is a presentation event unless it also caused runtime-owner loss.

### Flow

| Step | Required behavior |
|---:|---|
| 1 | For client-only reconnect with a healthy owner, rebuild presentation without changing task/agent execution state. Otherwise enter `RECOVERING` and load authoritative task, plan, operation, control, approval, workspace, artifact, and verification facts; do not treat the last transcript line as truth. |
| 2 | Validate record versions/integrity and preserve corrupt/incompatible evidence instead of silently resetting it. |
| 3 | Establish exactly one currently authorized owner under a versioned or equivalent stale-owner proof; reject stale owners/workers. E2 selects the mechanism. |
| 4 | Classify each interrupted operation using durable pre-effect/post-effect evidence and current target readback where safe. |
| 5 | Never blindly repeat an operation whose effect might have occurred; require idempotency evidence or reconciliation. |
| 6 | Revalidate repository/workspace/authority/approval/provider/tool/budget preconditions. |
| 7 | Resume at the earliest safe step or enter a typed waiting, blocked, unverified, or failed state. |
| 8 | Record recovery cause, duration, actions, data-loss boundary, changed assumptions, and result in the evidence bundle. |

### Acceptance

Every nonterminal task state has a tested restart path. An ambiguous outcome is visible and blocks `COMPLETED`.

## 11. UF-09 — Approval request, denial, expiry, and revocation

### Trigger

The next normalized action is consequential and within admitted task authority but requires separate human approval. An action outside admitted limits first follows UF-06 task-amendment semantics and is then re-presented for approval if consequential.

### Request flow

1. Stop before the effect boundary and enter `WAITING_FOR_APPROVAL`.
2. Show the actor, task/operation, exact capability/action, target/resource, every material input inline or through an immutable full-content reference, effect/reversibility class, credential/network use, limits, policy version, expiry/use count, risk, alternatives, and expected readback. A digest binds inspectable bytes but never substitutes for them; untrusted content is inert/escaped and cannot hide target/effect through markup, control/bidirectional text, or truncation.
3. The user may approve once, request a narrower action permitted by already admitted authority, deny, revoke a still-valid standing permission, stop, or redirect. A narrower action is normalized and re-presented before approval.
4. A valid approval receipt is durable and bound to the exact normalized action; authorization policy is rechecked at execution time.
5. Mutation, target substitution, policy change, task version change, expiry, revocation, wrong actor/owner, or replay invalidates the receipt.
6. After an approved consequential effect, the product obtains a fresh receipt/readback and records the exact observed result. If readback is unavailable or contradictory, the task cannot be completed.

### Denial and expiry

Denial or expiry launches no effect. The task either replans within existing authority, waits for user direction, becomes blocked/partial/cancelled, or fails according to its predicates. It cannot repeatedly nag or auto-widen the request.

## 12. UF-10 — Remote Git, pull request, issue, deployment, publish, or message requested

These actions are consequential external effects and are not required for v0.1's core success path. If the optional capability is not separately admitted and supported, the product returns typed failure `UNSUPPORTED_CAPABILITY` with zero effect and separately selects the truthful wait/block/disposition; approval cannot create the missing capability.

1. The agent may prepare local commands, patch, branch, commit, draft title/body, or another review package when authorized.
2. Preparation must be clearly labeled as not executed externally.
3. An actual remote action requires a capability allowed by the task/policy and an exact human approval receipt.
4. The operation must use the approved remote/target, ref/object, content, identity, and limits.
5. Completion requires fresh external readback, such as the remote ref/object/version or resulting external record.
6. A command exit or provider response without readback is insufficient.
7. Failure, partial application, conflict, or unknown effect is reported honestly and blocks `COMPLETED` for that external-action predicate.

## 13. UF-11 — Secret or interactive authentication needed

1. The product identifies the purpose, target, capability, and minimum scope without asking the user to paste the secret into chat or a repository file.
2. If a supported secret-safe or human-takeover boundary does not exist, enter `WAITING_FOR_USER` or `BLOCKED`; do not improvise through ordinary model context, shell history, screenshots, logs, or artifacts.
3. During protected entry, agent/model/tool capture of keystrokes, clipboard, screen/screenshot, accessibility state, terminal stream, and secret value stops; only a non-secret outcome/receipt returns.
4. Secret acquisition/use is bound to the exact task/capability/endpoint and excludes the value from general/inherited environment and records or descendants.
5. The user can deny, revoke, or rotate access. Queued use invalidates; active use cancels/reconciles with possible exposure explicit.
6. After use, receipts record only non-secret identity/scope/outcome facts; evidence scanning confirms no leaked value and ordinary work resumes only after authority/state revalidation.
7. If accidental secret propagation may already have occurred, record a safe possible/confirmed exposure, destination class/time/scope, cleanup and rotation action without echo/digest, and block completion until the applicable predicate is reconciled.

## 14. UF-12 — Provider/model failure or route change

1. Record the requested and resolved provider/model/configuration and the accountable failure layer.
2. Preserve partial stream/tool/effect facts without turning the error into assistant success text.
3. Apply only the predeclared retry policy; authorization/policy/refusal/unknown-effect/terminal failures are not generic retry candidates.
4. Do not silently switch providers or models.
5. If an explicit fallback policy exists, create a new attributed route/attempt and revalidate data, tool, context, cost, and permission compatibility.
6. A fallback result is evaluated and billed as its own configuration.
7. If no eligible route remains, preserve the work phase and record the applicable wait/blocker, or intentionally close with `PARTIALLY_COMPLETED`/`FAILED`; keep verification and effect axes separate.

## 15. UF-13 — Context compaction or reconstruction

1. Detect that model working context approaches a configured limit or must be rebuilt after restart.
2. Identify the source task/message/operation ranges and current authoritative versions.
3. Produce a derived bounded working view with provenance and explicit omission/loss facts.
4. Preserve pending instructions, task scope, approvals, unresolved failures, tool/effect status, source references, and completion predicates—or reopen them directly from authoritative records rather than trusting a summary.
5. Reject a stale compaction result if newer authoritative state exists.
6. Do not delete or downgrade durable conversation, task, effect, approval, artifact, audit, source, test, or verification evidence.
7. If required information cannot be reconstructed safely, enter `RECOVERING`, `WAITING_FOR_USER`, or `BLOCKED`; never guess from a summary.

## 16. UF-14 — Independent verification and changes required

### Preconditions

- Author execution has produced a fixed review revision/package and draft evidence bundle.
- The verifier has no authority to silently modify the proposed result while calling that same pass verification.

### Flow

| Step | Verifier behavior |
|---:|---|
| 1 | Load the original request, current task contract, governing instructions, plan/predicates, exact reviewed revision, diff, and evidence bundle. |
| 2 | Check repository/workspace identity and reject stale or mixed evidence. |
| 3 | Independently rerun or inspect deterministic predicates and use fresh state/readback where required. Verifier outputs are isolated/declared and may not mutate the review revision/package. |
| 4 | Evaluate scope, unrelated changes, required/negative checks, security/secret/provenance constraints, artifacts, approvals, limitations, and outcome classification. |
| 5 | Record a predicate-by-predicate result: `PASS`, `FAIL`, `BLOCKED`, `NOT_APPLICABLE`, or `INCONCLUSIVE` with evidence. |
| 6 | Return `PASSED`, `CHANGES_REQUIRED`, `BLOCKED`, or `INCONCLUSIVE`; retain disagreements and verifier identity. |
| 7A | `PASSED`: task may become `COMPLETED` only if all applicable predicates pass and the reviewed revision is unchanged. |
| 7B | `CHANGES_REQUIRED`: close the reviewed attempt as `SUPERSEDED` with that cause, preserve verdict/revision, and create a linked unverified correction attempt; any change requires re-verification. |
| 7C | `BLOCKED`/`INCONCLUSIVE`: finish verification with that verdict, create the applicable task blocker, and leave the attempt noncomplete. |

Any material verifier or concurrent mutation stops verification and makes the new state `UNVERIFIED`. A `PASSED` verdict and final bundle validation must bind the immutable candidate bundle, exact review revision, and exact final bundle revision.

The same author may run self-checks, but those are labeled author checks and do not satisfy the independent-verification requirement for consequential work.

## 17. UF-15 — Honest partial, blocked, failed, or unverified closure

When predicates cannot pass, the product updates the narrowest honest axes without flattening them:

| Axis-qualified value | User-visible meaning | Required evidence |
|---|---|---|
| wait `WAITING_FOR_USER` | A specific material answer is required; safe work may continue only inside the recorded boundary. | Question, suspended phase, reason, affected predicates, continuation boundary. |
| wait `WAITING_FOR_APPROVAL` | An exact consequential action is proposed but not dispatched. | Full inspectable normalized action and zero-dispatch/receipt state. |
| task blocker `BLOCKED` | Progress cannot safely continue without a named condition/authority change. | Blocker, owner, alternatives, unblock condition, preserved work. |
| disposition `PARTIALLY_COMPLETED` | Attempt is intentionally terminally closed with a usable requested subset and unmet predicates; no resumable wait remains. | Completed/unmet predicates, artifacts, failures, no complete claim. |
| disposition `FAILED` | Attempt terminally ended unsuccessfully under its current contract. | Failure class/layer, attempts, effects, cleanup/recovery, artifacts. |
| disposition `CANCELLED` | User/policy ended the attempt; partial-result facts and effects remain separate. | Stop receipt, `STOPPING` reconciliation, operation outcomes, preserved changes. |
| verification status `UNVERIFIED` | Independent verification has not passed; this may coexist with any open/noncomplete disposition or qualifier. | Reviewed revision/candidate if any, status/verdict, missing/failed predicates. |
| effect `OUTCOME_UNCERTAIN` | A material operation's effect cannot yet be authoritatively resolved. | Operation identity, receipt/readback attempts, duplicate risk, next safe action. |

Every path produces the applicable evidence profile and a concise next safe action. None is a synonym for `COMPLETED`.

## 18. UF-16 — Reserved E1-002 contribution-flow boundary

E1-001 intentionally defines no ordered contributor procedure. E1-002 exclusively owns reproducible setup, contribution, evaluation, maintainer-review, and release steps after E1-001 is independently verified.

The later flow must trace to the same nonwaivable product constraints: clean public source/specifications without private chat, credentials, customer data, or reconstructed material; isolated bounded changes; retained security controls; deterministic/evidence checks; independent review; and separate human approval for merge, publish, release, or another external effect. E1-002 instantiates these constraints and does not “replace” or weaken them.

## 19. Flow coverage matrix

| Requirement area | Primary flow coverage |
|---|---|
| Intake, user, supported use case | UF-01, UF-02 |
| Repository/workspace, filesystem, terminal, Git, tests | UF-01, UF-02, UF-10 |
| Pause/stop/redirect/resume | UF-04 through UF-07 |
| Restart/recovery and uncertain effects | UF-08, UF-15 |
| Permissions, approvals, secrets, external actions | UF-09 through UF-11 |
| Bounded autonomy and resource ceilings | Global invariants, UF-01, UF-06, UF-07, UF-12, UF-15 |
| Retention, cleanup, holds, and deletion claims | Global invariants, UF-05, UF-11, UF-15 |
| Provider abstraction/routing failures | UF-12 |
| Context compaction | UF-13 |
| Independent verification and completion | UF-14, UF-15 |
| Observability, evidence, and reliability semantics | Global invariants, UF-02, UF-08, UF-13 through UF-15 |
| E1-002 contribution ownership boundary | UF-16 |

## 20. Flow non-goals

These flows do not define UI layout, protocol, storage, scheduling, sandbox implementation, provider adapter, credential store, Git library/CLI, test runner, event architecture, or workflow engine. They also do not add cloud execution, multiple agents/users, SaaS, Finance, routines, marketplaces, mobile, or production deployment/release automation. Optional human-approved external capabilities are not part of the required core workflow and return `UNSUPPORTED_CAPABILITY` unless separately admitted and implemented after later authorized design/build work.
