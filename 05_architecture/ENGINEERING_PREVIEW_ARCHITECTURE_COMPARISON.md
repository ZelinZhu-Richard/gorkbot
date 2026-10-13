# Engineering Preview Architecture Comparison

Status: **E2-003 FIXER PASS — READY_FOR_REVIEW; NOT VERIFIED**

Comparison version: `EP-ARCH-COMP-0.2`

Task: `E2-003`

Original author base commit: `b5b35a7fc5190ddbe359bd99f51fea4189ccff6a`

Fixer base commit: `dcb35439003fe2e1814b09e6e0c725e754d02dac`

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
| `ARCHITECTURE_SEAM_CONFIRMED_E3_VALIDATION_OUTSTANDING` | The architecture exposes the required interface, ownership, trust, and fail-closed boundary, but a concrete selected mechanism has not been tested. The cell is analytically viable, receives no empirical credit, and retains the named E3 handback rule. |
| `ANALYSIS_RESOLVABLE` | Paper analysis is still needed. No final cell remains in this state after this fixer pass. |
| `ARCHITECTURE_BLOCKING_SPIKE` | The hard property cannot be credited before bounded E2-004 evidence. No final E2-003 cell remains in this state. |
| `KNOWN_VIOLATION` | The candidate fails the hard gate unless a repair preserves its architecture identity. No such result was found. |
| `QUALITATIVE_TRADEOFF_NO_SCORE` | The preference is described structurally, without weight, numeric value, rank, or compensation for a hard result. |

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

The E2-002 verification commit is `1a1c5423da83d3dfe9c7f759300bf10d68e4281e`. The original author base, `b5b35a7fc5190ddbe359bd99f51fea4189ccff6a`, adds only the independent E2-002 verification/governance transition over that candidate baseline. The fixer starts from `dcb35439003fe2e1814b09e6e0c725e754d02dac`, which records the independent challenger review of author commit `c870c83a5f97c639c0c248c2e650ad31371c5164`. No candidate artifact has been changed by E2-003.

## 3. Comparison method and weighting discipline

The prospective method is:

1. Apply all 59 hard constraints as non-compensating gates.
2. Resolve the candidate-declared E2-003 paper questions using the frozen requirements and the candidate's own process, authority, persistence, recovery, security, packaging, and migration contracts.
3. Apply the plan §13 stage test to every empirical residual: retain an E2-004 spike only if its outcome can differ by candidate and can change architecture selection. Otherwise confirm the architecture seam only, assign concrete selected-mechanism validation to E3/E4, retain fail-closed behavior and an explicit E2/ADR handback trigger, and grant no empirical credit.
4. Compare the six preferences qualitatively only after the hard-gate pass. No numerical score, ordering, or winner is produced.
5. Compare all 25 domains, 20 threat boundaries, 19 Level B families, recovery/security/testability, contributor burden, implementation complexity, local-first behavior, future evolution, and reversibility using the same evidentiary bar.
6. Test strict dominance and decision sensitivity without selecting or recommending.

Final weights are not authorized or evidenced. They are not assigned. The weight owner is the later E2-005 decision-authority process, which may preserve an explicit qualitative rationale or seek founder priority input after independently verified E2-004 closure. Any prospective numeric weighting would need a reviewed pre-result amendment.

Each of the six verified preferences has exactly one primary comparison group. These are the only primary preference groups used in the matrix:

| Primary group | Exact preference |
|---|---|
| `PREF_PRIMARY_01_INTERACTIVE_CONTROL_LATENCY` | `AR-PRF-001` |
| `PREF_PRIMARY_02_OPERATIONAL_MAINTENANCE_COMPLEXITY` | `AR-PRF-002` |
| `PREF_PRIMARY_03_MIGRATION_REVERSIBILITY` | `AR-PRF-003` |
| `PREF_PRIMARY_04_REMOTE_CONCURRENCY_ADAPTATION` | `AR-PRF-004` |
| `PREF_PRIMARY_05_EVIDENCE_LARGE_OUTPUT_OVERHEAD` | `AR-PRF-005` |
| `PREF_PRIMARY_06_CONTRIBUTOR_LOCAL_PACKAGING_BURDEN` | `AR-PRF-006` |

The verified E2-001 correlation sets remain a separate, many-to-many disclosure layer. They do not create another preference, membership is not additive, and any later E2-005 weighting policy must count each primary preference at most once:

| Correlation set | Preference membership | Related non-preference subjects |
|---|---|---|
| `PREF_CORRELATION_RECOVERY_CORRECTNESS_EVIDENCE` | `AR-PRF-005` | durability, recovery, history, evidence integrity, false completion |
| `PREF_CORRELATION_SECURITY_AUTHORITY_EFFECT_ISOLATION` | none | capability, approval, secret, process, network, effect fencing; hard properties cannot become preference credit |
| `PREF_CORRELATION_MAINTAINABILITY_PACKAGING_MIGRATION` | `AR-PRF-002`, `AR-PRF-003`, `AR-PRF-006` | operational complexity, packaging, schema/topology migration, contributor burden |
| `PREF_CORRELATION_FUTURE_REMOTE_CONCURRENCY_REVERSIBILITY` | `AR-PRF-003`, `AR-PRF-004` | remote seams, multiple owners/clients, reversibility |
| `PREF_CORRELATION_PERFORMANCE_LOCAL_OVERHEAD_COST` | `AR-PRF-001`, `AR-PRF-005` | latency, local/evidence overhead, resource and cost instrumentation |

`AR-PRF-003` deliberately appears in two correlation sets but only in primary group `PREF_PRIMARY_03_MIGRATION_REVERSIBILITY`; this makes the overlap visible without double counting. No weight, score, or final ordering is assigned.

## 4. Hard-constraint comparison

### 4.1 Gate result

All three candidates survive analytical hard-gate elimination. Two hard properties have confirmed architecture seams and outstanding E3 mechanism validation; neither is a candidate-discriminating preselection spike. Repository lifecycle still requires an independently verified E2-004 no-spike closure before E2-005 may proceed.

| Candidate | Confirmed satisfied for comparison | Seam confirmed / E3 validation outstanding | Analysis remaining | E2 preselection spike | Known violation | Consequence |
|---|---:|---:|---:|---:|---:|---|
| `EP-ARCH-C01` | 57 | 2 | 0 | 0 | 0 | `ANALYTICALLY_VIABLE`; E2-005 requires independently verified E2-004 `NO_PRESELECTION_SPIKE_REQUIRED` closure. |
| `EP-ARCH-C02` | 57 | 2 | 0 | 0 | 0 | Same consequence and evidentiary bar as C01. |
| `EP-ARCH-C03` | 57 | 2 | 0 | 0 | 0 | Same consequence and evidentiary bar as C01. |

This result does not rewrite the verified E2-002 source statuses. The matrix preserves `input_generation_status` and separately records the E2-003 comparison result.

### 4.2 Five paper-resolvable hard properties

