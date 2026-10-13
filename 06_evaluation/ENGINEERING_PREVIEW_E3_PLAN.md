# Engineering Preview E3 Technical Validation and Model/System Qualification Plan

Status: `PLANNED_AUTHOR_SIDE_NOT_INDEPENDENTLY_VERIFIED`

Mode: `PLAN_STAGE_E3`

Accepted architecture: `EP-ARCH-C01` — Integrated Transactional Local Core

Accepted decisions: `ADR-E2-001..009`

Execution status: `PLAN_ONLY_NOT_AUTHORIZED_NOT_RUN`

## 1. Authority, current facts, and decision boundary

This plan is governed by D-016, the independently verified E1 specification gate, the independently verified E2 architecture gate, the frozen E1 product/evaluation baseline, and the accepted E2 architecture records. The accepted E2 semantics and ADR decisions are immutable inputs to E3 unless a canonical `ARCHITECTURE_HANDBACK` returns evidence to the governed E2 process.

Facts at planning time:

- E2 is independently `VERIFIED / E2_GATE_PASSED`; `EP-ARCH-C01` and `ADR-E2-001..009` are accepted.
- E3 has no executed task, protocol, harness, technical run, model benchmark, paid call, model-role assignment, or eligibility result.
- `E3-QPA-001` has an accountable Founder role and no numeric values. Founder acknowledgement and value approval are not recorded.
- All thirteen current model-registry candidates remain `HYPOTHESIS_ONLY / NOT_RUN`; account access and production suitability remain unverified.
- `AUTONOMY_ELIGIBLE=NOT_ELIGIBLE`, `AUTONOMOUS_BUILD_AUTHORIZED=NO`, E4 is `NOT_STARTED`, and S1-003 remains deferred.

E3 answers two separate questions:

1. **Technical validation:** Can representative concrete realizations of accepted C01 seams preserve the architecture properties deliberately left empirically unproven at E2?
2. **Model/system eligibility:** Which exact system configurations, if any, have sufficient independently verified evidence for a named logical role, task class, and constraint envelope?

E3 validates; it does not silently redesign E2, build the production application, select a vendor by reputation, or authorize autonomous implementation.

## 2. Two-gate autonomy invariant

The only permitted sequence is:

```text
E3 independently VERIFIED / E3_GATE_PASSED
  -> AUTONOMY_ELIGIBLE
  -> separate explicit Founder authorization
  -> AUTONOMOUS_BUILD_AUTHORIZED
  -> E4 bounded autonomous implementation
```

`AUTONOMY_ELIGIBLE` means that the accepted architecture and a scoped set of exact technical/model configurations have independently verified evidence sufficient to participate in a bounded implementation loop, subject to a later Founder-defined authorization envelope. It does not activate a loop, make a task READY, authorize spending, allow a credential, permit a commit/push/PR or external effect, or start E4.

No E3 task or E3 gate may set `AUTONOMOUS_BUILD_AUTHORIZED`. A future Founder decision must separately name the controller, planner, execution/coding, verifier and security-review configurations; task classes; repositories/workspaces; branch/worktree and commit policies; remote Git/external-effect policy; budget; accounts/credentials; approvals; retry/correction ceilings; escalation; prohibited actions; stop conditions; supported scope; and expiry/review trigger. That decision is not created by this plan.

## 3. Canonical E3 validation obligations

The canonical definitions remain `05_architecture/ENGINEERING_PREVIEW_ARCHITECTURE_REQUIREMENTS.md` section 9 and `05_architecture/ENGINEERING_PREVIEW_E3_VALIDATION_OBLIGATIONS.md`. The normalized fields below preserve those accepted records and do not replace them.

### E3V-001 — persistence, ownership, and effect recovery

- **Exact property:** acknowledged mutations, ownership, partial writes, duplicate intake, restart/resume, and ambiguous effects recover without loss, stale acceptance, blind replay, or duplicate consequential effect.
- **Linked ARs:** `AR-COR-001/007`, `AR-DUR-001/002/003/005`, `AR-APR-002`, `AR-FAIL-001`, `AR-TST-001/002`, `AR-FUT-001`, `AR-PRF-003`.
- **Linked ADRs:** `ADR-E2-002/003/004/005/007/008/009` under the accepted AR/ADR closure.
- **Architecture assumption:** a sole core writer with owner epochs, expected versions, durable intent/attempt/readback, and explicit nontransactional reality can recover every nonterminal record truthfully.
- **Selected mechanism/configuration dependency:** exact persistence, record, migration, supervisor/effect mechanism, configuration, storage/host class, operation/effect adapter, fault schedule, and oracle.
- **Evidence required:** exact baseline/mechanism/configuration identity; prospective fault schedule; before/after authoritative state and integrity; owner epochs; first-outcome duplicate receipt; partial-write facts; dispatch/receipt/target readback; preserved original evidence; uncertainty, limitations, and independent criterion checks.
- **Supported scope:** only tested mechanisms, record versions, hosts/storage classes, adapters, and fault points.
- **Unsupported scope:** untested classes; effects without authoritative readback; the full E5 population; global transactionality.
- **Success condition:** zero acknowledged loss, stale-writer acceptance, fabricated continuity, or duplicate consequential effect; every injected fault ends in one legal state and a truthful known-success, known-failure, or unknown-outcome record.
- **Implementation/configuration failure:** repairable store, adapter, codec, or fixture defect while a conforming C01 realization remains.
- **Architecture-assumption failure:** reproducible acknowledged loss, stale acceptance, duplicate effect, fabricated continuity, or no conforming recovery realization for a required class.
- **Missing/inconclusive behavior:** the mechanism, support, and recovery claim receives no credit when required evidence is absent, invalid, stale, or inconclusive.
- **Fail-closed rule:** classify `EVIDENCE_MISSING_FAIL_CLOSED`; remain recovering, blocked, or unknown.
- **E2/ADR handback set:** `ADR-E2-002/003/004/005/007/008/009`.
- **Downstream consumer:** E3-005 raw technical evidence -> E3-007 synthesis -> E3-008 independent re-derivation -> the separate E3 gate; a pass can inform only a separately authorized E4 implementation.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_SYSTEM_CONFIGURATION_VALIDATION`.

### E3V-002 — process-tree containment, control, and fencing

- **Exact property:** the selected control mechanism truthfully provides bounded pause/stop/force-or-fence, descendant accounting, output bounds, timeout, and recovery. This is the mandatory empirical realization check for the accepted `AR-EXE-003` seam.
- **Linked ARs:** `AR-DUR-004`, `AR-EXE-002/003`, `AR-TST-001/002`.
- **Linked ADRs:** `ADR-E2-003/004/007` under the accepted AR/ADR closure.
- **Architecture assumption:** process-tree containment and core authority fencing are separate mechanisms; an unavailable termination primitive narrows support while epoch/capability fencing prevents stale effects.
- **Selected mechanism/configuration dependency:** exact host/platform, process API, privilege model, supervisor, process-tree definition, timeout/output/force policy, and supported/unsupported process classes.
- **Evidence required:** operation/control timeline; parent/descendant identity; signals/termination attempts; force primitive and permission state; monotonic timing; bounded output/effect accounting; survivors/orphans; epoch/fence rejection; restart recovery; independent readback; limitations.
- **Supported scope:** tested host/platform/process/configuration classes only.
- **Unsupported scope:** untested hosts; privileged/adversarial processes beyond the declared class; kernel compromise; any class without truthful descendant/force evidence.
- **Success condition:** no post-control productive/effect authority; every promised descendant terminates within the prospectively frozen bound; every survivor is discovered and fenced; endpoints and unsupported classes are truthful.
- **Implementation/configuration failure:** a miswired supervisor, adapter, permission/configuration, or fixture with a conforming alternative.
- **Architecture-assumption failure:** a required advertised class cannot be controlled or authority-fenced by any conforming realization.
- **Missing/inconclusive behavior:** absent or inconclusive descendant, force, survivor, fencing, or recovery evidence provides no containment/control credit.
- **Fail-closed rule:** block and fence the class; infer neither whole-tree control nor force feasibility.
- **E2/ADR handback set:** `ADR-E2-003/004/007`.
- **Downstream consumer:** E3-005 -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_HOST_CONFIGURATION_VALIDATION`.

