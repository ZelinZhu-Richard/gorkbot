# ADR-E2-001 — System, Client, and Core-Runtime Boundary

ADR ID: `ADR-E2-001`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `FOUNDATIONAL_HIGH_COST`

## Context

Engineering Preview v0.1 needs one local user, one persistent named engineering agent, durable task ownership through client interruption, protected human takeover and a contributor-operable local lifecycle. The client must not become authoritative. Future remote or multi-client operation is compatibility scope, not current implementation scope.

## Decision

Propose C01's integrated task-bound persistent local core as the sole authoritative application runtime. A detachable local client submits authenticated commands and renders derived projections. Client exit/reload is non-authoritative while the core remains healthy. The core may remain headless for an accepted active task, but v0.1 requires neither a permanent installed daemon nor a cloud service. Full core loss is recovered as owner loss under ADR-E2-003, not misclassified as client-only continuity.

The integrated core contains separately versioned logical ports for persistence, orchestration/recovery, workspace/execution, policy/capabilities/effects, provider routing, evidence and projections. Untrusted child execution and independent verification remain separate execution contexts. Protected entry is a dedicated controller outside ordinary input/model/log/evidence capture; its concrete client mechanism is deferred.

## E1/E2 constraints and trace

- Primary preference assignment: `AR-PRF-001`.
- Cross-cutting hard constraints: `AR-COR-001/002`, `AR-DUR-002`, `AR-DAT-001`, `AR-SEC-001/006`, `AR-MOD-001`, `AR-PKG-001`, `AR-FUT-001/002`.
- Domains: `D01_CLIENT_INTERACTION_BOUNDARY`, `D02_CORE_APPLICATION_RUNTIME`; shared `D21_LOCAL_FIRST_PACKAGING` and `D22_FUTURE_REMOTE_EXECUTION` through ADR-E2-009.
- E1 interaction/control evidence includes `EP-CTL-016`: a client-only detach must be distinguishable from full-core shutdown.

## Options considered

1. C01 integrated transactional local core.
2. C02 persistent user-local control service with replaceable leased/fenced workers.
3. C03 command/event and journal/reducer core with rebuildable projections.

## Rationale

All options pass the hard comparison. D-016 scope makes local single-user operation required now and remote/multi-worker operation reserved. C01 gives the current workflow the shortest authority/control path and no mandatory service/IPC/lease lifecycle while retaining replaceable ports. This is qualitative scope precedence, not a weighted rank or a claim that fewer processes are automatically better.

## Rejected alternatives

- C02 is not proposed because permanent service lifecycle, IPC/authentication and worker leasing add present surfaces before replaceable remote workers are required. Reopen if remote worker replacement or service continuity becomes a present hard property.
- C03 is not proposed because event/reducer/projection authority adds present semantic burden. Reopen if causal replay or coordinator-free operation becomes a present hard property.
- No hybrid is permitted without a new candidate comparison.

## Consequences and trade-offs

Positive: simple local lifecycle; direct current-state access; short in-process traces; detachable presentation; no hidden mandatory service.

Negative: a core crash affects scheduling, policy and persistence access together; strict internal ports must prevent a monolith; later service/remote extraction is substantial; no real-time deadline enforcement exists while the entire core is absent.

## Security implications

The client is a derived/untrusted presentation surface. Authentication and admission terminate at the core; client presence, text and cached projections grant no authority. Protected entry bypasses ordinary capture, and untrusted process/provider/verifier paths remain separately constrained. A broad trusted core increases review burden and may not rely on in-process memory separation alone for secrets or untrusted execution.

## Recovery implications

Client reconnect rebuilds projections without task-state mutation. Core restart establishes a new owner epoch, reconciles all nonterminal operations/effects and invalidates stale client commands. Full shutdown fences children and preserves durable truth; overdue state is classified on restart.

## Evidence and verification implications

Evidence must show client/core lifetime distinction, source versions for every projection, exact core owner epoch and separate verifier context. `EP-CTL-016` must not be passed by keeping authority only in the client.

## Missing evidence and current evidence limit

No client/core implementation, process-lifetime test, packaging trial, provider-boundary conformance result, or protected-entry capture-exclusion result exists. `EP-CTL-016` and `E3V-003/004/006` are unrun, so this ADR establishes only a proposed ownership boundary; it does not prove headless continuity, local operability, provider isolation, or secret safety.

## Reversibility and migration

Client and presentation adapters are `REVERSIBLE_EARLY`. The integrated authority/lifetime boundary is `FOUNDATIONAL_HIGH_COST`. Migration to C02-like service topology requires extracting versioned core ports, authority-preserving state transfer, authenticated IPC, ownership/lease translation, nonterminal drain/reconciliation and rollback. Migration to C03-like authority requires E2 reopening and a state/history semantic conversion, not an implementation refactor.

## Future compatibility

The client/core command/result and projection ports must be serializable and scoped by principal, agent, task, workspace, operation and policy versions. This preserves later multiple clients or remote placement without implementing them now.

## E3 validation obligations

- `E3V-003`: local packaging, client/core lifecycle and contributor setup.
- `E3V-004`: provider-gateway placement/semantic conformance.
- `E3V-006`: protected acquisition and ordinary-capture exclusion.

## Handback and reopen conditions

- `E3V-003` structural mandatory-service or local-boundary contradiction hands back the frozen `ADR-E2-001/004/009` set.
- `E3V-004` interface-level placement/semantic contradiction hands back `ADR-E2-001/005/006/008`.
- `E3V-006` inability to provide a conforming protected client boundary hands back `ADR-E2-001/004/005/008`.
- Reopen if a prospective verified E1 amendment makes service continuity, remote execution or multi-client ownership required now.

## Unresolved implementation details

Client form; language/runtime; process-lifetime mechanism; local authentication; headless lifecycle; projection transport; installer/updater; protected-entry UI/carrier; supported platforms.

## Source evidence and provenance

Frozen E1 charter §§4, 6, 15, 19; architecture plan ADR map; requirements `AR-*` and §9; C01 f02-f04/f19/f20/f28/f30; comparison §§6, 12-14, 17-18; verified no-spike closure and E2-004 verifier notes N2-N4/N9. External audit patterns are non-authoritative Level-B inputs only; no Level-C implementation is imported.
