# Engineering Preview Architecture Comparison

Status: **E2-003 AUTHOR PASS — READY_FOR_REVIEW; NOT VERIFIED**

Comparison version: `EP-ARCH-COMP-0.1`

Task: `E2-003`

Author base commit: `b5b35a7fc5190ddbe359bd99f51fea4189ccff6a`

Architecture selection: **NOT_SELECTED**

Preferred candidate: **NONE**

Accepted architecture ADRs: **0**

Architecture spikes, evaluation cases, model benchmarks, paid calls, and application-code changes performed by E2-003: **0 / 0 / 0 / 0 / 0**

## 1. Authority, scope, and non-decision

This comparison applies the independently verified `EP-ARCH-REQ-0.2` contract to the three independently verified `EP-ARCH-CANDIDATE-0.3` records. It is a comparison-layer analysis. It does not modify the candidate definitions, select or recommend an architecture, create an ADR, choose a technology, assign a provider/model, or execute a spike.

The frozen E1 specification, the E2 plan, the E2-001 requirements/traceability pair, and the E2-002 candidate records remain authoritative inputs. Candidate prose is a design proposal, not implemented or observed capability. The companion decision matrix records one row for each of the `3 × 65 = 195` candidate/criterion cells.

Claim types are used literally:

| Claim type | Meaning in this comparison |
|---|---|
| `FACT` | Repository state or mechanically reproduced count/hash. |
| `INFERENCE` | A bounded conclusion from the verified requirement and candidate records. |
| `PROPOSAL` | A candidate's unimplemented structural contract. |
| `UNKNOWN` | Evidence is insufficient; the item receives no favorable credit. |

Comparison results are also literal:

| Result | Consequence |
|---|---|
| `CONFIRMED_SATISFIED_FOR_COMPARISON` | The design supplies a coherent structural path for the hard property. Implementation conformance remains unproven and the listed E3/E5 obligation remains. |
| `ANALYSIS_RESOLVABLE` | Paper analysis is still needed. No final cell remains in this state after this author pass. |
| `ARCHITECTURE_BLOCKING_SPIKE` | The hard property cannot be credited before bounded E2-004 evidence. No favorable score or assumed pass is allowed. |
| `KNOWN_VIOLATION` | The candidate fails the hard gate unless a repair preserves its architecture identity. No such result was found. |
| `QUALITATIVE_CHARACTERIZATION_ONLY_NO_SCORE` | The preference is described structurally, without weight, numeric value, rank, or compensation for a hard result. |

## 2. Frozen comparison input

The author mechanically reproduced the input before comparing it.

| Input | Reproduced value | Source/binding |
|---|---:|---|
| Candidates | 3 | `EP-ARCH-C01`, `EP-ARCH-C02`, `EP-ARCH-C03` under `05_architecture/candidates/` |
| Architecture requirements | 65 | 59 `HARD_CONSTRAINT`; 6 `WEIGHTED_PREFERENCE` |
| Canonical frozen E1 IDs | 127 | Verified traceability baseline; 119 case-backed and 8 protocol-backed IDs |
| Decision domains | 25 | `D01`–`D25` per candidate |
| Threat boundaries | 20 | `TB-01`–`TB-20` per candidate |
| Level B families | 19 | `LB-01`–`LB-19` per candidate |
| E3 obligations | 8 | `E3V-001`–`E3V-008` per candidate |
| Evaluation assets | 170 cases; 18 oracles; 11 fixture families | Also 23 negative families, 16 repository rows, 30 Git/effect rows, 9 adequacy variants, 16 compositions, and 8 protocols |
| Normalized E2-002 spike questions | 5 | 2 shared, 3 candidate-specific, 9 candidate references, 0 run |
| E2-002 uncertainty records | 28 | 10 analysis, 9 spike references, 3 E3, 3 E4, 3 future |
| Input hard map per candidate | `52 / 5 / 2 / 0` | Satisfied by design / plausible for E2-003 / spike unknown / violated |
| Architecture selection | `NOT_SELECTED` | Preferred candidate `NONE`; ADRs 0 |

The compared candidate bytes are fixed by these SHA-256 values:

| Candidate | SHA-256 |
|---|---|
| `EP-ARCH-C01` | `ea9ff609a2c89c96b721fef4f6005d28238940b17085ffc2d82a13ff5b688e92` |
| `EP-ARCH-C02` | `899f7fa0933da3a7657a928f0aa5e2b4b94ffc80778bf6ba8d5a36fb6c45ba81` |
| `EP-ARCH-C03` | `72cacf1cf6d7d99807b3d0c4c10180bb9dc079516443843ac3c87919d319e4f0` |

The E2-002 verification commit is `1a1c5423da83d3dfe9c7f759300bf10d68e4281e`. The current author base, `b5b35a7fc5190ddbe359bd99f51fea4189ccff6a`, adds only the independent E2-002 verification/governance transition over that candidate baseline. No candidate artifact has been changed by E2-003.

## 3. Comparison method and weighting discipline

The prospective method is:

1. Apply all 59 hard constraints as non-compensating gates.
2. Resolve the candidate-declared E2-003 paper questions using the frozen requirements and the candidate's own process, authority, persistence, recovery, security, packaging, and migration contracts.
3. Preserve any empirically undecidable hard property as an E2-004 blocker. `UNKNOWN` receives no point, midpoint, tie-break benefit, or assumed pass.
4. Compare the six preferences qualitatively only after the hard-gate pass. No numerical score, ordering, or winner is produced.
5. Compare all 25 domains, 20 threat boundaries, 19 Level B families, recovery/security/testability, contributor burden, implementation complexity, local-first behavior, future evolution, and reversibility using the same evidentiary bar.
6. Test strict dominance and decision sensitivity without selecting or recommending.

Final weights are not authorized or evidenced. They are not assigned. The weight owner is the later E2-005 decision-authority process, which may preserve an explicit qualitative rationale or seek founder priority input after E2-004 evidence. Any prospective numeric weighting would need a reviewed pre-result amendment.

The following correlated groups prevent double counting:

| Correlation group | Criteria/subjects | Policy |
|---|---|---|
| `RECOVERY_CORRECTNESS_EVIDENCE` | durability, recovery, history, evidence integrity, false completion | Describe distinct mechanisms and consequences; do not count one retained history property repeatedly. |
| `SECURITY_AUTHORITY_EFFECT_ISOLATION` | capability, approval, secret, process, network, effect fencing | A shared enforcement boundary is one fact, not multiple favorable credits. |
| `MAINTAINABILITY_PACKAGING_MIGRATION` | operational complexity, contributor burden, packaging, schema/topology migration | Expose the separate user effects but do not add them into a score. |
| `FUTURE_REMOTE_CONCURRENCY_REVERSIBILITY` | remote seam, multiple owners/clients, reversibility | Minimum compatibility is hard; lower adaptation cost is only a preference. |
| `PERFORMANCE_LOCAL_OVERHEAD_COST` | latency, evidence overhead, resource/cost instrumentation | Structural path is an inference; actual values remain E3 observations. |