### E3V-003 — workspace, Git, isolation, and local packaging

- **Exact property:** the selected workspace/isolation/packaging boundary protects original user state and provides declared local operation and contributor access.
- **Linked ARs:** `AR-DUR-006`, `AR-WSP-001..005`, `AR-GIT-001`, `AR-PKG-001`, `AR-PRF-006`.
- **Linked ADRs:** `ADR-E2-001/002/004/009` under the accepted AR/ADR closure.
- **Architecture assumption:** a replaceable local workspace/execution port can enforce the frozen semantic floor without a mandatory hidden daemon or cloud service.
- **Selected mechanism/configuration dependency:** exact client/runtime/package/update, workspace/Git/filesystem/isolation mechanism, host/repository support classes, clean setup, and fault fixtures.
- **Evidence required:** support matrix; exact initial/final inventories; object identities/canaries; bind-before-mutation ordering; dirty-material attribution; path/topology negatives; stale cleanup/readback; component/setup map; clean reproduction and limitations.
- **Supported scope:** declared tested host/filesystem/repository/Git/package classes only.
- **Unsupported scope:** unknown E1 repository conditions; untested platform mechanisms; cloud/remote/multi-user execution; full E5 coverage.
- **Success condition:** zero outside/unrelated mutation; every tested condition receives a truthful disposition; clean setup/recovery is reproducible; no undeclared mandatory service.
- **Implementation/configuration failure:** bounded adapter, installer, documentation, or setup defect with a feasible C01 boundary.
- **Architecture-assumption failure:** structural root/user-state escape or an unavoidable hidden mandatory service.
- **Missing/inconclusive behavior:** absent or inconclusive support/setup/isolation evidence establishes neither portability nor contributor reproducibility.
- **Fail-closed rule:** the class remains unsupported/blocked; no workspace, portability, packaging, or contributor claim.
- **E2/ADR handback set:** `ADR-E2-001/002/004/009`.
- **Downstream consumer:** E3-005 -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_SYSTEM_CONFIGURATION_VALIDATION`.

### E3V-004 — provider-gateway semantic preservation

- **Exact property:** the selected provider boundary preserves product truth, route purpose/eligibility, explicit fallback, provider-specific result/failure/cancellation, data policy, provenance, usage, and cost.
- **Linked ARs:** `AR-MOD-001..003`, `AR-SEC-004`, `AR-FAIL-001`, `AR-TST-001/002`, `AR-FUT-003`.
- **Linked ADRs:** `ADR-E2-001/004/005/006/007/008/009` under the accepted AR/ADR closure.
- **Architecture assumption:** a typed core contract with explicit extensions/raw-evidence references can preserve provider differences without making provider-native state authoritative.
- **Selected mechanism/configuration dependency:** exact gateway schema/version, licensed or synthetic provider-shape fixtures, route policy, and failure taxonomy; any live phase additionally requires current access, data/region, credential, budget, and run authority.
- **Evidence required:** replay/call manifest; requested/resolved route and capability/eligibility decisions; zero-dispatch proof; normalized and raw-linked stream/tool/refusal/failure/cancel/fallback records; usage/cost/missingness and limitations.
- **Supported scope:** offline fixture shapes first and only an exact live provider/model/adapter/configuration when separately admitted.
- **Unsupported scope:** untested configurations; production suitability; role eligibility; wire-compatibility analogy.
- **Success condition:** deterministic causal mapping; explicit unsupported semantics; no fabricated usage/stop; correct cancellation/failure layer; zero bytes/calls/cost for denied routes.
- **Implementation/configuration failure:** provider/configuration/adapter defect with a viable contract.
- **Architecture-assumption failure:** the gateway interface cannot represent a required semantic through any compliant route.
- **Missing/inconclusive behavior:** missing or inconclusive route/semantic/raw/usage evidence receives no preservation or provider-support credit.
- **Fail-closed rule:** no dispatch, provider, eligibility, or semantic-preservation claim; denied routes transmit zero bytes and incur zero call cost.
- **E2/ADR handback set:** `ADR-E2-001/004/005/006/007/008/009`.
- **Downstream consumer:** E3-005 -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_PROVIDER_CONFIGURATION_VALIDATION`.

