# Engineering Preview E3 Validation Obligations for Proposed C01 Baseline

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Task: `E2-005`

Proposed architecture: `EP-ARCH-C01` — Integrated Transactional Local Core

Execution status: `PLAN_ONLY_NOT_AUTHORIZED_NOT_RUN`

Architecture selected: `false`

## 1. Authority and use

This register carries the canonical `E3V-001..008` meanings from independently verified `ENGINEERING_PREVIEW_ARCHITECTURE_REQUIREMENTS.md` §9 into the C01 proposal. The compact E2-003 uncertainty-register descriptions are not used as replacements. Each obligation has one canonical ADR handback set, a C01 assumption, bounded evidence, fail-closed behavior and a root-cause split. When these records discuss stored inputs or results, the only architecture-level state classes are `AUTHORITATIVE STATE`, `DERIVED PROJECTION`, `EPHEMERAL WORKING CONTEXT`, and `LOSSY SUMMARY`; operational logs/telemetry are rebuildable observations, not a fifth authority class.

E2-005 authorizes no E3 run, prototype, model benchmark, provider call, paid call, credential use, implementation, role assignment or support claim. E3 begins only after the full E2 architecture gate is independently verified and an eligible E3 task is registered and authorized. Real/provider/paid work additionally requires applicable account, budget, credential, region and data-policy authorization.

### 1.1 Root-cause vocabulary

| Outcome | Consequence |
|---|---|
| `VALIDATED_FOR_TESTED_SCOPE_ONLY` | The selected mechanism/configuration passes prospectively frozen focused criteria. This validates only the tested mechanism and support class, never full product/release compliance. |
| `IMPLEMENTATION_CONFIGURATION_FAILURE` | The architecture still admits a conforming realization, but the tested adapter, policy wiring, fixture, implementation or configuration fails. Correct/replace and revalidate; do not reopen an ADR automatically. |
| `PRODUCT_CLASS_UNSUPPORTED` | A host, client, repository, process, provider or capability class cannot currently satisfy the contract. Narrow support and fail closed; reopen E2 only if an ADR requires that class and no conforming alternative remains. |
| `EVIDENCE_MISSING_FAIL_CLOSED` | Evidence is missing, inconclusive, stale, invalid or outside the tested scope. Grant no credit; remain blocked/fenced/waiting/unknown/unverified/unassigned as applicable. |
| `ARCHITECTURE_HANDBACK` | Reproducible evidence disproves an indispensable selected interface/property or shows a required hard boundary cannot exist for the declared required support class. Stop affected E3 work and return to the frozen ADR set. |

E3 may not redesign E2. An architecture handback returns the exact evidence to E2-005 for baseline/ADR revision, independent challenge, fresh E2-006 verification and renewed E2 stage-gate evaluation before affected E3 work resumes.

## 2. Obligation index and canonical handback closure

For each E3V, closure is computed without changing frozen E2-001 ownership:

1. union the canonical linked ARs in verified E2-001 §9 with C01-specific linked ARs recorded in the verified decision matrix;
2. join those ARs to the proposed primary ADR owner in the baseline §13 and include every owner whose architecture assumption the E3V failure would disprove;
3. add only an explicitly justified secondary ADR whose selected structural boundary would also be contradicted; and
4. normalize the ADR IDs as an unordered set and require exact equality everywhere the E3V handback is represented.

| ID | E3 lane / downstream owner | Linked ARs -> primary ADR owners | Justified secondary ADR(s) | Canonical ADR handback set |
|---|---|---|---|---|
| `E3V-001` | Technical/mechanism / `E3_TECHNICAL_VALIDATION_OWNER` | `AR-COR-001/007 -> 003`; `AR-DUR-001/005, AR-PRF-003 -> 002`; `AR-DUR-002/003 -> 003`; `AR-APR-002 -> 005`; `AR-FAIL-001 -> 008`; `AR-TST-001/002 -> 004/007`; `AR-FUT-001 -> 009` | None. | `ADR-E2-002/003/004/005/007/008/009` |
| `E3V-002` | Technical/mechanism / `E3_TECHNICAL_VALIDATION_OWNER` | `AR-DUR-004 -> 003`; `AR-EXE-002/003, AR-TST-001 -> 004`; `AR-TST-002 -> 007` | None. | `ADR-E2-003/004/007` |
| `E3V-003` | Technical/mechanism / `E3_TECHNICAL_VALIDATION_OWNER` | `AR-DUR-006 -> 002`; `AR-WSP-001..005, AR-GIT-001 -> 004`; `AR-PKG-001, AR-PRF-006 -> 009` | `001`: client/core lifetime and no-hidden-service package topology. | `ADR-E2-001/002/004/009` |
| `E3V-004` | Provider-contract conformance / `E3_TECHNICAL_VALIDATION_OWNER` | `AR-MOD-001..003 -> 006`; `AR-SEC-004 -> 005`; `AR-FAIL-001 -> 008`; `AR-TST-001/002 -> 004/007`; `AR-FUT-003 -> 009` | `001`: embedded gateway placement. | `ADR-E2-001/004/005/006/007/008/009` |
| `E3V-005` | Technical/mechanism / `E3_TECHNICAL_VALIDATION_OWNER` | `AR-COR-003, AR-DAT-001/002 -> 002`; `AR-COR-004..006, AR-EVD-001..003, AR-VER-001..003 -> 007`; `AR-CTX-001/002 -> 006`; `AR-GIT-002 -> 004`; `AR-OBS-002 -> 008` | `003`: causal operation identity; `005`: approval/effect authority used as evidence. | `ADR-E2-002/003/004/005/006/007/008` |
| `E3V-006` | Security mechanism / `E3_SECURITY_VALIDATION_OWNER` | `AR-EXE-001/004, AR-TST-001 -> 004`; `AR-SEC-001..006, AR-APR-001/003 -> 005`; `AR-TST-002 -> 007`; `AR-FUT-002 -> 009` | `001`: protected client surface; `008`: capture/log exclusion and failure presentation. | `ADR-E2-001/004/005/007/008/009` |
| `E3V-007` | Measurement mechanism / `E3_MEASUREMENT_VALIDATION_OWNER` | `AR-OBS-001, AR-FAIL-002, AR-TST-003, AR-PERF-001/002 -> 008`; `AR-PRF-001 -> 001`; `AR-PRF-005 -> 007` | `002`: durable raw inputs; `009`: package/runtime limit surface. | `ADR-E2-001/002/007/008/009` |
| `E3V-008` | Model/configuration benchmark / `E3_MODEL_BENCHMARK_OWNER` | `AR-MOD-001..003 -> 006` | None; ordinary model/configuration failure is not architectural. | `ADR-E2-006` |

