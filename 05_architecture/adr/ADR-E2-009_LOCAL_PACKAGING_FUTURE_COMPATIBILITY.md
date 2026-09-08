# ADR-E2-009 — Local Packaging plus Future Remote, Multi-Client, Extension, General, Finance, and SaaS Compatibility Boundaries

ADR ID: `ADR-E2-009`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `REVERSIBLE_EARLY`

Decision status and reversibility class are separate governance axes. Later ecosystem adoption may raise migration cost, but that future condition does not create a fourth current class.

## Context

v0.1 must be locally installable, understandable, recoverable and testable by open-source contributors. It must preserve a credible migration path for remote execution, multiple clients/writers/agents, skills/routines/connectors, General/Finance and SaaS without implementing distributed, vertical or tenant features now. A hidden service/cloud dependency would violate local-first scope.

## Decision

Propose one contributor-operable local package/lifecycle containing the detachable client and task-bound integrated core, with explicitly owned child/verifier processes and no mandatory permanent service or cloud dependency. Exact packaging/update technologies are deferred.

Every replaceable boundary carries versioned serializable identities/contracts where future placement matters: principal, agent, task, conversation/message, workspace, operation/effect, approval, artifact/evidence, provider/model/configuration and policy; owner epoch/version/idempotency/correlation; capability/security/support declarations; schema/migration version.

Required now is limited to the local single-user product. Reserved compatibility includes remote executor/provider/capability ports, multiple-client reconciliation identities, later ownership/fencing, governed extension manifests and shared-core domain neutrality. Cloud workers, distributed queues, multi-agent messaging, routines/schedules, connectors/marketplaces, General/Finance product behavior, SaaS/multi-tenancy/billing/enterprise controls and production operations are deferred.

General and Finance may later be governed extension packs over the shared domain-neutral core. The core may not import Finance-specific schemas or depend on a pack. No finance, trading, customer or tenant behavior is selected.

## E1/E2 constraints and trace

- Primary ARs: `AR-PKG-001`, `AR-FUT-001/002/003`, `AR-PRF-002/004/006`.
- Cross-cutting: `AR-COR-001`, `AR-WSP-002`, `AR-SEC-002`, `AR-MOD-001`, `AR-EVD-002`.
- Domains: `D21_LOCAL_FIRST_PACKAGING`, `D22_FUTURE_REMOTE_EXECUTION`, `D23_FUTURE_CONCURRENCY_MULTI_AGENT`, `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY`; shared `D01_CLIENT_INTERACTION_BOUNDARY`.

## Options considered

1. C01 integrated local package with explicit extraction/adapter seams.
2. C02 visible persistent service/client/worker package optimized for later remote placement.
3. C03 local journal/runtime package with command/event adapter evolution.
4. Build distributed/SaaS/extension systems now (rejected).

## Rationale

C01 best matches the current local topology and contributor scope while satisfying the same future seam floor. C02 has the lowest direct remote-worker adaptation cost; C03 has replayable state portability; C01 must later extract boundaries. Future optionality cannot override v0.1 scope, and speculative distributed machinery would increase present burden without verified need.

## Rejected alternatives

C02 and C03 packaging shapes follow their rejected authority topologies. A hidden daemon, mandatory cloud service, immediate multi-tenant platform, generic marketplace or Finance implementation is rejected. They remain possible only through later authorized tasks and, for structural topology changes, reopened E2.

## Consequences and trade-offs

Positive: low mandatory process/lifecycle count; straightforward contributor start; current deployment has no cloud dependency; future identities/ports are explicit.

Negative: later remote/service extraction is more costly than C02; strict boundaries must be maintained within one package; compatibility contracts create documentation/testing burden; extension governance remains unimplemented.

## Security implications

Packaging must declare every process, file, update, network, credential and executable dependency surface; no installer/update action is implicitly authorized. Future extension packs require version/capability/provenance/signing/revocation/migration policy before use. Future scopes cannot reuse current global authority accidentally.

## Recovery implications

Install/update/migration must preserve authoritative records, evidence and nonterminal/effect truth or roll back visibly. No package operation may silently clean user state. Client/core lifecycle and verifier/process recovery remain explicit across supported platforms.

## Evidence and verification implications

E3 must show clean setup, declared process/component map, local operation/restart and contributor reproducibility for tested platforms. E5 later owns full clean-install/update/rollback, documentation, license/provenance, package and release-candidate checks.

## Missing evidence and current evidence limit

No package format, installer/updater, supported-platform matrix, clean setup, contributor reproduction, restart, rollback, capture-boundary, instrumentation, compatibility adapter, remote worker, concurrent agent, extension, edition or SaaS implementation exists. `E3V-003/006/007` and all E5 release checks are unrun, so no platform support, distribution readiness or future-feature operability is claimed.

## Reversibility and migration

Before ecosystem/release adoption, package and client mechanics are `REVERSIBLE_EARLY`. Published port identities and contributor lifecycle become `MODERATELY_COSTLY`. Remote/service migration must preserve authority and effect identities, complete a conformance/security matrix, provide export/import/rollback and introduce no silent support widening.

## Future compatibility

`REQUIRED_NOW`: local single-user persistent engineering agent and review/evidence flow.

`RESERVED_COMPATIBILITY`: remote placement, multi-client/multi-writer/agent identities, governed skills/routines/connectors and shared-core extension seams.

`DEFERRED_TO_LATER_STAGE`: actual remote/cloud workers, concurrency, multiple agents, groups, schedules/events, connectors, General/Finance behavior, SaaS/tenant/billing/enterprise and production deployment.

## E3 validation obligations

- `E3V-001`: package/runtime lifecycle preserves recoverability and future port identities.
- `E3V-003`: package/setup/support matrix and no hidden mandatory service.
- `E3V-004`: packaged provider boundary preserves explicit adapter/fallback semantics.
- `E3V-006`: packaged enforcement/capture boundaries remain complete.
- `E3V-007`: package/runtime instrumentation and enforceable limits.

## Handback and reopen conditions

Canonical handbacks: `E3V-001 -> ADR-E2-002/003/004/005/007/008/009`; `E3V-003 -> ADR-E2-001/002/004/009`; `E3V-004 -> ADR-E2-001/004/005/006/007/008/009`; `E3V-006 -> ADR-E2-001/004/005/007/008/009`; `E3V-007 -> ADR-E2-001/002/007/008/009`. Reopen if local operation necessarily requires an undeclared service/cloud, required setup/support is structurally unreproducible, or future compatibility cannot be preserved without breaking current authority semantics. Ordinary installer/docs/platform defects remain correction or narrow support.

## Unresolved implementation details

Language/runtime; client form; process packaging; installer/updater; dependency lock/provenance; supported OS/architectures/filesystems; migration/backup UI; extension manifest/signing/SBOM; remote transport; release distribution.

## Source evidence and provenance

D-001/D-016; frozen charter §§4, 14-15, 21-22 and contribution/release contracts; E2 plan; requirements `AR-PKG`, `AR-FUT`, preferences and E3V-003/006/007; C01 f19/f20/f22/f28/f30; comparison §§12-14, 17-18; closure §10 E4 bundles. External packaging/extension patterns are non-authoritative and no reconstructed product layout is copied.