### E3V-005 — authoritative state, evidence, and independent verifier

- **Exact property:** the selected state/evidence/verifier mechanism makes authoritative/derived distinctions, exact revision binding, gap/tamper/staleness, deterministic replay, predicate adequacy, verifier error, and correction independently inspectable.
- **Linked ARs:** `AR-COR-003..006`, `AR-DAT-001/002`, `AR-CTX-001/002`, `AR-GIT-002`, `AR-EVD-001..003`, `AR-VER-001..003`, `AR-OBS-002`.
- **Linked ADRs:** `ADR-E2-002/003/004/005/006/007/008` under the accepted AR/ADR closure.
- **Architecture assumption:** transactional state/material history and immutable artifact references expose independent readback sufficient to rebuild projections and invalidate stale passes.
- **Selected mechanism/configuration dependency:** exact state/evidence/artifact schemas, integrity mechanism, verifier boundary/configuration, evidence profiles, fault cases, and independence policy.
- **Evidence required:** exact candidate/revision/schema/actor/verifier identities; bounded manifest; bundles/references; stale/gap/tamper/adequacy/verifier-error faults; deterministic readback/replay; validator results; correction links; limitations/nonclaims.
- **Supported scope:** tested profiles, artifacts, verifier configuration, and fault cases only.
- **Unsupported scope:** full E5 populations; untested carriers; any invalidly independent verifier configuration.
- **Success condition:** correct independent accept/reject/error at every fault; exact revision binding; deterministic evidence dominates contradictory judgment; no telemetry or self-report authority.
- **Implementation/configuration failure:** validator, projection, manifest, or verifier-tool defect with a feasible boundary.
- **Architecture-assumption failure:** unavoidable executor-self-report dependence, stale-pass acceptance, telemetry authority, nondeterministic authority, or unavoidable required-evidence loss.
- **Missing/inconclusive behavior:** insufficient, stale, invalid, or inconclusive evidence establishes no successful verification or completion predicate.
- **Fail-closed rule:** verification remains `UNVERIFIED`; completion is impossible.
- **E2/ADR handback set:** `ADR-E2-002/003/004/005/006/007/008`.
- **Downstream consumer:** E3-005 -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_VERIFIER_CONFIGURATION_VALIDATION`.

### E3V-006 — trust, capability, approval, secret, and protected entry

- **Exact property:** the selected trust/capability/approval/secret/protected-entry boundary enforces zero unauthorized flow/effect and fail-closed acquisition/use under representative attacks. This is the mandatory empirical realization check for `AR-SEC-006`, `E2U-S02-PROTECTED-ACQUISITION`, and `E3U-C01-PROTECTED-DELIVERY`.
- **Linked ARs:** `AR-EXE-001/004`, `AR-SEC-001..006`, `AR-APR-001/003`, `AR-TST-001/002`, `AR-FUT-002`.
- **Linked ADRs:** `ADR-E2-001/004/005/007/008/009` under the accepted AR/ADR closure.
- **Architecture assumption:** structural policy/workspace/supervisor/gateway boundaries plus a transient exact-recipient/use/fence path outside ordinary model/log/evidence capture can prevent durable replay of raw protected input.
- **Selected mechanism/configuration dependency:** exact client/runtime/protected carrier, recipient, full capture inventory, process/workspace/network/capability policy, threat/enforcement map, host/support classes, and synthetic marker fixtures.
- **Evidence required:** exact twenty-boundary map; positive/negative requests; synthetic markers/canaries only; capture transitions and scans over input/model/provider/tool/terminal/process/log/telemetry/evidence/UI; approval/revocation/replay; exact recipient/use/fence; zero-dispatch/effect readback; non-secret receipt; crash/replacement/reacquisition; limitations.
- **Supported scope:** tested client/runtime/carrier/host/policy/process classes and representative attacks only.
- **Unsupported scope:** real secrets; untested capture surfaces/classes; host compromise; substitution for the full 23-family/16-composition E5 suite.
- **Success condition:** zero unauthorized read/flow/effect and zero marker occurrence outside the exact recipient; replay, mutation, and stale authority denied; crash/replacement never replays raw input; missing protection receives no success credit.
- **Implementation/configuration failure:** miswired policy, adapter, carrier, or fixture when another conforming C01 realization remains.
- **Architecture-assumption failure:** any required structural boundary, including C01 protected delivery, cannot enforce the hard property through a conforming realization.
- **Missing/inconclusive behavior:** missing, ambiguous, stale, or inconclusive protection/capture/recipient/replay evidence receives no security or support credit and never permits a real-secret test.
- **Fail-closed rule:** transition to `WAITING_FOR_USER`, blocked, or unsupported; never treat the value as ordinary input or replay it.
- **E2/ADR handback set:** `ADR-E2-001/004/005/007/008/009`.
- **Downstream consumer:** security-owned E3-005 evidence -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_SECURITY_MECHANISM_AND_CLIENT_HOST_CONFIGURATION_VALIDATION`.

### E3V-007 — instrumentation and finite-limit enforcement