Every primary owner in the joined column is included. Secondary inclusion has a local rationale; no ADR is included for convenience. A validator must extract this index, each obligation's `Canonical handback` row, the baseline, all carrying ADRs, the current task record and both current handoffs; normalization followed by set comparison must yield eight equal groups. Any missing primary owner or unequal representation blocks E2-005 review.

## 3. E3V-001 — persistence, ownership and effect recovery

**Canonical property.** Acknowledged mutations, ownership, partial writes, duplicate intake, restart/resume and ambiguous effects recover without loss, stale acceptance, blind replay or duplicate consequential effect. Sources: `AR-COR-001/007`, `AR-DUR-001/002/003/005`, `AR-APR-002`, `AR-FAIL-001`, `AR-TST-001/002`, `AR-FUT-001`, `AR-PRF-003`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01's transactional authoritative state plus material history/outbox/effect ledgers preserve acknowledgements and first outcomes through each selected crash/ownership/effect boundary without claiming cross-boundary atomicity? |
| Selected-architecture assumption | A sole core writer with owner epochs, expected versions, durable intent/attempt/readback and explicit nontransactional reality can recover every nonterminal record truthfully. |
| Prerequisites | E2 gate verified; exact C01 persistence, record, migration and supervisor/effect mechanism/configuration selected by an authorized future task; representative support classes declared; fault schedule and oracles frozen. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`; future executable task must name the accountable assignee and independent reviewer. |
| AR/ADR closure | Linked ARs and their primary owners are recorded in §2; every owner is included in `ADR-E2-002/003/004/005/007/008/009`, with no secondary addition. |
| Required evidence | Exact baseline/mechanism/config IDs; prospective fault schedule; before/after authoritative state and integrity facts; owner epochs; first-outcome duplicate receipt; partial-write facts; dispatch/receipt/target readback; original evidence; uncertainty/limitations; independent criterion check. |
| Supported scope | Only the tested persistence mechanism, record versions, host/storage class, operation/effect adapters and fault points. |
| Unsupported scope | Untested storage/host/adapters; effects with no authoritative readback; full 170-case/E5 population; global transactionality. |
| Hard gate / success | Zero acknowledged loss, stale-writer acceptance or duplicate consequential effect; every fault ends with one legal state and `KNOWN_SUCCESS`, `KNOWN_FAILURE` or `UNKNOWN_OUTCOME`; projection loss never becomes canonical recovery input. |
| Configuration failure | Repairable store/adapter/codec/fault-fixture defect where a conforming C01 mechanism remains. |
| Missing evidence | `EVIDENCE_MISSING_FAIL_CLOSED`: no recovery/support claim; task stays recovering/blocked/unknown. |
| Architecture failure | Reproducible acknowledged loss, duplicate effect, stale acceptance, fabricated continuity, or architecture-incapable recovery with no conforming C01 realization. |
| Authorization, stop and budget | Synthetic/local focused validation first; no external effect or paid/provider call without separate authority. Stop on a hard violation, uncertain real effect, ceiling/budget exhaustion, unsafe fixture or architecture contradiction. |
| Canonical handback | `ADR-E2-002/003/004/005/007/008/009`; stop affected work and return the exact fault/evidence chain to E2. |

## 4. E3V-002 — process control, descendant containment and fencing

**Canonical property.** The selected control mechanism truthfully provides bounded pause/stop/force-or-fence, descendant accounting, output bounds, timeout and recovery. Sources: `AR-DUR-004`, `AR-EXE-002/003`, `AR-TST-001/002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | On each claimed supported host/process class, can C01's owned supervisor identify descendants, bound output/effects, cancel or force where promised, and always fence stale productive/effect authority across control and owner loss? |
| Selected-architecture assumption | Process-tree containment and core authority fencing are separate mechanisms; unavailable termination narrows support while the epoch/capability fence prevents stale effects. |
| Prerequisites | Exact host, process API, privilege model, supervisor mechanism, tree definition, timeout/output/force policy and supported/unsupported classes selected and frozen; safe synthetic descendants only. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`. |
| AR/ADR closure | Linked ARs and primary owners are recorded in §2; closure is `ADR-E2-003/004/007`, including ADR-E2-007 as primary owner of `AR-TST-002`. |
| Required evidence | Operation/control timeline; parent/descendant identities; signals/termination attempts; force primitive and permissions; monotonic timing; output/effect accounting; survivors/orphans; epoch/fence rejection; restart recovery; independent readback; limitations. |
| Supported scope | Tested host/platform/process/configuration classes only. |
| Unsupported scope | Untested hosts, privileged/adversarial processes beyond the claim, kernel compromise and any class without truthful descendant/force evidence. |
| Hard gate / success | No post-control productive/effect authority; promised descendants terminate within the frozen bound; every survivor is discovered/fenced; endpoints and unsupported classes are truthful. |
| Configuration failure | Miswired supervisor, bad adapter, incorrect permission/configuration or faulty fixture with a conforming alternative. |
| Missing evidence | Block/fence the class; do not infer whole-tree or force feasibility. |
| Architecture failure | A required advertised class cannot be controlled or authority-fenced by any conforming realization. |
| Authorization, stop and budget | Local synthetic processes within a registered E3 task and frozen finite limits; stop on containment escape, unauthorized effect, survivor with authority, ceiling exhaustion or unsafe host condition. |
| Canonical handback | `ADR-E2-003/004/007`. |

## 5. E3V-003 — workspace, Git, isolation and local packaging

**Canonical property.** The selected workspace/isolation/packaging boundary protects original user state and provides declared local operation and contributor access. Sources: `AR-DUR-006`, `AR-WSP-001..005`, `AR-GIT-001`, `AR-PKG-001`, `AR-PRF-006`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can the selected C01 local package, workspace/filesystem/Git brokers and support matrix establish isolation before mutation, preserve original user state through stale/dirty/topology cases and remain reproducible for contributors? |
| Selected-architecture assumption | A replaceable local workspace/execution port can enforce the frozen semantic floor without a mandatory hidden daemon or cloud service. |
| Prerequisites | Exact client/runtime/package/update, workspace/Git/filesystem/isolation mechanisms and supported repository/host classes chosen; clean setup and fault fixtures frozen. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`. |
| AR/ADR closure | Primary owners `ADR-E2-002/004/009` plus secondary ADR-E2-001's client/core package topology produce `ADR-E2-001/002/004/009`. |
| Required evidence | Support matrix; exact initial/final inventories; object identities/canaries; bind-before-mutation order; dirty-material attribution; path/topology negatives; stale cleanup/readback; component/setup map; clean reproduction and limitations. |
| Supported scope | Declared, tested host/filesystem/repository/Git/package classes. |
| Unsupported scope | Any unknown E1 repository condition or platform mechanism not tested; cloud/remote/multi-user execution; full E5 release matrix. |
| Hard gate / success | Zero outside/unrelated mutation; every tested condition receives a truthful disposition; clean setup/recovery is reproducible; no undeclared mandatory service. |
| Configuration failure | Bounded adapter, installer, documentation or setup defect where the C01 local boundary remains feasible. |
| Missing evidence | Class stays unsupported/blocked; no portability or contributor claim. |
| Architecture failure | Structural root/user-state escape or an unavoidable hidden mandatory service contradicts C01/E1. |
| Authorization, stop and budget | Synthetic/task-owned fixtures only; no destructive user-state operation, download, dependency execution or network without separate grants. Stop on canary change, ownership ambiguity, escape or resource ceiling. |
| Canonical handback | `ADR-E2-001/002/004/009`. |

