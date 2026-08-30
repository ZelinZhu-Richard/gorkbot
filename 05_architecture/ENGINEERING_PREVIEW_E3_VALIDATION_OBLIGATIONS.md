# Engineering Preview E3 Validation Obligations for Proposed C01 Baseline

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Task: `E2-005`

Proposed architecture: `EP-ARCH-C01` — Integrated Transactional Local Core

Execution status: `PLAN_ONLY_NOT_AUTHORIZED_NOT_RUN`

Architecture selected: `false`

## 1. Authority and use

This register carries the canonical `E3V-001..008` meanings from independently verified `ENGINEERING_PREVIEW_ARCHITECTURE_REQUIREMENTS.md` §9 into the C01 proposal. The compact E2-003 uncertainty-register descriptions are not used as replacements. Each obligation has one frozen ADR handback set, a C01 assumption, bounded evidence, fail-closed behavior and a root-cause split.

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

## 2. Obligation index and frozen handback sets

| ID | E3 lane | Focused owner class | C01 ADR linkage | Frozen ADR handback set |
|---|---|---|---|---|
| `E3V-001` | Technical/mechanism | `E3_TECHNICAL_VALIDATION_OWNER` | ADRs 002, 003, 004, 005 | `ADR-E2-002/003/004/005` |
| `E3V-002` | Technical/mechanism | `E3_TECHNICAL_VALIDATION_OWNER` | ADRs 003, 004 | `ADR-E2-003/004` |
| `E3V-003` | Technical/mechanism | `E3_TECHNICAL_VALIDATION_OWNER` | ADRs 001, 004, 009 | `ADR-E2-001/004/009` |
| `E3V-004` | Technical provider-contract conformance; live calls separately gated | `E3_TECHNICAL_VALIDATION_OWNER` | ADRs 001, 005, 006, 008 | `ADR-E2-001/005/006/008` |
| `E3V-005` | Technical/mechanism | `E3_TECHNICAL_VALIDATION_OWNER` | ADRs 002, 003, 005, 007, 008 | `ADR-E2-002/003/005/007/008` |
| `E3V-006` | Technical/security mechanism | `E3_SECURITY_VALIDATION_OWNER` | ADRs 001, 004, 005, 008 | `ADR-E2-001/004/005/008` |
| `E3V-007` | Technical/measurement mechanism | `E3_MEASUREMENT_VALIDATION_OWNER` | ADRs 002, 007, 008, 009 | `ADR-E2-002/007/008/009` |
| `E3V-008` | Model/configuration benchmark | `E3_MODEL_BENCHMARK_OWNER` | ADR 006 | `ADR-E2-006` only when an indispensable architectural capability is impossible through every compliant route |

Each set above is normative for this proposed package. Narrower or wider linkage elsewhere is historical provenance, not a second handback set. In particular, the widest coherent `E3V-006` set is frozen, and ADR-E2-008 explicitly carries that obligation because log/telemetry/capture exclusion is part of the boundary.

## 3. E3V-001 — persistence, ownership and effect recovery