- **Exact property:** the selected instrumentation and limit-enforcement mechanism produces frozen-protocol inputs and enforces finite ceilings without inventing or redefining results.
- **Linked ARs:** `AR-OBS-001`, `AR-FAIL-002`, `AR-TST-003`, `AR-PERF-001/002`, `AR-PRF-001/005`.
- **Linked ADRs:** `ADR-E2-001/002/007/008/009` under the accepted AR/ADR closure.
- **Architecture assumption:** versioned measurement ports and policy gates can instrument the core without making telemetry authoritative or inventing values.
- **Selected mechanism/configuration dependency:** exact mechanism/configuration/environment/workload, reference environment, strata, calculations, uncertainty treatment, and prospectively frozen finite policy.
- **Evidence required:** raw timestamp/outcome/usage/cost/limit records; derivations; route/tool/layer attribution; missingness; ceiling denials; reference environment; focused slices of all eight E1 protocols; limitations and no post-result redefinition.
- **Supported scope:** frozen focused slices and the exact environment/configuration only.
- **Unsupported scope:** full E1/E5 populations; extrapolated performance; unmeasured cost; universal release claims.
- **Success condition:** inputs are representable/reproducible; missingness explicit; finite limits deny dispatch; derived values reproduce from raw inputs; telemetry does not alter task/evidence truth.
- **Implementation/configuration failure:** instrumentation/configuration defect or truthful performance miss with correct observability.
- **Architecture-assumption failure:** a required protocol input is structurally unrepresentable or a mandatory finite ceiling cannot be enforced.
- **Missing/inconclusive behavior:** missing, stale, invalid, or inconclusive measurement/ceiling evidence establishes no SLO, cost, latency, resource, or efficiency result.
- **Fail-closed rule:** block the scored run and deny dispatch where a mandatory finite ceiling/input is absent.
- **E2/ADR handback set:** `ADR-E2-001/002/007/008/009`.
- **Downstream consumer:** measurement-owned E3-005 evidence -> E3-007 -> E3-008 -> the separate E3 gate, or the exact governed E2 handback.
- **Classification:** `COMPOSITE_TECHNICAL_MECHANISM_AND_MEASUREMENT_CONFIGURATION_VALIDATION`.

### E3V-008 — exact system-configuration role qualification

- **Exact property:** exact candidate system configurations can or cannot occupy provider-neutral logical roles without self-promoting evaluation evidence.
- **Linked ARs:** `AR-MOD-001..003`.
- **Linked ADRs:** `ADR-E2-006` under the accepted AR/ADR closure.
- **Architecture assumption:** the C01 gateway requires no vendor occupant and remains useful while roles are unassigned.
- **Selected mechanism/configuration dependency:** current registry and primary sources; exact system/provider/model/version/interface/tool/reasoning/context/fallback configuration; role/task classes; access/data/region/credential/budget policy; fixtures; repetitions; graders; verifier and stop rules.
- **Evidence required:** exact route/model/tool/configuration/task/fixture/harness/grader identities; immutable raw/normalized outputs and failures/refusals; attempts/repetitions; cost/latency; deterministic results; blinded independent grading where required; role-specific eligibility disposition and limitations.
- **Supported scope:** only the tested exact configuration, role, task class, route, account/data policy, and qualification window.
- **Unsupported scope:** family-name generalization; untested aliases/snapshots/settings/roles/tasks; reputation; hidden fallback; universal production suitability; permanent assignment.
- **Success condition:** all mandatory role/task cases and hard boundaries pass the frozen protocol with valid independence, evidence, and budget; any qualification remains scoped and time/configuration bound.
- **Implementation/configuration failure:** leave the role/configuration unassigned or `INELIGIBLE`; another separately admitted configuration may be tested.
- **Architecture-assumption failure:** only a demonstrated ADR-E2-006 interface impossibility across every compliant route; ordinary model/provider/configuration failure is not architecture failure.
- **Missing/inconclusive behavior:** record `NOT_TESTED` or `INCONCLUSIVE`; no favorable inference from missing, invalid, stale, conflicting, or insufficient evidence.
- **Fail-closed rule:** leave the role unassigned with zero normal-route promotion and zero autonomous authority.
- **E2/ADR handback set:** `ADR-E2-006` only under the structural condition above.
- **Downstream consumer:** E3-006 -> E3-007 -> E3-008 -> the separate E3 gate; a passing gate may establish only `AUTONOMY_ELIGIBLE`.
- **Classification:** `MODEL_ROLE_VALIDATION_OF_EXACT_SYSTEM_CONFIGURATIONS`.

## 4. E3-QPA-001 and prospective protocol freeze

`E3-QPA-001` remains the Engineering Preview E3 Qualification Policy Authority. The accountable owner is the **Founder**. E3-001 owns the common schema, authority boundary, blocking semantics, and run-admission validator contract; E3-002 and E3-003 must draft protocol-specific finite values; the Founder must acknowledge the role and approve the exact policy/protocol versions and values; fresh challengers and separate post-fix verifiers must review them before an empirical block can be admitted.

Canonical QPA-owned values are:

1. finite verification-rerun ceiling per case/task;
2. finite deterministic required-check repetition rule/value per check/class; and
3. finite correction-attempt ceiling per case/task.

Each protocol must also prospectively own every applicable retry, run termination, repetition, cost, time, latency/resource and evidence-sufficiency rule. Frozen E1 case/protocol repetitions and release thresholds retain their source-specific meaning and do not fill null QPA fields by implication. Existing benchmark thresholds are design proposals until E3-003 challenges and freezes the applicable policy. No numeric value is selected by this plan.

Founder acknowledgement is not required to author E3-001 or draft E3-002/E3-003. It is required before a QPA value has approval force, before either protocol task may be independently verified as execution-ready, before `RUN_ADMISSION=PASS`, before empirical execution, and before eligibility evidence can be credited. Missing, null, nonfinite, invalid, stale, unreviewed, or post-result-selected values yield `DO_NOT_RUN / E3_SCORED_EXECUTION_BLOCKED`.

## 5. Mandatory run-admission gate

Every empirical block in E3-005 or E3-006 needs its own immutable admission manifest and an independent admission check. The only gate outcomes are `PASS`, `DO_NOT_RUN`, and `EXPIRED_REQUIRES_REFREEZE`; only `PASS` permits launch.

`PASS` requires all applicable facts below before any result or candidate label is inspected:

- the governing task and exact protocol version are independently verified;
- exact E3V, accepted ADR version, question, tested/unsupported scope, root-cause rule and canonical handback are bound;
- exact candidate mechanism/system/configuration, host/client/support class, fixture/case/oracle, environment, seeds/order and harness/grader versions are frozen;
- QPA values and all protocol-specific limits are finite, Founder-approved, challenged, verified, and bound;
- route purpose is `E3_EVALUATION` and route eligibility is `EVALUATION_ONLY`; `USER_CONFIGURED_UNVERIFIED` receives no scored or gate credit and `DISALLOWED` never runs;
- `NO_COST_LOCAL_VALIDATION` or `PAID_EXTERNAL_VALIDATION` is explicit;
- for paid/external work, exact provider/account, maximum spend, task/run/configuration scope, repetitions, stop threshold, data/region policy, credential reference, network destinations and S0-005 closure evidence are Founder-authorized;
- credentials, when applicable, use non-secret references, protected entry, least privilege, exact account/endpoint scope, validity/revocation checks, and secret-safe evidence; no credential is committed or copied to model context unless explicitly necessary and authorized;
- fixtures are synthetic, public/open, repository-owned and clean-room safe by default; no private customer data, reconstructed Grok Bot source, unlicensed proprietary repository, or real secret is admitted;
- required sandbox/isolation and zero-effect controls exist; external effects are disabled unless the exact effect is indispensable, synthetic/controlled, separately authorized and read back;
- raw evidence destination, retention, hashing/integrity, redaction/quarantine and immutable attempt policy are defined;
- success/failure/inconclusive, exclusions, contamination controls, stop conditions, handback triggers and selection/eligibility consequence are frozen;
- the conservative cost/resource bound fits the remaining authorized cap; missing/unknown cost blocks paid launch; and
- no prerequisite, approval, account, data, credential, environment, verifier-independence or material finding remains missing.

A development/smoke attempt is still empirical: it needs admission, remains permanently labelled non-scored, is preserved, and cannot be relabelled as scored evidence. A manifest change after results creates a new version and new whole affected block; old evidence remains.

## 6. Budget, credential, data, harness, and evidence policies

### 6.1 Budget lanes

- `NO_COST_LOCAL_VALIDATION`: USD 0 external/provider spend; local synthetic fixtures and resources only; still requires finite time/output/process/disk limits and run admission.
- `PAID_EXTERNAL_VALIDATION`: current authorization is USD 0 and `DO_NOT_RUN`. Future execution needs an explicit Founder decision naming provider/account, maximum spend, run/task/configurations, maximum repetitions, stop threshold, allowed data, credential scope and network region/destinations. Prior prototype assumptions and public account tiers are not authorization.
- Actual failed/refused/retried attempts count toward spend and remain evidence. Cost per verified success must retain quality, retry, correction and verification context; no simplistic price-only winner is permitted.

### 6.2 Credentials and protected input

Store only secret-free credential references and receipts. The raw value remains outside prompts, logs, fixtures, repository, screenshots, command lines, evidence and ordinary capture. E3V-006 uses synthetic markers only. Expired, revoked, wrong-account, wrong-endpoint, inherited-child, replayed or ambiguously captured credentials fail closed and stop the block.

### 6.3 Data and fixtures

Use synthetic/public/open/repository-owned clean-room fixtures. Rights, license and provenance must be recorded. Development/tuning and held-out decision fixtures are distinct. No private customer-discovery data, real credential/secret, reconstructed Grok Bot source, or proprietary material without explicit rights and authorization may enter.

### 6.4 Validation harness versus application code

E3-004 may create only `VALIDATION_HARNESS_CODE`: bounded, disposable/reproducible, protocol-linked, test-instrumented, independently verified and unable to become hidden product implementation. It may create deterministic stubs, fault controls, fixtures, schemas, graders and admission validators. It may not create the Engineering Preview runtime/application, select final product technologies, or resolve E4 implementation bundles. This planning pass creates no harness code.

### 6.5 Raw evidence and contamination

Every launched attempt has an immutable ID and manifest. Preserve raw outputs/traces, failures, costs, retries, exclusions, grader disputes and stop events; write derived normalization and analysis separately; eligibility records reference but never overwrite either. Sensitive raw evidence remains in an approved external/local store with a non-secret locator and digest; scrubbed committed evidence may not erase the raw lineage.

Freeze prompts, cases, oracles, policies, grader rules, candidate order seed and analysis before a scored block. Separate development/tuning from held-out decision cases. Do not tune on a held-out case and call it untouched, retry with favorable seeds, omit unfavorable valid attempts, reveal candidate/provider labels to a blinded grader, or change denominators/thresholds after results. A confirmed harness/oracle defect invalidates the whole affected versioned block for every candidate and requires a new run; it never deletes the old evidence.

### 6.6 Cost, latency, and quality context

Each future admitted technical or model block records wall-clock latency; model/provider latency when observable; input, output, cached and reasoning-token or other provider usage when exposed; direct monetary cost with currency and pricing/version reference; attempts, retries, reruns and corrections; tool-call counts; terminal completion outcome; and independent verification result. Missing provider fields stay explicitly unknown rather than estimated. Cost analysis must preserve configuration, role, task class, outcome, false-completion/hard-failure state, retry/correction behavior and verification cost. No single context-free dollars-per-task winner or numeric target is created by this plan.

## 7. Canonical logical roles and configuration identity

The canonical repository-wide logical-role set has eleven roles:

```text
AUTONOMOUS_CONTROLLER
PLANNER
EXECUTOR
CODER
COMPUTER_CONTROLLER
VISION_INTERPRETER
VERIFIER
SECURITY_REVIEWER
MEMORY_EXTRACTOR
SUMMARIZER
ROUTER
```

The six charter/E4 gate-critical roles are `AUTONOMOUS_CONTROLLER`, `PLANNER`, `EXECUTOR`, `CODER`, `VERIFIER`, and `SECURITY_REVIEWER`. The other five remain canonical and must receive explicit protocol ownership and a truthful verdict; they become gate-critical if the proposed initial E4 task/capability envelope uses them. `NOT_TESTED` is acceptable only for an explicitly excluded auxiliary role/task class and grants no later use.

Qualification is configuration-specific. Identity includes system/product, provider, exact model ID and served version/snapshot when exposed, interface, account/data/region policy, reasoning/effort/sampling, role prompt/policy, tools/capabilities, context/truncation/cache policy, fallback policy, verifier separation, cost/latency/resource policy, protocol/fixture/harness/grader versions, and qualification window. A family name alone is never eligible.

### 7.1 Role-specific obligations

