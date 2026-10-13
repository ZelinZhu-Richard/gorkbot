# E3 technical-validation harness contract

Status: E3-002 FIXER DRAFT — READY_FOR_POST-FIX VERIFICATION; NOT VERIFIED; NOT EXECUTION-READY

Authority: `E3_TECHNICAL_VALIDATION_PROTOCOLS.yaml`, `E3-QPA-POLICY-001`, the accepted
EP-ARCH-C01 baseline and ADR-E2-001..009, and frozen E1 suite `EP-EVAL-0.2`.

This document is a technology-neutral input contract for future task E3-004. It is not harness
code, a harness design selection, a mechanism selection, a run manifest, a run admission, an
architecture result, or empirical evidence. E3-004 must independently choose and verify bounded
validation-only implementations without hiding product/application behavior in the harness.

## 1. Non-authorizations

This contract authorizes none of the following:

- application, client, core, provider, workspace, secret-broker, or process-supervisor code;
- validation-harness implementation or execution;
- a process-containment, persistence, isolation, provider, protected-carrier, or evidence technology;
- a real provider call, network action, paid action, account or credential check, destructive effect,
  real secret, private data, or user workload;
- a QPA value, protocol/resource ceiling, support-class claim, run-admission `PASS`, E3V result,
  mechanism qualification, model/role assignment, eligibility verdict, architecture handback,
  `AUTONOMY_ELIGIBLE`, `AUTONOMOUS_BUILD_AUTHORIZED`, or E4 work.

Current admission is `DO_NOT_RUN`. Every authoritative QPA and protocol-limit value remains `null`
and `FOUNDER_DECISION_REQUIRED`. E3-002 now supplies the non-authoritative author proposal
`E3-002-QPA-PROP-001` (1 same-revision verification-error rerun, exactly 3 ordered invocations per
applicable deterministic check, and 2 material corrections after the initial block). Founder review,
any required fresh challenge, and separate verification remain pending; the proposal authorizes nothing.

## 2. Trust and responsibility boundaries

The future harness must keep these responsibilities separate and version-bound:

| Responsibility | May do | Must not do |
|---|---|---|
| Subject adapter | Invoke the exact admitted mechanism/configuration and expose declared observations. | Select its own oracle, rewrite expected results, self-admit, or self-verify. |
| Fixture controller | Create only frozen synthetic, repository-owned, public/open-with-rights, or clean-room inputs and inject frozen faults. | Use real secrets/private data, mutate user state, or change a fixture after result inspection. |
| Observer | Capture independently observable state, process, filesystem, Git, route, effect, resource, and marker facts at declared boundaries. | Treat missing capture as clean, infer unobservable facts, or become product authority. |
| Deterministic oracle | Compare captured facts with frozen expected state and invariant rules. | Accept narration, telemetry, schema validity, or a digest as semantic proof. |
| Residual grader | Judge only a prospectively declared semantic residue with bounded inputs. | Override a deterministic failure or see candidate labels/private author reasoning. |
| Raw evidence writer | Append the exact admitted attempt record and complete unfavorable history. | Overwrite, delete, redact silently, derive eligibility, or share a raw locator with analysis. |
| Analyzer | Recompute the frozen per-protocol disposition from immutable raw records. | Invent missing values, change exclusions/denominators, or collapse E3V verdicts. |
| Admission checker | Resolve current governance and issue only the policy's three outcomes. | Be the operator/author, accept null QPA/limits, or use schema validity as `PASS`. |
| Independent verifier | Re-run/read back frozen predicates on the exact subject. | Mutate the subject, fix findings, or rely on the operator's conclusion. |

The subject under test and its oracle cannot share an unverified authority source. A product record
may be observed as the subject claim, but a harness-held canary, controlled target, external
readback, process inventory, exact repository/Git snapshot, or independently reconstructed state
must decide the claim.

## 3. Required E3-004 deliverable boundary