| Requirement | C01 evidence and analysis | C02 evidence and analysis | C03 evidence and analysis | Result and later evidence |
|---|---|---|---|---|
| `AR-DUR-005` corruption, partial write, evolution | `f08/f09` define transactional old-or-new current state, versioned migration, quarantine, preserved original evidence, and explicit interrupted endpoints. | `f08/f09` define transactional service records/inbox/outbox, migration and quarantine, plus itemized partial-write recovery. The missing `f27` pointer is bookkeeping, not missing design evidence. | `f08/f09` require durable payload before event acknowledgement, ordered journal validation, quarantine/trusted replay, visible migration, and orphan-payload reconciliation. The missing `f27` pointer is bookkeeping. | All three `CONFIRMED_SATISFIED_FOR_COMPARISON`; actual corruption and migration faults remain `E3V-001/005`. |
| `AR-WSP-003` confinement/adversarial paths | The integrated workspace broker normalizes and re-resolves objects at open, mutation, and cleanup and fails closed on unsupported topology. | The service broker plus worker boundary revalidates object/root identity; the service remains authority over workspace scope. | Command admission and the workspace adapter bind object/root identity; events record denial/readback rather than granting path authority. | All three confirmed at design level. Exact supported-host mechanisms and all negative cases remain `E3V-003/006`; no host primitive is claimed proven. |
| `AR-SEC-003` exact protected recipient | A separate one-use, recipient/use/fence-bound protected path excludes ordinary core/model/log/evidence routes and returns only a non-secret receipt. | The service issues a non-secret, lease/fence-bound authorization; raw bytes travel directly from protected client broker to the exact current recipient and never through service state. | The protected broker is outside the command/event/payload/projection path; only a non-secret receipt event rejoins authority. | All three confirmed structurally. Candidate-specific delivery implementation is `E3V-006`, not a preselection hard-feasibility blocker. |
| `AR-SEC-004` network boundary | Embedded gateway/network policy binds destination, data, credential, budget, redirects, and zero-dispatch denial. | Service network gate and worker policy enforce the same contract at both control and execution boundaries. | Network capability commands and adapters record the effective target and zero-dispatch/uncertain-effect outcome as material events. | All three confirmed structurally; negative and adapter evidence remains `E3V-004/006`. |
| `AR-PKG-001` local-first, contributor-operable boundary | One visible task-bound application/core plus declared child processes and local state; no hidden service or cloud. Broad-core coupling is a preference cost. | A visible local service, clients, workers, state, lifecycle, and update/recovery contract; no hidden mandatory cloud. Multi-process setup is a preference cost, not a hard failure. | A visible local runtime, journal/payload boundary, reducer/projection/checkpoint tools, and migrations; no mandatory daemon or cloud. Conceptual burden is a preference cost. | All three confirmed at the packaging hard floor; exact toolchain/setup remains `E3V-003` and later implementation. |

### 4.3 Architecture seams confirmed; mechanism evidence outstanding

| Requirement | Architecture fact established in E2 | Empirical fact not established | Stage owner and consequence |
|---|---|---|---|
| `AR-EXE-003` | Every candidate identifies the supervisor-owned process tree, cooperative-cancel and bounded force-or-fence interface, descendant/effect accounting, and candidate-specific stale-authority rejection (`owner epoch`, `service lease/fence`, or `workflow owner/fence`). Control-authority fencing is distinct from process-tree containment. | No supported host/process primitive has been tested; E2 does not claim that force termination, whole-tree observation, or post-fence deprivation works on any concrete platform/configuration. | `E2U-S01-DESCENDANT-CONTAINMENT` is `RECLASSIFIED_TO_E3` under `E3V-002`. Missing evidence keeps the affected host/workload class unsupported and fail closed. A structural inability of the selected architecture to realize the property triggers `E3_HAND_BACK_TO_E2`; a faulty adapter/configuration requires correction or an alternate conforming mechanism. |
| `AR-SEC-006` | Every candidate defines a protected acquisition boundary distinct from ordinary input, capture exclusion/suspension, exact-recipient handoff, unauthorized-surface exclusion, non-secret receipt, no replay, and fail-to-`WAITING_FOR_USER`/blocker behavior. | No selected client surface or platform mechanism exists, so E2 cannot observe real keystroke, clipboard, screen/accessibility, terminal, model, transcript, log, telemetry, artifact, or evidence behavior. | `E2U-S02-PROTECTED-ACQUISITION` is `RECLASSIFIED_TO_E3` under `E3V-006`. A mechanism/configuration failure requires correction or an alternate mechanism; product/client-class infeasibility narrows support and fails to wait; only structural impossibility for a required accepted-ADR property triggers `E3_HAND_BACK_TO_E2`. |

The plan §13 test is answered **NO** for both items: their concrete feasibility depends on a selected host/client mechanism shared across the candidate shapes, and no outcome at this stage can prefer one of C01/C02/C03. The E2-004 preselection set is therefore empty. This is architecture-level closure only, not empirical feasibility proof.

### 4.4 Required material rechecks

| Requirement | E2-003 conclusion |
|---|---|
| `AR-EXE-003` | Architecture seam confirmed and concrete mechanism moved to `E3V-002`; logical/control-authority fencing is not treated as physical descendant containment, and no host feasibility is claimed. |
| `AR-DUR-003` | All candidates preserve intent/attempt/receipt/readback/unknown across the record-to-effect crash window. The ambiguity differs in topology but is not removed by any candidate; design-level hard status remains confirmed and fault evidence remains E3. |
| `AR-DUR-004` | All candidates preserve duplicate original outcomes, resume revalidation, event correlation, and owner/agent lifecycle. No-live-owner intervals are visible availability/preference characteristics, not fictitious deadline enforcement. |
| `AR-DUR-005` | Resolved for all candidates as described above; the C02/C03 comparison layer supplies the missing `f27` rationale. |
| `AR-FUT-001` | C01's replaceable executor port, C02's worker interface, and C03's serializable dispatch contract all meet the hard compatibility floor; extraction/adaptation cost remains preference-only. |
| `AR-FUT-002` | Version/epoch, lease/fence, or stream-sequence/owner records prevent permanent global-singleton semantics without implementing future concurrency. All remain confirmed. |
| `AR-SEC-003` | Paper-resolved uniformly; SPQ-03/04/05 affected lists were overbroad for preselection classification. |
| `AR-SEC-006` | Architecture seam confirmed; shared acquisition/capture and candidate delivery are postselection `E3V-006` validations against the selected client/execution configuration, with fail-to-WAIT and handback rules. |
| `AR-TST-002` | Each candidate exposes 9 family seams, 16 composition seams, and `EP-CTL-016`; all remain confirmed without rewarding the number of internal components. |
| `AR-PKG-001` | Confirmed at the explicit/no-hidden-service hard floor; setup and contributor cost remain preference evidence. |

### 4.5 E2-002 verifier finding dispositions