**Canonical property.** Acknowledged mutations, ownership, partial writes, duplicate intake, restart/resume and ambiguous effects recover without loss, stale acceptance, blind replay or duplicate consequential effect. Sources: `AR-COR-001/007`, `AR-DUR-001/002/003/005`, `AR-APR-002`, `AR-TST-001/002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01's transactional authoritative state plus material history/outbox/effect ledgers preserve acknowledgements and first outcomes through each selected crash/ownership/effect boundary without claiming cross-boundary atomicity? |
| Selected-architecture assumption | A sole core writer with owner epochs, expected versions, durable intent/attempt/readback and explicit nontransactional reality can recover every nonterminal record truthfully. |
| Prerequisites | E2 gate verified; exact C01 persistence, record, migration and supervisor/effect mechanism/configuration selected by an authorized future task; representative support classes declared; fault schedule and oracles frozen. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`; future executable task must name the accountable assignee and independent reviewer. |
| Required evidence | Exact baseline/mechanism/config IDs; prospective fault schedule; before/after authoritative state and integrity facts; owner epochs; first-outcome duplicate receipt; partial-write facts; dispatch/receipt/target readback; original evidence; uncertainty/limitations; independent criterion check. |
| Supported scope | Only the tested persistence mechanism, record versions, host/storage class, operation/effect adapters and fault points. |
| Unsupported scope | Untested storage/host/adapters; effects with no authoritative readback; full 170-case/E5 population; global transactionality. |
| Hard gate / success | Zero acknowledged loss, stale-writer acceptance or duplicate consequential effect; every fault ends with one legal state and `KNOWN_SUCCESS`, `KNOWN_FAILURE` or `UNKNOWN_OUTCOME`; projection loss never becomes canonical recovery input. |
| Configuration failure | Repairable store/adapter/codec/fault-fixture defect where a conforming C01 mechanism remains. |
| Missing evidence | `EVIDENCE_MISSING_FAIL_CLOSED`: no recovery/support claim; task stays recovering/blocked/unknown. |
| Architecture failure | Reproducible acknowledged loss, duplicate effect, stale acceptance, fabricated continuity, or architecture-incapable recovery with no conforming C01 realization. |
| Authorization, stop and budget | Synthetic/local focused validation first; no external effect or paid/provider call without separate authority. Stop on a hard violation, uncertain real effect, ceiling/budget exhaustion, unsafe fixture or architecture contradiction. |
| Frozen handback | `ADR-E2-002/003/004/005`; stop affected work and return exact fault/evidence chain to E2. |

## 4. E3V-002 — process control, descendant containment and fencing

**Canonical property.** The selected control mechanism truthfully provides bounded pause/stop/force-or-fence, descendant accounting, output bounds, timeout and recovery. Sources: `AR-DUR-004`, `AR-EXE-002/003`, `AR-TST-001/002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | On each claimed supported host/process class, can C01's owned supervisor identify descendants, bound output/effects, cancel or force where promised, and always fence stale productive/effect authority across control and owner loss? |
| Selected-architecture assumption | Process-tree containment and core authority fencing are separate mechanisms; unavailable termination narrows support while the epoch/capability fence prevents stale effects. |
| Prerequisites | Exact host, process API, privilege model, supervisor mechanism, tree definition, timeout/output/force policy and supported/unsupported classes selected and frozen; safe synthetic descendants only. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`. |
| Required evidence | Operation/control timeline; parent/descendant identities; signals/termination attempts; force primitive and permissions; monotonic timing; output/effect accounting; survivors/orphans; epoch/fence rejection; restart recovery; independent readback; limitations. |
| Supported scope | Tested host/platform/process/configuration classes only. |
| Unsupported scope | Untested hosts, privileged/adversarial processes beyond the claim, kernel compromise and any class without truthful descendant/force evidence. |
| Hard gate / success | No post-control productive/effect authority; promised descendants terminate within the frozen bound; every survivor is discovered/fenced; endpoints and unsupported classes are truthful. |
| Configuration failure | Miswired supervisor, bad adapter, incorrect permission/configuration or faulty fixture with a conforming alternative. |
| Missing evidence | Block/fence the class; do not infer whole-tree or force feasibility. |
| Architecture failure | A required advertised class cannot be controlled or authority-fenced by any conforming realization. |
| Authorization, stop and budget | Local synthetic processes within a registered E3 task and frozen finite limits; stop on containment escape, unauthorized effect, survivor with authority, ceiling exhaustion or unsafe host condition. |
| Frozen handback | `ADR-E2-003/004`. |

## 5. E3V-003 — workspace, Git, isolation and local packaging