## 6. E3V-004 — provider-gateway semantic preservation

**Canonical property.** The selected provider boundary preserves product truth, route purpose/eligibility, explicit fallback, provider-specific result/failure/cancellation, data policy, provenance and usage/cost. Sources: `AR-MOD-001..003`, `AR-SEC-004`, `AR-FAIL-001`, `AR-TST-001/002`, `AR-FUT-003`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01's embedded gateway normalize core orchestration while retaining materially different streaming, tool, refusal, usage, stop, cancellation and failure semantics and proving zero dispatch for denied routes? |
| Selected-architecture assumption | A typed core contract plus explicit provider extensions/raw-evidence references can preserve rather than erase provider differences without provider-native state becoming product truth. |
| Prerequisites | Exact gateway schema/version and controlled licensed/synthetic provider-shape fixtures; route policy and failure taxonomy frozen. Any live phase also needs current primary-source/account access, data, region, credential, run and budget approvals. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`; live provider execution remains separately approved. |
| AR/ADR closure | Primary owners `ADR-E2-004/005/006/007/008/009` plus secondary ADR-E2-001's embedded placement produce `ADR-E2-001/004/005/006/007/008/009`. |
| Required evidence | Replay/call manifest; requested/resolved route and capability/eligibility decisions; zero-dispatch facts; normalized and raw-linked stream/tool/refusal/failure/cancel/fallback records; usage/cost/missingness and limitations. |
| Supported scope | Offline fixture shapes first; any later tested exact provider/model/adapter/config only. |
| Unsupported scope | Untested providers/configurations, production suitability, role eligibility and hidden analogy from wire compatibility. |
| Hard gate / success | Deterministic causal mapping, explicit unsupported semantics, no fabricated usage/stop, correct cancellation/failure layer and zero bytes/calls/cost for denied routes. |
| Configuration failure | Provider/configuration/adapter defect with a viable contract. |
| Missing evidence | No dispatch, eligibility or semantic-preservation claim. |
| Architecture failure | The gateway interface itself cannot represent/preserve a required semantic through any compliant route. |
| Authorization, stop and budget | Offline/synthetic zero-cost work first. Live calls stop at the separately authorized cap, policy/data mismatch, unknown cost, hard semantic loss or any unauthorized dispatch. No paid call is authorized by this plan. |
| Canonical handback | `ADR-E2-001/004/005/006/007/008/009`. |

## 7. E3V-005 — state, evidence and independent verifier

**Canonical property.** The selected state/evidence/verifier mechanism makes `AUTHORITATIVE STATE` / `DERIVED PROJECTION` distinctions, exact revision binding, gaps/tamper/staleness, deterministic replay, adequacy, verifier error and correction independently inspectable. Sources: `AR-COR-003..006`, `AR-DAT-001/002`, `AR-CTX-001/002`, `AR-GIT-002`, `AR-EVD-001..003`, `AR-VER-001..003`, `AR-OBS-002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01 build revision-bound evidence from authoritative state and allow a separate least-privilege verifier to detect weak predicates, stale mutation, gaps/tamper and verifier-layer errors without trusting executor narrative? |
| Selected-architecture assumption | Transactional state/material history and immutable artifact references expose enough independent readback to rebuild derived bundles and invalidate stale passes. |
| Prerequisites | Exact state/evidence/artifact schemas, integrity mechanism, verifier boundary/configuration, representative profiles and fault cases frozen; verifier independence policy satisfied. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`, with an independent verifier distinct from the E3 mechanism implementer/operator. |
| AR/ADR closure | Primary owners `ADR-E2-002/004/006/007/008` plus secondary causal/effect authorities ADR-E2-003/005 produce `ADR-E2-002/003/004/005/006/007/008`. |
| Required evidence | Exact candidate/revision/schema/actor/verifier identities; bounded manifest; bundles/references; induced stale/gap/tamper/adequacy/verifier-failure cases; deterministic readbacks/replays; validator results; correction linkage; limitations/nonclaims. |
| Supported scope | Tested profiles, artifacts, verifier configuration and fault cases only. |
| Unsupported scope | Full E5 evidence/release population, untested artifact carriers, and any verifier whose independence or deterministic access is invalid. |
| Hard gate / success | Correct independent accept/reject/error result at every fault; exact revision binding; deterministic evidence outranks contradictory judgment; no telemetry/self-report authority. |
| Configuration failure | Validator, projection, manifest or verifier-tool implementation defect with a feasible C01 boundary. |
| Missing evidence | Verification remains `UNVERIFIED`; completion is impossible. |
| Architecture failure | Unavoidable executor-self-report dependence, stale-pass acceptance, telemetry authority, nondeterministic authority or unavoidable required-evidence loss. |
| Authorization, stop and budget | Read-only/synthetic exact-candidate checks within frozen limits; stop on candidate mutation, invalid independence, evidence contamination, secret exposure or ceiling exhaustion. |
| Canonical handback | `ADR-E2-002/003/004/005/006/007/008`. |

## 8. E3V-006 — trust, capability, approval, secret and protected entry

**Canonical property.** The selected trust/capability/approval/secret/protected-entry boundary enforces zero unauthorized flow/effect and fail-closed acquisition/use under representative attacks. Sources: `AR-EXE-001/004`, `AR-SEC-001..006`, `AR-APR-001/003`, `AR-TST-001/002`, `AR-FUT-002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can every C01 enforcement point deny representative unauthorized flows/effects, and can its co-resident protected controller acquire/deliver once to the exact current recipient while excluding every ordinary capture surface? |
| Selected-architecture assumption | Policy/workspace/supervisor/gateway boundaries plus a transient recipient/use/fence path outside ordinary core/model/log/evidence capture can enforce the hard contract; raw secret state is never durably replayable. |
| Prerequisites | Exact client/runtime/protected carrier, recipient, capture inventory, process/workspace/network/capability policies and threat/enforcement map selected; synthetic markers/canaries only; support classes frozen. |
| Owner | `E3_SECURITY_VALIDATION_OWNER`, independently reviewed by a security reviewer who did not author the mechanism under test. |
| AR/ADR closure | Primary owners `ADR-E2-004/005/007/009` plus secondary client/capture owners ADR-E2-001/008 produce `ADR-E2-001/004/005/007/008/009`. |
| Required evidence | Exact 20-boundary/enforcement map; positive/negative requests; synthetic markers/canaries; capture-state transitions; forbidden-surface scans covering input/model/provider/tool/terminal/process/log/telemetry/evidence/UI; approval/revocation/replay; exact recipient/use/fence; zero-dispatch/effect readback; non-secret receipt; crash/replacement/reacquisition; limitations. |
| Supported scope | Tested client/runtime/carrier/host/policy/process classes and representative attack subset only. |
| Unsupported scope | Real secrets, untested capture surfaces/classes, host compromise and the full 23-family/16-composition E5 suite. |
| Hard gate / success | Zero unauthorized read/flow/effect and zero marker occurrence outside exact recipient; replay/mutation/stale authority denied; crash/replacement never replays raw input; missing protection fails to wait/closed. |
| Configuration failure | Miswired policy/adapter/carrier/fixture when an alternate conforming C01 realization remains. |
| Missing evidence | `WAITING_FOR_USER`, blocked or unsupported; never ordinary input and never favorable credit. |
| Architecture failure | Any required structural boundary—including C01 protected delivery—cannot enforce the hard property through any conforming realization. |
| Authorization, stop and budget | Synthetic markers only; zero real credentials; stop immediately on marker escape, unauthorized dispatch/effect, unsafe capture state, ambiguous raw-value handling or any ceiling. |
| Canonical handback | `ADR-E2-001/004/005/007/008/009`. C01-specific `SPQ-E2-002-03` is attached to ADR-E2-005 and is explicitly unproven. |