`V-E2-002-01` is resolved by comparison-layer analysis. C02 and C03 already contain the required `AR-DUR-005` mechanisms in `f08/f09`; their missing `f27` pointers do not change the frozen candidates. The uncertainty register adds `AR-DUR-005` to the affected comparison-layer paper resolution for `C02-U03` and `C03-U04` and records the exact source evidence.

`V-E2-002-02` is resolved uniformly. `AR-SEC-003` is paper-resolvable and confirmed from the exact-recipient protocols. SPQ-03/04/05 are related to delivery implementation but their affected-AR linkage is overbroad for preselection: they are reclassified to candidate-scoped `E3_POSTSELECTION_TECHNICAL_VALIDATION` under `E3V-006`. Concrete `AR-SEC-006` acquisition/capture feasibility is likewise `E3V-006`; its architecture seam is confirmed, its empirical mechanism is not, and no raw protected value is evidence.

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
| `D08` execution/process | Integrated supervisor and child executors. | Leased/fenced worker supervisor. | Executor adapter plus workflow fence. | C02 replaces workers most directly; C01 has fewer control crossings; C03 records control causality. None proves descendant containment from logical fencing. | U: concrete descendant/process-class behavior is E3V-002. H: containment and fencing seams confirmed; validation outstanding. P: contributor/latency. M: executor seams vary. |
| `D09` isolation | Shared Tier 2 semantic boundary owned by core brokers/supervisor. | Shared Tier 2 floor across service and workers. | Shared Tier 2 floor across command/adapters/executor. | More processes do not prove stronger isolation; fewer processes do not prove weaker isolation. Boundary locality and enforcement burden differ. | U: exact supported-host containment/isolation mechanism is E3V-002/003. H: structural floor confirmed, empirical scope not proven. P: portability/burden. M: technology unselected. |
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
| `D20` security | Core policy plus brokers/gateways. | Client/service/worker enforcement with service as high-authority boundary. | Command policy plus adapters and event admission. | C01 has a broader trusted core; C02 has more authenticated crossings and a service blast radius; C03 depends heavily on correct admission/reducers while keeping raw secrets out of events. | U: protected capture and containment mechanisms are E3V-006/E3V-002; full negatives remain E3. H: required seams confirmed with scoped validation outstanding. P: enforcement burden. M: trust boundaries foundational. |
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

The outcome vocabulary is frozen across all candidates: `KNOWN_SUCCESS`, `KNOWN_FAILURE`, and `UNKNOWN_OUTCOME`. A transaction, replaceable worker, or journal may improve local reconstruction but never proves an external effect or filesystem outcome without receipt/readback.

Each cell states **truth; action; ambiguity; evidence/readback; burden** in that order.

| Frozen recovery scenario | C01 | C02 | C03 |
|---|---|---|---|
| Stale workspace | **Truth:** core store plus bound workspace/revision inventory. **Action:** reacquire and reread before mutation/resume. **Ambiguity:** changed material becomes blocked/partial, never silently rebased. **Evidence:** actual bytes, identity, dirty/base/ref readback. **Burden:** broad core performs the reconciliation. | **Truth:** service store plus workspace lease/inventory. **Action:** service withholds replacement-worker authority until reread/rebind. **Ambiguity:** stale lease/workspace is rejected. **Evidence:** service record plus current filesystem/Git readback. **Burden:** service-worker correlation. | **Truth:** journal identity plus workspace-adapter observations. **Action:** append observed divergence and require a new admissible command/base. **Ambiguity:** projections cannot cure stale bytes. **Evidence:** event correlation plus actual filesystem/Git readback. **Burden:** event/adapter reconciliation. |
| Duplicate task/input delivery | **Truth:** accepted-command identity and first core result. **Action:** return the recorded first result. **Ambiguity:** a missing acknowledgement does not authorize a new task. **Evidence:** acceptance sequence/result readback. **Burden:** integrated dedupe index. | **Truth:** service inbox/command identity and first result. **Action:** dedupe before dispatch. **Ambiguity:** duplicate client/service delivery cannot create a worker claim. **Evidence:** inbox and dispatch ledger. **Burden:** cross-boundary idempotency. | **Truth:** accepted command/event identity and stream position. **Action:** reject/return the original outcome. **Ambiguity:** replay is not a second acceptance. **Evidence:** journal position and reducer result. **Burden:** stable event identity/evolution. |
| Duplicate operation | **Truth:** core operation intent/attempt record. **Action:** reuse identity and reconcile the existing attempt. **Ambiguity:** concurrent/late attempt stays explicit. **Evidence:** ledger plus target/workspace readback. **Burden:** coupled operation state. | **Truth:** service command/dispatch/result ledger. **Action:** dedupe across client, service, and worker. **Ambiguity:** stale worker response is fenced. **Evidence:** operation ID, lease/fence, and readback. **Burden:** more correlation IDs. | **Truth:** intent/dispatch/observation event chain. **Action:** reduce duplicates to the recorded operation. **Ambiguity:** event absence is not effect absence. **Evidence:** causal positions plus target readback. **Burden:** reducer/schema discipline. |
| Duplicate external effect | **Truth:** core effect ledger and target receipt/readback. **Action:** never blind retry; reuse idempotency identity when supported. **Ambiguity:** unresolved becomes `UNKNOWN_OUTCOME`. **Evidence:** external target readback. **Burden:** centralized effect reconciliation. | **Truth:** service outbox/effect ledger independent of worker life. **Action:** fence stale worker, reconcile target, then decide. **Ambiguity:** replacement does not imply failure of the old effect. **Evidence:** service ledger, receipt, target state. **Burden:** service/effect/worker fencing. | **Truth:** effect intent/attempt/receipt/readback events. **Action:** replay history, then reread target. **Ambiguity:** journal cannot authenticate the external world. **Evidence:** target receipt/readback linked to events. **Burden:** causal history plus adapter correctness. |
| Stale approval | **Truth:** versioned core approval receipt bound to action/scope/revision. **Action:** reject and reacquire. **Ambiguity:** no widened or resumed use. **Evidence:** policy/action hash and current approval readback. **Burden:** core binding checks. | **Truth:** service approval ledger bound to worker lease/fence. **Action:** reject at service and worker boundary. **Ambiguity:** replacement revokes stale use. **Evidence:** ledger plus current policy/lease. **Burden:** duplicated enforcement consistency. | **Truth:** approval lifecycle events and current reducer state. **Action:** admission rejects stale event/scope and requires new approval. **Ambiguity:** historical approval is evidence, not authority. **Evidence:** stream position/current policy readback. **Burden:** reducer/admission correctness. |
| Stale verification | **Truth:** core revision/evidence/verifier-run binding. **Action:** invalidate on mutation or evidence drift. **Ambiguity:** prior PASS remains history only. **Evidence:** exact revision and predicate/evidence reread. **Burden:** core must keep history/current truth aligned. | **Truth:** service-owned revision plus verifier-worker lease/run. **Action:** reject stale verifier result and rerun only under current inputs. **Ambiguity:** worker replacement grants no PASS. **Evidence:** service revision, run identity, underlying state. **Burden:** cross-process binding. | **Truth:** journal position, payload refs, reducer version, verifier run. **Action:** invalidate if head/input changes. **Ambiguity:** rebuilt projection alone is not verification. **Evidence:** exact event/payload positions and reread. **Burden:** versioned replay chain. |
| Client-only interruption | **Truth:** task-bound core and durable state, not presentation. **Action:** continue or wait under existing authority; reconnect with fresh projection. **Ambiguity:** client close is not full shutdown. **Evidence:** owner/core identity and durable state. **Burden:** integrated runtime must distinguish presentation detach. | **Truth:** healthy service authority. **Action:** continue independently and resnapshot client on return. **Ambiguity:** stale client has no lease/control authority. **Evidence:** service epoch and current projection. **Burden:** client/service protocol. | **Truth:** journal/current owner, not client projection. **Action:** continue if coordinator active or reconstruct on next owner. **Ambiguity:** projection disconnect is not owner loss. **Evidence:** journal/head/owner readback. **Burden:** resubscribe/rebuild semantics. |
| Full-system shutdown | **Truth:** durable core records and unresolved-operation/effect state. **Action:** authenticated quiesce/cancel/force-or-fence, persist, then recover on restart. **Ambiguity:** absent core enforces no live deadline. **Evidence:** shutdown/control timeline, descendants/effects, restart readback. **Burden:** broad coordinated shutdown. | **Truth:** service store, epochs, leases, ledgers. **Action:** stop claims, fence workers, reconcile, persist. **Ambiguity:** no live service means no real-time enforcement. **Evidence:** service/worker inventory and restart reconciliation. **Burden:** multi-process quiescence. | **Truth:** journal/payloads plus current owner/fence. **Action:** append shutdown/control facts, fence adapter, checkpoint only as validated. **Ambiguity:** absent coordinator enforces no deadline. **Evidence:** event/control/descendant/effect readback. **Burden:** event plus host reconciliation. |
| Partial filesystem write | **Truth:** store intent plus actual workspace bytes. **Action:** quarantine/inspect; classify partial/blocked/unverified; never claim transaction covers filesystem. **Ambiguity:** exact write boundary may be unknown. **Evidence:** byte/inode/path/Git inventory. **Burden:** centralized scan. | **Truth:** service intent/operation record plus actual bytes. **Action:** withhold replacement work until itemized recovery. **Ambiguity:** worker death does not roll back files. **Evidence:** workspace inventory and service ledger. **Burden:** service-worker-file correlation. | **Truth:** event intent plus actual workspace bytes; journal is not filesystem atomicity. **Action:** append observations/quarantine/reconcile orphan state. **Ambiguity:** event presence does not imply complete bytes. **Evidence:** adapter readback and event linkage. **Burden:** two-authority observation discipline. |
| Lost acknowledgement | **Truth:** accepted intent/attempt and any receipt. **Action:** reread first outcome/target; no blind replay. **Ambiguity:** unresolved is `UNKNOWN_OUTCOME`. **Evidence:** core ledger and target. **Burden:** centralized reconciliation. | **Truth:** inbox/outbox/effect ledger. **Action:** service reconciles after worker/client loss. **Ambiguity:** missing response is not failure. **Evidence:** ledger, lease/fence, target readback. **Burden:** more message boundaries. | **Truth:** material intent/attempt/receipt chain. **Action:** replay and reread target/payload. **Ambiguity:** missing receipt event is not proof of no effect. **Evidence:** journal plus external readback. **Burden:** history and adapter reconciliation. |
| Coordinator/worker/core loss | **Truth:** core store/history and owner epoch. **Action:** fence children/results, restart core, reconcile every in-flight operation/effect. **Ambiguity:** owner death does not prove descendant death. **Evidence:** owner/process tree/fence/effect/readback. **Burden:** largest failure blast radius. | **Truth:** service store and epoch; worker lease/fence. **Action:** replace worker when safe; service loss requires new epoch and global reconciliation. **Ambiguity:** worker replaceability does not prove process containment or effect failure. **Evidence:** service/worker/process/effect records and readback. **Burden:** service availability plus fencing. | **Truth:** journal/payload/head and workflow owner/fence. **Action:** replay under a new coordinator/adapter lease and reconcile. **Ambiguity:** replay cannot prove descendant/effect termination. **Evidence:** journal, owner/fence, process/effect readback. **Burden:** replay/reducer/schema plus host state. |