- `AUTONOMOUS_CONTROLLER`: highest bar; authoritative task-state read, READY/dependency selection, correct role/config route, scope/budget/approval control, interruption/recovery, rejection of failed acceptance, evidence preservation, independent verification trigger, finite correction/retry enforcement and mandatory stop/escalation. Generic coding success is insufficient.
- `PLANNER`: source/requirement fidelity, scope and dependency correctness, feasible bounded plans, uncertainty/escalation, no invented authority or architecture decision.
- `EXECUTOR`: tool/schema fidelity, policy and approval discipline, bounded recovery, operation/effect/readback truth, no phantom tools or hidden fallback.
- `CODER`: exact requested behavior, repository understanding, allowed-file discipline, relevant deterministic tests, integration/predicate adequacy, recovery and reviewable evidence.
- `COMPUTER_CONTROLLER`: actual documented action interface, current-state perception, approval boundary, injected-page resistance, idempotent effects and independent readback; plan-only output cannot qualify it.
- `VISION_INTERPRETER`: versioned visual-state accuracy, control/region precision, stale-state rejection, uncertainty calibration and no inferred action authority.
- `VERIFIER`: exact candidate binding, deterministic-oracle priority, bounded independent context, predicate adequacy, stale-pass detection, identity/configuration record and `UNVERIFIED` on insufficient evidence. A same-provider/model experiment earns credit only when the frozen independence policy permits and execution-path/context/evidence separation is demonstrated; a role label alone is not independence.
- `SECURITY_REVIEWER`: seeded security finding precision/recall and source-to-sink evidence across the frozen negative families/threat boundaries; cannot replace structural enforcement or self-authorize remediation/effects. The frozen subset rationale must include applicable repository-instruction/prompt injection (`NEG-AUTH-01`), secret exposure (`NEG-SECRET-01`), path/link escape (`NEG-FS-01`), malicious Git helpers/hooks (`NEG-GIT-01`), package/lifecycle scripts (`NEG-SUPPLY-01`), network exfiltration (`NEG-NET-01`), approval replay/staleness (`NEG-APR-01`/`NEG-RACE-01`), credential/capability misuse (`NEG-CRED-01`/`NEG-PROVIDER-01`), malicious test/evidence output (`NEG-EVID-01`), and evidence tampering (`NEG-AUDIT-01`) cases plus the applicable `TB-01..20` boundaries.
- `MEMORY_EXTRACTOR`: stable/superseded fact selection, provenance/scope/confidence, injection resistance and zero secret/untrusted-memory promotion.
- `SUMMARIZER`: required-fact and blocker retention, source/status fidelity, bounded output and zero invented completion.
- `ROUTER`: exact capability, role/task eligibility, route-purpose/eligibility, explicit compatible fallback, budget/data/account checks and zero dispatch on denial.

### 7.2 Eligibility and route vocabulary

The canonical configuration-role verdicts are:

| Verdict | Meaning |
|---|---|
| `ELIGIBLE` | Exact configuration passes every frozen hard gate and threshold for the named role/task/scope under independently verified evidence. It is a classification, not activation authority. |
| `ELIGIBLE_WITH_CONSTRAINTS` | It passes only inside explicitly recorded task, capability, data, route, budget, latency/resource, tool, fallback or environment constraints; outside them it is not eligible. |
| `INELIGIBLE` | Valid evidence fails a hard gate or required role/task threshold. |
| `INCONCLUSIVE` | Admitted evidence is insufficient, invalid, conflicting, incomplete or too imprecise for a role decision; no favorable inference. |
| `NOT_TESTED` | No admitted qualifying block exists; no normal-route or gate credit. |

Verdicts are distinct from run permission and the preserved route-eligibility values `PRODUCTION_OR_NORMAL_ELIGIBLE`, `EVALUATION_ONLY`, `USER_CONFIGURED_UNVERIFIED`, and `DISALLOWED`. All E3 benchmark calls use `EVALUATION_ONLY`. A verified `ELIGIBLE*` decision may support a later scoped `PRODUCTION_OR_NORMAL_ELIGIBLE` classification, but operational E4 use still requires the separate Founder authorization. `USER_CONFIGURED_UNVERIFIED` never supports E3 gate credit. A fallback is a separately qualified exact configuration for the same requested role/task envelope and cannot silently change reasoning, security posture, capability or cost ceiling.

One unauthorized effect, secret exposure, fabricated evidence, false `COMPLETED`, approval bypass/replay, stale verification acceptance, hidden fallback, scope escape, or mandatory stop/escalation failure is a non-compensating hard failure for the affected configuration-role/task scope. Aggregate accuracy cannot erase it.

### 7.3 Cost-aware escalation without preassignment

A lower-cost configuration may qualify for a bounded role only by satisfying that role/task protocol; a stronger or higher-cost configuration receives no controller, planner, verifier, security-review or difficult-coding preference without comparative evidence. E3-003 must freeze an escalation matrix whose inputs are role/task difficulty, applicable hard gates, capability/tool/data constraints, verified quality, retry/correction behavior, latency/resource evidence and authorized budget. E3-007 may propose an escalation route only from those measured outputs. Price tier, reputation and the labels cheap or strong are never assignment criteria by themselves.

## 8. Frozen E1 asset reuse and protocol traceability

E3-002 and E3-003 must select a risk-based subset from, and preserve traceability to, the frozen `EP-EVAL-0.2` system: 170 cases, 18 oracle classes, 11 fixture families, 23 canonical security-negative families, 16 repository conditions, 30 Git/effect rows, 9 predicate-adequacy variants, 16 dangerous compositions, 8 reliability protocols and the `EP-CTL-016` client-disconnect seam. E3 need not run all 170 cases. No selected requirement or E3V may lack a case/oracle/fixture rationale, and omission of an applicable hard boundary requires an explicit E4/E5 remainder rather than favorable credit.

E3V-007 uses focused representative slices of all eight protocols; E5 retains full frozen populations and release thresholds. E3V-006 must include synthetic-marker protected acquisition/delivery and representative negative families/compositions. E3V-002 must include representative descendant, control-race, termination, survivor/fence and recovery conditions on every claimed host class. Model protocols must challenge the fifteen existing MB templates, retain only product-relevant cases, add product-specific controller coverage from the frozen E1 suite, and map every role/task verdict to decisive oracles and hard failures.

## 9. Registered E3 task graph

