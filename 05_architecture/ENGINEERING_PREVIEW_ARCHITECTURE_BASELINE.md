# Engineering Preview Proposed Architecture Baseline

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Task: `E2-005`

Proposed candidate: `EP-ARCH-C01` — Integrated Transactional Local Core

Selection authority: E2-005 may recommend one verified survivor and author a proposed baseline and proposed ADRs. It may not accept an ADR, independently select or verify the architecture, pass the E2 gate, begin E3, or authorize implementation.

Architecture selected: `false`

Accepted ADR count: `0`

## 1. Decision statement

E2-005 proposes `EP-ARCH-C01` unchanged as the Engineering Preview v0.1 architecture baseline. This is a qualitative proposal from the three independently verified, analytically viable candidates. It is not a score, rank, implementation result, or claim that C01 is universally superior.

The decision rule is:

1. Hard constraints are non-compensating. Each candidate has the same verified comparison result: 57 hard requirements confirmed for comparison, two architecture seams confirmed with E3 validation outstanding, and zero hard violations.
2. Confirmed D-016 scope precedence controls unresolved preferences: the local-first, single-user Engineering Preview is `REQUIRED_NOW`; remote execution, concurrent tasks, multiple agents/clients, extensions, General/Finance, and SaaS are `RESERVED_COMPATIBILITY` or later-stage work.
3. Within that scope, C01 supplies the shortest current authority/control path and avoids requiring a permanent local service, service IPC/authentication, worker-lease lifecycle, or journal/reducer/projection authority model before those structures earn present value. Sensitivity profiles A and D support this current-shape advantage; they do not establish an overall rank.
4. C01's costs are accepted openly: the integrated core has a wider crash/coupling radius, remote execution later requires interface extraction, and its transactional state/history/effect meanings are foundational. ADR boundaries, replaceable ports, migrations, and explicit reopen triggers contain rather than deny those costs.
5. Missing E3 evidence receives no favorable interpretation. C01's descendant containment/fencing and protected acquisition/delivery remain unproven under `E3V-002` and `E3V-006`; every other canonical E3V obligation also remains unrun.

This proposal does not combine C02 service/lease topology or C03 journal/reducer authority into a new candidate. C01's own append-only material history, outbox/effect ledgers, derived projections, supervisor port, provider gateway, and future adapter seams remain exactly the candidate-defined C01 shape. There is no hidden C04.

### 1.1 Candidate disposition

| Candidate | Verified strengths preserved | E2-005 disposition | Why not proposed for v0.1 | Reopen conditions |
|---|---|---|---|---|
| `EP-ARCH-C01` | Minimal mandatory local topology; short authority path; compact current-state access; in-process traceability; no mandatory daemon or cloud service. | **PROPOSED**, pending E2-005 challenge/fix/task verification and fresh E2-006 architecture verification. | Not applicable. Its broad-core coupling, crash radius, later extraction cost, and foundational state semantics remain risks. | Reopen this proposal if E3 disproves a linked structural assumption, contributor/setup evidence shows the integrated boundary is untenable, or a frozen product amendment makes remote worker replacement or causal replay a present hard requirement. |
| `EP-ARCH-C02` | Clearest direct remote-worker seam; replaceable leased/fenced workers; worker fault isolation; explicit subsystem boundaries. | Analytically viable, not proposed. | Its mandatory user-local service, IPC/authentication, lease/fence, correlation, and lifecycle surfaces add present operational and security burden before remote/multi-worker behavior is in v0.1 scope. | Reconsider if verified requirements make independently replaceable remote workers, service continuity across all client lifetimes, or multiple execution owners present requirements rather than compatibility seams. Migration requires extracting C01 control/state ports into a service and introducing versioned IPC plus lease/effect protocols. |
| `EP-ARCH-C03` | Strongest causal replay/reconstruction and projection rebuilding; deterministic reducer fixtures; coordinator may be absent. | Analytically viable, not proposed. | Its event identity/order/evolution, immutable payload, reducer, checkpoint, projection, retention, and rebuild concepts impose a larger present semantic and contributor burden than the verified single-user local workflow requires. | Reconsider if verified evidence makes full causal reconstruction, independently replayable projections, or coordinator-free operation decisive. Migration requires defining an event cutover, dual-read/verification period, transactional-state export, reducer equivalence, and rollback checkpoint. |

### 1.2 Six qualitative preferences, without weights

The six preference criteria break the hard-constraint tie only through an explicit prospective priority: minimize the mandatory topology and authority-path burden for the confirmed D-016 `REQUIRED_NOW` scope. No numeric weight, aggregate score, hidden rank, measured performance claim, or compensation for a hard failure is used.

| Preference | C01 trade-off | C02 trade-off | C03 trade-off | Proposal implication |
|---|---|---|---|---|
| `AR-PRF-001` interactive/control latency | Fewer top-level local crossings; latency is unmeasured. | Service, IPC and worker crossings add hops; latency is unmeasured. | Append, reduce and project steps add work; latency is unmeasured. | C01 has the shortest prospective path for current scope, subject to `E3V-007`; this is not a performance result. |
| `AR-PRF-002` operational/maintenance complexity | One runtime reduces lifecycle count but concentrates broad-core coupling. | Service, IPC, lease and fence lifecycles trade against narrower subsystem ownership. | Event, reducer, projection, checkpoint and migration concepts add learning burden. | C01 avoids mandatory present lifecycles; its coupling cost remains explicit and no universal complexity winner is claimed. |
| `AR-PRF-003` migration/reversibility | State export is possible; extracting integrated authority is costly. | Clients/workers are replaceable; service, store and protocol semantics remain foundational. | Adapters/projections are replaceable; event semantics/evolution remain foundational. | No candidate has an overall reversal advantage. C01's costly commitments are accepted only with the ADR migration contracts and `E3V-001` handback. |
| `AR-PRF-004` remote/concurrency adaptation | Serializable ports exist; remote control requires authority extraction. | Direct worker seam; remote authentication and transport remain absent. | Serializable dispatch; remote transport and authority remain absent. | C02 is the clearest direct future remote-worker seam and C03 also has a strong serializable boundary. C01 is still proposed because remote/concurrent execution is not required now. |
| `AR-PRF-005` evidence/large-output overhead | Transactional current reads may reduce topology overhead; evidence cost is unmeasured. | Service history plus inbox/outbox paths may add overhead; cost is unmeasured. | Journal, payload, replay and projection paths may add overhead; cost is unmeasured. | C01 has a compact prospective current-state path, but no overhead winner exists until `E3V-007`. C03 retains the strongest reconstruction property. |
| `AR-PRF-006` contributor/local packaging burden | One package/runtime is topologically simple; broad-core ownership/docs are heavier. | Multi-process setup/debugging are heavier; subsystem boundaries are narrower. | No daemon is required; event/replay concepts raise contributor burden. | C01 best matches the present single-package lifecycle assumption, subject to `E3V-003`; documentation and coupling remain acceptance risks. |

