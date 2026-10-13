# Engineering Preview Proposed Architecture Baseline

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Task: `E2-005`

Proposed candidate: `EP-ARCH-C01` — Integrated Transactional Local Core

Selection authority: E2-005 may recommend one verified survivor and author a proposed baseline and proposed ADRs. It may not accept an ADR, independently select or verify the architecture, pass the E2 gate, begin E3, or authorize implementation.

Architecture selected: `false`

Accepted ADR count: `0`

## 1. Decision statement

E2-005 proposes `EP-ARCH-C01` unchanged as the Engineering Preview v0.1 architecture baseline. This is a qualitative proposal from the three independently verified, analytically viable candidates. It is not a score, rank, implementation result, or claim that C01 is universally superior.

The decision rule is an ordered, non-numeric qualitative rule:

1. **Hard non-compensating gate.** Each candidate has the same independently verified comparison result: 57 hard requirements confirmed for comparison, two architecture seams confirmed with E3 validation outstanding, and zero hard violations. No preference can compensate for a hard failure (`ENGINEERING_PREVIEW_ARCHITECTURE_REQUIREMENTS.md` §5 and `ENGINEERING_PREVIEW_ARCHITECTURE_COMPARISON.md` §§3-4).
2. **Current verified scope.** D-016 makes the local-first, single-user Engineering Preview `REQUIRED_NOW`; remote execution, concurrent tasks, multiple agents/clients, extensions, General/Finance, and SaaS remain `RESERVED_COMPATIBILITY` or later-stage work (`DECISION_LOG.md` D-016 and charter §19). D-016 bounds the decision but does not, by itself, distinguish the three local-first candidates.
3. **Qualitative present-structure proportionality.** Within that scope, immediately mandatory operational and authority-path complexity receives more present-day scrutiny than machinery reserved only for future compatibility. This follows the E2 plan §15 rule against speculative machinery that increases v0.1 complexity without satisfying a current E1 requirement, `AR-PRF-002`'s preference for fewer independent failure/upgrade/operational surfaces with clear ownership, and `AR-PRF-004`'s warning that v0.1 must not absorb unnecessary distributed-system complexity. No numeric weight, aggregate score, or hidden conversion of a preference into a hard constraint is introduced.
4. **Apply the rule once, without assuming contributor results.** C01 supplies the shortest current authority/control path and avoids requiring a permanent local service, service IPC/authentication, worker-lease lifecycle, or journal/reducer/projection authority model before those structures earn present value. Contributor accessibility is assessed from the verified comparison §§5, 13, and 17.2—not inferred from process count: C01's visible runtime is offset by broad-core coupling, C02's narrower subsystems by multi-process setup, and C03's replay fixtures by event/reducer onboarding.
5. **Preserve future evolution as a real preference.** C02's direct remote-worker seam and C03's causal replay/reconstruction remain material advantages and explicit reopen triggers. Sensitivity profile A supports C01's minimal-topology fit; profile D supports only C01's setup-topology sub-dimension and gives each candidate a different contributor advantage. Profiles B/C/G preserve recovery, remote-evolution, and differentiated testability pressure; profiles E/F produce no stable candidate-wide winner. No sensitivity profile is treated as an overall winner (`ENGINEERING_PREVIEW_ARCHITECTURE_COMPARISON.md` §17.2).
6. **Retain costs and missing evidence.** C01's integrated core has a wider crash/coupling radius, later remote extraction cost, and foundational transactional state/history/effect meanings. Missing E3 evidence receives no favorable interpretation: descendant containment/fencing and protected acquisition/delivery remain unproven under `E3V-002` and `E3V-006`, and every other canonical E3V obligation remains unrun.

This proposal does not combine C02 service/lease topology or C03 journal/reducer authority into a new candidate. C01's own append-only material history, outbox/effect ledgers, derived projections, supervisor port, provider gateway, and future adapter seams remain exactly the candidate-defined C01 shape. There is no hidden C04.

### 1.1 Candidate disposition

| Candidate | Verified strengths preserved | E2-005 disposition | Why not proposed for v0.1 | Reopen conditions |
|---|---|---|---|---|
| `EP-ARCH-C01` | Minimal mandatory local topology; short authority path; compact current-state access; in-process traceability; no mandatory daemon or cloud service. | **PROPOSED**, pending E2-005 challenge/fix/task verification and fresh E2-006 architecture verification. | Not applicable. Its broad-core coupling, crash radius, later extraction cost, and foundational state semantics remain risks. | Reopen this proposal if E3 disproves a linked structural assumption, contributor/setup evidence shows the integrated boundary is untenable, or a frozen product amendment makes remote worker replacement or causal replay a present hard requirement. |
| `EP-ARCH-C02` | Clearest direct remote-worker seam; replaceable leased/fenced workers; worker fault isolation; explicit subsystem boundaries. | Analytically viable, not proposed. | Its mandatory user-local service, IPC/authentication, lease/fence, correlation, and lifecycle surfaces add present operational and security burden before remote/multi-worker behavior is in v0.1 scope. | Reconsider if verified requirements make independently replaceable remote workers, service continuity across all client lifetimes, or multiple execution owners present requirements rather than compatibility seams. Migration requires extracting C01 control/state ports into a service and introducing versioned IPC plus lease/effect protocols. |
| `EP-ARCH-C03` | Strongest causal replay/reconstruction and projection rebuilding; deterministic reducer fixtures; coordinator may be absent. | Analytically viable, not proposed. | Its event identity/order/evolution, immutable payload, reducer, checkpoint, projection, retention, and rebuild concepts impose a larger present semantic and contributor burden than the verified single-user local workflow requires. | Reconsider if verified evidence makes full causal reconstruction, independently replayable projections, or coordinator-free operation decisive. Migration requires defining an event cutover, dual-read/verification period, transactional-state export, reducer equivalence, and rollback checkpoint. |

### 1.2 Six qualitative preferences, without weights

The six preference criteria break the hard-constraint tie only through the ordered qualitative rule above: after the hard tie and D-016 scope boundary, apply the E2 plan §15 / `AR-PRF-002` / `AR-PRF-004` present-structure proportionality rule once. No numeric weight, aggregate score, hidden rank, measured performance claim, or compensation for a hard failure is used. Future compatibility remains a genuine preference and a reopen surface rather than being assigned zero value.

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
| D. Contributor accessibility | C01 has one visible runtime, C02 narrower subsystems, and C03 deterministic replay fixtures. | Supports only C01's setup-topology sub-dimension; broad-core coupling/documentation remains under `E3V-003`, and the profile gives no candidate-wide contributor winner. |
| E. Migration reversibility | No stable overall advantage; each candidate has a different lock-in center. | Requires explicit foundational commitments, export/import/rollback evidence and direction-specific reopen triggers; gives C01 no favorable universal reversibility credit. |
| F. Security-boundary clarity | C01 centralizes authority, C02 physicalizes more boundaries, and C03 makes admission/event flow explicit; no stable overall winner. | Requires C01's in-process semantic boundaries, separate child/verifier processes and protected path to remain externally testable under `E3V-002/004/005/006`. |
| G. Testability/debuggability | C03 gains replay fixtures, C02 substitution/fault isolation, and C01 short in-process traces. | Supports no overall winner; C01 must expose the entire frozen fault/readback suite and dangerous compositions without relying on low component count. |