## 4. Hard-constraint comparison

### 4.1 Gate result

All three candidates survive analytical hard-gate elimination, but none is selection-ready because two shared hard properties still require E2-004 evidence.

| Candidate | Confirmed satisfied for comparison | Analysis resolvable remaining | Architecture-blocking spike | Known violation | Consequence |
|---|---:|---:|---:|---:|---|
| `EP-ARCH-C01` | 57 | 0 | 2 | 0 | `NEEDS_E2_004`; conditionally eligible for E2-005 only if both blockers pass. |
| `EP-ARCH-C02` | 57 | 0 | 2 | 0 | `NEEDS_E2_004`; conditionally eligible for E2-005 only if both blockers pass. |
| `EP-ARCH-C03` | 57 | 0 | 2 | 0 | `NEEDS_E2_004`; conditionally eligible for E2-005 only if both blockers pass. |

This result does not rewrite the verified E2-002 source statuses. The matrix preserves `input_generation_status` and separately records the E2-003 comparison result.

### 4.2 Five paper-resolvable hard properties

| Requirement | C01 evidence and analysis | C02 evidence and analysis | C03 evidence and analysis | Result and later evidence |
|---|---|---|---|---|
| `AR-DUR-005` corruption, partial write, evolution | `f08/f09` define transactional old-or-new current state, versioned migration, quarantine, preserved original evidence, and explicit interrupted endpoints. | `f08/f09` define transactional service records/inbox/outbox, migration and quarantine, plus itemized partial-write recovery. The missing `f27` pointer is bookkeeping, not missing design evidence. | `f08/f09` require durable payload before event acknowledgement, ordered journal validation, quarantine/trusted replay, visible migration, and orphan-payload reconciliation. The missing `f27` pointer is bookkeeping. | All three `CONFIRMED_SATISFIED_FOR_COMPARISON`; actual corruption and migration faults remain `E3V-001/005`. |
| `AR-WSP-003` confinement/adversarial paths | The integrated workspace broker normalizes and re-resolves objects at open, mutation, and cleanup and fails closed on unsupported topology. | The service broker plus worker boundary revalidates object/root identity; the service remains authority over workspace scope. | Command admission and the workspace adapter bind object/root identity; events record denial/readback rather than granting path authority. | All three confirmed at design level. Exact supported-host mechanisms and all negative cases remain `E3V-003/006`; descendant containment is separately blocked. |
| `AR-SEC-003` exact protected recipient | A separate one-use, recipient/use/fence-bound protected path excludes ordinary core/model/log/evidence routes and returns only a non-secret receipt. | The service issues a non-secret, lease/fence-bound authorization; raw bytes travel directly from protected client broker to the exact current recipient and never through service state. | The protected broker is outside the command/event/payload/projection path; only a non-secret receipt event rejoins authority. | All three confirmed structurally. Candidate-specific delivery implementation is `E3V-006`, not a preselection hard-feasibility blocker. |
| `AR-SEC-004` network boundary | Embedded gateway/network policy binds destination, data, credential, budget, redirects, and zero-dispatch denial. | Service network gate and worker policy enforce the same contract at both control and execution boundaries. | Network capability commands and adapters record the effective target and zero-dispatch/uncertain-effect outcome as material events. | All three confirmed structurally; negative and adapter evidence remains `E3V-004/006`. |
| `AR-PKG-001` local-first, contributor-operable boundary | One visible task-bound application/core plus declared child processes and local state; no hidden service or cloud. Broad-core coupling is a preference cost. | A visible local service, clients, workers, state, lifecycle, and update/recovery contract; no hidden mandatory cloud. Multi-process setup is a preference cost, not a hard failure. | A visible local runtime, journal/payload boundary, reducer/projection/checkpoint tools, and migrations; no mandatory daemon or cloud. Conceptual burden is a preference cost. | All three confirmed at the packaging hard floor; exact toolchain/setup remains `E3V-003` and later implementation. |

### 4.3 Two hard blockers

| Requirement | Why paper analysis stops | Normalized blocker | Consequence |
|---|---|---|---|
| `AR-EXE-003` | Epochs, leases, fences, and workflow state can reject stale authority, but prose cannot prove supported-host descendant termination, post-fence effect deprivation, or whole-tree accounting. | `E2U-S01-DESCENDANT-CONTAINMENT` | E2-005 consideration for every candidate is blocked until E2-004 passes the shared host primitive and each topology wrapper. |
| `AR-SEC-006` | A proposed protected boundary cannot prove that the supported client/host excludes keystroke, clipboard, screen/accessibility, terminal, model, transcript, log, telemetry, artifact, and evidence capture. | `E2U-S02-PROTECTED-ACQUISITION` | E2-005 consideration for every candidate is blocked until E2-004 proves shared acquisition/capture exclusion and fail-closed unavailability. |

### 4.4 Required material rechecks

| Requirement | E2-003 conclusion |
|---|---|
| `AR-EXE-003` | Remains a shared E2-004 blocker; logical fencing is not treated as physical descendant containment. |
| `AR-DUR-003` | All candidates preserve intent/attempt/receipt/readback/unknown across the record-to-effect crash window. The ambiguity differs in topology but is not removed by any candidate; design-level hard status remains confirmed and fault evidence remains E3. |
| `AR-DUR-004` | All candidates preserve duplicate original outcomes, resume revalidation, event correlation, and owner/agent lifecycle. No-live-owner intervals are visible availability/preference characteristics, not fictitious deadline enforcement. |
| `AR-DUR-005` | Resolved for all candidates as described above; the C02/C03 comparison layer supplies the missing `f27` rationale. |
| `AR-FUT-001` | C01's replaceable executor port, C02's worker interface, and C03's serializable dispatch contract all meet the hard compatibility floor; extraction/adaptation cost remains preference-only. |
| `AR-FUT-002` | Version/epoch, lease/fence, or stream-sequence/owner records prevent permanent global-singleton semantics without implementing future concurrency. All remain confirmed. |
| `AR-SEC-003` | Paper-resolved uniformly; SPQ-03/04/05 affected lists were overbroad for preselection classification. |
| `AR-SEC-006` | Shared acquisition/capture remains blocked; candidate delivery moves to E3 postselection validation. |
| `AR-TST-002` | Each candidate exposes 9 family seams, 16 composition seams, and `EP-CTL-016`; all remain confirmed without rewarding the number of internal components. |
| `AR-PKG-001` | Confirmed at the explicit/no-hidden-service hard floor; setup and contributor cost remain preference evidence. |

### 4.5 E2-002 verifier finding dispositions

`V-E2-002-01` is resolved by comparison-layer analysis. C02 and C03 already contain the required `AR-DUR-005` mechanisms in `f08/f09`; their missing `f27` pointers do not change the frozen candidates. The uncertainty register adds `AR-DUR-005` to the affected comparison-layer paper resolution for `C02-U03` and `C03-U04` and records the exact source evidence.

