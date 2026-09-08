# ADR-E2-006 — Model/Provider Abstraction, Routing/Capability Discovery, and Context/Compaction Boundary

ADR ID: `ADR-E2-006`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `MODERATELY_COSTLY`

Decision status and reversibility class are separate governance axes.

## Context

Core product truth must remain provider/model neutral while preserving provider-specific streaming, tools, refusal, usage, stop, cancellation and error semantics. Route purpose and eligibility must be explicit; hidden fallback is forbidden. Model context is bounded and lossy; durable conversation, authority, effects and evidence must survive outside it. E2 may select the gateway shape but no provider, model, configuration or permanent role occupant.

## Decision

Propose C01's embedded provider-neutral gateway. It exposes versioned typed requests/results, explicit provider extensions and raw-evidence references; owns requested/resolved provider/model/config identity, `route_purpose`, `route_eligibility`, capability discovery, data/network/cost policy, explicit fallback decision and usage/missingness. Unsupported or disallowed routes dispatch zero bytes/calls/cost.

Provider-native sessions/state may assist an adapter but never define task, approval, effect, artifact, evidence or completion truth. A fallback is a separately admitted route with its own provenance; it never inherits the requested route's credit.

Context building is a derived projector over authoritative task/conversation/source/operation/evidence records. Compaction/summarization retains source identities, trust, versions, corrections, revocations, unresolved items and limitation metadata; stale or poisoned context is discarded. Model context can be truncated or lost without destroying authoritative state.

The logical roles `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER` and `SECURITY_REVIEWER` remain unassigned. The verifier also requires the independent path in ADR-E2-007; routing a second model alone does not create independence.

## E1/E2 constraints and trace

- Primary ARs: `AR-CTX-001/002`, `AR-MOD-001/002/003`.
- Cross-cutting: `AR-SEC-001/004`, `AR-EXE-001`, `AR-DAT-001`, `AR-FAIL-001`, `AR-PERF-001/002`.
- Domains: `D13_MODEL_PROVIDER_GATEWAY`, `D14_ROUTING_CAPABILITY_DISCOVERY`, `D15_CONTEXT_MEMORY_COMPACTION`.

## Options considered

1. C01 embedded gateway and derived context projector.
2. C02 gateway at persistent local service boundary.
3. C03 route/result commands/events with context projections from journal authority.
4. Direct provider integrations without a stable boundary (rejected).

## Rationale

The embedded gateway keeps provider policy close to C01's sole authority while preserving replacement. Service or event placement would import rejected topology. Direct integration would amplify provider lock-in and risk semantic erasure. No verified evidence supports a provider or role winner.

## Rejected alternatives

C02/C03 placements are not proposed because their authority topologies are not proposed. Lowest-common-denominator normalization, hidden fallback, consumer-session state as product authority, and role assignment from public reputation/current authoring surface are rejected.

## Consequences and trade-offs

Positive: core remains model/provider neutral; explicit semantics and zero-dispatch; context is safely disposable; adapters are replaceable.

Negative: provider differences expand the contract; adapter conformance and raw-evidence handling are substantial; gateway bugs share the core process; exact eligibility remains blocked until E3.

## Security implications

Every dispatch revalidates data, destination, credential, budget, purpose and eligibility. Model/provider output is untrusted data and cannot grant authority or prove completion. Raw protected input is excluded. Provider logs/raw evidence obey redaction, retention and provenance policy.

## Recovery implications

In-flight model calls have stable operation/route identity and explicit cancellation/result status. Restart never silently repeats a maybe-billed/effectful route, infers fallback or relies on provider session continuity. Context is rebuilt from authoritative current sources.

## Evidence and verification implications

Evidence includes requested/resolved route, exact known configuration/version, capability/eligibility authority, input classification, cancellation/stop/refusal/failure layer, fallback, usage/cost and missingness. Benchmark evidence remains evaluation-only until independent qualification and founder authorization.

## Missing evidence and current evidence limit

No provider adapter, routing implementation, semantic-conformance fixture result, context projector, supported configuration, capability measurement, live call, cost observation, model assignment, or benchmark result exists. `E3V-004/005/008` are unrun, so no provider/model/configuration is eligible for any logical role and no fallback, compaction or usage behavior is proven.

## Reversibility and migration

Provider adapters and routing policies are `REVERSIBLE_EARLY`; the provider-neutral semantic envelope/provenance is `MODERATELY_COSTLY`. Replacement requires offline conformance, preserved raw evidence links, no semantic loss, explicit fallback and context reconstruction equivalence.

## Future compatibility

New providers, open/self-hosted models or remote gateways may enter through the same contract after policy/evidence. No tenant routing, model marketplace, distributed router or permanent fallback hierarchy is implemented.

## E3 validation obligations

- `E3V-004`: offline provider-shape conformance first; live calls separately gated.
- `E3V-005`: context/source authority, stale summary and evidence interactions.
- `E3V-008`: separately authorized exact configuration qualification by logical role/task class.

## Handback and reopen conditions

Canonical handbacks: `E3V-004 -> ADR-E2-001/004/005/006/007/008/009`; `E3V-005 -> ADR-E2-002/003/004/005/006/007/008`; `E3V-008 -> ADR-E2-006` only if an indispensable ADR capability is impossible through every compliant route. Ordinary provider/model/config failure leaves the role unassigned. Reopen if the envelope structurally erases required semantics or provider-native state must become product authority.

## Unresolved implementation details

Gateway schema/transport; adapter SDKs; credential injection; raw-evidence storage; capability negotiation; data/region policy; token/context budgeting; compaction algorithm; model registry integration; qualified routes, configs and role occupants.

## Source evidence and provenance

D-004/D-016; frozen route/context contracts; model registry and benchmark plan; E2 plan; requirements `AR-MOD`, `AR-CTX` and E3V-004/005/008; C01 f13/f14/f23/f28/f30; comparison §§10, 13-14, 18; closure §9. External provider-router patterns are Level-B evidence only; no model or provider facts are promoted by this ADR.