### 1.3 Seven-profile sensitivity cross-check

Every verified sensitivity profile was considered. The profiles remain conditional lenses rather than weights, scores, ranks, or independent selection rules.

| Profile | Verified comparative signal | Effect on the C01 proposal |
|---|---|---|
| A. Minimal local topology | C01 gains from one integrated core; C03 also avoids a mandatory service. | Directly supports current D-016 scope fit, while operational cost remains unmeasured. |
| B. Recovery rigor | C03 has the clearest journal-position/reducer reconstruction; all candidates retain external-effect ambiguity. | Preserves C03 as the stronger replay alternative and makes recovery/history evidence plus a replay-driven reopen trigger mandatory; it does not invalidate C01's hard recovery seam. |
| C. Future remote evolution | C02 has the most direct worker seam; C03 also benefits from command/event adapters. | Counts against C01, whose authority/control extraction is costlier. D-016 keeps this future optionality from overriding current mandatory burden. |
| D. Contributor accessibility | C01 has one visible runtime, C02 narrower subsystems, and C03 deterministic replay fixtures. | Supports C01's present setup topology but keeps broad-core coupling/documentation under `E3V-003`; no contributor result is assumed. |
| E. Migration reversibility | No stable overall advantage; each candidate has a different lock-in center. | Requires explicit foundational commitments, export/import/rollback evidence and direction-specific reopen triggers; gives C01 no favorable universal reversibility credit. |
| F. Security-boundary clarity | C01 centralizes authority, C02 physicalizes more boundaries, and C03 makes admission/event flow explicit; no stable overall winner. | Requires C01's in-process semantic boundaries, separate child/verifier processes and protected path to remain externally testable under `E3V-002/004/005/006`. |
| G. Testability/debuggability | C03 gains replay fixtures, C02 substitution/fault isolation, and C01 short in-process traces. | Supports no overall winner; C01 must expose the entire frozen fault/readback suite and dangerous compositions without relying on low component count. |

Profiles A and D supply the strongest present-scope reason for C01. Profiles B, C and G preserve material C02/C03 advantages; E and F explicitly produce no stable candidate-wide advantage. The proposal therefore does not emerge from cherry-picking only favorable profiles.

### 1.4 Nineteen Level-B pattern-family dispositions

Level-B evidence supplies implementation-neutral pattern families only. The table preserves all 19 candidate-record dispositions and assigns each to a proposed ADR. It does not import any Level-C engine, schema, module, identifier, asset, layout, constant, provider, algorithm, framework, or observed external behavior.

| Pattern | Family | C01 disposition and boundary | Proposed ADR owner |
|---|---|---|---|
| `LB-01` | Canonical authority/checkpoints/roots/reachability/migration | `USED`: single authority root, snapshots and migration ledger; no engine/schema selected. | `ADR-E2-002` |
| `LB-02` | Content-addressed identity/referents | `NOT_USED`: stable record/artifact identity plus integrity metadata is sufficient; privacy, retention and deletion questions stay unresolved. | `ADR-E2-007` |
| `LB-03` | Derived projections/transcript rebuilding | `USED`: client, summary and context views rebuild from authority. | `ADR-E2-002`, `ADR-E2-006` |
| `LB-04` | Authority/history persistence alternatives | `USED`: transactional current state plus material history/outbox defines C01. | `ADR-E2-002` |
| `LB-05` | Operation journal/recovery | `USED`: durable operation/effect ledgers support deduplication and recovery without event-sourced authority. | `ADR-E2-003`, `ADR-E2-005` |
| `LB-06` | Typed failure registry | `USED`: layered typed failures drive bounded retry and recovery. | `ADR-E2-008` |
| `LB-07` | Typed process ports/owned boundaries | `USED`: typed supervisor and gateways isolate untrusted execution. | `ADR-E2-001`, `ADR-E2-004` |
| `LB-08` | Provider/router abstraction | `USED`: embedded provider-neutral gateway preserves role/provider neutrality. | `ADR-E2-006` |
| `LB-09` | Explicit task/execution state | `USED`: orthogonal durable records and legal transitions. | `ADR-E2-003` |
| `LB-10` | Structured approvals/capability receipts | `USED`: exact one-shot approval and scoped grants. | `ADR-E2-005` |
| `LB-11` | Local/remote execution abstraction | `USED`: local executor implements a versioned replaceable port; remote execution remains reserved. | `ADR-E2-004`, `ADR-E2-009` |
| `LB-12` | Long-running/cloud-agent lifecycle | `SUBSUMED`: local disable/retire/ownership semantics live in task/control state; cloud lifecycle is deferred. | `ADR-E2-003`, `ADR-E2-009` |
| `LB-13` | Context compaction/structured summary blocks | `USED`: versioned lossy summary plus context manifest. | `ADR-E2-006` |
| `LB-14` | Direct adapters versus capability gateway | `USED`: one core gate precedes ordinary adapters; protected raw delivery is a separate one-use path. | `ADR-E2-005` |
| `LB-15` | Concurrency/multi-writer safety | `USED`: single writer plus versions/epochs rejects stale activity and reserves future scopes. | `ADR-E2-003`, `ADR-E2-009` |
| `LB-16` | Telemetry/audit/evidence/presentation topology | `USED`: semantic separation exists inside one local-store boundary. | `ADR-E2-007`, `ADR-E2-008` |
| `LB-17` | Corruption quarantine/salvage/migration recovery | `USED`: startup quarantine and versioned migrations are proposed. | `ADR-E2-002` |
| `LB-18` | Evidence packets/manifests/anchors/drift/attestations | `USED`: versioned manifests plus drift/stale checks; attestations are not required. | `ADR-E2-007` |
| `LB-19` | Extension/vertical-package boundary | `USED`: a versioned capability contract reserves bounded extensions. | `ADR-E2-009` |