`V-E2-002-02` is resolved uniformly. `AR-SEC-003` is paper-resolvable and confirmed from the exact-recipient protocols. SPQ-03/04/05 are related to delivery implementation but their affected-AR linkage is overbroad for preselection: they are reclassified to candidate-scoped `E3_POSTSELECTION_TECHNICAL_VALIDATION` under `E3V-006`. `AR-SEC-006` retains the shared acquisition/capture blocker `SPQ-E2-002-02`; no raw protected value is evidence.

## 5. Preference comparison

No weight or numeric score is assigned. Structural characterizations receive no empirical or favorable-unknown credit.

| Preference | C01 | C02 | C03 | Sensitivity and evidence limit |
|---|---|---|---|---|
| `AR-PRF-001` lower latency | Fewer top-level crossings on the ordinary local control path; core/child boundaries still exist. | Client/service/worker IPC, authentication, lease, and dispatch crossings add local path length. | Append/admit/reduce/project work adds logical steps; no permanent service is required. | C01 gains if short local control paths dominate, but actual latency is unknown until `E3V-007`. |
| `AR-PRF-002` lower operational/maintenance complexity | One integrated authority simplifies lifecycle count but broadens coupling and failure blast radius. | Clear service/worker ownership and replaceability add service lifecycle, IPC/authentication, and lease/fence operations. | Deterministic event authority and rebuildable projections add event schema, reducer, checkpoint, replay, and evolution concepts. | Preference depends on whether topology count, bounded subsystem ownership, or replay rigor is valued; no additive complexity score is justified. |
| `AR-PRF-003` migration/reversibility | Ports exist, but extracting the integrated single-writer core and record semantics is a material migration. | Clients/workers are replaceable; service/store and lease/effect protocol are foundational. | Adapters/projections are replaceable; canonical event identity/order/meaning and journal/payload boundary are foundational. | Each has a different lock-in center; no candidate is universally lowest-lock-in. |
| `AR-PRF-004` remote/concurrency adaptation | Versioned ports/epochs preserve the floor, but remote control ownership requires extraction and a new transport/auth boundary. | Local service/worker separation and leases resemble the future seam, while real remote transport, tenancy, and authorization remain absent. | Serializable commands/events and replaceable adapters help transport/replay, while distributed ordering/retention are not implemented. | C02 and C03 gain under remote-seam priority; C01 avoids some current distributed-style burden. This is not a hard-status difference. |
| `AR-PRF-005` lower evidence overhead | Transactional current state plus material history can keep the common read path compact; actual retention/serialization cost is unknown. | Service history/inbox/outbox/effect/evidence records add cross-component correlation overhead; actual cost is unknown. | Journal, payload references, projections, and checkpoints maximize replay information but can add retention and rebuild overhead. | C03 gains on reconstructability but may lose on storage/replay overhead; measured values belong to `E3V-007`. |
| `AR-PRF-006` contributor/local packaging burden | One visible package/runtime is topologically simpler; broad-core ownership and safe subsystem changes need strong port/dependency discipline. | More processes, setup, IPC/auth, and lifecycle debugging; narrower worker/service boundaries can localize changes. | No permanent daemon is required, but event/reducer/projection/migration/replay concepts increase onboarding and documentation burden. | Contributor accessibility is not inferred from component count. `E3V-003` and the later contributor walkthrough must observe it. |

## 6. Decision-domain comparison

In the final column, `U` is unresolved evidence, `H/P` is the hard/preference implication, and `M` is the migration implication.

