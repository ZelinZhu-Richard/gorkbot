# ADR-E2-005 — Capability, Permission, Approval, Secret, External-Effect, and Reconciliation Boundary

ADR ID: `ADR-E2-005`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `FOUNDATIONAL_HIGH_COST`

## Context

Untrusted repository/tool/model content must not broaden authority. Capabilities need typed runtime validation and deny-by-default scope. Consequential effects need exact human approval, durable receipts and authoritative readback. Protected values must never traverse ordinary model/input/log/evidence surfaces. External reality cannot share the core transaction, so uncertainty is a first-class outcome.

## Decision

Propose one integrated policy/capability/approval/effect authority in the C01 core, with replaceable target adapters and a distinct protected-entry controller.

Capability admission binds actor, task, current owner epoch, versioned capability/schema, normalized target/action, declared effect class, scope, limits, network/credential policy and expected result/readback. Invalid, stale, unknown, oversized or unauthorized requests dispatch zero effects.

Consequential effects use durable `INTENT -> APPROVAL -> ATTEMPT -> OBSERVED_EFFECT -> CONFIRMED_EFFECT | KNOWN_FAILURE | UNKNOWN_EFFECT` semantics. Approval is authenticated, inspectable, exact-scope, policy/version/base/owner bound, expiring or one-shot, revocable, mutation-detecting and replay-protected. It cannot widen task authority or enable a prohibited action. Dispatch has stable idempotency/effect identity; fresh target readback alone confirms success. Lost acknowledgement or contradictory truth yields `UNKNOWN_EFFECT` and prohibits blind retry/completion.

Protected acquisition/delivery uses a dedicated controller inside the trusted application boundary but outside ordinary request/model/transcript/terminal-output/log/telemetry/evidence/screenshot/accessibility capture. A one-use current recipient/use/fence grant delivers raw input only into transient protected memory; only a non-secret receipt returns. Crash, recipient/owner replacement, revocation or uncertain consumption requires reacquisition; raw input is never persisted or replayed. Missing protection returns `WAITING_FOR_USER`/blocked.

## E1/E2 constraints and trace

- Primary ARs: `AR-EXE-001`, `AR-SEC-001/002/003/006/004/005`, `AR-APR-001/002/003`.
- Cross-cutting: `AR-DUR-003`, `AR-COR-002`, `AR-EVD-002/003`, `AR-FAIL-001`, `AR-PERF-001`.
- Domains: `D11_APPROVAL_PERMISSION_SYSTEM`, `D12_EXTERNAL_EFFECT_RECONCILIATION`, `D20_SECURITY_BOUNDARIES`; shared capability/provider/evidence domains through ADRs 006-008.

## Options considered

1. C01 integrated policy/approval/effect authority and co-resident exact-recipient protected path.
2. C02 service authority with direct client-to-current-worker protected delivery under service-issued non-secret authorization/lease/fence.
3. C03 command admission/effect records with a raw-value broker outside journal/payload/projection authority.

## Rationale

C01 keeps exact authority and effect correlation on the shortest current path while maintaining adapters and a structurally separate protected controller. The candidate-specific protected-delivery seam is the most decision-sensitive residual, but E2-004 verified that testing before client/runtime selection would test an arbitrary mechanism, not distinguish architecture. It remains unproven and fail-closed under E3V-006.

## Rejected alternatives

C02 and C03 protected paths are coherent but inseparable from their rejected topologies. They are not cherry-picked. Conversational approval, caller Boolean flags, tool-name heuristics, model-enforced policy, raw-secret persistence and response-as-effect-proof are prohibited alternatives.

## Consequences and trade-offs

Positive: one authoritative policy/effect chain; explicit zero-dispatch and unknown outcomes; consistent exact approval; no raw secret in durable/general surfaces.

Negative: policy kernel and receipt/effect identities are foundational; every adapter must support accurate action classification/readback or remain unsupported; protected-entry surface is unselected and may narrow client support; the trusted core carries high assurance burden.

## Security implications

This ADR owns `TB-01`, `TB-03`, `TB-05`, `TB-08`, `TB-11`-`TB-17` and shares all other threat boundaries. Repository/model/tool text grants nothing. Secrets use least-scope exact recipient/use, no ambient child inheritance, no raw evidence/logging and revocation/reacquisition. Approval/replay/mutation, destination substitution, hidden fallback and external-effect ambiguity fail closed.

## Recovery implications

Recovery revalidates task authority, owner/base/policy/capability versions, approval validity/consumption, adapter/readback availability and every nonterminal effect. It never replays protected input or blindly repeats a maybe-dispatched action. Duplicates receive the first outcome; uncertainty remains durable.

## Evidence and verification implications

Evidence links intent, authority, approval/denial/revocation, attempt, adapter result, readback and final certainty without raw secrets. It records zero-dispatch proof, requested/effective target, bytes/calls/cost and independent readback. Protected entry records capture-state changes and a non-secret receipt only.

## Missing evidence and current evidence limit

No policy engine, grant/approval store, adapter, target-readback mechanism, protected-entry channel, capture-surface inventory, secret scanner result, or ambiguous-effect fault run exists. `E3V-001/004/005/006` are unrun; C01-specific `SPQ-E2-002-03` and residual `AR-SEC-006` remain open. This ADR therefore proves neither zero unauthorized effects nor safe protected-value delivery.

## Reversibility and migration

Individual adapters are `MODERATELY_COSTLY`; capability/approval/effect/protected-receipt semantics are `FOUNDATIONAL_HIGH_COST`. Migration preserves normalized action and effect identities, approval scope/use/revocation, policy versions, receipt/readback lineage and unknown outcomes. Client/adapter replacement must revalidate protected exact-recipient delivery and forbidden surfaces.

## Future compatibility

Explicit principal/task/workspace/capability/target/policy scopes prevent today's single user from becoming a permanent global singleton. Later tenant, connector or remote-worker boundaries may use the same semantics only after their own authorization/isolation evidence; none is implemented now.

## E3 validation obligations

- `E3V-001`: effect ambiguity, duplicate/lost-ack recovery.
- `E3V-004`: capability/provider adapter semantic and zero-dispatch behavior.
- `E3V-005`: evidence/authority integrity for approvals/effects.
- `E3V-006`: every trust/capability/approval/secret boundary, including C01-specific `SPQ-E2-002-03` protected delivery.

## Handback and reopen conditions

Frozen handbacks: `E3V-001 -> ADR-E2-002/003/004/005`; `E3V-004 -> ADR-E2-001/005/006/008`; `E3V-005 -> ADR-E2-002/003/005/007/008`; `E3V-006 -> ADR-E2-001/004/005/008`. Reopen if normalized identity cannot bind approval to execution/readback, if unknown effects cannot remain noncomplete, or if no conforming C01 protected acquisition/delivery path exists. A failed carrier/policy/adapter with another conforming realization is correction or unsupported class, not automatic handback.

## Unresolved implementation details

Policy representation; capability/schema tooling; approval UI; action canonicalization; receipt encoding; target-specific readback adapters; idempotency mechanism; credential broker/store; protected client/acquisition/carrier; capture exclusion primitive; supported external effects.

## Source evidence and provenance

Frozen approval/effect/secret/negative contracts; E2 plan; requirements §§4-5 and E3V-001/004/005/006; C01 f05/f07/f10/f12/f18/f23/f26/f30; comparison §§9-11, 14, 18; closure §§7-9 and E2-004 verifier N3/N9. External approval/capability patterns are non-authoritative inputs; no reconstructed mechanism is copied.