## 9. E3V-007 — instrumentation and finite-limit enforcement

**Canonical property.** The selected instrumentation and limit-enforcement mechanism can produce protocol inputs and enforce finite ceilings without inventing or redefining results. Sources: `AR-OBS-001`, `AR-FAIL-002`, `AR-TST-003`, `AR-PERF-001/002`, `AR-PRF-001/005`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01 expose raw attributed timestamps, outcomes, usage, cost, limits and missingness across core/supervisor/gateway/evidence boundaries and deny dispatch when prospectively frozen finite ceilings are missing or exceeded? |
| Selected-architecture assumption | Versioned measurement ports and policy gates can instrument the integrated core without turning telemetry into authority or inventing values. |
| Prerequisites | Exact mechanism/config/environment/workload, reference environment, strata, calculations, uncertainty treatment and finite ceiling policy frozen before any scored attempt. |
| Owner | `E3_MEASUREMENT_VALIDATION_OWNER`; numeric ceiling policy is owned separately by `E3-QPA-001` below. |
| AR/ADR closure | Primary owners `ADR-E2-001/007/008` plus durable-input/package-surface owners ADR-E2-002/009 produce `ADR-E2-001/002/007/008/009`. |
| Required evidence | Raw timestamp/outcome/usage/cost/limit records; derivations; route/tool/layer attribution; missing fields; ceiling denials; reference environment; focused slices of all eight protocols; limitations and no post-result redefinition. |
| Supported scope | Frozen focused protocol slices and exact environment/configuration only. |
| Unsupported scope | Full E1/E5 populations, extrapolated performance, unmeasured costs and any universal release claim. |
| Hard gate / success | Inputs are representable and reproducible; missingness explicit; finite limits deny dispatch; derived values match raw data; telemetry never changes task/evidence truth. |
| Configuration failure | Instrumentation/configuration defect or truthful performance miss with correct observability. |
| Missing evidence | No SLO, limit or efficiency claim; scored run blocked when required inputs/ceilings are absent. |
| Architecture failure | Required protocol input is structurally unrepresentable or a mandatory finite ceiling cannot be enforced. |
| Authorization, stop and budget | Run only under `E3-QPA-001` frozen values and task budget; stop at any limit, definition mismatch, missing mandatory field or post-freeze mutation. |
| Canonical handback | `ADR-E2-001/002/007/008/009`. |