| Domain | C01 shape | C02 shape | C03 shape | Comparative strengths and weaknesses | U / H/P / M |
|---|---|---|---|---|---|
| `D01` client/interaction | Presentation can detach from a task-bound integrated core. | Thin clients speak to a persistent user-local control service. | Clients issue commands and consume rebuildable projections. | C01 has a short local path; C02 makes client loss least coupled to control ownership; C03 keeps presentation most explicitly derived but adds projection semantics. | U: protected capture. H: client truth/detach satisfied. P: latency/setup. M: client protocol differs. |
| `D02` core runtime | Broad integrated policy/orchestration/store core. | High-authority local service with replaceable workers. | Journal/append gate plus deterministic reducers; coordinator replaceable. | C01 minimizes top-level components but centralizes coupling; C02 modularizes execution but creates a service availability boundary; C03 makes history/rebuild structural at the highest conceptual cost. | U: implementation validation only. H: all preserve authority. P: complexity. M: core/service/event model foundational. |
| `D03` orchestration | Core scheduler/state loop. | Service scheduler with leases/fences. | Workflow commands/events reduced into state. | Direct control, explicit worker ownership, and deterministic replay are different strengths; none removes effect ambiguity. | U: E3 faults. H: confirmed. P: operability. M: orchestration state representation locks in. |
| `D04` persistence | Transactional current state plus material history/outbox/effect ledger. | Service-owned transactional state/history/inbox/outbox. | Append-only material journal plus durable payload refs; projections disposable. | C01/C02 simplify current-state reads; C03 improves causal reconstruction but adds replay/evolution/retention burden. | U: E3 corruption/performance. H: confirmed. P: overhead/complexity. M: durable format is foundational. |
| `D05` canonical models | Integrated versioned task/conversation/evidence records. | Service-owned versioned records exposed to clients/workers. | Typed events and payloads are authority; reducer outputs are canonical current views. | All keep six semantic responsibilities distinguishable. C03 aligns history and rebuild most directly; C01/C02 require disciplined current/history reconciliation. | U: E3 semantic fault evidence. H: confirmed. P: maintainability. M: identity/schema evolution. |
| `D06` operation history | Core material history and operation/effect ledgers. | Service command/dispatch/result/effect history. | Material journal is the operation and causal history. | C03 has the most direct replay path; C01/C02 have simpler transactional coordination but two representations to reconcile. | U: crash injection E3. H: confirmed. P: recovery overhead. M: history model foundational. |
| `D07` workspace/filesystem | Core workspace broker. | Service broker controls workers. | Workspace adapter actions are event-correlated. | C02 centralizes scope across replaceable workers; C01 shortens the path; C03 maximizes event traceability. All rely on the same fail-closed object/path floor. | U: mechanism negatives E3. H: confirmed. P: portability. M: broker interface replaceable; workspace identity is durable. |
| `D08` execution/process | Integrated supervisor and child executors. | Leased/fenced worker supervisor. | Executor adapter plus workflow fence. | C02 replaces workers most directly; C01 has fewer control crossings; C03 records control causality. None proves descendant containment from logical fencing. | U: shared E2-004 process spike. H: blocker. P: contributor/latency. M: executor seams vary. |
| `D09` isolation | Shared Tier 2 semantic boundary owned by core brokers/supervisor. | Shared Tier 2 floor across service and workers. | Shared Tier 2 floor across command/adapters/executor. | More processes do not prove stronger isolation; fewer processes do not prove weaker isolation. Boundary locality and enforcement burden differ. | U: descendant containment E2-004; exact mechanism E3. H: blocker only for AR-EXE-003. P: portability/burden. M: technology unselected. |
| `D10` Git | Core Git adapter and gateway. | Service Git adapter with worker invocation policy. | Git command/event adapter. | All enforce the same 30-row matrix; C02 adds cross-process correlation, C03 adds event evidence, C01 has a short path. | U: full E3/E5 matrix. H: confirmed. P: operability. M: adapter replaceable. |
| `D11` approvals | Core approval ledger serialized with dispatch. | Service approval ledger and worker receipts. | Approval lifecycle events/reducer gate dispatch. | C02 centralizes across replaceable workers; C03 preserves immutable history; C01 reduces crossings. All fail closed on replay/mutation. | U: E3 negatives. H: confirmed. P: latency/complexity. M: receipt schema foundational. |
| `D12` effect reconciliation | Core intent/attempt/readback ledger. | Service-owned effect bridge and outbox/inbox. | Effect workflow events plus target adapter/readback. | C01 centralizes ambiguity; C02 separates worker loss from effect authority but adds fencing; C03 explains causality but does not eliminate external uncertainty. | U: E3 crash/readback. H: confirmed. P: recovery burden. M: effect identity stays durable. |
| `D13` provider gateway | Embedded role-neutral gateway. | Service provider gateway. | Provider command/result event adapter. | C01 has fewer crossings; C02 centralizes multi-worker routing; C03 makes provenance replayable. No provider quality is compared. | U: E3V-004/008. H: neutrality confirmed. P: latency/maintainability. M: gateway contract replaceable. |
| `D14` routing/capability discovery | Core policy/gateway. | Service registry/policy gateway. | Command admission and capability events. | All preserve purpose/eligibility and zero dispatch; topology affects locality, not product semantics. | U: E3 conformance/model benchmark. H: confirmed. P: operational burden. M: provider/model unselected. |
| `D15` context/memory | Core assembler and derived summaries. | Service context assembler/manifests. | Source-range summary projections. | C03 makes staleness/rebuild explicit; C01/C02 can offer simpler current reads. All preserve original authority. | U: E3 context faults. H: confirmed. P: overhead. M: summary mechanism replaceable. |
| `D16` verification | Separate verifier process/context invoked by core. | Separate verifier worker with service-owned inputs. | Verifier adapter reads journal/payload/current projection and exact revision. | C02/C03 have explicit replaceable verifier boundaries; C01 still has process/context separation. None has runtime verification evidence. | U: E3V-005/008. H: confirmed. P: complexity/latency. M: verifier interface durable. |
| `D17` evidence/artifacts | Core evidence builder over authoritative records. | Service evidence service and artifact refs. | Evidence projector plus immutable payload refs/positions. | C03 naturally reconstructs provenance; C01/C02 avoid making all material facts events. All distinguish evidence from telemetry. | U: E3/E5 validation. H: confirmed. P: overhead. M: artifact representation replaceable within identity contract. |
| `D18` observability | Core observability port and derived views. | Service observability with thin-client projections. | Observability projectors from material events plus separate telemetry. | C03 maximizes deterministic replay of views; C02 offers central multi-process correlation; C01 has fewer layers. | U: E3 instrumentation. H: confirmed. P: overhead. M: telemetry sink replaceable. |
| `D19` failures | Typed registry and core recovery decisions. | Cross-process typed failure service/contract. | Typed failure events and reducers. | C02 must preserve layer attribution across IPC; C03 must preserve schema/evolution semantics; C01 must avoid broad-core coupling. | U: E3 faults. H: confirmed. P: maintenance. M: stable codes/contracts required. |
| `D20` security | Core policy plus brokers/gateways. | Client/service/worker enforcement with service as high-authority boundary. | Command policy plus adapters and event admission. | C01 has a broader trusted core; C02 has more authenticated crossings and a service blast radius; C03 depends heavily on correct admission/reducers while keeping raw secrets out of events. | U: protected capture and process E2-004; full negatives E3. H: two blockers only. P: enforcement burden. M: trust boundaries foundational. |
| `D21` local packaging | One integrated package/core plus declared children. | Visible service/client/workers and service lifecycle. | Local runtime/journal/payload/projection tools; coordinator need not be a daemon. | C01 is topologically lightest; C02 has the most lifecycle setup; C03 has the largest conceptual/tooling model. Each exposes state and migration. | U: setup walkthrough E3. H: confirmed. P: packaging/contributor. M: topology/tooling migration. |
| `D22` future remote execution | Replaceable executor port needs control extraction. | Worker interface and leases already cross a local service boundary. | Serializable dispatch/result/fence events and replaceable adapters. | C02/C03 expose more direct remote seams; C01 pays less current control-plane machinery. None implements cloud. | U: future product deferred. H: compatibility floor confirmed. P: adaptation. M: C01 extraction vs C02 transport vs C03 distributed event semantics. |
| `D23` future concurrency/multi-agent | Versions/epochs and scoped IDs; integrated single writer now. | Service versions/leases/fences; one service authority now. | Expected sequence/owner/fence per stream; one owner now. | All reject stale activity and avoid permanent global identity. C02/C03 expose concurrency machinery more directly but do not implement multi-agent behavior. | U: future product deferred. H: floor confirmed. P: adaptation/current complexity. M: conflict model later. |
| `D24` extensions/skills/connectors | Core capability ports and versioned extension contract. | Service capability adapter boundary. | Versioned extension commands/events. | All preserve a governed boundary without a loader/marketplace. C02 centralizes activation; C03 makes evolution explicit; C01 has fewer crossings. | U: future product/E4 detail. H: confirmed. P: contributor burden. M: extension ABI/schema later. |
| `D25` E1-suite testability | Ports, store fault points, separate verifier. | Replaceable workers/services and IPC fault points. | Deterministic event fixtures, reducer replay, replaceable adapters/projections. | C03 is naturally replayable, C02 naturally substitutable, C01 lower-topology; extra injection points are not automatically better. | U: adapters unimplemented. H: confirmed. P: harness burden. M: all must retain stable test contracts. |

## 7. Correctness comparison

| Correctness property | C01 | C02 | C03 | Comparative conclusion |
|---|---|---|---|---|
| Truthful completion / false completion | Core derives completion from current records, effects, evidence, and verifier result. | Service derives completion and rejects worker self-report. | Reducer derives current completion only from valid material events and current verifier evidence. | All align structurally; C03's history is more intrinsic, while C01/C02 require disciplined current/history reconciliation. No runtime correctness is claimed. |
| Revision binding / stale invalidation | Store/history bind review revision and owner epoch. | Service binds revision and worker/verifier leases. | Journal position/payload/reducer version bind the reviewed state. | All can invalidate stale verification and post-pass mutation. |
| Independent verification | Separate process/context reads underlying core authority. | Separate verifier worker reads service authority, not executor report. | Separate verifier adapter reads journal/payload and exact projection inputs. | C02/C03 make replacement explicit; C01 still meets the same independence floor. |
| Predicate adequacy | Core evidence builder exposes obligation/predicate map. | Service-owned map supplied independently to verifier. | Versioned events/payload refs preserve map changes and results. | All expose the required seam; no candidate may infer adequacy from passing listed checks. |
| Partial/noncomplete outcomes | Orthogonal core state and effect records. | Orthogonal service state across worker loss. | Typed events/reducers preserve every outcome axis. | All preserve useful output without upgrading disposition. |
| Evidence integrity | Transactional records plus material history and gap/stale checks. | Service records plus immutable verification runs and cross-process correlation. | Ordered journal/payload integrity and rebuildable evidence projection. | C03 offers the clearest replay explanation but also the largest schema/reducer correctness burden. |
| Executor/verifier separation | Separate verifier process; broad core remains trusted authority. | Replaceable executor and verifier workers under service authority. | Executor and verifier adapters separated by commands/events and exact state. | The shape differs; the hard independence floor is equal. |