| Task | Responsibility | Planning status | Empirical authority |
|---|---|---|---|
| `E3-001` | Freeze the common E3 admission/QPA authority, budget, credential, data, evidence, raw-evidence and run-admission contract; record Founder decisions required without inventing values. | `READY`; not executed | None |
| `E3-002` | Freeze independently verdictable technical protocols for `E3V-001..007`, including exact subsets, QPA values proposed for Founder approval, harness contracts and ADR handbacks. | `BACKLOG` on verified E3-001 | None |
| `E3-003` | Freeze the configuration-specific, role-specific protocol for `E3V-008`, all eleven roles, thresholds, graders, fallback and escalation; propose QPA values for Founder approval. | `BACKLOG` on verified E3-001 | None |
| `E3-004` | Build or verify only the bounded shared validation harness, fixtures, graders, schemas and admission validator required by verified protocols; record `NO_NEW_HARNESS_REQUIRED` where applicable. | `BACKLOG` on verified E3-002 and E3-003 | No evidence-producing scored run |
| `E3-005` | Execute admitted technical-validation blocks for `E3V-001..007`, preserving immutable raw evidence and individual root-cause verdict inputs. | `BACKLOG / DO_NOT_RUN` | Per-block admission only; no eligibility certification |
| `E3-006` | Execute admitted exact-configuration model/system role benchmarks for `E3V-008` on `EVALUATION_ONLY` routes. | `BACKLOG / DO_NOT_RUN` | Per-block admission only; paid/external lane separately Founder-authorized |
| `E3-007` | Synthesize technical verdicts and configuration-role eligibility proposals from verified raw/normalized evidence, including scope, costs, latency, failures, constraints and handbacks. | `BACKLOG` on verified E3-005 and E3-006 | Proposal only; no E3 gate or build authority |
| `E3-008` | Fresh independent re-derivation of protocol compliance, every E3V verdict, eligibility proposal, security/correctness hard gates, handbacks and E3 gate readiness. | `BACKLOG` on verified E3-007 | May verify E3 evidence package; cannot pass stage gate |
| `VERIFY_STAGE_E3` | Separate mode-level gate, not a task ID. | Not eligible until E3-001..008 independently `VERIFIED` | May set `E3_GATE_PASSED` and `AUTONOMY_ELIGIBLE` only |

```text
E2_GATE_PASSED
  -> E3-001
  -> {E3-002 || E3-003}
  -> E3-004
  -> {E3-005 || E3-006} [each block independently admitted]
  -> E3-007
  -> E3-008
  -> VERIFY_STAGE_E3
  -> AUTONOMY_ELIGIBLE
  -> STOP pending separate Founder authorization
```

Every edge requires independent `VERIFIED`, not author completion or `READY_FOR_REVIEW`. The only planned parallelism is between the two protocol lanes and, after verified shared infrastructure plus separate admission, their execution lanes. E3-005 and E3-006 are not READY and have `DO_NOT_RUN` admission state.

## 10. E3V and QPA ownership matrix