C01's transactional label is limited to its committed core records, C02's replaceable label is limited to replaceable workers under service authority, and C03's journal label is limited to recorded material history. None removes external ambiguity. C03 improves causal reconstruction but carries gap/reducer/evolution risk; C01 reduces crossings but centralizes responsibility; C02 localizes worker loss but adds service/lease/fence coordination. These are tradeoffs, not a recovery winner.

## 9. Security and threat-boundary comparison

All 20 boundaries retain the same fail-closed semantic floor. The table compares enforcement locality and burden; it does not infer security from process count.

| Boundary | C01 enforcement | C02 enforcement | C03 enforcement | Comparative implication |
|---|---|---|---|---|
| `TB-01` user/authority | Core admission/policy kernel. | Client authenticator plus service admission. | Command policy/append admission. | C01 has one high-authority locus; C02 authenticates a crossing; C03 makes accepted/rejected authority material history. |
| `TB-02` repository | Core admission/workspace broker. | Service workspace broker. | Admission command/workspace adapter. | Same hard floor; C02 centralizes worker policy, C03 adds event evidence, C01 shortens path. |
| `TB-03` instructions | Core instruction interpreter/policy. | Service instruction-policy evaluator. | Instruction-policy command validator. | All keep content unable to widen authority; different persistence/locality only. |
| `TB-04` filesystem | Core workspace/filesystem broker. | Service plus worker broker enforcement. | Workspace adapter with event-correlated decisions. | C02 must keep two enforcement points consistent; C03 must keep adapter result/event truth aligned; C01 has a broader broker blast radius. |
| `TB-05` protected secret | Protected-entry controller and exact recipient inside separate path. | Client broker, non-secret service authorization, lease/fence-bound recipient; raw bypasses service. | Protected broker/recipient outside journal/payload/projection. | Acquisition and delivery mechanisms remain `E3V-006`; C02 has more authenticated crossings, C03 excludes raw values from its event path, and C01 carries co-residency separation burden. These are distinct costs, not a security order. |
| `TB-06` paths/topology | Core broker at open/mutate/cleanup. | Service and worker broker path. | Adapter at every access/cleanup. | All fail closed and re-resolve; negative implementation evidence remains E3. |
| `TB-07` subprocess | Integrated supervisor. | Worker supervisor plus service fence. | Executor supervisor plus workflow fence. | No logical fence is credited as descendant containment; host mechanism validation remains `E3V-002` with fail-closed unsupported scope. |
| `TB-08` terminal/protected I/O | I/O multiplexer plus protected controller. | Worker I/O plus client broker. | I/O adapter plus protected broker. | Output and protected input remain separate; selected-client capture exclusion remains `E3V-006`. |
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
| `TB-20` human protected entry | Dedicated controller outside ordinary input pipeline. | Client broker to exact current worker; service sees only authorization/receipt. | Broker outside normal command/event path. | Acquisition and candidate delivery remain E3V-006 validations. Missing evidence fails to `WAITING_FOR_USER`/blocker; raw values never become comparison evidence. |