## 8. Durability and recovery comparison

| Recovery dimension | C01 | C02 | C03 |
|---|---|---|---|
| `RECOVERY_SOURCE_OF_TRUTH` | Transactional authoritative store, material history, operation/effect ledgers, exact workspace/artifact readback. | Service store, history, inbox/outbox, leases/fences, operation/effect ledgers, target readback. | Validated ordered journal plus durable payload refs; deterministic reducers, checkpoints, and target readback. |
| `RECOVERY_COMPLEXITY` | Lower topology, but a broad integrated recovery coordinator must reconcile many coupled responsibilities. | Worker loss is localized, but service/IPC/lease/fence/dispatch reconciliation adds coordination states. | Replay/rebuild is explicit, but journal/payload ordering, reducer determinism, schema evolution, checkpoints, retention, and gap handling are the largest conceptual surface. |
| `SINGLE_POINT_OF_FAILURE` | The live integrated core is the task authority; full core loss pauses live enforcement until restart/recovery. | The control service is the sole live authority and availability boundary; worker loss alone is replaceable. | The append gate/current stream owner is the live mutation boundary; coordinator absence is permitted, but no absent process enforces live deadlines. |
| `AMBIGUOUS_EFFECT_STRATEGY` | Persist intent/attempt, inspect receipts/readback, preserve `UNKNOWN_EFFECT`, never blind retry. | Service outbox/effect ledger survives worker loss; fence stale workers and read back the target. | Material intent/attempt/observed/readback events preserve uncertainty; replay never invents effect truth. |
| `RECONCILIATION_COST` | Centralized scans and fewer crossings; broad state ownership increases coupled fault reasoning. | More identities/correlations across service and workers, but replaceable execution narrows worker recovery. | Deterministic replay can reconstruct causality; long histories, payload availability, reducer versions, and checkpoint trust increase operational cost. |
| Partial writes/corruption | Transactional old/new plus quarantine/migration. | Transactional service records plus itemized inbox/outbox/workspace recovery and quarantine. | Payload-before-event, append validation, quarantine/trusted replay, orphan reconciliation. |
| Client exit | Detached presentation does not imply core loss; if core is absent, recovery happens on restart. | Thin-client exit does not affect a healthy service. | Client exit does not affect a healthy coordinator; coordinator may also be intentionally absent between active work. |
| Pause/stop/force | Core supervisor orders control and fences stale results; physical descendants remain an E2 blocker. | Service orders worker control and fences lease results; physical descendants remain an E2 blocker. | Control events plus executor fence preserve order; physical descendants remain an E2 blocker. |

C03's event model reduces ambiguity about what the product recorded and makes projection reconstruction explicit; it does not make external effects self-authenticating or remove gap/reducer/evolution risk. C01's integration reduces cross-process coordination but centralizes recovery responsibility and failure blast radius. C02's replaceable workers localize worker failure but add lease/fence and service availability complexity. These are tradeoffs, not a recovery winner.

## 9. Security and threat-boundary comparison

All 20 boundaries retain the same fail-closed semantic floor. The table compares enforcement locality and burden; it does not infer security from process count.

| Boundary | C01 enforcement | C02 enforcement | C03 enforcement | Comparative implication |
|---|---|---|---|---|
| `TB-01` user/authority | Core admission/policy kernel. | Client authenticator plus service admission. | Command policy/append admission. | C01 has one high-authority locus; C02 authenticates a crossing; C03 makes accepted/rejected authority material history. |
| `TB-02` repository | Core admission/workspace broker. | Service workspace broker. | Admission command/workspace adapter. | Same hard floor; C02 centralizes worker policy, C03 adds event evidence, C01 shortens path. |
| `TB-03` instructions | Core instruction interpreter/policy. | Service instruction-policy evaluator. | Instruction-policy command validator. | All keep content unable to widen authority; different persistence/locality only. |
| `TB-04` filesystem | Core workspace/filesystem broker. | Service plus worker broker enforcement. | Workspace adapter with event-correlated decisions. | C02 must keep two enforcement points consistent; C03 must keep adapter result/event truth aligned; C01 has a broader broker blast radius. |
| `TB-05` protected secret | Protected-entry controller and exact recipient inside separate path. | Client broker, non-secret service authorization, lease/fence-bound recipient; raw bypasses service. | Protected broker/recipient outside journal/payload/projection. | Shared capture is E2-blocking. Delivery shapes differ and remain `E3V-006`; C02 has the most authenticated crossings, C03 the strongest raw-event exclusion rule, C01 co-residency burden. |
| `TB-06` paths/topology | Core broker at open/mutate/cleanup. | Service and worker broker path. | Adapter at every access/cleanup. | All fail closed and re-resolve; negative implementation evidence remains E3. |
| `TB-07` subprocess | Integrated supervisor. | Worker supervisor plus service fence. | Executor supervisor plus workflow fence. | No logical fence is credited as descendant containment; shared E2 blocker. |
| `TB-08` terminal/protected I/O | I/O multiplexer plus protected controller. | Worker I/O plus client broker. | I/O adapter plus protected broker. | Output and protected input remain separate; capture exclusion is shared blocker. |
| `TB-09` packages/scripts | Core gateway/supervisor. | Service gate plus worker supervisor. | Capability command plus executor. | Same deny-by-default rule; C02 has cross-process consistency burden, C03 event/result integrity burden. |
| `TB-10` Git helpers/effects | Core Git adapter/gateway. | Service Git adapter plus worker policy. | Git command adapter. | All enforce 30 rows; no process-count security inference. |
| `TB-11` network | Core network gate before adapter. | Service gate plus worker network policy. | Network capability adapter. | C02 has two enforcement locations; C03 records target/cost events; C01 centralizes blast radius. |
| `TB-12` remote Git | Git adapter, approval, network. | Service Git/approval/network. | Git/network/approval adapters and events. | All require exact approval/readback; topology changes reconciliation evidence, not policy. |
| `TB-13` external APIs | Core capability gateway/effect ledger. | Service gateway/effect ledger. | Capability adapter/effect workflow. | C03 explains causal history most directly; C01/C02 simplify current intent lookup. External ambiguity remains equal. |
| `TB-14` provider | Embedded gateway/result validator. | Service gateway/result validator. | Provider command/result adapter. | All preserve provider neutrality; no provider quality or confidentiality claim is inferred. |
| `TB-15` capabilities/tools | Core gateway request/result validation. | Service gateway plus worker validators. | Command/result validators. | C02 narrows worker authority but expands crossing surface; C03 depends on event admission; C01 broad core compromise has larger blast radius. |
| `TB-16` approval | Core ledger serialized with dispatch. | Service approval ledger. | Approval reducer before dispatch. | All structurally resist replay/mutation; actual negative evidence is E3. |
| `TB-17` external effect | Core ledger and target readback. | Service effect ledger/adapter. | Effect workflow reducer/adapter. | None permits response-as-proof or blind replay. |
| `TB-18` evidence | Core builder/validator plus verifier. | Service validator plus verifier worker. | Evidence reducer/validator/verifier. | C03 makes gaps/replay prominent; C01/C02 must preserve history/current consistency. All bind exact revision. |
| `TB-19` recovery | Core startup recovery coordinator/epoch. | Service recovery coordinator/epoch/leases. | Recovery reducer and append gate. | C01 has centralized recovery; C02 adds lease transfer; C03 adds replay/reducer complexity. |
| `TB-20` human protected entry | Dedicated controller outside ordinary input pipeline. | Client broker to exact current worker; service sees only authorization/receipt. | Broker outside normal command/event path. | Shared acquisition proof blocks all; candidate delivery remains E3. Raw values never become comparison evidence. |