E3-004 may create only validation-harness code and versioned fixtures needed to instantiate these
protocols. Its complete implementation inventory must prove that no path is imported by or packaged
as the production application, and no validation double silently satisfies an application
requirement. E3-004 must end with its own author, fresh challenger, bounded fixer if needed, and
separate verifier lifecycle before any empirical block can be admitted.

After E3-002 and E3-003 protocol-criteria Phase A verification, E3-004 may implement this parameterized
contract without an exact execution manifest, selected production mechanism, approved QPA number, or
empirical protocol result. At minimum E3-004 must produce independently verifiable contracts for:

1. strict manifest parsing plus current semantic admission verification;
2. immutable block, attempt, case, fixture, oracle, fault, seed/order, environment, and configuration identity;
3. synthetic fixture creation, canary placement, deterministic fault injection, and safe teardown;
4. independent state/readback, repository/Git, process-tree, effect-sink, route, resource, and marker observers;
5. deterministic oracle execution and bounded residual grading;
6. separate append-only raw, versioned derived, and eligibility-decision destinations;
7. complete attempt indexing, QPA/limit reservation, single-use launch consumption, stop/fence,
   evidence quarantine, and post-record readback required by `E3-QPA-POLICY-001`;
8. replay and independent recomputation without a subject process, provider, model, or external network;
9. an implementation inventory and denylist proving absence of application code and hidden product functionality.

No harness component may authorize a run merely because it exists or passes its own tests.

## 4. Common harness capability matrix

| Capability | E3V-001 | E3V-002 | E3V-003 | E3V-004 | E3V-005 | E3V-006 | E3V-007 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Authoritative state/version/owner readback | required | required | required | route state | required | authority state | required |
| Deterministic fault scheduler | required | required | required | required | required | required | required |
| Filesystem/repository/Git canaries | required | as applicable | required | not primary | revision binding | required | as applicable |
| Controlled local effect sink | required | required | as applicable | zero-call/offline | as applicable | required | as applicable |
| Process-tree/resource observer | as applicable | required | helper detection | bounded adapter | verifier process | required | required |
| Offline provider-shape replayer | not primary | not primary | forbidden network | required | provenance only | malicious-shape negative | missingness shape |
| Evidence gap/tamper/revision canaries | required | required | required | required | required | required | required |
| Synthetic-marker surface capture | negative | negative | path surfaces | request/response surfaces | evidence surfaces | required complete inventory | evidence/audit surfaces |
| Independent metric recomputation | recovery facts | control facts | mutation facts | route facts | verifier facts | security facts | required all protocols |

“Required” means the capability must be present in the later exact verified harness configuration;
it does not select how it is implemented.

## 5. Fixture contract

Every fixture set must be immutable, versioned, rights/provenance reviewed, and bound before results.
It must declare:

- fixture ID/version/digest and exact source class;
- creator, rights/license, region, retention, privacy, and training-use facts;
- exact initial state, canaries, allowed mutation/effect surface, and forbidden surfaces;
- variant IDs, expected event/fault boundary, expected result, and decisive oracle;
- deterministic seed/order or an explicit unresolved value that blocks admission;
- setup, readback, quarantine, retention, and safe teardown contract;
- a proof that teardown cannot touch original, unrelated, user, shared, or unknown material.

The frozen E1 fixture registry is used by reference. E3-004 may instantiate it, but may not weaken
its expected outcomes or treat an unavailable fixture as `PASS`. A material fixture defect
independently confirmed after execution invalidates the whole affected block and requires a new
fixture/protocol version and block; prior evidence stays preserved.

E3V-002 fixtures are safe synthetic task-owned descendants only. E3V-006 fixtures use unique
synthetic markers only. E3V-004 uses licensed/synthetic offline provider shapes and a zero-call sink.

## 6. Fault injection and scheduling

The future scheduler must freeze the complete matrix before any result is available. Each scheduled
cell binds the exact protocol/configuration/support class, case/variant, fixture, fault boundary,
operation order, seed/order, oracle, QPA assignment, all protocol limits, and evidence destination.

Fault injection must be observable independently both immediately before and after the boundary.
A reported injection without a harness-held boundary witness is inconclusive. The scheduler must not:

- repeat only failures or rerun favorable seeds;
- change placement/order after observing results;
- reset QPA, retry, correction, or limit ledgers with a new ID/version;
- inject a real destructive, provider, credential, network, or user workload;
- continue productive dispatch after a hard failure or exhausted frozen limit.

## 7. E3V-002 containment and fencing capability

The E3-004 implementation for E3V-002 must expose, without selecting the production mechanism:

- exact host family/version/architecture/security posture and declared privilege class;
- task-owned parent, child, and grandchild identities and ownership/fence binding;
- cooperative and uncooperative synthetic workloads, including output pressure and effect-boundary variants;
- durable pause, stop, timeout, cancel, force/fence, redirect, resume, and owner-loss timelines;
- independent actual process/descendant/resource/effect observation;
- survivor/orphan discovery after immediate-parent loss and supervisor/owner recovery;
- separate facts for “process terminated,” “descendant contained,” and “stale authority fenced”;
- host restart only where the exact support class claims it, plus explicit unsupported-host denial;
- zero real-user/destructive workload and no inferred container/VM security claim.

A surviving descendant is not automatically a failure if the frozen support contract explicitly
allows a survivor and the harness proves it has no productive, repository, effect, credential,
network, or authority path. Conversely, process death does not prove fencing. Missing descendant or
actual-state observation is fail-closed. `EP-CTL-016` must prove that a client disconnect does not
fabricate execution-owner loss or recovery.

## 8. E3V-006 protected-entry capability

The E3-004 implementation for E3V-006 must create a protected boundary that ordinary manifests and
subject code cannot select or dereference. Before a run it must bind the exact client, host, carrier,
protected store reference/broker, runtime recipient, operation/use, attempt, owner epoch, fence,
approval/revocation state, one-use rule, and capture inventory.

The mandatory capture inventory includes:

- ordinary chat input/transcript and user-visible summaries;
- repository, worktree, diff, artifact, evidence, and repository-local temp/cache paths;
- every operating-system or user temp root writable by the subject process tree;
- runtime, framework, dependency, tool, and package-manager temp/cache/log/state roots writable by it;
- application-support, cache, preference, session, autosave, local-database, and persistence roots writable by it;
- user-home dotfiles plus tool configuration and state paths writable or updated by it;
- crash reports, core dumps, minidumps, diagnostics, profiles, and debug bundles it can cause to be emitted;
- filesystem-backed spool, queue, socket metadata, lock, and interprocess-transfer paths writable by it;
- shell, terminal, editor, and tool history/transcript/recovery/session paths it can update;
- generated prompts/context packets before model dispatch;
- serialized model/provider requests and controlled responses at the adapter boundary;
- every tool argument/result and dispatched/received environment value;
- terminal stdin/stdout/stderr;
- parent/descendant argv, environment, output, exception, and stack surfaces;
- intermediate traces/events, logs, telemetry, audit, and evidence records;
- approval, summary, UI, notification, accessibility, screenshot, and clipboard surfaces;
- controlled network payloads at the local interceptor; and
- the exact protected recipient boundary.

The filesystem portion is the exact frozen subject-process-tree writable view, not a repository-only
list. Before generating a marker, E3-004 must inventory the effective user/group, sandbox/container,
mount namespace, path configuration, crash/diagnostic policy, and observed create/write/rename/link/
delete targets. It must enumerate each writable or causally emitted path class or independently prove
that the exact process tree cannot write it. A sandbox may reduce the inventory only when E3-004
verifies both the scanned roots and enforced denial of writes elsewhere. Deleted or rotated content
requires write-time observation sufficient for the marker oracle.

An unobservable, unbounded, or incompletely scanned relevant writable class yields
`PRODUCT_CLASS_UNSUPPORTED` or `EVIDENCE_MISSING_FAIL_CLOSED`; it cannot support a leakage-absence
claim. A favorable result is limited to the exact frozen client/host/runtime/process tree and complete
inventory. It does not claim coverage of swap, hibernation, hypervisor, firmware, proprietary
vendor-internal, or other surfaces outside the prospectively declared observable boundary.