## 2. Proposed system shape

```text
detachable local client / presentation (non-authoritative)
                    |
                    v
integrated task-bound persistent local core (sole authoritative writer)
  |-- admission, policy, task/orchestration and recovery coordinator
  |-- embedded authoritative-state/history/effect persistence port
  |-- workspace + filesystem/Git broker
  |-- owned execution supervisor ------> bounded untrusted child process tree
  |-- capability/approval/effect gateway
  |-- protected-entry controller ------> exact transient recipient only
  |-- provider-neutral model gateway --> explicit provider adapters later
  |-- evidence builder + derived presentation/context projections
  |
  +---- immutable review candidate/evidence references
                         |
                         v
separate least-privilege verifier process/context/workspace (non-authoring path)
```

The client is detachable and never owns task truth. Closing or reconnecting only the client is a presentation event while the task-bound core remains healthy. The core may remain headless while its accepted task is active, but v0.1 does not require an installed permanent daemon or hidden service. Full core exit is an owner-loss event and invokes restart reconciliation; it is not misreported as client-only continuity.

The core is the single accountable writer for authoritative local records. It owns admission, policy, orchestration, owner epochs, recovery, capability dispatch, approval/effect correlation, routing provenance, evidence assembly, and projection invalidation. It delegates untrusted execution to an owned supervisor/process boundary and verification to a separate least-privilege execution path. Logical separation inside the core is enforced through typed, versioned ports and state categories; model memory or prose never enforces policy.

The persistence pattern is transactional current state plus append-only material history and outbox/effect records. A local transaction covers only core-owned authoritative records. It never claims atomicity across filesystem, process, Git, network, provider, or other external reality. Those boundaries use durable intent, stable operation/effect identity, at-most-one admitted dispatch where feasible, observation, target readback, reconciliation, and explicit uncertainty.

No client framework, programming language, database product, schema library, process API, isolation technology, secret store, provider SDK, model, package system, installer, or update technology is selected here.

## 3. Ownership and state classes

| Concern | Class | Proposed owner | Persistence/reconstruction rule |
|---|---|---|---|
| Agent identity; task identity, contract, scope, plan, limits, predicates and status tuple | `AUTHORITATIVE` | Integrated core / canonical-state port | Versioned durable records; acknowledged only after authoritative commit and reread; never reconstructed from transcript. |
| Durable conversation/message ordering, authorship, authority context and source references | `AUTHORITATIVE` | Integrated core / canonical-state and material-history ports | Retained at the detail needed for authorization, recovery, audit and verification; summaries cannot replace it. |
| Owner epoch, operation identity/status/outcome, control, retries, cancellation, fences and first outcome | `AUTHORITATIVE` | Core recovery/orchestration coordinator | One current writer epoch; stale writes/results/effects rejected; nonterminal records reconciled on recovery. |
| Approval/refusal/revocation/consumption and effect `INTENT`/`ATTEMPT`/observation/readback | `AUTHORITATIVE` | Capability/approval/effect gateway plus core ledger | Exact normalized scope, one-use/replay protection, policy and owner version; uncertainty remains durable. |
| Workspace identity, repository/base binding, ownership, support-class disposition and before/after facts | `AUTHORITATIVE` | Workspace broker plus core record | Bound before mutation; fresh readback invalidates stale bindings; external bytes remain external truth. |
| Requested/resolved route, purpose, eligibility, capability/configuration, fallback, usage/cost and provider result provenance | `AUTHORITATIVE` | Provider-neutral gateway plus core record | Provider-specific semantics remain visible; denied/unknown route dispatches zero bytes/calls/cost. |
| Artifact/evidence identities, provenance, integrity/gap/staleness state, candidate revision and verification run/verdict | `AUTHORITATIVE` | Evidence builder, artifact boundary and independent verifier | Frozen candidate and bundle references are immutable; any material mutation invalidates the current pass. |
| Material causal/operation history needed for recovery, reconciliation, audit and migration | `AUTHORITATIVE` | Append-only material-history port owned by core | Append-only semantics with integrity/evolution state; it complements transactional current state and is not C03 event-sourced authority. |
| Transcript/activity/search/UI views, dashboards, context windows and summaries | `DERIVED` | Projection/context components | Rebuild from authoritative sources; version and provenance checked; stale or poisoned view discarded. |
| Final validated evidence bundle representation | `AUTHORITATIVE_ARTIFACT_DERIVED_FROM_AUTHORITY` | Evidence builder then independent verifier | Derived construction becomes a versioned immutable candidate artifact only after schema/integrity binding; it still cannot manufacture missing source evidence. |
| Optional telemetry, sampled performance views and presentation logs | `LOSSY` | Observability adapters | Never authorize, recover, prove completion, or replace audit/evidence; missing samples are explicit. |
| Live stream fragments, process handles, in-memory caches and temporary working buffers | `EPHEMERAL` | Owning adapter/process | May disappear. Anything required for acknowledgement, recovery, effect truth or proof must be promoted durably first. |
| Model working context and compacted summaries | `LOSSY_DERIVED` | Context projector | Source/provenance/version bound; may be discarded; cannot overwrite task, message, effect, approval, evidence or verification authority. |

## 4. Process, authority and trust boundaries