## 10. E3V-008 — model/configuration role qualification

**Canonical property.** Candidate systems/configurations can or cannot occupy logical roles without self-promoting evaluation evidence. Sources: `AR-MOD-001..003`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Which separately authorized exact system/model/provider/tool/configurations, if any, qualify for each logical role and eligible task class through the unchanged provider-neutral C01 gateway? |
| Selected-architecture assumption | The gateway does not require a particular occupant; architecture remains useful with roles unassigned until independent evidence exists. |
| Prerequisites | E2 gate verified; model registry current; suite/cases/role map challenged and frozen; exact candidates/configs/access/data/region/credentials/budget/repetitions/graders/verification/stop rules authorized; `E3-QPA-001` values frozen. |
| Owner | `E3_MODEL_BENCHMARK_OWNER`; open-ended selection-affecting grading must meet the independent grader/verifier rules. |
| AR/ADR closure | `AR-MOD-001..003` are primarily owned by ADR-E2-006; there is no justified secondary ADR. |
| Required evidence | Exact route/model/tool/config/task/fixture/harness/grader identities; raw/normalized output and failures/refusals; attempts/repetitions; costs/latency; deterministic results; blinded independent grading where required; eligibility disposition; limitations. |
| Supported scope | Only tested exact configurations, roles, task classes, routes, account/data policy and qualification window. |
| Unsupported scope | Untested aliases/snapshots/settings, other roles/tasks, production suitability by reputation, hidden fallback and permanent universal assignment. |
| Hard gate / success | Every mandatory case and hard boundary passes under the frozen protocol with valid independence and budget; qualification remains scoped and provisional to its window/configuration. |
| Configuration failure | Leave the role/configuration unassigned; another separately authorized configuration may be evaluated. |
| Missing evidence | Role remains unassigned; zero normal-route promotion and zero autonomous authority. |
| Architecture failure | Only when ADR-E2-006 made an indispensable capability impossible to satisfy through every compliant route; ordinary model/provider failure is not architecture failure. |
| Authorization, stop and budget | No execution without founder-approved benchmark budget, accounts, data/region/credential policy and run authorization. Stop on a hard-boundary failure, invalid grader independence, definition drift, missing cost, ceiling/budget exhaustion or unauthorized route. This document authorizes USD 0 and zero calls. |
| Canonical handback | `ADR-E2-006` only under the structural condition above. |