The marker may be present only inside the exact protected recipient boundary under its frozen
expected-presence rule. Any raw marker on an unauthorized surface is a hard failure. Any missing,
late, truncated, reordered, or unscanned mandatory capture is `EVIDENCE_MISSING_FAIL_CLOSED`; final
logs cannot establish cleanliness. Ordinary records may retain only a non-secret opaque receipt and
safe incident facts—never the marker, a reversible encoding, low-entropy digest, content-derived
correlation value, protected locator, or access handle.

Wrong recipient/use/attempt/owner/fence, stale or revoked approval, replay, alias/symlink swap,
crash ambiguity, and replacement-runtime reuse must deny. Replacement requires fresh protected
reacquisition. If protected delivery is unavailable, the subject must enter `WAITING_FOR_USER` or
`BLOCKED`, never success. Any marker incident stops/fences the affected lane, retires the marker,
quarantines protected evidence, and requires independent security root-cause review before a new block.

## 9. Oracle implementation rules

The 18 frozen E1 oracle IDs are all represented by the seven protocols. E3-004 must bind each oracle
to a versioned implementation and a deterministic applicability rule. For every oracle it must state:

- authoritative inputs and exact observation boundary;
- comparison/decision algorithm and expected output vocabulary;
- known blind spots and what it cannot prove;
- missing, malformed, stale, conflicting, or unavailable-input behavior;
- independence from the subject and from any residual grader;
- immutable raw output plus recomputation method.

`OR-BOUNDED-RUBRIC` is never allowed to override deterministic ground truth. `OR-METRIC-PROTOCOL`
validates frozen populations, numerators, denominators, exclusions, missingness, uncertainty, and
amendments; it does not decide semantic correctness. `OR-SECRET-MARKER` proves only the frozen marker
and observable surfaces, not detection of every real secret or proprietary provider internals.

## 10. Evidence and integrity contract

The future harness must allocate three physically/logically separate non-secret locators:

1. `RAW_RUN_EVIDENCE`: operator append-only and immutable;
2. `DERIVED_ANALYSIS`: analyzer-versioned and immutable; and
3. `ELIGIBILITY_DECISION`: eligibility-authority-versioned and immutable.

The storage, sealing, digest, and locator technologies remain E3-004 choices subject to independent
review. Whatever is selected must implement the manifest-global integrity profile, append-only attempt
index, complete unfavorable history, independent seal/readback, retention, redaction, and quarantine
rules from E3-001. A raw and derived locator cannot be the same. An amendment appends; it never
rewrites. An evidence bundle schema pass is necessary but never sufficient for a protocol pass.

Each raw attempt must make these facts reconstructable without the subject narrative:

- exact task/block/run/attempt, operator, authority, admission decision, and launch receipt;
- exact E3V/protocol/harness/configuration/environment/host/client/support scope;
- case, fixture, oracle, composition, fault, seed/order, and expected outcome;
- all operations, controls, descendants, effects, approvals, readbacks, timestamps, and outcomes;
- all QPA/limit reservations and consumption, resource usage, cost, stop reason, and safety reserve;
- every evidence locator, integrity status, gap/tamper/secret finding, contamination class, and amendment;
- independent analyzer/verifier identity, inputs, disposition, root-cause record, and reviewed subject.

## 11. Cross-protocol sequencing and evidence reuse

E3-004 verification is a prerequisite for all empirical work. Within a future admitted execution
portfolio, these safety dependencies apply:

- E3-004 must first verify E3V-003-required harness isolation controls before any mutating fixture;
  an empirical E3V-003 verdict is not its own or another protocol's prerequisite.
- E3-004 must first verify E3V-002-required descendant discovery/control/fencing controls before any
  descendant-spawning fixture; an empirical E3V-002 verdict is not a prerequisite.
- E3-004 must first verify E3V-006-required marker/capture controls before any marker fixture; an
  empirical E3V-006 verdict is not a prerequisite.