| Boundary | Authority and allowed flow | Fail-closed behavior |
|---|---|---|
| Client ↔ core | Authenticated user intent, controls and display requests enter typed admission; projections leave. Client text/presence is not truth. | Invalid/stale request is denied or waits; client loss changes no durable task fact. |
| Core ↔ authoritative persistence | Sole-writer epoch, expected versions and transaction boundary over core records only. | Failed/ambiguous commit is reread; no acknowledgement or productive resume until resolved. |
| Core ↔ workspace/filesystem/Git | Scoped, versioned operations against pinned workspace/object identity. | Unknown topology, root/ownership ambiguity, stale workspace or unsafe helper class blocks access/mutation. |
| Core ↔ execution supervisor/children | Capability envelope, process-tree ownership, limits, cancel/force/fence and result validation. | Unsupported containment class stays blocked/fenced; stale child cannot publish or effect. |
| Core ↔ capabilities/network/external targets | Exact grant, approval when required, stable effect identity and authoritative readback. | Zero dispatch before grant; after ambiguous dispatch, `UNKNOWN_EFFECT` blocks completion and blind retry. |
| Protected entry ↔ exact recipient | Capture-excluded, transient, one-use value flow outside ordinary input/model/log/evidence; only non-secret receipt returns. | If exclusion/binding cannot be established, fail to `WAITING_FOR_USER`; never replay raw value. |
| Core ↔ provider adapter | Explicit purpose/eligibility/capability/configuration and provider-native semantic preservation. | Denied/unknown route sends zero bytes/calls/cost; no hidden fallback. |
| Candidate/evidence ↔ independent verifier | Read-only exact-revision manifest and authoritative evidence/readback through a separate context/workspace. | Invalid independence, stale candidate, inadequate predicates, verifier error or missing proof leaves `UNVERIFIED`. |

The unsupported-host assumption remains explicit: a fully compromised kernel, privileged administrator, firmware or physical-storage adversary is outside the v0.1 guarantee. No process, worker, container or encryption mechanism is assumed to be a security boundary without E3 evidence for its claimed class.

## 5. Twenty threat-boundary instantiation

| ID | C01 enforcement location | Required evidence and recovery consequence |
|---|---|---|
| `TB-01` user/founder authority | Core admission and policy kernel. | Principal/request/authority version and zero-effect denial; reauthenticate and never infer consent. |
| `TB-02` repository content | Admission classifier and workspace broker. | Base/condition/scope/canaries; stale identity invalidates workspace. |
| `TB-03` instruction precedence | Instruction interpreter plus policy kernel. | Source/trust/precedence/conflict record; discard poisoned derived context. |
| `TB-04` filesystem scope | Workspace/filesystem broker at resolution, access, mutation and cleanup. | Resolved object identities/canaries; ambiguity blocks. |
| `TB-05` secrets/private data | Secret classifier and protected-entry controller. | Non-secret recipient/use receipt only; reacquire after recovery. |
| `TB-06` path/link traversal | Object/descriptor identity checks in workspace broker. | Pre/post resolution; link/topology race denies. |
| `TB-07` process execution | Owned execution supervisor and core authority fence. | Tree/limits/timeline/termination/fence evidence; survivors remain fenced and task blocked. |
| `TB-08` terminal I/O | Bounded I/O multiplexer; protected entry bypasses ordinary capture. | Inert bounded output or wait; raw protected input never replayed. |
| `TB-09` package scripts | Capability gateway, execution supervisor and network gate. | Script identity/grant/process/network outcome; retrieval never implies execution. |
| `TB-10` Git hooks/helpers | Sanitized Git adapter plus capability gateway. | Git/effect row and fresh refs/index/worktree; unsupported helper flow denied. |
| `TB-11` network | Destination/data/credential/budget policy before adapter dispatch. | Requested/effective target and bytes/calls/cost; redirects revalidated. |
| `TB-12` remote Git | Git adapter, approval gate, network gate and effect ledger. | Intent-to-readback chain; lost acknowledgement remains unknown, no blind retry. |
| `TB-13` external APIs | Capability/provider gateway and effect ledger. | Normalized request/idempotency/response/readback/usage; ambiguous effect reconciled. |
| `TB-14` model/provider | Provider gateway and result validator. | Requested/resolved route, eligibility, failure, usage/cost; output cannot grant authority or prove completion. |
| `TB-15` tool/capability | Versioned schema/capability/policy at request and result. | Unknown/malformed request denied; invalid post-dispatch result enters reconciliation. |
| `TB-16` approvals | Durable approval ledger serialized with dispatch admission. | Exact display/scope/version/revocation/consumption; stale/replay/mutation denied. |
| `TB-17` external effects | Effect ledger and target-specific readback adapter. | Intent/attempt/observed/confirmed chain; unknown blocks completion. |
| `TB-18` evidence integrity | Evidence builder/validator and separate verifier. | Manifest/provenance/gap/tamper/staleness results; invalid evidence blocks verification. |
| `TB-19` recovery/replay | Core startup recovery coordinator and owner epoch. | Recovery scan and rejected stale activity; reconcile every nonterminal operation before work. |
| `TB-20` protected human entry | Dedicated controller outside ordinary input/model/log/evidence capture. | Capture-state transitions and non-secret receipt; failure becomes wait/closed. |

## 6. Approval and external-effect model

Every potentially consequential effect uses this durable semantic chain:

```text
INTENT -> APPROVAL (when required) -> ATTEMPT -> OBSERVED_EFFECT
       -> CONFIRMED_EFFECT | KNOWN_FAILURE | UNKNOWN_EFFECT
```