Trusted-computing-boundary tradeoff: C01 has fewer authenticated crossings but a broad high-authority core. C02 narrows disposable worker authority but makes the service a high-value availability/security boundary and adds IPC/lease authentication. C03 makes material history and policy admission explicit, but correctness of schemas, reducers, append validation, and adapters becomes part of the trusted design. None is declared more secure overall.

## 10. Protected entry

`AR-SEC-006`, `AR-SEC-003`, and `UF-11` define two architecture properties and four postselection mechanism questions:

1. **Protected acquisition/capture.** The architecture must provide a path distinct from ordinary conversation/tool input, suspend or exclude ordinary capture, deliver no raw value into an unauthorized surface, produce only a non-secret receipt, avoid replay, and fail to `WAITING_FOR_USER` or a blocker if safety is unavailable. All candidates expose this boundary. Concrete feasibility depends on the selected client/platform and is `E2U-S02-PROTECTED-ACQUISITION` under `E3V-006`.
2. **Exact-recipient delivery.** C01 uses a co-resident but separately gated one-use path; C02 uses a non-secret service authorization and direct client-to-current-worker handoff; C03 keeps raw delivery outside journal/payload/projection. `SPQ-E2-002-03/04/05` retain historical provenance and map respectively to the three `E3U-*-PROTECTED-DELIVERY` records under `E3V-006`.

E3V-006 must validate the selected client/execution configuration across acquisition, capture exclusion, exact-recipient delivery, replacement/recovery, no replay, unauthorized-surface exclusion, and fail-to-WAIT. A failed mechanism or misconfiguration requires correction or a different conforming mechanism. If the declared client class has no safe mechanism, the product narrows that support class and fails closed. Only evidence that the accepted architecture itself cannot expose the required boundary triggers `E3_HAND_BACK_TO_E2` and reopens `ADR-E2-001` and/or `ADR-E2-005`. No real secret or client technology is selected or tested here.

## 11. Isolation

All candidates assume the same technology-neutral `TIER_2_OS_ENFORCED_EXECUTION_ISOLATION` semantic floor for untrusted execution. E2-003 does not choose a container, VM, worktree, operating-system API, process mechanism, or supported-host product matrix.

| Property | Shared floor | C01 locality | C02 locality | C03 locality | Remaining evidence |
|---|---|---|---|---|---|
| Filesystem | Object/path scope, ownership, link/topology checks, fail closed. | Core broker. | Service plus worker broker. | Workspace adapter/command events. | E3 negative mechanisms; paper hard floor confirmed. |
| Process tree | Account for descendants; bounded cancel/force/fence; no orphan effect authority. | Integrated supervisor. | Worker supervisor plus service fence. | Executor supervisor plus workflow fence. | Architecture seam confirmed; concrete representative process-tree/descendant mechanism remains `E3V-002`. |
| Network | Exact destination/data/credential/budget and effective-target revalidation. | Core gate. | Service plus worker gate. | Capability adapter. | E3 negatives; paper hard floor confirmed. |
| Secret exposure | Protected classification overrides root; raw value only exact recipient and no descendants/ordinary surfaces. | Core protected path. | Client-to-recipient protected path. | Out-of-event protected path. | Acquisition, capture exclusion, and delivery remain `E3V-006`; fail-to-WAIT until demonstrated. |
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

## 15. Consequence model

These terms are exclusive enough to prevent result-time substitution among “eliminate,” “block,” and “no-go”:

| Term | Exact meaning |
|---|---|
| `CANDIDATE_NONVIABLE` | Current evidence proves a candidate-specific structural contradiction with a hard AR. That candidate leaves the survivor set; another candidate is never selected by default. No current candidate has this status. |
| `E2_005_BLOCKED` | The repository lifecycle or a verified selection-blocking uncertainty prevents E2-005 from starting. Currently E2-005 is blocked only because E2-003 and the required E2-004 no-spike closure are not independently verified. |
| `ARCHITECTURE_REVISION_REQUIRED` | A proposed baseline must be changed before it can remain coherent; it does not by itself say whether one candidate or every candidate is nonviable. |
| `E3_HAND_BACK_TO_E2` | Later E3 evidence structurally disproves a property or assumption required by a proposed/accepted linked ADR. The affected E3 work stops and the evidence returns to E2-005/E2-006 and the E2 gate; E3 may not redesign silently. |
| `IMPLEMENTATION_CONFIGURATION_FAILURE` | A selected adapter, mechanism, fixture, wiring, or supported configuration fails while an alternate conforming realization remains architecturally possible. Correct/replace and revalidate in E3/E4; do not reopen an ADR automatically. |
| `PRODUCT_CLASS_UNSUPPORTED` | No demonstrated safe mechanism exists for a host/client/workload class. The product narrows that class and fails closed; this becomes `E3_HAND_BACK_TO_E2` only if the accepted ADR requires the class/property and no conforming alternative remains. |
| `EVIDENCE_MISSING_FAIL_CLOSED` | Missing, invalid, incomplete, or inconclusive evidence grants no success credit and cannot broaden tested scope. Execution remains waiting, blocked, unsupported, or eligibility-unassigned according to the property. |

Outcome rule: successful paper analysis establishes only the recorded architecture fact; successful E3 evidence validates only the exact tested mechanism/configuration/scope; failure is root-caused into one of the terms above; inconclusive or missing evidence is always `EVIDENCE_MISSING_FAIL_CLOSED`. A preference never compensates for any hard outcome.

## 16. Uncertainty closure and true minimum E2-004 set

The normalized source arithmetic remains 28 items. Reclassification changes the partition, not the historical provenance:

| Classification | Count | Current disposition |
|---|---:|---|
| `PAPER_RESOLVABLE` | 10 | 10 resolved; 0 remaining. |
| `E2_PRESELECTION_SPIKE_REQUIRED` | 0 | Empty after applying the plan §13 candidate-discrimination test. |
| `E3_POSTSELECTION_TECHNICAL_VALIDATION` | 8 | S01, S02, three candidate protected-delivery records, and three candidate technical bundles. |
| `E3_MODEL_OR_CONFIGURATION_BENCHMARK` | 3 | One `E3V-008` bundle per candidate; no model/provider assigned. |
| `DEFERRED_OUT_OF_SCOPE` | 7 | Three E4 bundles, three future-product bundles, and one E2-005 preference-authority item. |
| **Total** | **28** | Every item has one class, owner, decision link, consequence profile, and fail-closed rule. |

The symmetric analytic-resolution vocabulary separates fact from valence:

| Resolution | Count | Meaning |
|---|---:|---|
| `RESOLVED_TRADEOFF` | 5 | Candidate-specific consequence/cost is characterized without positive/negative winner valence. |
| `RESOLVED_SUPPORTS_PROPERTY` | 2 | Repository design evidence establishes the bounded structural property. |
| `RESOLVED_ARCHITECTURE_SEAM_PRESENT_E3_VALIDATION_REQUIRED` | 3 | The structural floor is present, while host/toolchain/client mechanism feasibility remains explicitly E3-owned. |

No positive/negative candidate-valence resolution or candidate valence count remains. C01's extraction cost is preserved as tradeoff prose under the same vocabulary used for C02 service/protocol lock-in and C03 event/history lock-in.

Historical spike-question dispositions are prospective, not deletions:

| Source question | Original question | Why it does not block E2 | Existing seam | E3 owner/evidence | Success / failure / handback / fail-closed |
|---|---|---|---|---|---|
| `SPQ-E2-002-01` | Can descendants terminate or lose productive/effect authority after cancel, owner loss, or fence? | Host primitive is candidate-invariant; every candidate exposes supervisor plus control-authority fence. | C01 epoch, C02 lease/fence, C03 workflow owner/fence, each separate from process-tree containment. | `E3V-002`; exact tested host/process class, tree, timelines, fence, effects, stale results, recovery/readback, limitations. | Success validates only tested scope. Mechanism failure is correction/alternate mechanism; unsupported class fails closed; structural impossibility for the linked ADR triggers handback. |
| `SPQ-E2-002-02` | Can protected acquisition exclude ordinary capture and fail closed? | No selected client surface exists; the answer cannot distinguish candidate architecture. | Distinct protected path, capture exclusion interface, exact recipient, receipt, no replay, fail-to-WAIT in all candidates. | `E3V-006`; selected client/execution configuration and complete independent capture/unauthorized-surface evidence. | Same root-cause split; unavailable safety means `WAITING_FOR_USER`/blocker, never improvised entry. |
| `SPQ-E2-002-03` | Can C01 deliver once to its co-resident exact recipient without ordinary capture? | The one-use recipient/use/fence interface is explicit; mechanism behavior is postselection. | C01 protected-delivery path outside ordinary core/model/log/evidence capture. | `E3V-006`; exact delivery, crash/revocation/recovery, forbidden-surface scans, receipt and non-replay. | Success validates C01 configuration only; mechanism failure stays correction; structural inability reopens `ADR-E2-005`; until then fail closed. |
| `SPQ-E2-002-04` | Can C02's authorization and client-to-current-worker handoff preserve exact recipient/use/lease/fence? | Service-bypass raw path and lease/fence interface are explicit. | Non-secret service authorization; raw direct path; replacement revokes and reacquires. | `E3V-006`; authorization/delivery/replacement/crash/receipt evidence. | Same consequence split and fail-closed behavior. |
| `SPQ-E2-002-05` | Can C03 keep raw delivery outside events/payloads/projections and preserve truthful receipt/recovery? | Out-of-event broker and non-secret receipt interface are explicit. | Raw path excluded from journal/payload/projection; causal receipt/recovery records. | `E3V-006`; broker/recipient/crash ordering, zero raw replay, receipt and forbidden-surface evidence. | Same consequence split and fail-closed behavior. |

### 16.1 E2-004 no-spike closure contract

The minimal E2-004 preselection set is **zero**. E2-004 remains a real independent governance step and may publish `NO_PRESELECTION_SPIKE_REQUIRED` only if it verifies all nine conditions:

1. every E2-003 `PAPER_RESOLVABLE` item is resolved;
2. no empirical uncertainty remains whose outcome can differ by candidate and change selection;
3. every residual is legitimately assigned to E3/E4 rather than hidden;
4. every deferred hard property has a structural architecture seam in each analytically viable candidate;
5. every E3 deferral has exact evidence and tested-scope requirements;
6. every E3 deferral has explicit fail-closed product behavior;
7. every E3 deferral has a linked E2/ADR handback trigger;
8. no candidate receives favorable credit from missing empirical evidence; and
9. no spike was omitted merely to save effort.

E2-004 must independently reconcile the empty set to the verified register, preserve `technical_spikes_run=0`, and record any failure as `E2_005_BLOCKED`. This E2-003 fixer does not execute or bypass E2-004.

## 17. Dominance, sensitivity, and decision readiness

### 17.1 Strict pairwise dominance regression

Dominance requires the putative dominator to be no worse on every material dimension and strictly better on at least one, with no hidden or favorable empirical unknown. All six directions fail:

| Direction tested | Dominated? | Material counterexample preventing dominance |
|---|---|---|
| `C01 -> C02` | No | C01 has less-direct worker replacement, remote dispatch, and localized worker-failure isolation than C02. |
| `C01 -> C03` | No | C01 has less-direct causal replay, deterministic projection rebuild, and event-position provenance than C03. |
| `C02 -> C01` | No | C02 carries an additional local service/IPC/lease lifecycle and a longer contributor setup/control path. |
| `C02 -> C03` | No | C02 has less-direct deterministic replay, source-position history alignment, and projection reconstruction than C03. |
| `C03 -> C01` | No | C03 carries more event/reducer/projection concepts and less-direct current-state reads than C01. |
| `C03 -> C02` | No | C03 has less-direct replaceable-worker/service routing and a greater event-model onboarding burden than C02. |

Thus no candidate is strictly dominated. Simpler topology, a stronger remote seam, or stronger recovery reconstruction alone cannot establish dominance.

### 17.2 Bounded sensitivity profiles

These are conditional profiles, not weights, scores, a ranking, or a preferred-candidate recommendation:

| Profile | Characteristics emphasized | Comparative advantage on this profile | Additional burden | Remaining uncertainty | Why this is not overall selection |
|---|---|---|---|---|---|
| A. Minimal local topology | Few mandatory processes, short authority path, simple current-state access. | C01 gains from one integrated local core; C03 avoids a mandatory service process. | C02 adds service/IPC/lease lifecycle; C03 adds journal/reducer/projection concepts. | Operational cost remains unmeasured until E3/E4. | It ignores recovery reconstruction, remote evolution, security boundaries, and migration. |
| B. Recovery rigor | Causal reconstruction, replayable state, explicit ambiguity, projection rebuild. | C03 gains from defining journal positions and reducers. | C03 pays event/payload/projection evolution and retention burden; C01/C02 must reconcile transaction/history/outbox records. | External-effect ambiguity remains for all three and requires E3 validation. | It does not establish topology, contributor, latency, or migration value. |
| C. Future remote evolution | Replaceable execution, serializable dispatch, lease/fence ownership, adapter extraction. | C02 gains most directly; C03 also gains through command/event adapters. | C02 pays present service coordination; C03 pays protocol/event evolution; C01 later extracts core/control seams. | Future concurrency and remote operating evidence remain deferred. | Future optionality cannot override the v0.1 local-first hard floor or present cost. |
| D. Contributor accessibility | Setup simplicity, bounded ownership, debuggability, reproducible fixtures. | C01 gains a visible single runtime; C02 gains bounded subsystems; C03 gains deterministic replay fixtures. | C01 broad-core changes can couple concerns; C02 adds multi-process setup; C03 adds conceptual onboarding. | `E3V-003` must validate actual setup/recovery on supported platforms. | Different contributor tasks favor different structures; no single advantage spans all dimensions. |
| E. Migration reversibility | Stable ports, exportability, bounded lock-in, rollback and schema/event evolution. | No stable candidate-wide advantage: C01 has fewer present boundaries to migrate, C02 has explicit service/worker contracts, and C03 has replayable history. | C01 locks integrated core/store meaning, C02 locks service/lease/effect protocol, C03 locks event identity/order/semantics. | Concrete migration fixtures and direction are not yet selected. | The feared migration direction determines the tradeoff; no weight is authorized. |
| F. Security-boundary clarity | Single authority, explicit protected path, process/effect fences, unauthorized-surface exclusion. | No stable candidate-wide advantage: C01 centralizes authority, C02 physicalizes service/worker boundaries, C03 makes command/event admission explicit. | C01 must keep semantic boundaries clear in-process; C02 expands IPC/worker attack surface; C03 must exclude raw protected values from journal/payload/projections. | `E3V-002`, `E3V-004`, `E3V-005`, and `E3V-006` remain bounded empirical obligations. | Boundary clarity is distinct from tested mechanism safety and does not settle topology or recovery. |
| G. Testability/debuggability | Deterministic fixtures, fault injection, inspectable authority transitions, adapter substitution. | C03 gains replay fixtures; C02 gains component substitution and worker fault isolation; C01 gains short in-process traces. | C03 must debug reducer/event evolution; C02 cross-process timing; C01 coupled-core interactions. | Fault-injection and observability evidence remain E3/E4 work. | Each candidate helps a different test class, so the profile has no overall winner. |

### 17.3 Candidate readiness

| Candidate | Current status | Required lifecycle condition |
|---|---|---|
| `EP-ARCH-C01` | `ANALYTICALLY_VIABLE` | `READY_FOR_E2_005_AFTER_INDEPENDENTLY_VERIFIED_E2_004_NO_SPIKE_CLOSURE` |
| `EP-ARCH-C02` | `ANALYTICALLY_VIABLE` | `READY_FOR_E2_005_AFTER_INDEPENDENTLY_VERIFIED_E2_004_NO_SPIKE_CLOSURE` |
| `EP-ARCH-C03` | `ANALYTICALLY_VIABLE` | `READY_FOR_E2_005_AFTER_INDEPENDENTLY_VERIFIED_E2_004_NO_SPIKE_CLOSURE` |

No candidate has a hidden hard violation, `CANDIDATE_NONVIABLE` status, preference score, or selection credit. The two hard properties marked with outstanding E3 validation are not represented as empirically proven.

## 18. Downstream contracts

### 18.1 Crisp E2/E3 boundary

E2 decides system structure, authority ownership, interfaces, trust boundaries, the required containment and protected-entry seams, and the recovery/evidence/verification architecture. E3 validates concrete mechanism feasibility, selected platform/client behavior, model/provider/configuration eligibility, and the bounded empirical obligations attached to the proposed baseline. E3 failure hands architecture back to E2 only when evidence disproves an assumption or hard property required by a linked proposed/accepted ADR and no conforming implementation remains; E3 may not silently redesign E2.

### 18.2 `E3V-002` containment/fencing handoff

| Contract element | Requirement |
|---|---|
| Exact property | After stop, cancellation, owner loss, lease/epoch/fence change, or recovery, stale execution cannot retain productive control or authorize effects; descendants are terminated where the supported host mechanism promises termination and are always fenced from authority. |
| Required representative validation | On each claimed supported host/platform/configuration, exercise the selected supervisor mechanism with a parent and representative descendants, including ordinary exit, cancellation, forced stop, owner loss, stale result, and restart/recovery. |
| Process-tree/descendant behavior | Record descendant identity and tree membership, signals/termination attempts, bounded observation timing, survivor detection, and orphan behavior. Process-tree containment is distinct from control-authority fencing. |
| Stale execution fencing | Prove old epoch/lease/workflow-owner tokens cannot publish authoritative results, obtain approval, or perform/reconcile external effects after a fence change. |
| Force termination availability | State the exact primitive, permissions, limitations, and host/process classes for which force termination is available. Absence must never be papered over by a control fence. |
| Failure/recovery | Failed or unavailable force termination narrows the supported class and keeps the task blocked while authority is fenced; recovery must rediscover survivors and preserve `KNOWN_SUCCESS` / `KNOWN_FAILURE` / `UNKNOWN_OUTCOME`. |
| Evidence/readback | Preserve commands/configuration, host/tool versions, process-tree observations, monotonic timestamps, fence/authority records, result/effect rejection, recovery readback, and limitations. No benchmark is authorized here. |
| Scope | Success applies only to tested host/platform/process/configuration classes. Explicitly list unsupported or untested classes; never broaden by analogy. |
| Root-cause consequence | Broken wiring/one mechanism is `IMPLEMENTATION_CONFIGURATION_FAILURE`; no safe mechanism for a class is `PRODUCT_CLASS_UNSUPPORTED`; structural impossibility for a required linked ADR is `E3_HAND_BACK_TO_E2`; missing evidence is `EVIDENCE_MISSING_FAIL_CLOSED`. |

### 18.3 `E3V-006` protected-acquisition/delivery handoff

| Contract element | Requirement |
|---|---|
| Protected acquisition | On the selected client/execution configuration, acquire a synthetic sentinel only through the protected boundary; never use a real secret. |
| Capture exclusion | Demonstrate ordinary transcript, model context, telemetry, logs, evidence, clipboard/history where in scope, event journal/payload/projections, and unauthorized client surfaces exclude the raw sentinel. |
| Exact-recipient delivery | Bind one acquisition to the exact task, operation, recipient, purpose, lease/epoch/fence, and expiry; deliver once through the candidate seam. |
| Replacement/recovery | Exercise crash, cancellation, recipient replacement, owner/fence change, expiry, and recovery. A replacement must revoke and reacquire rather than inherit raw material. |
| No replay | Prove no raw value is persisted or replayed; retain only non-secret authorization/receipt/recovery facts sufficient for truthful state. |
| Unauthorized-surface exclusion | Inspect all independently named forbidden surfaces, not only application logs, and record the scan/readback method and scope. |
| Fail-to-WAIT | Any unavailable exclusion, delivery, receipt, or recovery guarantee leaves the task `WAITING_FOR_USER`/blocked and never diverts to ordinary input. |
| Root-cause consequence | A bad adapter/configuration or particular mechanism is `IMPLEMENTATION_CONFIGURATION_FAILURE` if an alternate conforming realization remains; a client/platform class with no safe mechanism is `PRODUCT_CLASS_UNSUPPORTED`; structural inability of the linked architecture/`ADR-E2-005` is `E3_HAND_BACK_TO_E2`; missing evidence is `EVIDENCE_MISSING_FAIL_CLOSED`. |
| Scope | Validate only the selected client/execution configuration and list unsupported/untested surfaces. Failure of one mechanism does not by itself invalidate the architecture, and success does not generalize beyond tested scope. |