Profile A supplies the direct minimal-topology signal for C01. Profile D supplies only a bounded setup-topology signal while preserving distinct C02/C03 contributor advantages. Profiles B, C and G preserve material C02/C03 advantages; E and F explicitly produce no stable candidate-wide advantage. No profile is an overall winner or a hidden weight.

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

The closed architecture-level vocabulary is exactly the E2-001 §3 vocabulary: `AUTHORITATIVE STATE`, `DERIVED PROJECTION`, `EPHEMERAL WORKING CONTEXT`, and `LOSSY SUMMARY`. Descriptive phrases below do not create additional state classes.

| Concern | Class | Proposed owner | Persistence/reconstruction rule |
|---|---|---|---|
| Agent identity; task identity, contract, scope, plan, limits, predicates and status tuple | `AUTHORITATIVE STATE` | Integrated core / canonical-state port | Versioned durable records; acknowledged only after authoritative commit and reread; never reconstructed from transcript. |
| Durable conversation/message ordering, authorship, authority context and source references | `AUTHORITATIVE STATE` | Integrated core / canonical-state and material-history ports | Retained at the detail needed for authorization, recovery, audit and verification; summaries cannot replace it. |
| Owner epoch, operation identity/status/outcome, control, retries, cancellation, fences and first outcome | `AUTHORITATIVE STATE` | Core recovery/orchestration coordinator | One current writer epoch; stale writes/results/effects rejected; nonterminal records reconciled on recovery. |
| Approval/refusal/revocation/consumption and effect `INTENT`/`ATTEMPT`/observation/readback | `AUTHORITATIVE STATE` | Capability/approval/effect gateway plus core ledger | Exact normalized scope, one-use/replay protection, policy and owner version; uncertainty remains durable. |
| Workspace identity, repository/base binding, ownership, support-class disposition and before/after facts | `AUTHORITATIVE STATE` | Workspace broker plus core record | Bound before mutation; fresh readback invalidates stale bindings; external bytes remain external truth. |
| Requested/resolved route, purpose, eligibility, capability/configuration, fallback, usage/cost and provider result provenance | `AUTHORITATIVE STATE` | Provider-neutral gateway plus core record | Provider-specific semantics remain visible; denied/unknown route dispatches zero bytes/calls/cost. |
| Artifact/evidence identities, provenance, integrity/gap/staleness state, candidate revision and verification run/verdict | `AUTHORITATIVE STATE` | Evidence builder, artifact boundary and independent verifier | Frozen candidate and bundle references are immutable; any material mutation invalidates the current pass. |
| Material causal/operation history needed for recovery, correctness evidence, reconciliation, audit and migration | `AUTHORITATIVE STATE` | The single append-only material-history port owned by the core under ADR-E2-002 | Append-only semantics with integrity/evolution/gap state; it complements transactional current state and is not C03 event-sourced authority or an ADR-E2-008 logging store. |
| Transcript/activity/search/UI/dashboard and operational-audit views | `DERIVED PROJECTION` | Projection and observability components | Rebuild from authoritative sources with source versions and limitations; stale or poisoned views are discarded and never used for recovery or completion. |
| Final validated evidence bundle representation | `AUTHORITATIVE STATE` | Evidence builder then independent verifier | The bundle is a versioned immutable evidence artifact constructed from other authoritative records and stable references; it cannot manufacture missing source evidence or supersede the underlying sources. |
| Optional telemetry samples, performance views and presentation logs | `LOSSY SUMMARY` | Observability adapters | May be durable operationally, but never authorize, recover, prove completion, or replace material history/evidence; missing samples are explicit. |
| Live stream fragments, process handles, in-memory caches, prompt assembly and temporary working buffers | `EPHEMERAL WORKING CONTEXT` | Owning adapter/process | May disappear. Anything required for acknowledgement, recovery, effect truth or proof must be promoted into the proper authoritative record first. |
| Model invocation context | `EPHEMERAL WORKING CONTEXT` | Context projector / invocation owner | Rebuilt from current authoritative sources; loss changes no task, approval, effect, evidence or verification truth. |
| Compacted summaries and resume briefs | `LOSSY SUMMARY` | Context projector | Source/provenance/version/omission bound, invalidatable and disposable; cannot overwrite or delete authoritative source history. |

### 3.1 Material history, evidence, and observability boundary

- ADR-E2-002 owns the canonical durable task/operation/approval/effect/evidence/material-history semantics and the one append-only material-history port required for recovery and correctness. A correctness-required audit fact is an `AUTHORITATIVE STATE` record in that port or in the authoritative evidence system; durability does not move it into observability ownership.
- ADR-E2-007 owns authoritative evidence artifacts, integrity state, exact-candidate binding, and independent verification. Logs or telemetry may cite an evidence ID but are never completion proof on their own.
- ADR-E2-008 owns operational observability, diagnostic/audit projections, metering, structured failure presentation, monitoring views, optional exporters, and `DERIVED PROJECTION` / `LOSSY SUMMARY` representations. Those views can be rebuilt or lost without losing authoritative history.
- No second audit log, telemetry stream, dashboard, or failure projection has precedence over ADR-E2-002 current state/material history or ADR-E2-007 evidence. A physical store may later be shared only if these semantic ownership and precedence rules remain enforceable.

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

Verified C01 candidate field `f05_trust_boundaries_and_threat_model.boundaries.TB-01..TB-20` is incorporated below unchanged as the normative proposed-C01 instantiation. The table carries all nine E2-001 §5.1 semantics rather than merely referring back to the candidate. E2-005 adds no mechanism: the proposed ADRs own the named enforcement points and E3V-006 later validates only a selected implementation/support class. Fully privileged host compromise remains unsupported as stated above.