- `INTENT` binds task, operation, actor, normalized action, exact target/resource, capability/effect class, arguments or inspectable content reference, policy/version, idempotency identity, base/owner epoch and expected readback.
- `APPROVAL` is authenticated, versioned, scoped, expiring or one-shot, revocable, mutation-detecting and replay-protected. Conversational confirmation is not approval. Approval cannot broaden admitted task authority or enable a prohibited v0.1 action.
- `ATTEMPT` is persisted before dispatch with stable dispatch/effect identity. A duplicate intake returns the first recorded outcome; it does not create another attempt.
- `OBSERVED_EFFECT` records adapter/target observations without treating a transport response as authoritative success.
- `CONFIRMED_EFFECT` requires fresh target-specific authoritative readback correlated to the exact attempt.
- `UNKNOWN_EFFECT` records that an effect may have occurred but truth is unavailable or contradictory. It is noncomplete, survives restart, and prohibits blind retry.
- Revocation or staleness before dispatch denies with zero effect. A dispatch/revocation/crash race is reconciled from durable ordering and readback; ambiguity stays unknown.

## 7. Recovery and reconciliation baseline

| Scenario | Durable basis | Required response | Permitted terminal knowledge |
|---|---|---|---|
| Client-only exit/reload | Task/core owner epoch and state remain live. | Rebuild presentation; do not pause/cancel/delete task. | Existing operation truth unchanged. |
| Integrated-core process crash | Transactional records, history, operation/effect ledgers. | New core instance establishes a new owner epoch, scans every nonterminal operation and revalidates policy/workspace/approval/route. | `KNOWN_SUCCESS`, `KNOWN_FAILURE`, or `UNKNOWN_OUTCOME`; never fabricated continuity. |
| Host restart | Same durable records plus host/workspace/process readback. | Recover as core loss; discover/fence surviving processes; reconcile bytes/Git/effects before productive work. | Same three-way knowledge. |
| Owner failure or stale owner | Owner epoch and expected versions. | Reject all old writes/results/approvals/effects; transfer ownership only after durable fence. | Rejected stale activity plus current outcome. |
| Worker/coordinator/child failure | Operation identity, supervisor tree and fence state. | Cancel/force where supported, always remove productive/effect authority, retain partial output and reconcile. | Known failure or unknown effect where dispatch crossed boundary. |
| Duplicate input | Client nonce/task identity and first outcome. | Return the original admission/outcome; create no duplicate task/effect. | Original recorded result. |
| Duplicate operation | Stable operation/idempotency identity. | Return first outcome or current nonterminal state; never redispatch blindly. | Original or explicit unknown. |
| Duplicate effect or acknowledgement loss | Stable request/operation/effect identity, committed acknowledgement/first outcome, attempt record and target readback. | A reconnect/retry with the same identity returns the committed acknowledgement or first outcome without redispatch; an ambiguous external effect is read back at the target and remains unknown if truth cannot be recovered. | Original acknowledgement/outcome, one confirmed effect, known failure, or explicit unknown. |
| Partial authoritative-state write | Transaction boundary, integrity/version metadata and prior record. | Roll back or detect/quarantine; reread before acknowledgement or resume. | Valid prior/new state or blocked corruption; never silent partial truth. |
| Partial filesystem write | Operation record plus fresh byte/object/Git readback. | Preserve actual bytes, classify partial state, repair only under current authority, invalidate old evidence. | Known bytes plus partial/failed/blocked; no cross-boundary rollback fiction. |
| Stale workspace/base/topology | Workspace binding, base identity, canaries and current readback. | Invalidate binding; preserve user material; rebind or block. | Known safe state or explicit ownership uncertainty. |
| Stale/expired/revoked approval | Approval tuple, owner/base/policy versions and consumption state. | Deny dispatch; request new approval only after current task authority is valid. | Zero dispatch or reconciled uncertainty if a race crossed dispatch. |
| Stale verification | Candidate revision, evidence version and immutable run. | Keep old verdict historical; set current candidate `UNVERIFIED`; require a new run. | Old revision result only; current state unverified. |
| Pause/stop/force-stop | Durable ordered control plus process/effect state. | Launch no new productive work; cancel/force where supported, fence always, reconcile in-flight effects and persist checkpoint/final disposition. | Cancelled/paused/blocked with known or unknown operation outcomes. |
| Full-system shutdown | Durable control/shutdown intent, owner epoch, process tree and nonterminal scan. | Fence and stop children within supported bounds; on restart classify overdue/surviving work before resumption. | No claim of real-time enforcement while no owner is live; truth recovered/read back. |

No row claims global transactionality across core records and external reality.

## 8. Execution and isolation baseline

- Potentially mutating reproduction or work begins only after a task-identified isolated workspace is bound and original user state is inventoried.
- The minimum supported untrusted-execution claim is the verified technology-neutral Tier 2 semantic floor: normalized allowed roots/object identity, process ownership, declared working directory/environment, bounded time/output/resources, denied-by-default network and secret scope, descendant accounting, cancellation/force-or-fence, stale authority rejection, and fresh state/effect readback.
- The supervisor owns every admitted process identity and descendant relationship it claims to support. Process-tree termination and authority fencing are distinct: unavailable force termination narrows the support class and blocks/fences work; it never permits stale effects.
- Git operations obey all 30 frozen classifications. Hooks, helpers, filters, signers, transports and package scripts are executable/effectful surfaces, not implicit consequences of a Git or dependency request.
- Exact host/process containment feasibility is not proven. `AR-EXE-003` remains linked to `E3V-002` and frozen handback set `ADR-E2-003/004`.

## 9. Protected entry

The integrated trusted application boundary contains a dedicated protected-entry controller that is outside ordinary request, model, transcript, terminal-output, logging, telemetry, screenshot/accessibility capture and evidence pipelines. It obtains an authenticated one-use recipient/use/fence authorization, suspends unauthorized observation surfaces, delivers the raw value only to the exact current recipient in transient protected memory, and returns only a non-secret receipt containing identity/scope/time/outcome facts.

Raw values are never placed in authoritative state, material history, context, projection, log or evidence; they are never replayed after crash/replacement. Revocation, owner/recipient replacement, uncertain consumption or failed capture exclusion invalidates the authorization and returns the task to `WAITING_FOR_USER` or blocked. The concrete client/acquisition/carrier mechanism is unselected and unvalidated. `AR-SEC-006` and the C01-specific delivery question remain under `E3V-006`; the frozen structural handback set is `ADR-E2-001/004/005/008`.

## 10. Provider and logical-role boundary