- E3V-005 is the evidence-credit gate for all affected protocol results; it is itself judged with
  harness-held canaries and state/readback to avoid circular self-validation.
- E3V-007 may recompute metrics from applicable immutable records only after integrity and
  contamination checks; synthetic protocol-shaped inputs may test all eight E1 protocol shapes
  without running or claiming E3V-008.

One raw attempt may support several derived analyses only if every exact applicability dimension
matches. The attempt is indexed once and cannot be counted twice. Each E3V receives a separate
root-cause disposition; a pass in one never compensates for another's failure or missing evidence.
The prospective DAG is: verified E3-002/E3-003 Phase A criteria -> E3-004 build and verification ->
Phase B execution-block binding and verification -> E3-005 per-launch admission -> admitted protocol
attempt -> integrity-gated synthesis. It contains no empirical protocol self-dependency.

## 12. Stop, contamination, and amendment behavior

Every common or protocol-specific hard failure immediately:

1. prevents new productive dispatch;
2. terminates or fences reachable authority;
3. preserves and quarantines raw evidence;
4. records a truthful noncomplete state and affected tuple;
5. permits only the separately bounded safety/control/readback/evidence reserve; and
6. requests an independent root-cause investigation.

Development, smoke, and scored partitions remain distinct. Candidate labels, held-out bytes, expected
results, and grader/private fixtures remain unavailable to tuning. Favorable retry/rerun, selective
omission, post-result threshold/exclusion/denominator/order change, pass-only reporting, and
development-to-scored relabeling are prohibited.

Material change creates a new version, whole affected block, single-use manifest, fresh admission,
and preserved prior evidence. A harness defect independently confirmed after a run invalidates the
whole affected block; the fix cannot rescue the old result.

## 13. Architecture-failure and handback behavior

An ordinary subject, fixture, adapter, harness, observer, oracle, configuration, host, or evidence
failure is not automatically an architecture handback—or automatically a configuration failure.
`IMPLEMENTATION_CONFIGURATION_FAILURE` requires reproducible localization to the exact realization
and at least one concrete, prospectively identified, materially distinct candidate that the accepted
architecture admits for the same property and scope. Mere plausibility is insufficient.

Candidate identities form a finite prospective envelope. Material distinction requires a different
property-relevant enforcement, authority, capture, observation, or recovery primitive; renaming,
repackaging, prompt-only changes, and trivial configuration variants remain one cumulative correction
lineage. When the envelope or Founder-approved correction ceiling is exhausted, or no concrete
alternative exists, the lane stops for mandatory independent architecture classification. Insufficient
evidence is `EVIDENCE_MISSING_FAIL_CLOSED`, not indefinite retry.

`ARCHITECTURE_HANDBACK` is reachable when a separate independent investigation and verification use
the preserved exact fault chain to disprove a named accepted architecture assumption, or show that an
indispensable accepted property cannot be satisfied in the architecture's claimed design envelope for
the exact tested support class. It does not require enumerating every imaginable implementation or
mathematical proof over future technology. The record must bind the protocol's set-equal canonical ADR
set. E3 does not edit an ADR: it stops the lane and returns through governed E2 challenge/fix, fresh
architecture verification, and a renewed E2 gate before a new E3 freeze.

For the unchanged E3-001 manifest binding named
`all_compliant_route_exhaustion_and_structural_impossibility_predicate`, “all compliant routes” means
the exact prospectively frozen materially distinct finite envelope for the same property and support
scope. It is not permission for an unbounded implementation search. A separately verified named
assumption disproof or required-property impossibility inside the claimed design envelope can establish
the structural predicate without executing nominal variants; finite-envelope exhaustion alone still
requires independent classification and is not automatic handback.

## 14. Two-phase freeze and E3-004 input contract