**Canonical property.** The selected workspace/isolation/packaging boundary protects original user state and provides declared local operation and contributor access. Sources: `AR-DUR-006`, `AR-WSP-001..005`, `AR-GIT-001`, `AR-PKG-001`, `AR-PRF-006`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can the selected C01 local package, workspace/filesystem/Git brokers and support matrix establish isolation before mutation, preserve original user state through stale/dirty/topology cases and remain reproducible for contributors? |
| Selected-architecture assumption | A replaceable local workspace/execution port can enforce the frozen semantic floor without a mandatory hidden daemon or cloud service. |
| Prerequisites | Exact client/runtime/package/update, workspace/Git/filesystem/isolation mechanisms and supported repository/host classes chosen; clean setup and fault fixtures frozen. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`. |
| Required evidence | Support matrix; exact initial/final inventories; object identities/canaries; bind-before-mutation order; dirty-material attribution; path/topology negatives; stale cleanup/readback; component/setup map; clean reproduction and limitations. |
| Supported scope | Declared, tested host/filesystem/repository/Git/package classes. |
| Unsupported scope | Any unknown E1 repository condition or platform mechanism not tested; cloud/remote/multi-user execution; full E5 release matrix. |
| Hard gate / success | Zero outside/unrelated mutation; every tested condition receives a truthful disposition; clean setup/recovery is reproducible; no undeclared mandatory service. |
| Configuration failure | Bounded adapter, installer, documentation or setup defect where the C01 local boundary remains feasible. |
| Missing evidence | Class stays unsupported/blocked; no portability or contributor claim. |
| Architecture failure | Structural root/user-state escape or an unavoidable hidden mandatory service contradicts C01/E1. |
| Authorization, stop and budget | Synthetic/task-owned fixtures only; no destructive user-state operation, download, dependency execution or network without separate grants. Stop on canary change, ownership ambiguity, escape or resource ceiling. |
| Frozen handback | `ADR-E2-001/004/009`. |

## 6. E3V-004 — provider-gateway semantic preservation

**Canonical property.** The selected provider boundary preserves product truth, route purpose/eligibility, explicit fallback, provider-specific result/failure/cancellation, data policy, provenance and usage/cost. Sources: `AR-MOD-001..003`, `AR-SEC-004`, `AR-FAIL-001`, `AR-TST-001/002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01's embedded gateway normalize core orchestration while retaining materially different streaming, tool, refusal, usage, stop, cancellation and failure semantics and proving zero dispatch for denied routes? |
| Selected-architecture assumption | A typed core contract plus explicit provider extensions/raw-evidence references can preserve rather than erase provider differences without provider-native state becoming product truth. |
| Prerequisites | Exact gateway schema/version and controlled licensed/synthetic provider-shape fixtures; route policy and failure taxonomy frozen. Any live phase also needs current primary-source/account access, data, region, credential, run and budget approvals. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`; live provider execution remains separately approved. |
| Required evidence | Replay/call manifest; requested/resolved route and capability/eligibility decisions; zero-dispatch facts; normalized and raw-linked stream/tool/refusal/failure/cancel/fallback records; usage/cost/missingness and limitations. |
| Supported scope | Offline fixture shapes first; any later tested exact provider/model/adapter/config only. |
| Unsupported scope | Untested providers/configurations, production suitability, role eligibility and hidden analogy from wire compatibility. |
| Hard gate / success | Deterministic causal mapping, explicit unsupported semantics, no fabricated usage/stop, correct cancellation/failure layer and zero bytes/calls/cost for denied routes. |
| Configuration failure | Provider/configuration/adapter defect with a viable contract. |
| Missing evidence | No dispatch, eligibility or semantic-preservation claim. |
| Architecture failure | The gateway interface itself cannot represent/preserve a required semantic through any compliant route. |
| Authorization, stop and budget | Offline/synthetic zero-cost work first. Live calls stop at the separately authorized cap, policy/data mismatch, unknown cost, hard semantic loss or any unauthorized dispatch. No paid call is authorized by this plan. |
| Frozen handback | `ADR-E2-001/005/006/008`. |

## 7. E3V-005 — state, evidence and independent verifier

**Canonical property.** The selected state/evidence/verifier mechanism makes authoritative/derived distinctions, exact revision binding, gaps/tamper/staleness, deterministic replay, adequacy, verifier error and correction independently inspectable. Sources: `AR-COR-003..006`, `AR-DAT-001/002`, `AR-CTX-001/002`, `AR-EVD-001..003`, `AR-VER-001..003`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01 build revision-bound evidence from authoritative state and allow a separate least-privilege verifier to detect weak predicates, stale mutation, gaps/tamper and verifier-layer errors without trusting executor narrative? |
| Selected-architecture assumption | Transactional state/material history and immutable artifact references expose enough independent readback to rebuild derived bundles and invalidate stale passes. |
| Prerequisites | Exact state/evidence/artifact schemas, integrity mechanism, verifier boundary/configuration, representative profiles and fault cases frozen; verifier independence policy satisfied. |
| Owner | `E3_TECHNICAL_VALIDATION_OWNER`, with an independent verifier distinct from the E3 mechanism implementer/operator. |
| Required evidence | Exact candidate/revision/schema/actor/verifier identities; bounded manifest; bundles/references; induced stale/gap/tamper/adequacy/verifier-failure cases; deterministic readbacks/replays; validator results; correction linkage; limitations/nonclaims. |
| Supported scope | Tested profiles, artifacts, verifier configuration and fault cases only. |
| Unsupported scope | Full E5 evidence/release population, untested artifact carriers, and any verifier whose independence or deterministic access is invalid. |
| Hard gate / success | Correct independent accept/reject/error result at every fault; exact revision binding; deterministic evidence outranks contradictory judgment; no telemetry/self-report authority. |
| Configuration failure | Validator, projection, manifest or verifier-tool implementation defect with a feasible C01 boundary. |
| Missing evidence | Verification remains `UNVERIFIED`; completion is impossible. |
| Architecture failure | Unavoidable executor-self-report dependence, stale-pass acceptance, telemetry authority, nondeterministic authority or unavoidable required-evidence loss. |
| Authorization, stop and budget | Read-only/synthetic exact-candidate checks within frozen limits; stop on candidate mutation, invalid independence, evidence contamination, secret exposure or ceiling exhaustion. |
| Frozen handback | `ADR-E2-002/003/005/007/008`. |

## 8. E3V-006 — trust, capability, approval, secret and protected entry

**Canonical property.** The selected trust/capability/approval/secret/protected-entry boundary enforces zero unauthorized flow/effect and fail-closed acquisition/use under representative attacks. Sources: `AR-EXE-001/004`, `AR-SEC-001..006`, `AR-APR-001/003`, `AR-TST-001/002`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can every C01 enforcement point deny representative unauthorized flows/effects, and can its co-resident protected controller acquire/deliver once to the exact current recipient while excluding every ordinary capture surface? |
| Selected-architecture assumption | Policy/workspace/supervisor/gateway boundaries plus a transient recipient/use/fence path outside ordinary core/model/log/evidence capture can enforce the hard contract; raw secret state is never durably replayable. |
| Prerequisites | Exact client/runtime/protected carrier, recipient, capture inventory, process/workspace/network/capability policies and threat/enforcement map selected; synthetic markers/canaries only; support classes frozen. |
| Owner | `E3_SECURITY_VALIDATION_OWNER`, independently reviewed by a security reviewer who did not author the mechanism under test. |
| Required evidence | Exact 20-boundary/enforcement map; positive/negative requests; synthetic markers/canaries; capture-state transitions; forbidden-surface scans covering input/model/provider/tool/terminal/process/log/telemetry/evidence/UI; approval/revocation/replay; exact recipient/use/fence; zero-dispatch/effect readback; non-secret receipt; crash/replacement/reacquisition; limitations. |
| Supported scope | Tested client/runtime/carrier/host/policy/process classes and representative attack subset only. |
| Unsupported scope | Real secrets, untested capture surfaces/classes, host compromise and the full 23-family/16-composition E5 suite. |
| Hard gate / success | Zero unauthorized read/flow/effect and zero marker occurrence outside exact recipient; replay/mutation/stale authority denied; crash/replacement never replays raw input; missing protection fails to wait/closed. |
| Configuration failure | Miswired policy/adapter/carrier/fixture when an alternate conforming C01 realization remains. |
| Missing evidence | `WAITING_FOR_USER`, blocked or unsupported; never ordinary input and never favorable credit. |
| Architecture failure | Any required structural boundary—including C01 protected delivery—cannot enforce the hard property through any conforming realization. |
| Authorization, stop and budget | Synthetic markers only; zero real credentials; stop immediately on marker escape, unauthorized dispatch/effect, unsafe capture state, ambiguous raw-value handling or any ceiling. |
| Frozen handback | `ADR-E2-001/004/005/008`. C01-specific `SPQ-E2-002-03` is attached to ADR-E2-005 and is explicitly unproven. |

## 9. E3V-007 — instrumentation and finite-limit enforcement

**Canonical property.** The selected instrumentation and limit-enforcement mechanism can produce protocol inputs and enforce finite ceilings without inventing or redefining results. Sources: `AR-OBS-001`, `AR-FAIL-002`, `AR-TST-003`, `AR-PERF-001/002`, `AR-PRF-001/005`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Can C01 expose raw attributed timestamps, outcomes, usage, cost, limits and missingness across core/supervisor/gateway/evidence boundaries and deny dispatch when prospectively frozen finite ceilings are missing or exceeded? |
| Selected-architecture assumption | Versioned measurement ports and policy gates can instrument the integrated core without turning telemetry into authority or inventing values. |
| Prerequisites | Exact mechanism/config/environment/workload, reference environment, strata, calculations, uncertainty treatment and finite ceiling policy frozen before any scored attempt. |
| Owner | `E3_MEASUREMENT_VALIDATION_OWNER`; numeric ceiling policy is owned separately by `E3-QPA-001` below. |
| Required evidence | Raw timestamp/outcome/usage/cost/limit records; derivations; route/tool/layer attribution; missing fields; ceiling denials; reference environment; focused slices of all eight protocols; limitations and no post-result redefinition. |
| Supported scope | Frozen focused protocol slices and exact environment/configuration only. |
| Unsupported scope | Full E1/E5 populations, extrapolated performance, unmeasured costs and any universal release claim. |
| Hard gate / success | Inputs are representable and reproducible; missingness explicit; finite limits deny dispatch; derived values match raw data; telemetry never changes task/evidence truth. |
| Configuration failure | Instrumentation/configuration defect or truthful performance miss with correct observability. |
| Missing evidence | No SLO, limit or efficiency claim; scored run blocked when required inputs/ceilings are absent. |
| Architecture failure | Required protocol input is structurally unrepresentable or a mandatory finite ceiling cannot be enforced. |
| Authorization, stop and budget | Run only under `E3-QPA-001` frozen values and task budget; stop at any limit, definition mismatch, missing mandatory field or post-freeze mutation. |
| Frozen handback | `ADR-E2-002/007/008/009`. |

## 10. E3V-008 — model/configuration role qualification

**Canonical property.** Candidate systems/configurations can or cannot occupy logical roles without self-promoting evaluation evidence. Sources: `AR-MOD-001..003`.

| Field | Frozen C01 obligation |
|---|---|
| Question | Which separately authorized exact system/model/provider/tool/configurations, if any, qualify for each logical role and eligible task class through the unchanged provider-neutral C01 gateway? |
| Selected-architecture assumption | The gateway does not require a particular occupant; architecture remains useful with roles unassigned until independent evidence exists. |
| Prerequisites | E2 gate verified; model registry current; suite/cases/role map challenged and frozen; exact candidates/configs/access/data/region/credentials/budget/repetitions/graders/verification/stop rules authorized; `E3-QPA-001` values frozen. |
| Owner | `E3_MODEL_BENCHMARK_OWNER`; open-ended selection-affecting grading must meet the independent grader/verifier rules. |
| Required evidence | Exact route/model/tool/config/task/fixture/harness/grader identities; raw/normalized output and failures/refusals; attempts/repetitions; costs/latency; deterministic results; blinded independent grading where required; eligibility disposition; limitations. |
| Supported scope | Only tested exact configurations, roles, task classes, routes, account/data policy and qualification window. |
| Unsupported scope | Untested aliases/snapshots/settings, other roles/tasks, production suitability by reputation, hidden fallback and permanent universal assignment. |
| Hard gate / success | Every mandatory case and hard boundary passes under the frozen protocol with valid independence and budget; qualification remains scoped and provisional to its window/configuration. |
| Configuration failure | Leave the role/configuration unassigned; another separately authorized configuration may be evaluated. |
| Missing evidence | Role remains unassigned; zero normal-route promotion and zero autonomous authority. |
| Architecture failure | Only when ADR-E2-006 made an indispensable capability impossible to satisfy through every compliant route; ordinary model/provider failure is not architecture failure. |
| Authorization, stop and budget | No execution without founder-approved benchmark budget, accounts, data/region/credential policy and run authorization. Stop on a hard-boundary failure, invalid grader independence, definition drift, missing cost, ceiling/budget exhaustion or unauthorized route. This document authorizes USD 0 and zero calls. |
| Frozen handback | `ADR-E2-006` only under the structural condition above. |

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

## 12. E4 implementation/configuration deferrals

| Bundle | Preserved choices | Applicability after E2/E3 | Guardrail |
|---|---|---|---|
| `E4U-C01-IMPLEMENTATION` | client/runtime; embedded store; schema/codec; process API; isolation mechanism; provider SDKs/adapters; package/update tooling | Applicable implementation bundle only if C01 becomes independently selected and E4 is separately authorized. | Implement C01 ports/authority/persistence/supervisor/gateways/package boundary; do not weaken E1/E2 or claim an unvalidated support class. |
| `E4U-C02-IMPLEMENTATION` | service/client/runtime; IPC/auth; store/schema; worker supervisor; isolation mechanism; provider adapters; installer/updater | Preserved as viable rejected-candidate provenance, not applicable to C01 without E2 reopening. | Do not smuggle service/lease topology into C01. |
| `E4U-C03-IMPLEMENTATION` | runtime/journal/payload; event/schema/reducer; projections/checkpoints; executor/isolation; provider adapters; client/package | Preserved as viable rejected-candidate provenance, not applicable to C01 without E2 reopening. | Do not make journal/reducer authority a hidden C01 implementation choice. |

E4 is not authorized. These bundles select no technology or product support class.

## 13. E3 execution admission checklist

Before any focused technical validation or model/configuration benchmark, the registered task must show all of the following:

- E2-005 independently task-verified, E2-006 passed, and the E2 stage gate independently verified;
- exact proposed/accepted ADR version and applicable frozen handback set;
- exact implementation/mechanism/configuration/host/client/support-class identity;
- prospective question, hard gate, fixture/oracle/fault schedule, success/failure/missing/unsupported classification and root-cause decision rule;
- accountable owner, independent challenger and verifier paths;
- `E3-QPA-001` finite verified ceiling policy bound before results;
- task/run budget, time, resource, network, credential, data and external-effect authorization;
- raw evidence retention, secret-safe handling, candidate/revision binding and stop conditions;
- zero claim beyond tested scope and a named E4/E5 remainder.

Failure of any admission item blocks execution. No E3 result can itself set `AUTONOMY_ELIGIBLE`; only independent E3 stage verification may do so, and a separate explicit founder decision is still required for `AUTONOMOUS_BUILD_AUTHORIZED`.
