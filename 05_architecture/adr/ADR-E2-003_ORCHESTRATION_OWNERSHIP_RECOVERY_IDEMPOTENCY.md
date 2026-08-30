# ADR-E2-003 — Task/Execution Orchestration, Ownership, Recovery, Idempotency, and Future Concurrency

ADR ID: `ADR-E2-003`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `FOUNDATIONAL_HIGH_COST`

## Context

The product requires durable task and operation lifecycle semantics, one accountable owner, ordered pause/stop/redirect/resume, restart reconciliation, duplicate intake/effect prevention, honest unknown outcomes and a future path beyond a local single writer. No durable workflow engine or queue technology has been selected.

## Decision

Propose a versioned explicit task/operation state loop inside the integrated core. One current owner epoch is authoritative for each active task. Every mutation carries expected record version, stable request/operation identity and current epoch. Stale writers, results, approval uses and effect attempts are rejected.

The core persists control requests before changing dispatch authority. It creates no new productive operation while paused/stopping/blocked, while separately preauthorized safety/control/readback/evidence reserve operations may run. Each operation records admission, start, progress where material, cancel/timeout/fence, result validation, effect state and first terminal outcome.

On owner loss, a successor obtains a new epoch, loads authoritative state, scans every nonterminal operation/effect, discovers/fences surviving children and revalidates workspace, policy, approvals, routing, budgets and predicates before resuming. Duplicate input or operation identity returns the first result. Effect ambiguity is reconciled through ADR-E2-005, never blind replay.

## E1/E2 constraints and trace

- Primary ARs: `AR-COR-001`, `AR-COR-002`, `AR-COR-007`, `AR-DUR-002`, `AR-DUR-003`, `AR-DUR-004`.
- Cross-cutting: `AR-EXE-002/003`, `AR-APR-002`, `AR-FUT-002`, `AR-FAIL-002`.
- Domains: `D03_TASK_WORKFLOW_ORCHESTRATION`, shared `D06_EVENT_OPERATION_HISTORY`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`.

## Options considered

1. C01 in-core state loop with epochs/version checks and material operation/effect history.
2. C02 service-owned orchestration with leases/fenced replaceable workers.
3. C03 journal/command admission with workflow owner/fence and reducer state.

## Rationale

C01 meets the verified ownership/recovery/idempotency hard floor without a mandatory service/worker lease lifecycle or event-reducer authority. Its owner epoch makes future replacement possible while preserving the immediate single-writer model. C02 is more direct for worker replacement; C03 is stronger for replay. Those advantages remain reopen triggers rather than hidden imports.

## Rejected alternatives

C02's leases and C03's journal owner are not adopted because they are structural candidate choices, not free implementation details. A future implementation may not add either in a way that changes authority without reopening E2.

## Consequences and trade-offs

Positive: explicit lifecycle; short ownership path; deterministic stale rejection; simple duplicate first-outcome behavior; recovery is centralized.

Negative: integrated-core loss pauses live control until restart; epoch/operation/effect tokens become durable compatibility contracts; later distributed ownership requires careful migration; core orchestration coupling needs strong module boundaries.

## Security implications

No model or child owns task authority. Owner epochs and capability grants are checked at every state/effect publication boundary. Pause/stop/revocation removes productive authority independently of best-effort process termination. Recovery never reuses cached approvals, routes or protected input.

## Recovery implications

Recovery distinguishes client loss, core owner loss, child loss and host loss. It preserves `KNOWN_SUCCESS`, `KNOWN_FAILURE` and `UNKNOWN_OUTCOME`; never assumes a missing acknowledgement means no effect. Nonterminal operations block productive resumption until classified or safely fenced.

## Evidence and verification implications

Evidence records state/version/epoch transitions, duplicate identity and first result, control ordering, process/effect endpoints and recovery owner. Deterministic fault injection must cover before/after acknowledgement, ownership transfer, dispatch, receipt, readback, control and terminal transition.

## Missing evidence and current evidence limit

No scheduler, operation ledger, epoch/fence implementation, crash/restart trace, duplicate-delivery trial, cancellation/descendant-containment trial, or effect-reconciliation run exists. `E3V-001/002/005` are unrun, including the residual `AR-EXE-003` seam, so no recovery, idempotency, stop, fence, ownership or completion behavior is yet proven.

## Reversibility and migration

Scheduler internals are `MODERATELY_COSTLY`. Owner epochs, operation/idempotency identity and recovery semantics are `FOUNDATIONAL_HIGH_COST`. A future service/distributed migration requires versioned token translation, drained or explicitly reconciled nonterminal work, one-writer cutover, stale-owner proof, duplicate/effect invariants and rollback.

## Future compatibility

Current ownership is scoped rather than global: principal, agent, task, workspace, operation and policy identities are explicit. Serializable operations and epoch/fence semantics preserve a credible path to remote workers, multiple clients and later concurrency without implementing queues, leases, actors or multi-agent work now.

## E3 validation obligations

- `E3V-001`: acknowledgement/ownership/duplicate/effect recovery.
- `E3V-002`: pause/stop/force-or-fence and descendant accounting.
- `E3V-005`: exact-state evidence, replay, adequacy and stale verification.

## Handback and reopen conditions

Frozen handback sets: `E3V-001 -> ADR-E2-002/003/004/005`; `E3V-002 -> ADR-E2-003/004`; `E3V-005 -> ADR-E2-002/003/005/007/008`. Reopen if C01 cannot prevent stale authority or duplicate effect, cannot reconstruct a legal state after required faults, or needs an unrecorded/global singleton to preserve correctness. Adapter or fixture failures stay correction when semantics remain feasible.

## Unresolved implementation details

State-machine representation; scheduling algorithm; epoch/version primitive; timers; checkpoint cadence; recovery scan implementation; queue/backpressure mechanics; operation payload encoding; fairness; future lease/actor migration approach.

## Source evidence and provenance

Frozen lifecycle/control/effect contracts; E2 plan; architecture requirements and handback rules; C01 f04/f06-f09/f12/f17/f20/f23/f28/f30; comparison recovery and sensitivity sections; closure E3V-001/002/005 ledger. Audit queue/lease/workflow patterns remain Level-B alternatives only.