No occupant is assigned here to `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER` or `SECURITY_REVIEWER`. The current model registry remains `HYPOTHESIS_ONLY` / `NOT_RUN`.

## 11. Finite ceiling-policy authority registration

Authority ID: `E3-QPA-001`

Name: Engineering Preview E3 Qualification Policy Authority

Accountable owner: **Founder**, acting as the repository's accountable qualification-policy authority; the future E3 task author may draft values but may not self-approve them.

Registration task: `E2-005`

Scope: prospectively select and version finite values for:

1. verification-rerun ceiling per case/task;
2. deterministic required-check repetition rule/value per check/class; and
3. correction-attempt ceiling per case/task.

Numeric values selected by E2-005: **none**. Existing frozen test/protocol repetitions and SLO measurements remain source-specific requirements; they do not fill these three null universal policy fields by implication.

### 11.1 Required independent review path

1. Before the first E3 scored attempt, an authorized future E3 planning/qualification task writes a versioned policy containing finite positive values, risk-class mapping, task/case/check scope, exhaustion behavior and exact owner reference.
2. The Founder acting as `E3-QPA-001` approves the exact policy version before initial verification/attempt execution and before any result or candidate-label inspection.
3. A fresh challenger independently reviews incentive effects, favorable-retry risk, completeness, finite enforcement, budget interaction and consistency with frozen E1 rules.
4. A separate post-fix verifier checks the exact policy bytes, task/case/check coverage, finite values, pre-result freeze evidence, operator immutability and exhaustion behavior.
5. The scored run manifest binds the verified policy version and values. The E3 operator cannot change them after start. A change creates a new policy version and new whole affected block under the frozen governance rule; old attempts remain evidence.

### 11.2 Blocking and exhaustion rules

- Missing accountable authority reference: `E2_005_BLOCKED`. This proposal supplies `E3-QPA-001` and its Founder owner.
- Missing, null, nonfinite, zero/negative where a positive count is required, unreviewed, stale or post-result-selected value: `E3_SCORED_EXECUTION_BLOCKED`.
- Mixed deterministic results are `FLAKY`; a later pass does not erase earlier ordered outcomes and receives no credit until the frozen complete repetition rule is satisfied.
- Same-revision verification rerun is permitted only for `VERIFICATION_ERROR` and within the frozen ceiling. `CHANGES_REQUIRED`, `BLOCKED` or `INCONCLUSIVE` needs a new versioned candidate/evidence basis.
- Correction-ceiling exhaustion stops productive/task-advancing dispatch. Only separately preauthorized bounded safety/control/readback/evidence reserve operations may run; status remains truthful and never `COMPLETED`.
- Every attempt, failure, cost/effect, retryability decision, ceiling value/owner/policy reference, exhaustion time/reason, reserve operation and final status tuple is retained.

## 12. Bundle-deferral and verified SP-C provenance chains

### 12.1 E3 carry-forward chains

Every carried C01/shared bundle is normalized below. `ARCHITECTURE_HANDBACK` applies only when evidence shows that no conforming realization can preserve the indispensable architecture property for a required class. A mechanism/configuration defect uses `IMPLEMENTATION_CONFIGURATION_FAILURE`; a missing or inconclusive record uses `EVIDENCE_MISSING_FAIL_CLOSED`.