The embedded provider-neutral gateway owns typed request/result contracts, route purpose and eligibility, capability discovery, explicit requested/resolved provider/model/configuration identity, streaming/tool/refusal/usage/stop/cancellation/error provenance, data/network policy, cost/limit accounting and explicit fallback. Provider-native state never defines core task, approval, effect, evidence or completion truth. Unknown, disallowed or budget-incomplete routing transmits zero bytes and incurs zero calls/cost.

The architecture preserves these logical roles without assigning an occupant: `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER`, and `SECURITY_REVIEWER`. E3 benchmark results are configuration-, role- and task-class-specific. Failure or missing evidence leaves a role unassigned; it does not trigger hidden fallback or change the architecture by assertion.

## 11. Evidence and independent verification

The core builds a versioned outcome-profile bundle from authoritative records and separately identified artifacts. It binds the original request, governing inputs, task/attempt/operation/actor identities, base/workspace/candidate revision, full changed-file inventory, commands/results, tests/checks/repetitions, approvals/effects/readbacks, routing/model/tool/configuration provenance, artifacts, failures/recovery, limitations, predicate coverage and final disposition. Output is bounded and secret-safe; large outputs use stable references with provenance/retention/staleness rules.

The verifier receives a bounded immutable manifest for the exact candidate and uses a separate process/context/workspace with least privilege and no shared mutable author state. It can reread authoritative state, repository bytes, deterministic checks and external targets where authorized. It assesses predicate adequacy before pass credit, distinguishes verifier infrastructure error from substantive verdict, and cannot depend solely on executor narration, transcript, telemetry or a self-authored digest. Any material candidate/evidence mutation invalidates current verification.

## 12. Frozen E1 testability contract

C01 must expose deterministic injection and readback seams sufficient for later materialization of the frozen suite; no case is implemented or run here.

| Frozen family | Count | Required C01 seam |
|---|---:|---|
| Evaluation cases | 170 | Versioned fixture admission, policy/state/operation/workspace/provider/evidence ports and exact candidate identity. |
| Independent oracles | 18 | Read-only authoritative state, repository/workspace/Git/process/target/evidence inspectors independent of executor summary. |
| Fixture families | 11 | Injectable store, workspace, process, provider, approval, recovery and evidence boundaries with deterministic schedules. |
| Security-negative families | 23 | Policy, path/workspace, execution, protected entry, capability/Git/network/provider and evidence gates. |
| Repository conditions | 16 | Admission/support matrix, ownership/topology inventory, bind/readback and safe unsupported outcome. |
| Git/effect classifications | 30 | Sanitized Git adapter and complete intent/approval/attempt/readback/zero-effect records. |
| Predicate-adequacy variants | 9 | Predicate registry, raw evidence access, exact-revision verifier and stale-pass invalidation. |
| Dangerous compositions | 16 | Fault scheduler across transaction, supervisor, workspace, provider, approval/effect and verifier boundaries. |
| Reliability protocols | 8 | Raw timestamp/outcome/usage/cost/limit/missingness ports with no invented threshold. |
| `EP-CTL-016` | 1 named case | Distinguishable client-only detach while healthy task-bound core continues; full core loss follows recovery instead. |

## 13. Requirement-to-ADR coverage

The coverage join is mechanical:

```text
127 frozen E1 IDs
  --ENGINEERING_PREVIEW_E1_ARCHITECTURE_TRACEABILITY.csv-->
65 AR IDs (59 hard + 6 preferences)
  --table below-->
ADR-E2-001..009
```

The frozen trace contains 127 unique rows and no orphan primary AR reference. The baseline table contains every one of the 65 unique matrix criteria exactly once as a primary ADR assignment; cross-ADR obligations remain in the ADRs. This preserves all 127 E1 requirements transitively without rewriting the frozen trace.

| Primary ADR | Architecture requirement IDs |
|---|---|
| `ADR-E2-001` | `AR-PRF-001` |
| `ADR-E2-002` | `AR-COR-003`, `AR-DUR-001`, `AR-DUR-005`, `AR-DUR-006`, `AR-DAT-001`, `AR-DAT-002`, `AR-PRF-003` |
| `ADR-E2-003` | `AR-COR-001`, `AR-COR-002`, `AR-COR-007`, `AR-DUR-002`, `AR-DUR-003`, `AR-DUR-004` |
| `ADR-E2-004` | `AR-WSP-001`, `AR-WSP-002`, `AR-WSP-003`, `AR-WSP-004`, `AR-WSP-005`, `AR-EXE-002`, `AR-EXE-003`, `AR-EXE-004`, `AR-GIT-001`, `AR-GIT-002`, `AR-TST-001` |
| `ADR-E2-005` | `AR-EXE-001`, `AR-SEC-001`, `AR-SEC-002`, `AR-SEC-003`, `AR-SEC-006`, `AR-SEC-004`, `AR-SEC-005`, `AR-APR-001`, `AR-APR-002`, `AR-APR-003` |
| `ADR-E2-006` | `AR-CTX-001`, `AR-CTX-002`, `AR-MOD-001`, `AR-MOD-002`, `AR-MOD-003` |
| `ADR-E2-007` | `AR-COR-004`, `AR-COR-005`, `AR-COR-006`, `AR-EVD-001`, `AR-EVD-002`, `AR-EVD-003`, `AR-VER-001`, `AR-VER-002`, `AR-VER-003`, `AR-TST-002`, `AR-PRF-005` |
| `ADR-E2-008` | `AR-OBS-001`, `AR-OBS-002`, `AR-FAIL-001`, `AR-FAIL-002`, `AR-TST-003`, `AR-PERF-001`, `AR-PERF-002` |
| `ADR-E2-009` | `AR-PKG-001`, `AR-FUT-001`, `AR-FUT-002`, `AR-FUT-003`, `AR-PRF-002`, `AR-PRF-004`, `AR-PRF-006` |

## 14. Twenty-five decision domains

