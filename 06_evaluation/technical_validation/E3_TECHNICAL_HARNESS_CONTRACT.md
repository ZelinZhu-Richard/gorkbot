# E3 technical-validation harness contract

Status: E3-002 AUTHOR DRAFT — READY_FOR_REVIEW; NOT VERIFIED; NOT EXECUTION-READY

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

Current admission is `DO_NOT_RUN`. Every QPA and protocol-limit value remains `null` and
`FOUNDER_DECISION_REQUIRED`.

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

At minimum E3-004 must produce independently verifiable contracts for:

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
- repository, worktree, diff, temp, cache, artifact, and evidence paths;
- generated prompts/context packets before model dispatch;
- serialized model/provider requests and controlled responses at the adapter boundary;
- every tool argument/result and dispatched/received environment value;
- terminal stdin/stdout/stderr;
- parent/descendant argv, environment, output, exception, and stack surfaces;
- intermediate traces/events, logs, telemetry, audit, and evidence records;
- approval, summary, UI, notification, accessibility, screenshot, and clipboard surfaces;
- controlled network payloads at the local interceptor; and
- the exact protected recipient boundary.

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

- E3V-003 isolation must protect any fixture that mutates a workspace.
- E3V-002 containment must protect any fixture that spawns descendants.
- E3V-006 protected capture must protect every synthetic-marker fixture.
- E3V-005 is the evidence-credit gate for all affected protocol results; it is itself judged with
  harness-held canaries and state/readback to avoid circular self-validation.
- E3V-007 may recompute metrics from applicable immutable records only after integrity and
  contamination checks; synthetic protocol-shaped inputs may test all eight E1 protocol shapes
  without running or claiming E3V-008.

One raw attempt may support several derived analyses only if every exact applicability dimension
matches. The attempt is indexed once and cannot be counted twice. Each E3V receives a separate
root-cause disposition; a pass in one never compensates for another's failure or missing evidence.

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
failure is not an architecture handback. The default root cause is
`IMPLEMENTATION_CONFIGURATION_FAILURE`, `PRODUCT_CLASS_UNSUPPORTED`, or
`EVIDENCE_MISSING_FAIL_CLOSED` as the evidence requires.

`ARCHITECTURE_HANDBACK` requires a separate independent investigation and verification proving that
an indispensable accepted property in the exact required support class is structurally impossible
across every compliant realization route. The record must bind the preserved raw fault chain and the
protocol's exact canonical ADR set. E3 does not edit an ADR. It stops the affected lane and returns to
governed E2 challenge/fix, fresh architecture verification, and a renewed E2 gate before a new E3 freeze.

## 14. E3-004 input contract

E3-004 must not begin implementation until both E3-002 and E3-003 are independently `VERIFIED` under
their completion rules. For E3-002 specifically, execution-ready implementation requires:

- a final protocol version/digest for every E3V-001..007 record;
- exact Founder acknowledgement and approved E3-QPA-001 scope-aware values;
- fresh independent challenge and separate verification of those values and protocols;
- resolved exact configuration, host/client/support class, selected assets, fault order/seed,
  evidence destinations, oracle identities, and every finite protocol/resource/cost limit;
- no unresolved material protocol finding or accepted-architecture conflict.

This author draft intentionally fails those execution-ready conditions. E3-004 remains `BACKLOG`.

E3-004 acceptance must include strict parsing, selector resolution, fixture/oracle negative tests,
subject-oracle separation, admission bypass tests, process and protected-entry specialist review,
evidence/integrity replay, contamination tests, allowed-path and no-application-code proof, and a
fresh independent verifier. It may not produce accepted scored/candidate evidence while building or
verifying the harness.

## 15. E3-005 input contract

E3-005 remains `BACKLOG` / `DO_NOT_RUN`. Each future technical-validation block requires all of:

- E3-001, E3-002, and E3-004 exact current independent verification references;
- exact protocol/configuration/support/fixture/oracle/fault/environment identities and digests;
- Founder-approved, challenged, and verified QPA values plus all finite protocol limits;
- exact no-cost or separately authorized paid lane, budget, account, credential, data, region,
  retention, network, effect, isolation, security, and evidence facts;
- one fresh immutable closed manifest and independent semantic `RUN_ADMISSION=PASS`;
- one single-use launch reservation consumed atomically before process start;
- no drift, contamination, prior hard failure, unresolved handback, or missing current authority.

Protocol verification is necessary but never sufficient for execution. E3-005 cannot create a model
eligibility verdict, assign a role, promote a route, establish the E3 gate, or authorize E4.

## 16. Completion boundary

This contract is ready for independent E3-002 challenge when it remains technology-neutral,
represents all seven separately verdictable protocols, preserves exact E1/E2/QPA/admission boundaries,
and passes static repository checks. It remains `NOT VERIFIED`, with zero empirical runs and zero
harness or application code. The next lifecycle command is `MODE: REVIEW_TASK_E3-002`.