Trusted-computing-boundary tradeoff: C01 has fewer authenticated crossings but a broad high-authority core. C02 narrows disposable worker authority but makes the service a high-value availability/security boundary and adds IPC/lease authentication. C03 makes material history and policy admission explicit, but correctness of schemas, reducers, append validation, and adapters becomes part of the trusted design. None is declared more secure overall.

## 10. Protected entry

`AR-SEC-006` and `UF-11` split into two questions:

1. **Shared acquisition/capture feasibility.** Can the supported client/host suspend or exclude ordinary keystroke, clipboard, screen/accessibility, terminal, model, transcript, log, telemetry, artifact, and evidence observation and fail closed when it cannot? This remains `E2U-S02-PROTECTED-ACQUISITION` and blocks every candidate.
2. **Candidate-specific delivery.** Given a protected acquisition boundary, can the raw value reach only the exact recipient/use and return a non-secret receipt? C01 uses a co-resident but separately gated path; C02 uses a non-secret service authorization and direct client-to-current-worker handoff; C03 keeps the raw path outside journal/payload/projection. These protocols are structurally explicit and are reclassified to E3 postselection implementation/security validation.

The candidate-specific topology is decision-relevant as a security and implementation-burden tradeoff, but it is not a separate E2 preselection feasibility blocker. A candidate's E3 delivery failure hands the selected ADR back for revision; it never becomes a favorable E2 assumption.

## 11. Isolation

All candidates assume the same technology-neutral `TIER_2_OS_ENFORCED_EXECUTION_ISOLATION` semantic floor for untrusted execution. E2-003 does not choose a container, VM, worktree, operating-system API, process mechanism, or supported-host product matrix.

| Property | Shared floor | C01 locality | C02 locality | C03 locality | Remaining evidence |
|---|---|---|---|---|---|
| Filesystem | Object/path scope, ownership, link/topology checks, fail closed. | Core broker. | Service plus worker broker. | Workspace adapter/command events. | E3 negative mechanisms; paper hard floor confirmed. |
| Process tree | Account for descendants; bounded cancel/force/fence; no orphan effect authority. | Integrated supervisor. | Worker supervisor plus service fence. | Executor supervisor plus workflow fence. | Shared E2-004 blocker. |
| Network | Exact destination/data/credential/budget and effective-target revalidation. | Core gate. | Service plus worker gate. | Capability adapter. | E3 negatives; paper hard floor confirmed. |
| Secret exposure | Protected classification overrides root; raw value only exact recipient and no descendants/ordinary surfaces. | Core protected path. | Client-to-recipient protected path. | Out-of-event protected path. | Shared capture E2-004; delivery E3. |
| Isolation failure recovery | Fence authority, classify effect uncertainty, reread workspace/target before resume. | Owner epoch. | Lease/fence and service epoch. | Stream owner/fence and replay. | E3 fault evidence. |

C01 reduces setup/process topology but concentrates enforcement. C02 makes worker replacement explicit at the cost of service/IPC lifecycle and portability burden. C03 makes control/evidence replay explicit at the cost of event/reducer concepts. Those are preferences and risks; the shared hard floor is unchanged.

## 12. E1-suite testability

| Frozen suite subject | C01 seam | C02 seam | C03 seam | Comparative assessment |
|---|---|---|---|---|
| 170 evaluation cases | Core ports/store/supervisor/evidence/verifier fixtures. | Replaceable service dependencies, workers, IPC, verifier. | Command/event fixtures, reducers, adapters, projections. | All map every case family; implementation adapters do not yet exist. |
| 18 oracles | Core authority and target readback ports. | Service authority plus worker/target readback. | Journal/payload/current-head plus target readback. | C03 supports deterministic replay; C01/C02 support direct authoritative current-state inspection. |
| 11 fixture families | Integrated dependency substitution. | Service/worker substitution. | Stream/payload/adapter fixture materialization. | More substitution points are not automatically better. |
| 23 security-negative families | Broker/gateway/supervisor boundaries. | Client/service/worker boundaries. | Admission/adapters/reducer boundaries. | All expose denial/effect canaries; full proof remains E3/E5. |
| 16 repository conditions | Workspace broker support matrix. | Service broker support matrix. | Workspace command/adapter matrix. | Equal semantic coverage; topology changes instrumentation. |
| 30 Git/effect rows | Core Git/effect adapters. | Service Git/effect/worker correlation. | Git/effect command and event chain. | All can assert effect class, disposition, approval, and readback independently. |
| 9 adequacy variants | Core evidence map and verifier input. | Service-owned map and verifier worker. | Versioned map/result events and verifier adapter. | All permit hidden-ground-truth checks without author transcript. |
| 16 dangerous compositions | Central fault scheduler across core boundaries. | IPC/lease/worker fault scheduler. | Deterministic event/fault schedule and replay. | C03 makes scheduling most explicit; C02 exposes replacement races; C01 has fewer moving parts. No score. |
| 8 reliability protocols | Core timestamps/counters/ceilings. | Service/IPC/worker/gateway instrumentation. | Event timestamps/counters/ceilings. | Actual overhead/coverage remains `E3V-007`; no protocol ran. |
| `EP-CTL-016` client-only disconnect | Presentation detach with healthy core. | Thin-client disconnect with healthy service. | Client projection disconnect with healthy coordinator. | All distinguish client loss from owner loss; no-live-owner intervals remain visible. |

Failure-injection ease differs: C03's ordered event input favors replay, C02's replaceable workers favor component-loss substitution, and C01's explicit ports/fault points provide coverage with lower topology. State observability differs similarly. None receives preference credit merely for internal complexity.