| Bundle / deferral provenance | Canonical E3 owner | Linked property / ARs | Linked ADR(s) | Evidence requirement | Fail-closed behavior | Failure classification | E2/ADR handback |
|---|---|---|---|---|---|---|---|
| `E2U-S01-DESCENDANT-CONTAINMENT` (`SPQ-E2-002-01`; verified closure §§8, 9) | `E3V-002` / `E3_TECHNICAL_VALIDATION_OWNER` | Descendant accounting, bounded stop/force-or-fence; `AR-DUR-004`, `AR-EXE-002/003`, `AR-TST-001/002` | `ADR-E2-003/004/007` | Exact host/process/config, tree/timeline/force permissions, fence/effect rejection, restart/readback, supported scope and limits | Unsupported class remains fenced/blocked; no whole-tree or host-containment claim | Bad adapter/config is `IMPLEMENTATION_CONFIGURATION_FAILURE`; missing data is `EVIDENCE_MISSING_FAIL_CLOSED`; no conforming required realization is `ARCHITECTURE_HANDBACK` | `ADR-E2-003/004/007` |
| `E2U-S02-PROTECTED-ACQUISITION` (`SPQ-E2-002-02`; verified closure §§8, 9) | `E3V-006` / `E3_SECURITY_VALIDATION_OWNER` | Capture-excluding acquisition and fail-to-wait; `AR-SEC-006`, `AR-TST-001/002` | `ADR-E2-001/004/005/007/008/009` | Synthetic marker, complete client/host capture inventory/scans, exact binding, lifecycle/reacquisition, non-secret receipt, scope and limits | `WAITING_FOR_USER`, blocked or unsupported; never ordinary input | Bad carrier/config is correction; missing/inconclusive capture proof is fail-closed; structural impossibility is handback | `ADR-E2-001/004/005/007/008/009` |
| `E3U-C01-PROTECTED-DELIVERY` (`SPQ-E2-002-03`; C01 f27) | `E3V-006` / `E3_SECURITY_VALIDATION_OWNER` | One-use co-resident recipient/use/fence delivery outside ordinary pipelines; `AR-SEC-003/006`, `AR-TST-001/002`, `AR-FUT-002` | `ADR-E2-001/004/005/007/008/009` | Exact delivery/capture/crash/revocation/recovery observations, forbidden-surface scan, receipt/readback and no-replay proof | `WAITING_FOR_USER` or blocked on absent, stale or ambiguous protection; require reacquisition | Mechanism/config failure first; missing proof fails closed; no conforming C01 delivery path is handback | `ADR-E2-001/004/005/007/008/009` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-001` record | `E3V-001` / `E3_TECHNICAL_VALIDATION_OWNER` | Acknowledgement, ownership, persistence and effect recovery; linked ARs in §2 | `ADR-E2-002/003/004/005/007/008/009` | §3 fault schedule, authoritative records, readbacks, certainty and independent checks | Recovering/blocked/unknown; no recovery claim | §3 root-cause split | `ADR-E2-002/003/004/005/007/008/009` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-002` record | `E3V-002` / `E3_TECHNICAL_VALIDATION_OWNER` | Process control/containment; linked ARs in §2 | `ADR-E2-003/004/007` | §4 tree/control/fence evidence | Fence/block unsupported class | §4 root-cause split | `ADR-E2-003/004/007` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-003` record | `E3V-003` / `E3_TECHNICAL_VALIDATION_OWNER` | Workspace, Git, isolation, package/contributor path; linked ARs in §2 | `ADR-E2-001/002/004/009` | §5 inventories, canaries, support matrix, clean reproduction | Unsupported/blocked; preserve user state | §5 root-cause split | `ADR-E2-001/002/004/009` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-004` record | `E3V-004` / `E3_TECHNICAL_VALIDATION_OWNER` | Provider semantic preservation and zero dispatch; linked ARs in §2 | `ADR-E2-001/004/005/006/007/008/009` | §6 offline licensed/synthetic conformance evidence first; any live phase separately authorized | No dispatch/eligibility/provider claim | §6 root-cause split | `ADR-E2-001/004/005/006/007/008/009` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-005` record | `E3V-005` / `E3_TECHNICAL_VALIDATION_OWNER` plus independent verifier | State/evidence/verifier integrity; linked ARs in §2 | `ADR-E2-002/003/004/005/006/007/008` | §7 exact-revision, gap/tamper/stale/adequacy/error evidence | `UNVERIFIED`; no completion | §7 root-cause split | `ADR-E2-002/003/004/005/006/007/008` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-006` record | `E3V-006` / `E3_SECURITY_VALIDATION_OWNER` | Trust/capability/approval/secret boundaries; linked ARs in §2 | `ADR-E2-001/004/005/007/008/009` | §8 twenty-boundary positive/negative and synthetic-marker evidence | Waiting/blocked/unsupported; zero ordinary fallback | §8 root-cause split | `ADR-E2-001/004/005/007/008/009` |
| `E3U-C01-TECHNICAL` / C01 f30 `E3V-007` record | `E3V-007` / `E3_MEASUREMENT_VALIDATION_OWNER` | Raw protocol inputs and finite-ceiling enforcement; linked ARs in §2 | `ADR-E2-001/002/007/008/009` | §9 raw/derived/missingness/denial records under prospectively frozen policy | No SLO/limit/efficiency credit; block scored run | §9 root-cause split | `ADR-E2-001/002/007/008/009` |
| `E3U-C01-MODEL-CONFIGURATION` / C01 f30 `E3V-008` record | `E3V-008` / `E3_MODEL_BENCHMARK_OWNER` | Exact role/configuration qualification; `AR-MOD-001..003` | `ADR-E2-006` | §10 independently governed exact-config benchmark evidence | Role remains unassigned; zero calls without authorization | Ordinary failure is configuration/eligibility failure; only gateway-level impossibility through every compliant route is handback | `ADR-E2-006` |

### 12.2 SP-C contract provenance and limits