| ID | Trust classification and protected assets | Authority source | Allowed flows | Forbidden flows | Enforcement point | Fail-closed behavior | Evidence / observability | Recovery / replay implications |
|---|---|---|---|---|---|---|---|---|
| `TB-01` | Authenticated but fallible user/founder; task authority, approvals, protected entry | Authenticated current user plus repository governance | Bounded task grants, controls, exact approvals, protected recipient designation | Conversational text silently broadening scope or waiving hard policy | Core admission and policy kernel | Reject or `WAITING_FOR_USER` with zero dispatch | Principal, request, authority version, decision, zero-effect record | Reauthenticate and revalidate current authority; never infer consent |
| `TB-02` | Untrusted repository content; source and user-owned material | Admitted task/root policy, not repository prose | Bounded reads and authorized isolated writes | Instruction, capability, network, secret, or approval escalation | Repository admission plus workspace broker | Deny, quarantine, or block unsupported condition | Base identity, condition row, scope and before/after canaries | Reread identity/topology and invalidate stale workspace |
| `TB-03` | Untrusted instruction files; workflow guidance | Higher project/user policy with instruction precedence | Narrow formatting, checks, paths, contribution procedure | Granting execution, roots, credentials, effects, routing, or weaker predicates | Instruction interpreter plus policy kernel | Typed conflict denial or unmet-precondition wait | Instruction source/trust label, conflict and applied restriction | Reload current versions and discard poisoned/stale derived context |
| `TB-04` | Host filesystem; repository, workspace, artifacts, user data | Normalized admitted roots and ownership records | Descriptor-relative bounded access to proven targets | Out-of-root, special-file, ambiguous-owner, or destructive access | Workspace/filesystem broker | Fail closed before access; quarantine ambiguous target | Resolved identity, path decision, canaries, mutation inventory | Reresolve every target and reconcile only task-owned material |
| `TB-05` | Protected secrets/private data; confidentiality and use scope | Protected-location policy and exact recipient/use grant | Opaque one-use delivery to exact authorized recipient | Model/chat/log/evidence/screenshot/clipboard/ambient child exposure | Secret classifier and protected-entry controller | Do not read; wait/block and record non-secret reason | Non-secret receipt identity, recipient, use, time, disposition | Reacquire after revalidation; raw value is never persisted or replayed |
| `TB-06` | Untrusted links, aliases, traversal and topology races; root integrity | Pinned root and descriptor/identity checks | Access whose resolved object stays in admitted scope | Traversal, symlink/hard-link swap, mount/device/archive escape | Workspace broker at open, mutation, and cleanup | Deny and preserve canaries | Pre/post object identity and resolution decision | Reresolve; stale topology forces recovery/block |
| `TB-07` | Untrusted subprocesses; host resources and task effects | Versioned capability grant and operation envelope | Bounded declared process tree in isolated workspace | Orphans, scope escape, undeclared descendants/effects, self-declared noninterruptibility | Execution supervisor | Cancel/force/fence; classify remaining effect uncertainty | Process tree, limits, timeline, exit/cancel/fence outcome | Discover/fence surviving ownership and reconcile effects before resume |
| `TB-08` | Terminal I/O and protected human entry; commands, output, raw input | Operation contract or protected-entry recipient grant | Bounded inert output; isolated protected recipient input | Output becoming authority; raw protected input entering ordinary capture | I/O multiplexer and protected-entry controller | Truncate safely, deny consumption, or fail to `WAITING_FOR_USER` | Output bounds/provenance and non-secret protected receipt | Do not replay raw input; rerun only after current grant/readback |
| `TB-09` | Untrusted package/lifecycle scripts; filesystem, process, network | Separately granted execution and network capabilities | Explicitly classified bounded script under declared support | Install/retrieval implying execution, egress, secret or scope access | Capability gateway plus execution supervisor | Deny or sandbox unsupported script; visible unmet precondition | Script identity, provenance, grant, process/network outcome | Revalidate package/workspace; no blind rerun after ambiguous effect |
| `TB-10` | Untrusted Git hooks/helpers/filters/signers/transports; repository and credentials | Git/effect matrix and exact capability/approval | Only classified helper-free local Git or separately supported effect | Implicit hooks, credential helpers, transports, prohibited ref/destructive actions | Git adapter and capability gateway | Zero dispatch/effect and typed denial | GE row, sanitized invocation, before/after refs/index/worktree | Fresh Git readback; uncertain remote effect remains noncomplete |
| `TB-11` | Untrusted network destinations and redirects; data, credentials, spend | Exact destination/data/credential/budget grant | Authorized route after effective-target revalidation | Undeclared egress, proxy/redirect bypass, private/metadata targets | Network policy boundary before adapter dispatch | Transmit zero bytes and incur zero calls | Requested/effective target, policy decision, bytes/calls/cost | Revalidate destination and reconcile any dispatched uncertainty |
| `TB-12` | Remote Git; refs, repository data, credentials and external effects | Git/effect matrix plus one-shot exact approval | Only supported remote read/effect with receipt and fresh readback | Force push, merge/rebase/cherry-pick, remote deletion, tag mutation or hidden credential flow | Git adapter, approval gate, network boundary | Deny; lost acknowledgement becomes `UNKNOWN_EFFECT` | Intent, approval, attempt, receipt, remote readback | Never blind retry; reconcile authoritative remote state |
| `TB-13` | External APIs; external state, data, credentials, cost | Capability policy and exact effect approval where consequential | Versioned bounded adapter request to supported endpoint | Ambient authority, hidden retry/fallback, unapproved mutation | Capability/provider gateway and effect ledger | Deny before dispatch or classify outcome uncertain | Normalized request, idempotency key, response, readback, usage | Read back authoritative target; retain known success/failure/unknown |
| `TB-14` | Untrusted model/provider output and provider service; task data, routing, cost | Role-neutral routing policy and eligibility registry | Authorized purpose-specific request to explicit eligible or experimental route | Model self-promotion, hidden fallback, output granting authority or proving completion | Provider gateway plus result validator | Zero dispatch or typed provider/model/transport/policy failure | Requested/resolved route, eligibility, provenance, latency, usage/cost | Explicit current fallback decision only; no hidden replay |
| `TB-15` | Untrusted tools/capabilities and results; effects and host access | Versioned schema, scoped capability receipt, policy | Validated exact request and correlated valid result | Unknown schema/version, target substitution, ambient tool power | Capability gateway at request and result | Pre-dispatch deny; post-dispatch invalid result enters reconciliation | Schema/version, grant, request/result validation, effect state | Do not consume invalid result; read back possible effect |
| `TB-16` | Approval boundary; user authority and consequential action | Authenticated exact durable approval object | One current unexpired use matching full normalized intent | Chat confirmation, replay, mutation, stale/revoked/hidden target use | Approval ledger serialized with dispatch | Deny with zero dispatch or reconcile crash ambiguity | Approval identity/scope/version/display/revocation/consumption | Current ownership and scope revalidated; ambiguous consumption blocks retry |
| `TB-17` | External-effect boundary; local/remote target truth | Approved operation plus target-specific authoritative readback | One idempotent/bounded attempt and reconciliation | Guessed success, blind retry, duplicate effect, response-as-proof | Effect ledger and adapter readback | `KNOWN_FAILED` or `UNKNOWN_EFFECT` blocks completion | Intent/approval/attempt/observed/confirmed chain | Return first outcome for duplicates and reconcile target truth |
| `TB-18` | Evidence/integrity boundary; proof, artifacts, exact revision | Evidence schema, authoritative records, independent readback | Validated secret-safe references and immutable verification runs | Telemetry/executor summary/self-hash replacing proof; gap or stale evidence | Evidence builder/validator and verifier | Mark invalid/incomplete and block verification/completion | Manifest, provenance, integrity/gap/staleness results | Rebuild derived bundle from retained authority/evidence; preserve tamper fact |
| `TB-19` | Recovery/replay boundary; ownership, operations, effects, controls | Durable history, first outcome, ownership epoch and current policy | Deterministic reconstruction and bounded reconciliation | Stale writer, duplicate command/effect, fabricated continuity, secret replay | Core startup recovery coordinator | `RECOVERING`, blocked, failed, or explicit uncertainty | Recovery owner, scan, revalidation, rejected stale activity | Single-writer epoch; reconcile every nonterminal operation before productive work |
| `TB-20` | UI/protected entry boundary; human raw value and observation surfaces | Authenticated takeover request and exact protected recipient/use | Suspend ordinary capture and hand raw input only to exact recipient | Chat/model/transcript/log/evidence capture or persistence of raw value | Dedicated protected-entry controller outside ordinary input pipeline | Fail to `WAITING_FOR_USER`/closed if exclusion cannot be guaranteed | Non-secret receipt and capture-state transitions | Receipt may survive; raw value must be reacquired and never replayed |