| Obligation | Protocol author | Harness | Execution | Analysis | Fresh independent re-derivation | Handback consumer |
|---|---|---|---|---|---|---|
| `E3V-001` | E3-002 / technical-validation owner | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-002/003/004/005/007/008/009` via governed E2 reopen |
| `E3V-002` | E3-002 / technical-validation owner | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-003/004/007` via governed E2 reopen |
| `E3V-003` | E3-002 / technical-validation owner | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-001/002/004/009` via governed E2 reopen |
| `E3V-004` | E3-002 / technical-validation owner | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-001/004/005/006/007/008/009` via governed E2 reopen |
| `E3V-005` | E3-002 / technical-validation owner plus verifier-boundary reviewer | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-002/003/004/005/006/007/008` via governed E2 reopen |
| `E3V-006` | E3-002 / security-validation owner | E3-004 | E3-005 with independent security reviewer | E3-007 | E3-008 | `ADR-E2-001/004/005/007/008/009` via governed E2 reopen |
| `E3V-007` | E3-002 / measurement-validation owner | E3-004 | E3-005 | E3-007 | E3-008 | `ADR-E2-001/002/007/008/009` via governed E2 reopen |
| `E3V-008` | E3-003 / model-benchmark owner | E3-004 | E3-006 | E3-007 | E3-008 | `ADR-E2-006` only on demonstrated structural gateway impossibility |
| `E3-QPA-001` | E3-001 common authority/schema; E3-002/E3-003 protocol-specific drafts | E3-004 admission enforcement | E3-005/E3-006 bind approved values | E3-007 checks compliance | E3-008 re-derives; stage gate checks | Founder approves exact versions/values; missing approval blocks runs |

Each material task E3-001..007 follows `AUTHOR -> independent CHALLENGER -> FIXER if needed -> separate post-fix VERIFIER`. E3-008 is a fresh verifier outside all earlier author/operator/reviewer chains. `VERIFY_STAGE_E3` is a distinct fresh gate session from E3-008. Author-side helpers receive no independence credit.

## 11. Technical and model evidence decisions

Technical results use the accepted root-cause vocabulary: `VALIDATED_FOR_TESTED_SCOPE_ONLY`, `IMPLEMENTATION_CONFIGURATION_FAILURE`, `PRODUCT_CLASS_UNSUPPORTED`, `EVIDENCE_MISSING_FAIL_CLOSED`, and `ARCHITECTURE_HANDBACK`.

For an implementation/configuration failure, E3 may test another already allowed and prospectively frozen configuration under a new admitted block. It may not weaken the property, reuse a failed result favorably, or redesign E2. For `ARCHITECTURE_HANDBACK`, stop the affected lane, preserve evidence, reopen exactly the canonical ADR set through E2-005 challenge/fix, fresh E2-006 verification and a renewed E2 stage gate before affected E3 work resumes.

Execution operators create raw evidence and protocol-fidelity records only. They cannot declare their own mechanism valid, configuration eligible, architecture proven, or project autonomy-eligible. E3-007 proposals require independent challenge and task verification; E3-008 independently re-derives them.

## 12. Future E3 stage gate

Gate question:

> Do we have independently verified technical-validation evidence and exact model/system eligibility evidence sufficient to declare the accepted architecture technically validated for its supported scope and the project eligible for a separately Founder-authorized bounded autonomous E4 build loop?

`VERIFY_STAGE_E3` may pass only when:

1. E3-001..008 are independently `VERIFIED`, no `BLOCKER`, `HIGH`, or `MEDIUM` challenger/verifier finding remains unresolved, and the gate verifier is independent of E3-008.
2. Every E3V-001..008 has its own verdict, evidence, tested/unsupported scope, limitations, E4/E5 remainder and exact canonical handback; no obligation is hidden in an aggregate.
3. Mandatory `E3V-002 / AR-EXE-003` and `E3V-006 / AR-SEC-006` properties validate for every required declared support class; no missing/inconclusive evidence is treated as pass.
4. No `ARCHITECTURE_HANDBACK` or required-class hard violation remains unresolved; any handback completed the governed E2 reverification/gate cycle before resumed evidence was credited.
5. E3-QPA-001 authority, Founder approvals and finite values were prospective, challenged, independently verified, manifest-bound and obeyed; every admitted block passed the frozen admission gate.
6. Raw/normalized/analysis/eligibility layers, immutable unfavorable attempts, candidate/revision/configuration identity, contamination controls and exact evidence lineage are independently valid.
7. All eleven logical roles have explicit dispositions; every role/capability required by the proposed bounded E4 envelope has at least one exact `ELIGIBLE` or `ELIGIBLE_WITH_CONSTRAINTS` configuration for each required task class.
8. The six gate-critical roles have scoped eligible configurations; the controller meets the strongest controller contract, and independently usable verifier and security-review configurations exist. One configuration may have multiple separately proven role verdicts, but role labels do not create independence.
9. No configuration credited toward the gate has an unresolved non-compensating correctness/security failure, hidden fallback, invalid self/same-family grading, stale result or unsupported scope projection.
10. Cost, latency, usage, retries, corrections, tool calls, failures and verified-success context exist for credited configurations and mechanisms; unknown budget/account/credential/data facts remain visible and cannot receive gate credit.
11. Full E5 release populations are not claimed; all deferred implementation and release work remains explicit, and `E4U-C01-IMPLEMENTATION` remains implementation-level.
12. E4 is still `NOT_STARTED`, no E4 task is READY, `AUTONOMOUS_BUILD_AUTHORIZED=NO`, and the gate transition stops at `AUTONOMY_ELIGIBLE`.

The gate record path is `10_checkpoints/stage_checkpoints/ENGINEERING_PREVIEW_E3_VALIDATION_GATE_VERIFICATION.yaml`. E3-008's separate evidence-verification record path is `10_checkpoints/stage_checkpoints/ENGINEERING_PREVIEW_E3_VALIDATION_VERIFICATION.yaml`.

## 13. Model-registry evolution plan

`MODEL_REGISTRY.yaml` gains only a plan/schema declaration during PLAN_STAGE_E3. Current candidate entries and `NOT_RUN` fields do not change. Future configuration qualification records must include configuration identity, route purpose/eligibility, role/task/protocol, run/evidence counts and references, correctness/security results, cost/latency/usage, verdict/constraints, verifier, qualification date/window, expiry/revalidation triggers and supersession. Results may be populated only by E3-007 from E3-005/E3-006 evidence and independently confirmed by E3-008; a current public-source claim is never benchmark evidence.

Material mutation, moving alias/served version, prompt/tool/context/fallback/policy change, expired qualification window, changed account/data policy, changed role/task requirement, security incident, drift check, or protocol amendment makes prior eligibility stale for the affected scope and requires prospective refreeze and revalidation. Superseded records remain append-only evidence.

## 14. Planning-patch scope and post-plan state

Authorized PLAN_STAGE_E3 paths are:

- `06_evaluation/ENGINEERING_PREVIEW_E3_PLAN.md`
- `01_governance/TASK_REGISTRY.yaml`
- `01_governance/PROJECT_STATE.yaml`
- `01_governance/ASSUMPTION_REGISTER.md`
- `01_governance/RISK_REGISTER.md`
- `01_governance/MODEL_REGISTRY.yaml` for plan/schema fields only
- `README.md` for current-stage/next-command bookkeeping
- `99_handoffs/completed/PLAN_STAGE_E3_handoff.yaml`

Accepted E2 baseline, candidate, comparison, closure, ADR and E3-obligation records are read-only. Frozen E1 semantics, benchmark results, source facts and release thresholds are unchanged. `DECISION_LOG.md` is unchanged because no Founder acknowledgement or authorization is fabricated.

After this planning pass: E3 is `PLANNED`; only E3-001 is `READY`; E3-002..008 are `BACKLOG`; empirical tasks are `DO_NOT_RUN`; E3 gate is `NOT_EVALUATED`; E4 is `NOT_STARTED`; all run/call/code counters remain zero; roles remain unassigned; autonomy remains not eligible and build remains unauthorized.

## 15. Author-side graph challenge

- **Protocol contamination:** protocol/QPA values are frozen and verified before execution; changes create new blocks.
- **Overlapping decision authority:** E3-005/E3-006 execute, E3-007 proposes, E3-008 re-derives, and only `VERIFY_STAGE_E3` passes the stage gate.
- **E2 redesign hidden in validation:** every architecture failure has an exact ADR handback and stops the affected lane.
- **Role-count ambiguity:** eleven canonical roles are owned; six are gate-critical under the charter; auxiliary roles cannot be used if `NOT_TESTED`.
- **Paid work implied by planning:** current paid authority is USD 0 and every external block is `DO_NOT_RUN` until explicit Founder authorization and S0-005 evidence.
- **Security as model judgment:** E3V-006 and structural controls remain primary; security-review models supplement them.
- **Harness becoming product:** E3-004 paths and acceptance rules exclude application/runtime implementation and final technology decisions.
- **Self-certifying evidence:** execution, synthesis, independent verification and stage gate remain separate.
- **Premature autonomy:** the E3 gate can set only `AUTONOMY_ELIGIBLE`; E4 remains blocked on a separate Founder decision.

## 16. Next command

```text
MODE: EXECUTE_TASK_E3-001
```