| E3V / bundle | Precise verified SP-C provenance | Reuse or distinction | Evidence status |
|---|---|---|---|
| `E3V-001`, `E3U-C01-TECHNICAL` | Verified reconstructed architecture audit §18 `SP-C01` (`minimum_prototype`, `test_workload`, `success_metrics`, `failure_metrics`, `required_evidence`); C01 f27 `SPQ-E2-002-01/03.sp_c_reuse` | Reuse deterministic crash placement, stable effect identity, duplicate/reordered delivery, and before/after evidence; distinguish C01 transactional current-state authority from SP-C01's alternative-comparison scope | Contract input only; not executed and not architecture proof |
| `E3V-002`, `E2U-S01-DESCENDANT-CONTAINMENT` | Audit §18 `SP-C05` lifecycle/cancel/cleanup/capability evidence plus `SP-C01` owner-loss fault injection; C01 f27 `SPQ-E2-002-01.sp_c_reuse` | Reuse lifecycle/control fields; add C01 integrated owner epoch and exact host descendant/force-or-fence claim | Contract input only; not executed |
| `E3V-003` | No direct SP-C substitution; frozen E1 repository/workspace/Git/contribution contracts and C01 f30 are authoritative | Do not infer packaging or workspace proof from an execution-provider contract | No spike evidence claimed |
| `E3V-004` | Audit §18 `SP-C03` provider-transport `minimum_prototype`, malformed/partial/refusal/cancel/usage workload and required evidence | Reuse offline licensed/synthetic transport shapes and preservation oracles; distinguish a C01 gateway conformance run from provider/model selection | Contract input only; not executed; live/paid authority remains USD 0 |
| `E3V-005` | Audit §18 `SP-C01` independent replay/projection and integrity evidence fields | Reuse deterministic fault scheduling and independently computed projection checks only; C01 authoritative evidence/verifier contract remains the governing architecture property | Contract input only; not executed |
| `E3V-006`, `E2U-S02-PROTECTED-ACQUISITION`, `E3U-C01-PROTECTED-DELIVERY` | Audit §18 `SP-C04` exact action/authorization/receipt/readback fields, `SP-C05` takeover/recovery lifecycle, and `SP-C01` crash injection; C01 f27 `SPQ-E2-002-02/03.sp_c_reuse` | Reuse fake/synthetic identity, negative matrix, receipt/readback and lifecycle fixtures; add all ordinary capture observers and distinguish co-resident C01 delivery | Contract input only; not executed; no protected-acquisition guarantee |
| `E3V-007` | No direct SP-C contract replaces the eight frozen reliability protocols or `E3-QPA-001` | SP-C latency/cost fields may be raw inputs only; they cannot select thresholds | No spike or measurement run claimed |
| `E3V-008` | No SP-C contract replaces the frozen model-role benchmark plan | Provider transport conformance cannot qualify a model role | No model benchmark or provider call run |

SP-C records are verified design contracts from the reconstructed architecture audit, not observed C01 results. E2-004 verifier carry-forward is satisfied by reusing or explicitly distinguishing them here. No spike, prototype, evaluation, benchmark, provider call, paid call, or technology choice is authorized or claimed.

### 12.3 E4 implementation/configuration deferrals

| Bundle / deferral | Canonical E4 owner | Linked property / ADR(s) | Future evidence requirement | Fail-closed / failure classification | E2/ADR handback |
|---|---|---|---|---|---|
| `E4U-C01-IMPLEMENTATION` | Future registered `E4_IMPLEMENTATION_OWNER`; none assigned | client/runtime, embedded store, schema/codec, process API, isolation mechanism, provider SDKs/adapters, package/update tooling behind ADR-E2-001..009 seams | Exact technology/configuration, conformance results for applicable E3V records, files/commands/tests/results and migration/security/recovery evidence | No implementation/support claim before authorization and passed evidence; a defect is implementation/configuration failure unless it disproves an indispensable ADR property | Applicable canonical E3V set returns to its exact ADR set; otherwise correct within E4 |
| `E4U-C02-IMPLEMENTATION` | Historical only; no active owner | C02 service/client/IPC/auth/store/worker/provider/package choices; relevant only if E2 reopens candidate choice | Fresh E2 selection package plus applicable E3 evidence before any E4 authorization | Do not smuggle service/lease topology into C01; remains inactive | Reopen E2 candidate decision before any C02 ADR/implementation path |
| `E4U-C03-IMPLEMENTATION` | Historical only; no active owner | C03 runtime/journal/event/reducer/projection/executor/provider/package choices; relevant only if E2 reopens candidate choice | Fresh E2 selection package plus applicable E3 evidence before any E4 authorization | Do not make journal/reducer authority a hidden C01 choice; remains inactive | Reopen E2 candidate decision before any C03 ADR/implementation path |

E4 is not authorized. `E4U-C01-IMPLEMENTATION` is implementation/configuration detail behind the proposed C01 ADR seams, not a hidden ADR. C02/C03 bundles are historical/reopen evidence, not active implementation plans. These three verified bundles are preserved, not resolved.

## 13. E3 execution admission checklist

Before any focused technical validation or model/configuration benchmark, the registered task must show all of the following:

- E2-005 independently task-verified, E2-006 passed, and the E2 stage gate independently verified;
- exact proposed ADR version and applicable canonical handback set; this register cannot accept an ADR;
- exact implementation/mechanism/configuration/host/client/support-class identity;
- prospective question, hard gate, fixture/oracle/fault schedule, success/failure/missing/unsupported classification and root-cause decision rule;
- accountable owner, independent challenger and verifier paths;
- `E3-QPA-001` finite verified ceiling policy bound before results;
- task/run budget, time, resource, network, credential, data and external-effect authorization;
- raw evidence retention, secret-safe handling, candidate/revision binding and stop conditions;
- zero claim beyond tested scope and a named E4/E5 remainder.

Failure of any admission item blocks execution. No E3 result can itself set `AUTONOMY_ELIGIBLE`; only independent E3 stage verification may do so, and a separate explicit founder decision is still required for `AUTONOMOUS_BUILD_AUTHORIZED`.