Primary ADR ownership is explicit rather than implied: ADR-E2-001 owns client/core admission and presentation placement; ADR-E2-004 owns repository/filesystem/path/process/Git enforcement; ADR-E2-005 owns authority, capability, network, approval, secret, protected-entry and external-effect policy; ADR-E2-006 owns provider routing/context; ADR-E2-007 owns evidence/integrity/verification; ADR-E2-008 owns only operational observability/failure presentation and capture exclusion. Every boundary is structurally enforced outside LLM judgment; no log, model statement, tool description, or repository instruction can grant authority.

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

Verified C01 `f09_recovery_model` is incorporated as the normative scenario source: its 18 named cases and seven workspace partial-write cases are retained below, while the E2 plan §11 and challenger-required redirect, resume, reordered delivery, provider ambiguity, duplicate-input and shutdown distinctions are made explicit. Equivalent cases are separated only where their authority, ambiguity, invalidation, or owner differs.

The only core transaction boundary is the ADR-E2-002 authoritative-record boundary. Filesystem, process, Git, network, provider, tool, protected-entry and other external reality are never included in that transaction. For every nontransactional effect, recovery preserves `INTENT`, `ATTEMPT`, actual-state readback, reconciliation, and one of `KNOWN_SUCCESS`, `KNOWN_FAILURE`, or `UNKNOWN_OUTCOME` where those classifications apply.