| Domain | Proposed ADR owner | C01 disposition |
|---|---|---|
| `D01_CLIENT_INTERACTION_BOUNDARY` | `ADR-E2-001`, `ADR-E2-009` | Detachable non-authoritative local client; protected takeover remains a separate seam. |
| `D02_CORE_APPLICATION_RUNTIME` | `ADR-E2-001` | One task-bound integrated persistent local core; no mandatory daemon. |
| `D03_TASK_WORKFLOW_ORCHESTRATION` | `ADR-E2-003` | Core-owned versioned task/operation state loop and owner epoch. |
| `D04_DURABLE_STATE_PERSISTENCE` | `ADR-E2-002` | Embedded transactional authoritative-state port plus integrity/evolution rules. |
| `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL` | `ADR-E2-002`, `ADR-E2-007` | Explicit authority classes; evidence bundle derives only from durable sources. |
| `D06_EVENT_OPERATION_HISTORY` | `ADR-E2-002`, `ADR-E2-003` | Append-only material history/outbox/effect records; not event-sourced authority. |
| `D07_FILESYSTEM_WORKSPACE_ABSTRACTION` | `ADR-E2-004` | Task-bound workspace/filesystem broker with object/root/ownership checks. |
| `D08_EXECUTION_PROCESS_CONTROL` | `ADR-E2-004` | Owned supervisor, bounded children, cancel/force-or-fence and readback. |
| `D09_ISOLATION_SANDBOXING` | `ADR-E2-004` | Technology-neutral Tier 2 semantic floor; supported mechanism deferred to E3/E4. |
| `D10_GIT_INTEGRATION` | `ADR-E2-004` | Sanitized adapter enforcing 30 Git/effect rows and review-package truth. |
| `D11_APPROVAL_PERMISSION_SYSTEM` | `ADR-E2-005` | Core policy/capability gate and exact durable approval ledger. |
| `D12_EXTERNAL_EFFECT_RECONCILIATION` | `ADR-E2-005` | Intent/approval/attempt/observed/confirmed-or-unknown lifecycle. |
| `D13_MODEL_PROVIDER_GATEWAY` | `ADR-E2-006` | Embedded provider-neutral gateway; no provider/model assigned. |
| `D14_ROUTING_CAPABILITY_DISCOVERY` | `ADR-E2-006` | Explicit purpose/eligibility/capability/configuration and zero-dispatch denial. |
| `D15_CONTEXT_MEMORY_COMPACTION` | `ADR-E2-006` | Derived, provenanced, invalidatable context; authoritative source retained. |
| `D16_VERIFICATION_ARCHITECTURE` | `ADR-E2-007` | Separate least-privilege verifier process/context/workspace. |
| `D17_EVIDENCE_ARTIFACT_SYSTEM` | `ADR-E2-007` | Versioned bundle/artifact identity, provenance, integrity, retention and stale rules. |
| `D18_OBSERVABILITY_LOGGING` | `ADR-E2-008` | Structured semantic audit separated from optional lossy telemetry/log sinks. |
| `D19_ERROR_FAILURE_MODEL` | `ADR-E2-008` | Typed bounded failures, accountable layer, retry/terminal/unknown semantics. |
| `D20_SECURITY_BOUNDARIES` | `ADR-E2-005`, `ADR-E2-008` | Twenty mapped enforcement points; logs/telemetry cannot bypass secret/evidence rules. |
| `D21_LOCAL_FIRST_PACKAGING` | `ADR-E2-009` | One contributor-operable local package/lifecycle; exact tooling deferred. |
| `D22_FUTURE_REMOTE_EXECUTION` | `ADR-E2-004`, `ADR-E2-009` | Serializable replaceable execution port; no remote runtime now. |
| `D23_FUTURE_CONCURRENCY_MULTI_AGENT` | `ADR-E2-003`, `ADR-E2-009` | Versioned scopes/epochs/idempotency identities; no multi-agent runtime now. |
| `D24_EXTENSION_SKILL_CONNECTOR_BOUNDARY` | `ADR-E2-009` | Versionable governed capability/extension seam; packs/connectors deferred. |
| `D25_E1_SUITE_TESTABILITY` | `ADR-E2-004`, `ADR-E2-007`, `ADR-E2-008` | Deterministic injection, authoritative readback, measurement and exact-revision verification seams. |

## 15. Reversibility and migration profile

| ADR | Commitment class | Early reversible elements | Costly/foundational elements | Required migration/reopen evidence |
|---|---|---|---|---|
| `ADR-E2-001` | `FOUNDATIONAL_HIGH_COST` | Client surface and presentation adapters. | Integrated core authority/process lifetime split. | Exported ports and authority-preserving service cutover if core must be separated. |
| `ADR-E2-002` | `FOUNDATIONAL_HIGH_COST` | Physical store and projection implementation behind contracts. | Canonical record meanings, acknowledgement boundary, material history/effect semantics. | Versioned export/import, integrity proof, dual-read equivalence, rollback and retained old evidence. |
| `ADR-E2-003` | `FOUNDATIONAL_HIGH_COST` | Scheduler algorithms and internal modules. | Owner epoch, operation identity, idempotency and recovery semantics. | Token/ownership translation, nonterminal drain/reconciliation and duplicate/stale-owner proof. |
| `ADR-E2-004` | `MODERATELY_COSTLY` | Workspace, process and Git adapters when semantics conform. | Isolation/support-class and process authority contract. | Conformance/support matrix, canaries, process/effect fencing and original-state preservation. |
| `ADR-E2-005` | `FOUNDATIONAL_HIGH_COST` | Individual capability and target adapters. | Authority/approval/protected-entry/effect identity and reconciliation chain. | Receipt/action/effect identity preservation, no replay, readback equivalence and secret-surface scan. |
| `ADR-E2-006` | `MODERATELY_COSTLY` | Provider adapters, routing policy and context projectors. | Provider-neutral core semantics and provenance fields. | Offline conformance replay, no semantic loss, explicit eligibility and no hidden fallback. |
| `ADR-E2-007` | `FOUNDATIONAL_HIGH_COST` | Artifact carrier and individual validators. | Evidence identity, candidate binding and verifier independence. | Manifest translation, old-bundle readability, exact-revision equivalence and verifier requalification. |
| `ADR-E2-008` | `MODERATELY_COSTLY` | Telemetry/log exporters and dashboards. | Stable semantic audit/failure/metric inputs required by gates. | Schema/version adapter, gap/redaction proof and no authority transfer to telemetry. |
| `ADR-E2-009` | `REVERSIBLE_EARLY_TO_MODERATELY_COSTLY` | Package/update/client mechanics before release. | Contributor lifecycle contract and reserved port identities after ecosystem adoption. | Reproducible setup/update/rollback, compatibility matrix and no hidden mandatory service/cloud. |

