# ADR-E2-002 — Canonical State, Persistence, Causal/Operation History, Projections, and Migration

ADR ID: `ADR-E2-002`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `FOUNDATIONAL_HIGH_COST`

Decision status and reversibility class are separate governance axes.

## Context

Frozen E1 requires durable acknowledged authority and the closed architecture-level classes `AUTHORITATIVE STATE`, `DERIVED PROJECTION`, `EPHEMERAL WORKING CONTEXT`, and `LOSSY SUMMARY`, plus recoverable causal/operation evidence, corruption and partial-write handling, retention/deletion accountability and migration. Transcript, context, UI and telemetry cannot become truth. External reality is not transactionally owned.

## Decision

Propose C01's embedded persistence pattern: transactional current `AUTHORITATIVE STATE` plus append-only authoritative material history and explicit outbox/effect records, all owned by the sole core writer. These are descriptions/subtypes within `AUTHORITATIVE STATE`, not new architecture-level classes. The transaction boundary covers only core-owned authoritative records. Durable acknowledgement occurs only after the applicable authoritative commit is confirmed/reread.

Material history retains the causal, version, integrity and operation/effect facts required for audit, recovery, reconciliation and migration. It does not make C01 an event-sourced C03 hybrid: current authoritative records remain normative, and no deterministic reducer over an immutable journal is introduced as system authority.

Presentation/transcript/search/activity projections are `DERIVED PROJECTION`; transient model/tool buffers are `EPHEMERAL WORKING CONTEXT`; compacted summaries are `LOSSY SUMMARY` even when retained. Operational logs/telemetry are rebuildable observations over those sources and never a source of truth. A final validated evidence bundle is an immutable `AUTHORITATIVE STATE` evidence artifact owned by ADR-E2-007 and derived from, but never able to manufacture, authoritative source records.

ADR-E2-002 exclusively owns the canonical durable task/operation/approval/effect/evidence/material-history semantics required for correctness, recovery and migration. ADR-E2-008 may expose operational audit/log projections of those records, but it cannot create a second authoritative history. If an audit fact is required to recover, authorize, reconcile, verify or prove completion, it belongs here (or in ADR-E2-007 for evidence artifacts), not in telemetry merely because a log sink is durable.

Schema/history evolution is explicit, versioned, fail-closed and reversible where declared. Corrupt/incompatible records are quarantined with retained evidence; neither silent reset nor summary reconstruction is allowed.

## E1/E2 constraints and trace

- Primary ARs: `AR-COR-003`, `AR-DUR-001`, `AR-DUR-005`, `AR-DUR-006`, `AR-DAT-001`, `AR-DAT-002`, `AR-PRF-003`.
- Cross-cutting: `AR-CTX-001/002`, `AR-EVD-001..003`, `AR-COR-006`, `AR-DUR-003`.
- Domains: `D04_DURABLE_STATE_PERSISTENCE`, `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL`, `D06_EVENT_OPERATION_HISTORY`.

## Options considered

1. C01 transactional current state plus material history/outbox/effect ledgers.
2. C02 authoritative control-service store with service/worker protocol state.
3. C03 append-only material journal and immutable payloads with normative reducer authority and rebuildable projections.

## Rationale

C01 meets the same hard floor while keeping current-state semantics compact for the immediate local workflow. C03 has a verified replay/reconstruction advantage but introduces event identity/order/evolution, reducer and checkpoint commitments; C02 adds service protocol coupling. The proposal accepts C01's transactional record/history lock-in and requires export, integrity and replay-equivalence evidence.

## Rejected alternatives

C02 is not proposed because its state authority is tied to the unselected service topology. C03 is not proposed because full journal/reducer authority is not presently required. Neither is invalid; C03 should be reconsidered if deterministic causal reconstruction becomes a verified present hard requirement.

## Consequences and trade-offs

Positive: direct current-state reads, atomic local record updates, clear acknowledgement boundary, compact local operation and derived views.

Negative: transactional schema and history/effect meanings become foundational; cross-record evolution is complex; reconstruction is less intrinsically journal-centric than C03; broad core/store failures share a blast radius.

## Security implications

State classes carry explicit confidentiality, ownership, retention and evidence roles. Protected raw values never enter any class. Derived projections cannot authorize. Integrity/digest material is not itself authorization, privacy, erasure or completeness evidence. Retention/hold/deletion actions require exact scope and readback or explicit uncertainty.

## Recovery implications

Recovery loads the latest valid acknowledged state, verifies integrity/version, establishes a new owner epoch and replays/scans material history only to reconcile—not replace—canonical truth. Partial writes are rolled back or detected/quarantined. Filesystem/process/network effects are read back independently and may remain unknown.

## Evidence and verification implications

The verifier must access authoritative records and original evidence references without depending on a projection. Gap/tamper/staleness and migration state are first-class. Old schemas/evidence remain readable or have a verified migration/rollback path.

## Missing evidence and current evidence limit

No store, schema, transaction boundary, migration, corruption-quarantine, salvage, projection-rebuild, or rollback mechanism has been selected or exercised. `E3V-001/005/007` are unrun, so acknowledgement, recovery, integrity, migration compatibility, evidence reconstruction and finite-limit support remain architectural obligations rather than observed properties.

## Reversibility and migration

Store engines and projection implementations are `MODERATELY_COSTLY` behind ports. Canonical record meanings, acknowledgement boundary and material history/effect semantics are `FOUNDATIONAL_HIGH_COST`. Migration requires versioned export/import, identity/correlation preservation, integrity checks, dual-read or independently compared equivalence, nonterminal/effect reconciliation, retention of old evidence and a rollback checkpoint. Moving to C03 requires a prospective ADR reopening and an event semantic cutover.

## Future compatibility

Every principal/agent/task/message/workspace/operation/approval/artifact/provider/policy record has explicit scope/version/correlation fields; current singleton values are not permanent schema assumptions. Future multi-writer mechanics remain unimplemented.

## E3 validation obligations

- `E3V-001`: acknowledgement, partial-write, duplicate, owner and effect recovery.
- `E3V-003`: durable workspace/base identity and recovery source for package/workspace validation.
- `E3V-005`: authority/derived separation, evidence integrity, deterministic readback and stale invalidation.
- `E3V-007`: raw measurement inputs and enforceable finite limits without telemetry authority.

## Handback and reopen conditions

Canonical handback sets: `E3V-001 -> ADR-E2-002/003/004/005/007/008/009`; `E3V-003 -> ADR-E2-001/002/004/009`; `E3V-005 -> ADR-E2-002/003/004/005/006/007/008`; `E3V-007 -> ADR-E2-001/002/007/008/009`. Reopen on unavoidable acknowledged loss, nondeterministic authority, unrepairable schema/history ambiguity, required evidence loss or unrepresentable gate inputs. Ordinary store/codec/migration implementation defects remain correction work when a conforming C01 realization exists.

## Unresolved implementation details

Store technology; schema and codec; physical log/layout; integrity mechanism; transaction/flush primitives; retention/hold/GC; backup/restore; corruption salvage; migration tooling; encryption boundary; projection engine.

## Source evidence and provenance

Frozen E1 state/context/evidence contracts; E2 plan ADR boundary; architecture requirements §§3, 6, 9; C01 f06/f08/f09/f14/f15/f23/f28/f30; comparison §§7-8, 14, 18; closure §§9-10. Audit transactional/outbox/history/projection patterns are comparison inputs only, not copied mechanisms.