| Scenario ID / scenario | Authoritative source of truth | Detection / readback | Recovery action | Ambiguity classification | Evidence produced | Recovery owner / escalation | Invalidation behavior | Final allowed dispositions | Relevant ADR(s) | Relevant AR(s) | E3 / E4 obligation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `REC-01` client-only exit/reload | Live core owner epoch and durable task/operation state | New client rereads current versions and projection sources | Rebuild presentation; do not pause, cancel, delete, or transfer task authority | Presentation-only; operation certainty unchanged | Detach/reconnect identity, source versions, rebuilt projection | Client/core boundary owner; escalate only if core is also lost | Cached client projection/control token invalidated | Existing task/operation disposition unchanged | ADR-E2-001, 002 | AR-COR-003, AR-DUR-002, AR-OBS-001 | E3V-003; E4U-C01-IMPLEMENTATION |
| `REC-02` integrated-core/process crash | Transactional current state, material history, operation/effect records | Startup integrity/version scan; nonterminal operation, process and target readback | Establish new owner epoch; fence stale authority; reconcile every nonterminal record before productive work | `KNOWN_SUCCESS`, `KNOWN_FAILURE`, or `UNKNOWN_OUTCOME`; never fabricated continuity | Crash point, recovered versions, epoch, scan, readbacks, limitations | Core recovery coordinator; E3V-001 owner; structural contradiction hands back | All live handles, derived views, cached policy/route/context and current verification invalidated | Recovering, blocked, failed, known success/failure, or unknown outcome | ADR-E2-002, 003, 004, 005 | AR-COR-001/007, AR-DUR-001/002/003/005 | E3V-001; E4U-C01-IMPLEMENTATION |
| `REC-03` host restart | Same durable records plus actual host, workspace, process and external-target state | Startup scan; discover surviving descendants; reread bytes/Git/effects | Recover as owner loss, fence survivors, reconcile actual state, then resume or remain blocked | Three-way knowledge; unobservable prior effect remains `UNKNOWN_OUTCOME` | Host/store identity, process inventory, canaries, Git/target readback, epoch | Core recovery coordinator; E3V-001/002 owner; unsupported host narrows scope | Handles, workspace binding, approval, route, context and verification invalidated until revalidated | Recovering, blocked, known success/failure, unknown outcome | ADR-E2-002, 003, 004, 005 | AR-DUR-002/003/004, AR-EXE-002/003 | E3V-001/002; E4U-C01-IMPLEMENTATION |
| `REC-04` owner failure or stale owner | Current owner epoch and expected entity versions | Compare-version/epoch rejection plus nonterminal scan | Reject old writes/results/approval uses/effects; transfer only after durable fence and reconciliation | Rejected stale attempt is known; crossed external dispatch may be unknown | Old/new epoch, rejected mutation/effect, transfer and scan record | Orchestration/recovery owner; E3V-001/002 owner; hand back if fencing structurally impossible | All old owner grants, approvals, handles, contexts and verification invalidated | Current owner continues, blocked, known failure, or unknown outcome | ADR-E2-003, 004, 005 | AR-COR-007, AR-DUR-002/004, AR-EXE-003 | E3V-001/002; E4U-C01-IMPLEMENTATION |
| `REC-05` owned-child failure | Operation identity, supervisor tree, fence and actual effect state | Exit/process-tree observation, output bounds, target readback | Cancel/force where supported, fence always, retain partial output, reconcile effects; retry only when known safe and within ceiling | `KNOWN_FAILURE` absent effect; `UNKNOWN_OUTCOME` after ambiguous dispatch | Tree/timeline/exit, output refs, fence rejection, effect readback | Execution supervisor then core recovery owner; E3V-002 owner | Child handles/results invalidated; affected evidence and verification stale | Known failure, unknown outcome, blocked, or bounded retry under new attempt | ADR-E2-003, 004, 005 | AR-DUR-003/004, AR-EXE-002/003 | E3V-001/002; E4U-C01-IMPLEMENTATION |
| `REC-06` model/provider timeout or loss | Core route/operation record plus provider/transport observations and usage facts | Provider/transport timeout layer, cancellation/readback if available, usage reconciliation | Record exact layer; cancel where supported; do not infer fallback or repeat a maybe-billed/effectful route | Known failure when non-dispatch/non-effect is proven; otherwise `UNKNOWN_OUTCOME` | Requested/resolved route, timeout layer, cancel, usage/cost/missingness, readback | Provider gateway owner; E3V-004 owner; structural envelope loss hands back | Route eligibility, context, result and dependent evidence invalidated; no role credit | Known failure, unknown outcome, blocked/unassigned, or separately admitted retry | ADR-E2-006, 008 | AR-MOD-001..003, AR-FAIL-001, AR-PERF-001 | E3V-004/007/008; E4U-C01-IMPLEMENTATION |
| `REC-07` tool/process timeout | Operation/process/effect record and actual process/target state | Deadline/timeout, descendant observation, output/effect readback | Persist timeout; request cancellation; force where supported; fence always; reconcile partial output/effect | Known failure if no effect; otherwise `UNKNOWN_OUTCOME` | Operation/control timeline, tree, bounds, output refs, target readback | Execution supervisor/capability gateway; E3V-002/006 owner | Tool result, capability grant, workspace/evidence/verification invalidated as affected | Known failure, unknown outcome, blocked, or bounded safe retry | ADR-E2-003, 004, 005 | AR-DUR-003/004, AR-EXE-001..003, AR-SEC-002 | E3V-001/002/006; E4U-C01-IMPLEMENTATION |
| `REC-08` lost tool result | Attempt/effect identity plus actual target/process/readback state | Missing/invalid correlation; target-specific readback and process/output inspection | Do not consume or redispatch blindly; reconcile possible effect and preserve gap | `KNOWN_FAILURE` only with zero-effect proof; else `UNKNOWN_OUTCOME` | Request/result correlation, missingness, process/target readback, effect state | Capability/effect gateway; E3V-001/006 owner | Result, derived evidence, completion predicate and verification invalidated | Known failure, unknown outcome, blocked; retry only after known non-effect | ADR-E2-003, 004, 005, 007 | AR-DUR-003, AR-EXE-001, AR-APR-002, AR-EVD-002 | E3V-001/005/006; E4U-C01-IMPLEMENTATION |
| `REC-09` partial authoritative-state write or corruption | Last valid acknowledged transaction plus integrity/version/migration metadata | Commit reread, startup integrity/gap/schema scan | Roll back to valid prior state or quarantine original bytes; block acknowledgement/resume until resolved | Valid old/new state is known; corrupt/incompatible authority is blocked, not guessed | Transaction/flush result, integrity/gap state, quarantined bytes, migration ledger | Persistence owner; E3V-001/005 owner; hand back if required durability is structurally impossible | Derived projections, context and verification invalidated; affected authority unavailable | Valid prior/new state, blocked corruption, known failure; never partial fabricated authority | ADR-E2-002, 007 | AR-DUR-001/005, AR-DAT-002, AR-EVD-003 | E3V-001/005; E4U-C01-IMPLEMENTATION |
| `REC-10` partial filesystem write | Actual filesystem/Git bytes and metadata; operation intent is not proof | Fresh per-object byte/metadata/Git/canary readback | Preserve actual state; classify every path; repair only under current authority; never claim cross-boundary rollback | Per-path known bytes with `PARTIAL`, `KNOWN_FAILURE`, blocked, or `UNKNOWN_OUTCOME` if ownership/truth unavailable | Intended paths, before/after object IDs/digests, actual subset, canaries, Git state | Workspace broker then recovery owner; E3V-003 owner; escape hands back | Workspace binding, aggregate predicates, artifacts/evidence and verification invalidated | Partial, blocked, unverified, known success/failure, or unknown outcome | ADR-E2-002, 003, 004, 007 | AR-DUR-003/006, AR-WSP-001..005, AR-GIT-001/002 | E3V-001/003/005; E4U-C01-IMPLEMENTATION |
| `REC-11` stale workspace/base/topology | Current repository/base/object topology and ownership, not cached binding | Reread repository identity, effective targets, canaries, Git/index/worktree | Invalidate binding; preserve user material; rebind/recreate only under current authority or block | Known safe current state or explicit ownership uncertainty | Old/new base, topology/object identities, attribution and canaries | Workspace broker; E3V-003/006 owner; structural escape hands back | Workspace, context, plan assumptions, evidence and verification invalidated | Rebound safe state, blocked, partial, known failure, or unknown outcome | ADR-E2-002, 004, 007 | AR-DUR-006, AR-WSP-001..005, AR-GIT-001/002 | E3V-003/005/006; E4U-C01-IMPLEMENTATION |
| `REC-12` duplicate input delivery | Stable client request nonce/task identity and first durable admission outcome | Duplicate identity lookup and current version reread | Return original admission/outcome with provenance; create no second task, operation, dispatch, or effect | Original result is authoritative; gap remains explicit | Duplicate request, original identity/outcome/version, zero-new-effect record | Core admission/orchestration owner; E3V-001 owner | Stale client expectation invalidated; current task state unchanged | Original recorded result or blocked if record integrity is unresolved | ADR-E2-001, 003 | AR-COR-001, AR-DUR-003 | E3V-001; E4U-C01-IMPLEMENTATION |
| `REC-13` duplicate operation | Stable operation/idempotency identity and first outcome | Operation lookup plus current nonterminal/terminal readback | Return first outcome/current state; do not redispatch; reconcile if first attempt is uncertain | Original known result or `UNKNOWN_OUTCOME` | Duplicate operation, attempt count, original result/current state, zero redispatch | Orchestration owner; E3V-001 owner | Duplicate-derived context discarded; no new approval/effect authority | Original known success/failure, unknown outcome, or current nonterminal state | ADR-E2-003, 005 | AR-DUR-003, AR-APR-002 | E3V-001; E4U-C01-IMPLEMENTATION |
| `REC-14` duplicate external effect | Stable effect identity, attempt record and authoritative target state | Effect-ledger lookup plus target-specific readback | Return first result; prohibit a second attempt; reconcile target discrepancy | One confirmed effect, known failure, or `UNKNOWN_OUTCOME` | Effect/idempotency identity, attempts, receipt, target readback, duplicate denial | Capability/effect owner; E3V-001/006 owner; hand back on unavoidable duplicates | Approval consumed/stale; dependent completion/evidence invalidated until reconciled | Known success, known failure, unknown outcome, blocked | ADR-E2-003, 005 | AR-DUR-003, AR-APR-002/003 | E3V-001/006; E4U-C01-IMPLEMENTATION |
| `REC-15` reordered/delayed or waited-event delivery | Event/request identity, version, source, causal predecessor and first outcome | Compare event/current versions and causal order; reread current authority | Reject stale/out-of-order delivery or buffer only within frozen bounds; return prior outcome for duplicate; never consume from stale context | Known stale/duplicate rejection; missing causal facts block | Event identity/source/version/order, decision, prior outcome and zero-effect proof | Orchestration/recovery owner; E3V-001 owner | Cached wait, context, approval and verification assumptions invalidated | Prior result, waiting, blocked, known failure; unknown if an external dispatch crossed | ADR-E2-002, 003, 006 | AR-COR-002/007, AR-DUR-002/003, AR-CTX-002 | E3V-001/005; E4U-C01-IMPLEMENTATION |
| `REC-16` stale, expired or revoked approval | Exact durable approval object, scope/version/expiry/revocation/consumption and current authority | Approval/current owner/base/policy/target reread serialized with dispatch | Deny zero-dispatch use; obtain a new approval only after current task authority is valid; reconcile any dispatch race | Known zero dispatch or `UNKNOWN_OUTCOME` if race crossed dispatch | Approval lifecycle, display/scope, denial/consumption, dispatch order/readback | Approval/effect owner; E3V-006 owner | Approval and any dependent cached command invalidated; verification stale if effect ambiguity changes candidate | Denied/known failure, unknown outcome, waiting for new approval | ADR-E2-003, 005 | AR-APR-001..003, AR-DUR-003 | E3V-001/006; E4U-C01-IMPLEMENTATION |
| `REC-17` stale verification | Current candidate revision/evidence version versus immutable historical run | Exact revision/integrity comparison and fresh repository/evidence readback | Preserve old run historically; set current candidate `UNVERIFIED`; require a new independent run | No ambiguity: old result applies only to old bytes; current pass absent | Old/new revision, mutation, invalidation reason, historical run identity | Evidence/verifier owner; E3V-005 owner | Current verification and completion gate invalidated; old evidence retained | Current `UNVERIFIED`, blocked, changes required, or later fresh verdict | ADR-E2-002, 007 | AR-COR-006, AR-EVD-001..003, AR-VER-002/003 | E3V-005; E4U-C01-IMPLEMENTATION |
| `REC-18` full-system shutdown | Durable shutdown/control intent, owner epoch, process tree and all nonterminal records | Quiesce scan before exit; on restart read overdue/surviving processes/workspaces/effects | Stop intake; cancel/force where supported; fence always; persist truthful partial/unknown states; reconcile before resume | Known endpoints where observed; otherwise explicit `UNKNOWN_OUTCOME`; no real-time enforcement claim while absent | Shutdown intent/order, process/effect endpoints, checkpoint, restart scan | Core control/recovery owner; E3V-001/002 owner | Live handles, routes, approvals, contexts and current verification invalidated as applicable | Paused/cancelled/blocked, known success/failure, unknown outcome | ADR-E2-001, 003, 004, 005 | AR-DUR-002/004, AR-EXE-002/003 | E3V-001/002; E4U-C01-IMPLEMENTATION |
| `REC-19` redirect | Durable current task/plan/control version and operation/effect state | Compare expected task/plan/base/owner versions; scan in-flight work/effects | Commit redirect before acknowledgement; stop new obsolete dispatch; cancel/fence or reconcile old work; derive a new plan only from current authority | Old work known/failed/unknown separately from new redirected work | Redirect cause/version, invalidated operations/predicates/evidence, reconciliation | Orchestration owner; E3V-001/005 owner | Old plan, context, pending approvals, workspace assumptions, predicates and verification invalidated | Redirected and active/waiting/blocked; old operations known failure/unknown | ADR-E2-002, 003, 005, 006, 007 | AR-COR-002/005/007, AR-DUR-004, AR-VER-003 | E3V-001/005; E4U-C01-IMPLEMENTATION |
| `REC-20` resume and full revalidation | Latest authoritative task/plan/owner plus actual repository/workspace/instruction/authority/approval/route/effect/verification state | Fresh readback of every resume precondition and waited-event identity/version | Resume only after all required checks pass; otherwise remain waiting/blocked/recovering; never replay protected input | Each precondition known; unresolved effect/protected delivery remains unknown or waiting | Revalidation manifest, sources/versions, denials, unresolved items, new epoch where needed | Core recovery/orchestration owner; E3V-001/005/006 owner | Every stale binding, context, approval, route, evidence and verification invalidated before reconstruction | Resumed, waiting, blocked, recovering, unknown outcome | ADR-E2-002, 003, 004, 005, 006, 007 | AR-DUR-002/004, AR-CTX-002, AR-SEC-006, AR-VER-003 | E3V-001/003/005/006; E4U-C01-IMPLEMENTATION |
| `REC-21` pause, stop or force-stop | Durable ordered control plus process/effect state | Control acknowledgement, process-tree observation, fence/effect readback | Launch no new productive work; cooperative cancel then force where supported; fence always; reconcile partial bytes/effects | Known cancelled/failed endpoints or `UNKNOWN_OUTCOME` for crossed effects | Control timeline, bounds, descendants, fence, actual bytes/effect readback | Orchestration/supervisor owner; E3V-002 owner; structural failure hands back | Productive grants, pending approvals, affected workspace evidence and verification invalidated | Paused, cancelled, blocked, known failure, unknown outcome; never completed by kill alone | ADR-E2-003, 004, 005 | AR-DUR-004, AR-EXE-002/003 | E3V-002; E4U-C01-IMPLEMENTATION |
| `REC-22` lost external-effect acknowledgement | Durable intent/attempt/effect identity plus authoritative external target state | Target-specific readback correlated to exact attempt; response alone is insufficient | Do not blind retry; reconcile until known or retain unknown; return committed first outcome on duplicate intake | `KNOWN_SUCCESS`, `KNOWN_FAILURE`, or `UNKNOWN_OUTCOME` | Intent/approval/attempt/transport receipt, target readback, certainty and limitations | Effect gateway owner; E3V-001 owner; structural bridge failure hands back | Completion, approval reuse and dependent verification invalidated until resolved | Known success, known failure, unknown outcome, blocked | ADR-E2-003, 005, 007 | AR-DUR-003, AR-APR-002, AR-EVD-001 | E3V-001/005; E4U-C01-IMPLEMENTATION |
| `REC-23` protected-entry or delivery ambiguity | Non-secret protected receipt/authorization state and exact current recipient/use/fence; raw value is never authority | Capture-state, recipient acceptance and non-secret receipt readback; no raw reconstruction | Revoke/fence old grant; do not replay; require fresh human acquisition after crash, replacement or uncertain consumption | Known not delivered, known delivered only with exact receipt/readback, or explicit unknown; missing protection waits closed | Non-secret authorization/receipt, capture-state scan, recipient/fence outcome, forbidden-surface scan | Protected-entry/capability owner; E3V-006 security owner; structural impossibility hands back | Old grant, recipient, context and any dependent operation invalidated; raw value absent from recovery | `WAITING_FOR_USER`, blocked, known failure, or unknown delivery; never ordinary-input fallback | ADR-E2-001, 004, 005, 008 | AR-SEC-003/006, AR-APR-003 | E3V-006; E4U-C01-IMPLEMENTATION |
| `REC-24` provider/request ambiguity | Core route/operation record plus actual provider/transport/usage state where observable | Correlation, route, transport/provider status, cancellation, usage/cost and result validation | Preserve requested/resolved route; no hidden fallback; cancel/read back where supported; retry only as a new admitted attempt after known non-effect | Known denial/failure or `UNKNOWN_OUTCOME`; unobserved billing/result is not zero | Route/request IDs, raw-linked response/failure, cancellation, usage/cost/missingness | Provider gateway owner; E3V-004 owner; structural semantic loss hands back | Context/result/evidence/role eligibility invalidated; budget consumption retained | Known failure, unknown outcome, blocked/unassigned, or separately admitted retry | ADR-E2-005, 006, 008 | AR-MOD-001..003, AR-SEC-004, AR-FAIL-001 | E3V-004/007/008; E4U-C01-IMPLEMENTATION |
| `REC-25` agent disable or retirement | Durable agent identity, disable/retire control, ownership and unresolved-operation/effect records | Current lifecycle/owner reread and nonterminal scan | Stop new claims; fence current productive authority; reconcile in-flight work/effects before releasing responsibility; preserve identity/history | Known final operations or `UNKNOWN_OUTCOME`; retirement does not erase responsibility | Lifecycle transition, claims denied, fence, in-flight disposition, retained evidence | Orchestration/recovery owner; E3V-001/002 owner | Grants, claims, context, approvals and current verification invalidated as applicable | Disabled/retired with all work known, blocked, or unresolved unknown retained | ADR-E2-003, 009 | AR-DUR-002/004, AR-FUT-002 | E3V-001/002; E4U-C01-IMPLEMENTATION |