`PHASE_A_PROTOCOL_CRITERIA_FROZEN_HARNESS_IMPLEMENTABLE` requires both E3-002 and E3-003 to be
independently `VERIFIED` for their questions, fixtures, observations, oracle/outcome semantics, hard
failures, support/evidence/handback contracts, QPA binding points, and parameterized mechanism metadata.
Phase A is sufficient for E3-004 implementation. It does not require an exact harness digest, selected
mechanism, Founder-approved QPA values, final runtime/resource limits, a closed execution manifest,
admission, or execution readiness.

E3-004 therefore builds and independently verifies strict schemas and enforcement interfaces using
explicit non-authoritative test fixtures for QPA/limit fields. Test fixture numbers cannot become
approved E3-QPA-001 values. E3-004 remains `BACKLOG` until E3-002 and E3-003 Phase A verification; it
then implements validation-only code and still creates no scored protocol evidence.

Only after E3-004 is independently `VERIFIED` may
`PHASE_B_EXECUTION_BLOCK_FROZEN_EXECUTION_READINESS_CANDIDATE` bind:

- the exact current protocol and harness versions/digests;
- one exact prospectively reviewed mechanism/configuration/environment/support class from the finite
  candidate envelope;
- Founder-approved, freshly challenged where required, and separately verified E3-QPA-001 values;
- exact fixtures, selectors/order/seeds, oracle implementations, evidence destinations, and every
  retry/repetition/repeated-failure/time/output/process/disk/network/cost limit; and
- all current authorities plus a complete immutable execution block.

The registered E3-005 prelaunch execution-block preparer, acting for the accountable validation owner
and distinct from the run operator/admission checker, owns this exact Phase B binding. The Phase B
candidate requires independent verification before any launch; it is still not admission by itself.

E3-004 acceptance must include strict parsing, selector resolution, fixture/oracle negative tests,
subject-oracle separation, admission bypass tests, process and protected-entry specialist review,
evidence/integrity replay, contamination tests, allowed-path and no-application-code proof, and a
fresh independent verifier. It may not produce accepted scored/candidate evidence while building or
verifying the harness.

## 15. E3-005 input contract

E3-005 remains `BACKLOG` / `DO_NOT_RUN`. Each future technical-validation block requires all of:

- E3-001, E3-002 Phase A/Phase B, E3-003 Phase A, and E3-004 exact current independent verification references;
- exact protocol/configuration/support/fixture/oracle/fault/environment identities and digests;
- Founder-approved, challenged, and verified QPA values plus all finite protocol limits;
- exact no-cost or separately authorized paid lane, budget, account, credential, data, region,
  retention, network, effect, isolation, security, and evidence facts;
- one fresh immutable closed manifest and independent semantic `RUN_ADMISSION=PASS`;
- one single-use launch reservation consumed atomically before process start;
- no drift, contamination, prior hard failure, unresolved handback, or missing current authority.

Protocol verification is necessary but never sufficient for execution. E3-005 cannot create a model
eligibility verdict, assign a role, promote a route, establish the E3 gate, or authorize E4.

## 16. E3-006 benchmark-lane input contract

The benchmark lane uses the same phase boundary. Independently verified E3-003 Phase A criteria and
E3-004's parameterized verified harness are sufficient inputs for harness construction only; they do
not admit a benchmark. After E3-004 verification, the registered E3-006 prelaunch benchmark-block
preparer—distinct from the benchmark operator and admission checker—must bind an exact Phase B
configuration/role/task/environment/support class, exact harness digest, Founder-approved QPA and
protocol limits, fixtures/order/graders/evidence destinations, and every account/budget/data/credential/
region/network/independence authority. Phase B receives separate verification and then a fresh
per-block admission. E3-006 remains `BACKLOG` / `DO_NOT_RUN`; no role or route is assigned by this contract.

## 17. Completion boundary

This fixed contract is ready for independent E3-002 post-fix verification when it remains technology-neutral,
represents all seven separately verdictable protocols, preserves exact E1/E2/QPA/admission boundaries,
and passes static repository checks. It remains `NOT VERIFIED`, with zero empirical runs and zero
harness or application code. The next lifecycle command is `MODE: VERIFY_TASK_E3-002`.