## 13. Contributor burden, complexity, local-first behavior, future evolution, and reversibility

| Subject | C01 | C02 | C03 |
|---|---|---|---|
| Setup/process count | One visible integrated runtime plus declared child processes. | Visible control service, clients, execution/verifier workers, IPC/auth/lifecycle. | Visible local runtime, journal/payload state, reducers/projections/checkpoints; no mandatory daemon. |
| Conceptual model | Broad transactional core, ports, history/outbox/effect ledger. | Service authority, commands, inbox/outbox, leases/fences, replaceable workers. | Event identity/order, payload refs, reducers, projections, replay/checkpoints/evolution. |
| Debugging/failure reproduction | Fewer crossings; broad coupled state can make ownership failures less localized. | More correlation/IPC lifecycle; worker failures are localized and replaceable. | Reproducible event histories; reducer/schema/payload/checkpoint failures need specialized tools. |
| Change one subsystem | Ports must prevent broad-core coupling. | Clear service/worker boundaries can localize work, with contract-version burden. | Adapters/projections replace easily; material event/reducer changes are cross-cutting. |
| Local startup/idle | No permanent service; task-bound core may detach while active. | Persistent user-local service adds lifecycle and idle-resource burden. | Coordinator may be task-bound/absent; journal/projection tooling adds startup validation/rebuild work. |
| Offline behavior | Fully local core; provider-dependent operations fail visibly. | Fully local control service/workers; provider-dependent operations fail visibly. | Fully local journal/coordinator/adapters; provider-dependent operations fail visibly. |
| Shutdown/update/migration | Core shutdown checkpoints and reconciles; integrated store/core migrations are coupled. | Client exit is cheap; service shutdown/update/migration is a central availability event. | Shutdown records/replays explicit events; long-history/schema/reducer migration is foundational. |
| Remote/cloud evolution | Extract control/execution across the existing port; larger topology migration. | Replace local worker transport/auth while retaining service contract; service may become a remote-control ancestor. | Replace adapters/transport serialized events; distributed ordering/retention still needs design. |
| Multiple clients/agents | Versions/epochs/scoped IDs are the floor; integrated single writer must evolve. | Service versions/leases are direct seams; no multi-agent behavior now. | Stream sequencing/ownership is a direct seam; no distributed conflict model now. |
| Skills/connectors/editions | Versioned core capability contract; no loader. | Service capability adapter contract; no loader. | Versioned extension command/event contract; no loader. |
| Foundational lock-in | Integrated single-writer core, store/history/effect record semantics. | Service/store authority and client/worker lease/effect protocol. | Canonical event identity/order/meaning, payload boundary, reducer evolution. |
| More reversible decisions | Presentation, provider/capability adapters, executor implementation, observability sinks. | Client UI, worker implementation, provider/capability adapters, observability sinks. | Projections, adapters, client UI, provider/capability adapters, checkpoint implementation. |

Relative implementation complexity is qualitative: C01 has the fewest architectural concepts but the highest risk of broad-core coupling; C02 adds the most process/lifecycle/authentication coordination; C03 adds the most state-model/evolution/replay concepts. Code quantity, schedule, and actual resource use are not estimated.

## 14. Level B pattern comparison

Pattern counts are not scores. `USED`, `SUBSUMED`, and `NOT_USED` are evaluated only for their effect on frozen properties and migration.

| Family | C01 | C02 | C03 | Comparative effect |
|---|---|---|---|---|
| `LB-01` canonical roots/checkpoints/migration | Integrated store root/snapshots/migration ledger. | Service store root/snapshots/migrations. | Journal/payload roots and validated checkpoints/migrations. | All help recovery; physical authority differs. |
| `LB-02` content-addressed identity | `NOT_USED`. | `NOT_USED`. | `NOT_USED`. | Stable IDs/integrity suffice; equality/privacy/retention/deletion risk is avoided. Neutral shared non-decision. |
| `LB-03` derived projections | Client/summary views rebuild. | Thin clients/views rebuild. | Defining reducer/projection model. | C03 receives stronger structural alignment and higher projection/evolution burden, not a count advantage. |
| `LB-04` persistence alternatives | Transactional current + history/outbox. | Service transaction + history/inbox/outbox. | Append-only event authority. | Defining state-model tradeoff and foundational migration commitment. |
| `LB-05` operation journal | Separate material ledgers. | Command/dispatch/result/effect ledgers. | `SUBSUMED` in material journal. | All preserve operation recovery; representation differs. |
| `LB-06` typed failures | Integrated registry. | Cross-process failure contract. | Failure events/reducer. | All satisfy stable failure semantics; C02/C03 add version-boundary burden. |
| `LB-07` process ports | Supervisor/gateways. | Client/service/worker/verifier ports. | Command/event adapter ports. | Supports testability and isolation; extra ports add coordination. |
| `LB-08` provider router | Embedded gateway. | Service gateway. | Provider route/result events. | Provider neutrality equal; locality differs. |
| `LB-09` explicit state | Orthogonal durable records. | Service state plus worker leases. | `SUBSUMED` in typed events/reducers. | C03 integrates history/state; current-state read complexity differs. |
| `LB-10` approvals/receipts | Core ledger/receipts. | Service ledger/worker receipts. | Immutable lifecycle/receipt events. | All support hard approval/effect properties. |
| `LB-11` local/remote abstraction | Replaceable executor port. | Worker interface. | Serializable dispatch/result/fence events. | C02/C03 reduce later adapter extraction; C01 pays less present coordination. |
| `LB-12` long-running lifecycle | `SUBSUMED` in local task/control model. | Used through service/worker leases. | `SUBSUMED` in workflow/owner events. | No cloud feature is implemented; present lifecycle burden differs. |
| `LB-13` context summaries | Versioned derived summaries. | Service manifests/summaries. | Source-range summary projections. | All preserve source authority; C03 replay is explicit. |
| `LB-14` adapters/gateway | In-process gateway before ordinary adapters; protected path separate. | Service gateway; protected raw service-bypass path. | Command admission before adapters; protected out-of-event path. | Direct ungated adapters are rejected uniformly; protected topology differs. |
| `LB-15` concurrency safety | Single writer + versions/epochs. | Service versions/leases/fences. | Expected sequence/owner/fence per stream. | All meet the floor; future adaptation and current complexity differ. |
| `LB-16` telemetry/audit/evidence topology | Semantically separate in one store boundary. | Service semantics plus client projections. | Material journal distinct from telemetry/projections. | C03 has clearest physical/logical distinction; C01 fewer components; C02 central service. |
| `LB-17` corruption quarantine | Startup quarantine/migration. | Service quarantine/snapshot migration. | Sequence validation/trusted replay/quarantine. | All paper-resolve `AR-DUR-005`; empirical fault evidence remains. |
| `LB-18` evidence manifests/drift | Versioned manifests/drift checks. | Service manifests/drift checks. | Evidence projection/position/payload validation. | All support exact binding; C03 ties evidence to journal positions. |
| `LB-19` extension boundary | Core capability contract. | Service capability adapter contract. | Extension commands/events. | All reserve governed extensions; none implements a marketplace/Finance feature. |