### 7.1 C01 workspace partial-write subcases

All seven C01 f09 subcases inherit every `REC-10` field, including its owner, invalidations, ADR/AR links and allowed dispositions. The delta below prevents a combined row from losing candidate semantics.

| C01 f09 subcase | Required detection/readback and action | Allowed result |
|---|---|---|
| Process dies during file write | Treat the edit as unconfirmed intent; inventory and reread actual bytes/metadata before any success claim. | `PARTIAL`, blocked, known failure/success only by readback, or `UNKNOWN_OUTCOME`. |
| Partially written file exists | Preserve the partial artifact and observed digest/size; do not overwrite user state merely to match intent. | Partial/blocked/unverified. |
| Interrupted rename or replace | Inspect source, destination, temporary objects and directory metadata; accept neither old nor new state without readback. | Known old/new only by readback; otherwise partial/blocked. |
| Multi-file edit partially completes | Reconcile every intended path against pinned base and operation record; retain achieved subset and invalidate aggregate predicates. | Partial, blocked, unverified; never inferred all-or-nothing success. |
| Git index differs from worktree | Reread HEAD, index and working tree; preserve discrepancy and do not stage/reset or attribute without evidence. | Blocked/partial/known current Git state. |
| Generated artifact partial write | Mark incomplete; retain safe bounded partial provenance; exclude from evidence/completion until regenerated and integrity-checked. | Incomplete/known failure/unverified. |
| Uncertain filesystem on recovery | Enter `RECOVERING`; compare pinned base and operations with actual state/canaries; invalidate stale verification. | Blocked, unverified, partial, known failure/success, or unknown outcome. |