`SPQ-E2-002-03`, `SPQ-E2-002-04`, and `SPQ-E2-002-05` retain their historical provenance and are prospectively owned by this contract.

### 18.4 Future `ADR-E2-001..009` comparison-evidence input map

This table is an input map only. It creates no ADR, accepts none, and names no preferred candidate. Every row can be proposed in E2-005 only after independent E2-004 closure.

| Future ADR boundary | Relevant comparison evidence and candidate difference | Remaining evidence / attached E3 obligation | Reversibility and migration implication | E2-005 proposal / later handback |
|---|---|---|---|---|
| `ADR-E2-001` system/client/core boundary | Sections 6, 9, 12, 13, 14 (`LB-07`, `LB-14`): C01 integrated core, C02 local service/workers, C03 command/event adapters. | `E3V-003`, `E3V-004`; packaging, client compatibility, port contract evidence. | C01 later extracts boundaries; C02 migrates service protocols; C03 migrates command/event adapters. | May propose after closure; hand back if supported client/platform cannot realize required authority boundary. |
| `ADR-E2-002` canonical state/persistence/history/projections/migration | Sections 7, 8, 14 (`LB-01`, `LB-03`, `LB-04`, `LB-17`): transactional integrated store, service store, or journal/reducers. | `E3V-001`, `E3V-007`; corruption, partial-write, replay/checkpoint, migration and evidence-binding fixtures. | Store schema/history coupling vs service schema vs event identity/order/semantic lock-in; require export/rollback path. | May propose after closure; hand back on structural inability to preserve truth/recovery/migration contract. |
| `ADR-E2-003` orchestration/ownership/recovery/idempotency/future concurrency | Sections 6-8, 11, 12 (`LB-05`, `LB-09`, `LB-12`, `LB-15`): core epochs, service leases/workers, journal owner/fence. | `E3V-001`, `E3V-002`, `E3V-005`; duplicate/lost-ack/stale-owner/effect fixtures. | Ownership and idempotency tokens become durable migration contracts. | May propose after closure; hand back if fencing/recovery semantics are structurally unrealizable. |
| `ADR-E2-004` workspace/filesystem/process execution/isolation/Git/local-remote seam | Sections 6, 8, 11, 12 (`LB-07`, `LB-11`, `LB-17`): supervisor port, worker interface, or command/event execution adapter. | `E3V-001`, `E3V-002`, `E3V-003`; host/filesystem/Git/process-class support matrix. | Preserve workspace identity and execution-port compatibility across local/remote adapter migration. | May propose after closure; hand back if a required supported class cannot provide safe containment/isolation. |
| `ADR-E2-005` capability/permission/approval/secret/effect/reconciliation | Sections 9-11, 14 (`LB-10`, `LB-14`): central integrated authority, service authority/direct raw path, or command admission/out-of-event broker. | `E3V-004`, `E3V-005`, `E3V-006`; approval expiry, external-effect ambiguity, protected acquisition/delivery. | Capability/receipt identifiers and forbidden-surface rules must survive adapter/client changes. | May propose after closure; hand back when no conforming protected/effect mechanism can realize the hard contract. |
| `ADR-E2-006` model/provider/routing/context | Sections 10, 13, 14 (`LB-08`, `LB-13`): embedded gateway, service gateway, or route/result events. | `E3V-008`; only eligible models/providers/configurations may be measured later. | Provider-neutral gateway and source-authoritative summaries limit replacement cost; no provider assigned now. | May propose structural routing after closure; hand back if validated eligibility disproves an ADR assumption, not for a single bad configuration alone. |
| `ADR-E2-007` verification/evidence/artifact/provenance/integrity | Sections 7-10, 14 (`LB-16`, `LB-18`): integrated manifests, service manifests, or journal-position projections. | `E3V-007`; artifact drift, verifier independence, manifest/readback and large-output evidence. | Evidence identity/manifests must remain portable; C03 adds journal-position coupling. | May propose after closure; hand back on structural inability to bind evidence independently and durably. |
| `ADR-E2-008` observability/audit/logging/metering/typed failure | Sections 9, 10, 14 (`LB-06`, `LB-16`): in-store semantic separation, service telemetry, or material journal plus projections. | `E3V-004`, `E3V-007`; redaction, typed failure, audit/telemetry separation and completeness fixtures. | Stable failure/audit schemas must version independently of optional telemetry sinks. | May propose after closure; hand back only for a structural hard-property contradiction. |
| `ADR-E2-009` local packaging/future remote/multiclient/extensions/General/Finance/SaaS | Sections 12-14 (`LB-11`, `LB-12`, `LB-19`): replaceable local executor, service/worker topology, or serializable command/event adapters. | `E3V-003`; E4 owns performance/UX/remote operational evidence; Finance/SaaS remain out of scope. | Preserve governed extension seam without committing optional future topology; migration direction remains explicit. | May propose bounded v0.1 seams after closure; hand back if required local packaging/support assumptions fail, never to implement deferred products silently. |

### 18.5 E2-005 future input contract

Only after E2-003 is independently verified and E2-004 independently verifies `NO_PRESELECTION_SPIKE_REQUIRED`, E2-005 receives:

- three analytically viable, unranked candidates and the corrected 195-cell comparison matrix;
- 59 hard ARs per candidate: 57 architecture-confirmed plus 2 architecture-seam-confirmed with E3 validation outstanding, with no violation or preference compensation;
- all six preferences in six primary groups, the correlation sets, no final weights/scores, and all seven sensitivity profiles;
- the 25-domain comparison, complete recovery scenarios, security/testability comparison, 19 Level B families, and migration/reversibility consequences;
- all 10 analytic resolutions, the unified consequence model, and the verified E2-004 no-spike closure;
- the `ADR-E2-001..009` evidence map, all `E3V-001..008` obligations, tested-scope restrictions, fail-closed behavior, and ADR handback rules; and
- remaining implementation/E3 unknowns without treating missing evidence as favorable.

E2-005 may propose a candidate/ADR baseline only after that independent closure; this fixer does not propose one.

## 19. Fixer-pass boundary

This document is `READY_FOR_REVIEW`, not verified. A fresh independent verifier must reproduce the hard gate, matrix completeness, uncertainty partition, zero-preselection-spike derivation, consequence consistency, and no-winner result before E2-003 can move to `VERIFIED`.

Architecture remains `NOT_SELECTED`; preferred candidate remains `NONE`; accepted ADRs remain 0; architecture spikes, evaluation runs, model benchmarks, paid calls, external effects, and application code remain 0/none; autonomy remains `NOT_ELIGIBLE` and autonomous build remains unauthorized.