## 16. Future scope boundary

| Classification | Included |
|---|---|
| `REQUIRED_NOW` | One local user, one persistent named agent, detachable client, one task-bound core owner, isolated local repository work, bounded processes/Git/tools, durable recovery, exact approval/effect semantics, provider-neutral gateway, independent verification, review package and evidence bundle. |
| `RESERVED_COMPATIBILITY` | Serializable execution/provider/capability ports; explicit principal/agent/task/workspace/operation/approval/artifact/provider/policy scopes and versions; owner epochs/idempotency/correlation; migration hooks for remote workers, multiple clients/writers/agents, skills, routines and connectors. |
| `DEFERRED_TO_LATER_STAGE` | Cloud workers, concurrent production execution, multiple visible agents, agent messaging, group chat, schedules/events, marketplace/connectors, General Edition packaging, Finance Edition semantics, SaaS/multi-tenancy/billing/enterprise controls, production operations. |

General and Finance remain governed extension possibilities over one domain-neutral core. No finance schema, trading behavior, tenant control, remote service, distributed queue, routine engine or connector marketplace is introduced.

## 17. Contributor and local-first implications

C01 is locally simpler in topology: one task-bound runtime/package plus explicitly owned child/verifier processes, with no always-installed control service. A contributor can follow authority transitions through a short in-process trace and reproduce failure by replaying transactional/history/effect fixtures. The cost is conceptual and organizational rather than process-count free: the core must preserve strict internal ports and state categories, broad-core changes can couple concerns, crash tests span several internal modules, and documentation must prevent derived views from becoming de facto authority.

The baseline therefore requires module/port contracts, deterministic fault points, state/effect diagrams, support matrices and ADR-linked contributor documentation. C01 is not justified because it has “fewer components”; it is proposed because its current mandatory lifecycle is proportionate to D-016 scope while every hard boundary remains explicit and externally testable.

## 18. E3 and E4 boundary

All eight canonical E3 obligations are defined without rewording in `ENGINEERING_PREVIEW_E3_VALIDATION_OBLIGATIONS.md`. `E3V-001..007` are technical/mechanism obligations. `E3V-008` is the separately authorized model/configuration benchmark. Missing, failed or inconclusive evidence cannot validate a support class or role.

The three verified E4 implementation bundles remain preserved:

- `E4U-C01-IMPLEMENTATION` (applicable if this proposal survives): client/runtime; embedded store; schema/codec; process API; isolation mechanism; provider SDKs/adapters; package/update tooling.
- `E4U-C02-IMPLEMENTATION` (provenance for the viable rejected alternative): service/client/runtime; IPC/auth; store/schema; worker supervisor; isolation mechanism; provider adapters; installer/updater.
- `E4U-C03-IMPLEMENTATION` (provenance for the viable rejected alternative): runtime/journal/payload; event/schema/reducer; projections/checkpoints; executor/isolation; provider adapters; client/package.

These are implementation/configuration choices behind defined seams. E2-005 selects none of their concrete technologies, and E4 remains unauthorized.

## 19. E2-006 review contract

E2-006 must independently rederive rather than inherit:

- exact derivation from `EP-ARCH-C01` with no hybridization;
- 127 E1 → 65 AR → nine ADR completeness and all 25 domains;
- 59 non-compensating hard results and six unweighted preference tradeoffs;
- all 20 threat boundaries, 15 recovery scenarios, approval/effect and protected-entry semantics;
- evidence/verifier independence and full frozen-suite testability seams;
- provider/model neutrality and zero role assignment;
- all eight canonical E3V definitions, one frozen ADR handback set each, fail-closed consequences and the registered finite-ceiling authority;
- all three E4 bundles as implementation-only deferrals;
- ADR coherence, reversibility, migration and rejected-alternative reopen triggers;
- zero implementation, spike, evaluation, benchmark, paid call, autonomy or S1-003 change.

Until E2-006 passes, this baseline and every ADR remain `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`, `architecture_selected` remains `false`, and the E2 gate remains `NOT_EVALUATED`.

## 20. Provenance pins and limitations

| Input | SHA-256 at authoring |
|---|---|
| E1 architecture trace | `f169aa82a462fd009b19810ad9bf095882601b099b78a6e5b06ecf69e98200b9` |
| 195-cell decision matrix | `0780d87b1311137047d7830b7a4bfd7c8bc4983886d7ce72e485a3584466a24f` |
| C01 candidate | `ea9ff609a2c89c96b721fef4f6005d28238940b17085ffc2d82a13ff5b688e92` |
| C02 candidate | `899f7fa0933da3a7657a928f0aa5e2b4b94ffc80778bf6ba8d5a36fb6c45ba81` |
| C03 candidate | `72cacf1cf6d7d99807b3d0c4c10180bb9dc079516443843ac3c87919d319e4f0` |
| Verified no-spike closure | `a28d5f890387e7db5b387f92b5f3e4d3cb02008a69338e5d1e56695156875ba3` |

Primary authority is the frozen E1 baseline and verified E2 artifacts. The reconstructed Grok Bot audit and adoption matrix contribute only implementation-neutral Level-B comparison patterns and test ideas; no external Level-C code, schema, names, layout, assets or claimed runtime behavior is imported. No runtime, architecture mechanism, platform support, latency, cost, reliability, model eligibility, product demand or production readiness has been observed by E2-005.