## 8. Execution and isolation baseline

- Potentially mutating reproduction or work begins only after a task-identified isolated workspace is bound and original user state is inventoried.
- The minimum supported untrusted-execution claim is the verified technology-neutral Tier 2 semantic floor: normalized allowed roots/object identity, process ownership, declared working directory/environment, bounded time/output/resources, denied-by-default network and secret scope, descendant accounting, cancellation/force-or-fence, stale authority rejection, and fresh state/effect readback.
- The supervisor owns every admitted process identity and descendant relationship it claims to support. Process-tree termination and authority fencing are distinct: unavailable force termination narrows the support class and blocks/fences work; it never permits stale effects.
- Git operations obey all 30 frozen classifications. Hooks, helpers, filters, signers, transports and package scripts are executable/effectful surfaces, not implicit consequences of a Git or dependency request.
- Exact host/process containment feasibility is not proven. `AR-EXE-003` remains linked to `E3V-002` and canonical handback set `ADR-E2-003/004/007`; ADR-E2-007 is included because the frozen `AR-TST-001/002` validation/readback contract is structurally affected if the claimed containment boundary cannot be evidenced independently.

## 9. Protected entry

The integrated trusted application boundary contains a dedicated protected-entry controller that is outside ordinary request, model, transcript, terminal-output, logging, telemetry, screenshot/accessibility capture and evidence pipelines. It obtains an authenticated one-use recipient/use/fence authorization, suspends unauthorized observation surfaces, delivers the raw value only to the exact current recipient in transient protected memory, and returns only a non-secret receipt containing identity/scope/time/outcome facts.

Raw values are never placed in authoritative state, material history, context, projection, log or evidence; they are never replayed after crash/replacement. Revocation, owner/recipient replacement, uncertain consumption or failed capture exclusion invalidates the authorization and returns the task to `WAITING_FOR_USER` or blocked. The concrete client/acquisition/carrier mechanism is unselected and unvalidated. `AR-SEC-006` and the C01-specific delivery question remain under `E3V-006`; the canonical handback set is `ADR-E2-001/004/005/007/008/009`. ADR-E2-007 is included for the primary `AR-TST-001/002` independent-evidence contract, while ADR-E2-009 is included because the selected packaged client/runtime boundary must preserve the same protected-entry property.

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
| `ADR-E2-009` | `REVERSIBLE_EARLY` | Package/update/client mechanics before release. | Contributor lifecycle contract and reserved port identities become more expensive only after ecosystem adoption; that possible later cost does not create a fourth class. | Reproducible setup/update/rollback, compatibility matrix and no hidden mandatory service/cloud. |

The closed reversibility vocabulary is `REVERSIBLE_EARLY`, `MODERATELY_COSTLY`, and `FOUNDATIONAL_HIGH_COST`. These classes describe migration cost only. They are a separate axis from the governance status `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`; none of the classes means accepted, selected, or verified.

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

### 18.1 Canonical E3V handback closure

The canonical set is computed mechanically as: (a) take the canonical linked ARs in verified E2-001 §9 plus the C01-specific linked ARs in the verified decision matrix; (b) include every primary ADR owner in §13 whose architecture assumption that E3V tests would be disproved by an architecture-class failure; and (c) include only a secondary ADR for an explicitly identified structural dependency. Frozen E2-001 AR ownership is unchanged. The set is neither narrowed to the ADR that happens to implement a fixture nor widened for review convenience.