## 15. Uncertainty closure and minimum E2-004 set

The verified source records recompute to 28: 10 analysis, 9 spike references, 3 E3, 3 E4, and 3 future. Deduplicating the six shared spike references into two shared questions reduces four records; splitting each mixed E3 bundle into technical (`E3V-001..007`) and model/configuration (`E3V-008`) adds three. That produces 27 source-derived normalized items. One new cross-candidate weight-authority item produces a final normalized register of 28:

| Classification | Count | Current disposition |
|---|---:|---|
| `PAPER_RESOLVABLE` | 10 | 10 resolved; 0 remaining. |
| `E2_PRESELECTION_SPIKE_REQUIRED` | 2 | Retained; not run; both block every candidate. |
| `E3_POSTSELECTION_TECHNICAL_VALIDATION` | 6 | Three candidate technical bundles plus three protected-delivery variants. |
| `E3_MODEL_OR_CONFIGURATION_BENCHMARK` | 3 | One `E3V-008` bundle per candidate; no model/provider assigned. |
| `DEFERRED_OUT_OF_SCOPE` | 7 | Three E4 implementation-detail bundles, three future-product bundles, and one E2-005 weight-authority item. |
| **Total** | **28** | Every item has exactly one classification, owner, decision link, rationale, and consequence. |

All 10 analysis-owned questions are resolved: `RESOLVED_FAVORABLE` 5, `RESOLVED_UNFAVORABLE` 1, and `RESOLVED_NEUTRAL` 4. These labels describe the bounded question, not candidate rank. No `ANALYSIS_RESOLVABLE` item remains.

The minimum E2-004 blocker set is:

- `E2U-S01-DESCENDANT-CONTAINMENT`, reusing and narrowing SP-C01 crash/fault and SP-C05 lifecycle/control material.
- `E2U-S02-PROTECTED-ACQUISITION`, reusing and narrowing SP-C04 exact authorization/receipt/readback and SP-C05 takeover/recovery material.

SPQ-03, SPQ-04, and SPQ-05 are removed from the preselection set and reclassified, respectively, to `E3U-C01-PROTECTED-DELIVERY`, `E3U-C02-PROTECTED-DELIVERY`, and `E3U-C03-PROTECTED-DELIVERY` under `E3V-006`. They are not run and receive no favorable credit.

The complete prospective spike contracts, budgets, stop rules, artifacts, no-go rules, and source reconciliation are in `ENGINEERING_PREVIEW_ARCHITECTURE_UNCERTAINTY_REGISTER.yaml`.

## 16. Dominance, sensitivity, and decision readiness

### 16.1 Dominance

No candidate is analytically dominated. C01 is not no-worse on all dimensions because C02 offers more direct worker replacement/remote seams and C03 offers more direct replay/projection reconstruction. C02 is not no-worse because C01 has lower local topology and C03 has more explicit causal reconstruction. C03 is not no-worse because C01/C02 have simpler current-state and contributor concepts. Each apparent advantage carries a material cost, and both shared hard blockers remain unresolved. Complexity alone is not dominance.

### 16.2 Sensitivity

| Priority emphasis | Candidate tendencies; no ranking or recommendation |
|---|---|
| Minimal local topology and short control path | C01 gains; C02 loses from service/IPC/lease lifecycle; C03 avoids a mandatory daemon but loses from event/reducer/projection concepts. |
| Maximum causal reconstruction and projection rebuild | C03 gains; C01/C02 retain complete material history but rely more on transaction/history reconciliation. |
| Replaceable workers and lower remote-execution adaptation | C02 gains most directly; C03 gains through serializable dispatch/adapters; C01 incurs core/control extraction. |
| Contributor accessibility | C01 gains from one visible runtime but loses if broad-core ownership is hard to change safely; C02 gains bounded subsystems but loses setup/debugging complexity; C03 gains deterministic replay but loses conceptual onboarding burden. |
| Lowest migration lock-in | No stable tendency: C01 locks integrated core/store semantics, C02 locks service/lease/effect protocol, and C03 locks event identity/order/meaning. The kind of migration feared determines the tradeoff. |
| Lowest evidence/storage overhead | C01/C02 may gain from transactional current-state reads; C03 may lose from journal/payload/projection retention while gaining reconstruction. Values remain unmeasured. |

### 16.3 Candidate readiness

| Candidate | Current status | Conditional status after E2-004 |
|---|---|---|
| `EP-ARCH-C01` | `NEEDS_E2_004` | `READY_FOR_E2_005_IF_SPIKES_PASS`; otherwise the exact failed property requires architecture/support-boundary revision or no-go. |
| `EP-ARCH-C02` | `NEEDS_E2_004` | `READY_FOR_E2_005_IF_SPIKES_PASS`; otherwise the exact failed property requires architecture/support-boundary revision or no-go. |
| `EP-ARCH-C03` | `NEEDS_E2_004` | `READY_FOR_E2_005_IF_SPIKES_PASS`; otherwise the exact failed property requires architecture/support-boundary revision or no-go. |

No candidate is `ANALYTICALLY_NONVIABLE` or `NEEDS_ARCHITECTURE_REVISION` on current paper evidence. That is not a selection, preference, or prediction that a spike will pass.

## 17. Downstream contracts

E2-004 receives exactly the two normalized blockers and may execute only their frozen, local, synthetic, finite contracts after E2-003 is independently verified. It must preserve every result, treat `FAIL` or `INCONCLUSIVE_BLOCKING` as blocking, and may not choose an architecture. E2-004 remains `BACKLOG` and blocked by `E2_003_NOT_INDEPENDENTLY_VERIFIED` during this author pass.

After independently verified E2-004 closure, E2-005 will need:

- this comparison and 195-cell matrix;
- all three currently surviving candidate definitions;
- the `57 confirmed / 2 blocker / 0 violation` hard map and verified E2-004 outcomes;
- unweighted preference tradeoffs and sensitivity;
- the 10 paper-question resolutions and both verifier-finding dispositions;
- recovery, security, testability, contributor, local-first, future, and migration evidence;
- the postselection E3 technical/model obligations and failure handback rules; and
- explicit decisions for proposed ADRs without treating the present comparison as a recommendation.

## 18. Author-pass boundary

This document is `READY_FOR_REVIEW`, not verified. A fresh challenger must recompute sampled/high-risk cells and inspect favorable-unknown handling, hard-failure compensation, correlated criteria, security/recovery/evidence independence, provider neutrality, future-scope proportionality, and the spike partition. Only a separate verifier may reproduce the full hard gate, matrix completeness, uncertainty partition, and no-winner result and move E2-003 to `VERIFIED`.

Architecture remains `NOT_SELECTED`; preferred candidate remains `NONE`; accepted ADRs remain 0; architecture spikes, evaluation runs, model benchmarks, paid calls, external effects, and application code remain 0/none; autonomy remains `NOT_ELIGIBLE` and autonomous build remains unauthorized.