| E3V | Primary-owner closure | Justified secondary dependency | Canonical ADR handback set |
|---|---|---|---|
| `E3V-001` | `AR-COR-001/007 -> ADR-E2-003`; `AR-DUR-001/005, AR-PRF-003 -> ADR-E2-002`; `AR-DUR-002/003 -> ADR-E2-003`; `AR-APR-002 -> ADR-E2-005`; `AR-FAIL-001 -> ADR-E2-008`; `AR-TST-001/002 -> ADR-E2-004/007`; `AR-FUT-001 -> ADR-E2-009` | None. | `ADR-E2-002/003/004/005/007/008/009` |
| `E3V-002` | `AR-DUR-004 -> ADR-E2-003`; `AR-EXE-002/003, AR-TST-001 -> ADR-E2-004`; `AR-TST-002 -> ADR-E2-007` | None. | `ADR-E2-003/004/007` |
| `E3V-003` | `AR-DUR-006 -> ADR-E2-002`; `AR-WSP-001..005, AR-GIT-001 -> ADR-E2-004`; `AR-PKG-001, AR-PRF-006 -> ADR-E2-009` | ADR-E2-001 owns the client/core lifetime and no-hidden-service topology exercised by the package. | `ADR-E2-001/002/004/009` |
| `E3V-004` | `AR-MOD-001..003 -> ADR-E2-006`; `AR-SEC-004 -> ADR-E2-005`; `AR-FAIL-001 -> ADR-E2-008`; `AR-TST-001/002 -> ADR-E2-004/007`; `AR-FUT-003 -> ADR-E2-009` | ADR-E2-001 owns gateway placement within the integrated runtime. | `ADR-E2-001/004/005/006/007/008/009` |
| `E3V-005` | `AR-COR-003, AR-DAT-001/002 -> ADR-E2-002`; `AR-COR-004..006, AR-EVD-001..003, AR-VER-001..003 -> ADR-E2-007`; `AR-CTX-001/002 -> ADR-E2-006`; `AR-GIT-002 -> ADR-E2-004`; `AR-OBS-002 -> ADR-E2-008` | ADR-E2-003 supplies causal operation identity; ADR-E2-005 supplies approval/effect authority used as evidence. | `ADR-E2-002/003/004/005/006/007/008` |
| `E3V-006` | `AR-EXE-001, AR-EXE-004, AR-TST-001 -> ADR-E2-004`; `AR-SEC-001..006, AR-APR-001/003 -> ADR-E2-005`; `AR-TST-002 -> ADR-E2-007`; `AR-FUT-002 -> ADR-E2-009` | ADR-E2-001 owns the client protected-entry surface; ADR-E2-008 owns capture/log exclusion and secret-safe failure presentation. | `ADR-E2-001/004/005/007/008/009` |
| `E3V-007` | `AR-OBS-001, AR-FAIL-002, AR-TST-003, AR-PERF-001/002 -> ADR-E2-008`; `AR-PRF-001 -> ADR-E2-001`; `AR-PRF-005 -> ADR-E2-007` | ADR-E2-002 supplies durable raw measurement inputs; ADR-E2-009 owns package/runtime limit exposure. | `ADR-E2-001/002/007/008/009` |
| `E3V-008` | `AR-MOD-001..003 -> ADR-E2-006` | None. Ordinary model/configuration failure does not reopen architecture. | `ADR-E2-006` |

Mechanical validation must extract each `E3V-*` set from this table, the E3 obligation index and record, every ADR that carries the E3V, the author/fixer handoffs, and the current task record; normalize ADR IDs as an unordered set; and require set equality. It must also join each linked AR above to the §13 primary owner and assert owner inclusion. A mismatch blocks review.

### 18.2 Bundle and SP-C provenance chains

The detailed, field-complete deferral chains are in the E3 validation register §12. At baseline level the carried chain is:

`E2U-S01-DESCENDANT-CONTAINMENT -> E3V-002 -> AR-EXE-003/AR-TST-001/002 -> ADR-E2-003/004/007 -> bounded descendant/force-or-fence evidence -> block/fence unsupported classes -> ARCHITECTURE_HANDBACK to that same canonical set when structurally disproven`.

`E2U-S02-PROTECTED-ACQUISITION` and `E3U-C01-PROTECTED-DELIVERY -> E3V-006 -> AR-SEC-003/006 plus AR-TST-001/002 and AR-FUT-002 -> ADR-E2-001/004/005/007/008/009 -> synthetic-marker acquisition/delivery/capture-exclusion evidence -> WAITING_FOR_USER or blocked on absence/ambiguity -> ARCHITECTURE_HANDBACK to that same set when structurally disproven`.

`E3U-C01-TECHNICAL` decomposes to `E3V-001..007`; `E3U-C01-MODEL-CONFIGURATION` maps only to `E3V-008`. Verified `SP-C01`, `SP-C03`, `SP-C04`, and `SP-C05` supply cited contract shapes, fixtures, negative cases, and evidence fields where applicable; they are not C01 architecture proof and no spike was run. The three E4 bundles below are implementation/configuration detail, not hidden ADRs.

The three verified E4 implementation bundles remain preserved:

- `E4U-C01-IMPLEMENTATION` (applicable if this proposal survives): client/runtime; embedded store; schema/codec; process API; isolation mechanism; provider SDKs/adapters; package/update tooling.
- `E4U-C02-IMPLEMENTATION` (provenance for the viable rejected alternative): service/client/runtime; IPC/auth; store/schema; worker supervisor; isolation mechanism; provider adapters; installer/updater.
- `E4U-C03-IMPLEMENTATION` (provenance for the viable rejected alternative): runtime/journal/payload; event/schema/reducer; projections/checkpoints; executor/isolation; provider adapters; client/package.

These are implementation/configuration choices behind defined seams. E2-005 selects none of their concrete technologies, and E4 remains unauthorized. `E4U-C01-IMPLEMENTATION` is the only proposal-applicable bundle if C01 later survives independent selection; the C02/C03 bundles remain historical reopen evidence, not active implementation plans.

## 19. E2-006 review contract

E2-006 must independently rederive rather than inherit:

- exact derivation from `EP-ARCH-C01` with no hybridization;
- 127 E1 → 65 AR → nine ADR completeness and all 25 domains;
- 59 non-compensating hard results and six unweighted preference tradeoffs;
- all 20 threat boundaries with all nine C01 fields, 25 recovery scenarios plus seven partial-filesystem subcases, approval/effect and protected-entry semantics;
- evidence/verifier independence and full frozen-suite testability seams;
- provider/model neutrality and zero role assignment;
- all eight canonical E3V definitions, primary-owner closure and set equality across every representation, one canonical ADR handback set each, fail-closed consequences and the registered plan-only finite-ceiling authority;
- explicit E2/E3 bundle and verified SP-C provenance chains, plus all three E4 bundles as implementation-only deferrals;
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
