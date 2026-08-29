# Engineering Preview architecture alternatives

Status: **E2-002 FIXER PASS — READY_FOR_REVIEW; NOT VERIFIED**

Task: `E2-002`

Candidate contract: `EP-ARCH-REQ-0.2`, fields 1–30

Authoring base: `38f673b82a1b40a277aa13b4e7ed17232521f3fa`

This artifact generates alternatives only. It assigns no weights or scores, ranks no candidate,
names no favorite or winner, selects no architecture or technology, accepts no ADR, and reports no
spike, evaluation, benchmark, model/provider, paid-call, or implementation result.

## 1. Authoritative basis and vocabulary

The three candidate records are bounded by the independently verified E1 product, correctness,
workflow, evaluation, and release-acceptance baseline; the independently verified
`EP-ARCH-REQ-0.2` requirements and traceability artifacts; D-016; charter §19; `SECURITY.md`; and
the current E2-002 registry contract. The repository is authoritative. Reconstructed Grok Bot
evidence was used only as non-authoritative Level B pattern inventory; no reconstructed source,
internal name, exact schema, layout, module, constant, asset, copy, score, or implementation detail
was adopted.

Each candidate contains exactly the verified 30 fields and explicitly covers:

- all 65 architecture requirements: 59 hard constraints and six unweighted preferences;
- all 127 canonical E1 IDs through a candidate-local primary-AR resolution map;
- all 25 architecture decision domains;
- all 20 threat boundaries with the nine required semantics;
- all 19 verified Level B pattern families;
- all eight `E3V-001..008` obligations;
- the frozen suite seams for 170 cases, 18 oracle classes, 11 fixture families, 23 security-negative
  families, 16 repository conditions, 30 Git/effect rows, nine predicate-adequacy variants,
  16 dangerous compositions, and eight reliability protocols; and
- an exhaustive candidate capability inventory using `REQUIRED_NOW`,
  `RESERVED_COMPATIBILITY`, or `DEFERRED_TO_LATER_STAGE` exactly once per capability.

Candidate records use both the verified contract vocabulary and the more explicit generation-time
vocabulary required by E2-002:

| Generation status | Verified contract projection | Consequence |
|---|---|---|
| `SATISFIED_BY_DESIGN` | `SATISFIED_BY_DESIGN` | The architecture already contains a sufficiently specified structural authority, mechanism, or enforceable seam establishing the hard property at design level; implementation and E3/E4 evidence may still be absent. |
| `PLAUSIBLY_SATISFIABLE_BUT_REQUIRES_E2_003_ANALYSIS` | `UNKNOWN` | A credible design path exists, but unresolved paper/design analysis remains before the property can be claimed structurally present; it receives no favorable surrogate. |
| `UNKNOWN_REQUIRING_SPIKE` | `UNKNOWN` | Empirical mechanism feasibility is genuinely architecture-blocking and cannot responsibly be decided by analysis alone; selection remains blocked until authorized E2-004 work closes it. |
| `VIOLATED` | `FAILED_HARD` | The candidate as defined contradicts the hard requirement and is inadmissible unless revised and independently reviewed. |
| `PREFERENCE_CHARACTERIZED_UNSCORED` | `UNKNOWN` for the preference entry | Comparative evidence remains for E2-003; no weight or score exists. |

`SATISFIED_BY_DESIGN` is not an implementation, evaluation, benchmark, release, or runtime-pass
claim. Every canonical E1 runtime result remains `SPECIFIED_NOT_IMPLEMENTED_NOT_RUN`; every
`SLO-*` or `MET-*` protocol remains `PROTOCOL_SPECIFIED_NOT_RUN`.

The rule above was applied to all 59 hard ARs in every candidate, not only to the challenged
examples. Equivalent unresolved properties receive the same status unless a candidate record
identifies an actual structural cause for a difference. Preference elegance, cost, future
extraction burden, or contributor burden never determines a hard status. In particular,
`AR-EXE-003`, `AR-DUR-003`, `AR-FUT-001`, `AR-FUT-002`, and `AR-TST-002` were rechecked under one
bar, and unknowns receive no favorable treatment.

## 2. Candidate set

### EP-ARCH-C01 — Integrated Transactional Local Core

One task-bound integrated local application core owns policy, orchestration, canonical writes, embedded
transactional state/history, recovery, provider/capability routing, client projections, and
evidence. Untrusted execution and independent verification use owned child-process and separate
workspace/context boundaries. A presentation may detach while the core safely continues or
suspends current work, but the core is not a separately installed permanent service and its
execution children are not independently replaceable authorities.

Full contract: [`candidates/EP-ARCH-C01.yaml`](candidates/EP-ARCH-C01.yaml)

### EP-ARCH-C02 — Local Control Service with Replaceable Workers

A persistent user-local control service is the sole authority independent of every client. Authenticated thin clients submit
idempotent commands and render projections. Leased, fenced execution and verifier workers are
disposable and have no direct canonical write access. The local service owns persistence,
scheduling, recovery, approvals/effects, routing, evidence, and worker fencing.

Full contract: [`candidates/EP-ARCH-C02.yaml`](candidates/EP-ARCH-C02.yaml)

### EP-ARCH-C03 — Durable Event and Workflow Core with Rebuildable Projections

An append-only material event journal plus immutable referenced payloads and deterministic
normative reducer rules are durable authority independent of every client and coordinator.
Deterministic reducers create rebuildable task, client, transcript, search, and evidence
projections. A task-bound coordinator may continue without a client or be absent and recovered;
coordinator process lifetime is not task identity. Fenced execution, provider,
protected-entry, and verifier adapters submit typed commands/events through one policy and append
boundary.

Full contract: [`candidates/EP-ARCH-C03.yaml`](candidates/EP-ARCH-C03.yaml)

## 3. Structural distinctions only

This table identifies system-shape differences. It is not a comparison result, preference,
ranking, or recommendation.

| Architecture dimension | EP-ARCH-C01 | EP-ARCH-C02 | EP-ARCH-C03 |
|---|---|---|---|
| Authority owner | Single-writer integrated local core | Persistent user-local control service | Journal append gate plus deterministic workflow reducer |
| Client boundary | Presentation session attaches to the integrated task-bound runtime; client-only close is distinct from full-runtime exit | Thin authenticated client over a persistent local-service boundary | Projection subscriber over a command/event boundary; journal authority is not a client projection |
| Required long-running topology | Task-bound integrated core/supervisor may run headless for admitted work or safely suspend; no permanent service | Persistent control service; clients are optional and workers exist only while leased | No mandatory daemon/platform; a task-bound coordinator may run detached or be absent between replay/recovery cycles |
| Execution ownership | Co-resident core supervisor owns child process trees under the same integrated authority epoch | Service grants replaceable workers bounded leases/fences; workers own process trees only for a lease | Durable dispatch eligibility comes from journal/reducer truth; task-bound coordinator grants a fenced executor adapter a lease |
| Verification boundary | Fresh separate process/context and review workspace | Separately leased verifier worker | Separate verifier adapter that independently replays/rereads and appends immutable run events |
| Persistence authority | Transactional current state plus material history and operation/effect ledgers | Service-owned transactional state/history plus command, dispatch, result, and effect inbox/outbox | Append-only material event journal plus immutable payloads; snapshots/projections are derived |
| Scheduling model | In-core scheduler under one owner epoch | Service scheduler grants worker leases/fences | Reducer derives eligible work; coordinator grants leases/fences from durable events |
| Recovery reconstruction | Validate transactional store, rebuild projections, reconcile nonterminal ledgers | Restart service epoch, invalidate leases/IPC, reconcile inbox/outbox/effects | Validate/replay journal and payloads, rebuild projections, reconcile nonterminal workflows |
| External-effect seam | Core approval/effect ledger around adapters | Service dispatch/result/effect bridge around workers | Ordered intent/approval/dispatch/observation/readback workflow events |
| Worker replaceability | Child executors may be restarted, but are not independent replaceable execution authorities; losing the core loses the live owner | Defining property: disposable workers can be replaced without changing durable service authority | Coordinator/executor processes are replaceable by journal replay and new owner/fence events; projections remain disposable |
| Projection/event model | Transactional current state/history are authoritative; projections are derived, but events do not define all authority | Service-owned state/history and inbox/outbox are authoritative; client/worker projections are derived | Material journal/payloads and normative reducer semantics define authority; every cached projection is rebuildable and non-authoritative |
| Remote-evolution boundary | A versioned executor port exists inside the integrated core and would require later transport/extraction work | Worker lease/request/result contract already crosses the service boundary; remote transport/auth remain absent | Serializable dispatch/result/fence event contract exists; remote transport/auth/coordination remain absent |
| Contributor burden shape | One broad core with fewer top-level processes but dense responsibility/port discipline and integrated recovery documentation | Service lifecycle, IPC/lease/fence, worker replacement, packaging and service-debugging concepts | Event schemas/evolution, deterministic reducers/replay, projections/checkpoints and adapter contracts |
| Principal architectural commitment | Integrated single-writer core and transactional record semantics | Local control-service lifecycle and lease/effect protocol | Canonical event meanings, ordering, evolution, journal/payload boundary and reducers |

Pairwise structural distinctness remains explicit after the lifetime corrections:

- **C01 versus C02:** C01 keeps control, scheduling, persistence, projections, and the execution
  supervisor inside one task-bound integrated runtime. Its presentation may detach, but full core
  loss ends the live owner and requires safe suspension/fencing plus restart reconciliation. C02
  instead requires a persistent service authority whose replaceable leased workers and clients
  may all disappear without ending the service epoch. C01 therefore did not acquire C02's daemon
  plus replaceable-worker topology.
- **C01 versus C03:** C01 reconstructs from transactional current state, material history, and
  operation/effect ledgers under an integrated writer. C03 reconstructs normative workflow state
  by replaying material journal/payload history through deterministic reducers and treats
  projections as disposable. Their external-effect and migration commitments remain different.
- **C02 versus C03:** C02's persistent service store and service scheduler own canonical state and
  grant disposable workers leases. C03's journal head plus reducer semantics remain authoritative
  even with no live coordinator; a coordinator is a replaceable interpreter/execution owner, not
  a persistent service that owns canonical state.

## 4. Hard-constraint generation status

No candidate contains a known hard violation. Unknowns are explicit and receive no score or pass
credit. A candidate cannot be selected while its selection-blocking spike items remain open.

| Candidate | Hard total | `SATISFIED_BY_DESIGN` | Plausible, E2-003 analysis | `UNKNOWN_REQUIRING_SPIKE` | `VIOLATED` |
|---|---:|---:|---:|---:|---:|
| EP-ARCH-C01 | 59 | 52 | 5 | 2 | 0 |
| EP-ARCH-C02 | 59 | 52 | 5 | 2 | 0 |
| EP-ARCH-C03 | 59 | 52 | 5 | 2 | 0 |

The complete per-AR evidence and owner records are in field 23 of each candidate. The full 127-ID
E1 mapping in the same field enumerates every canonical ID exactly once and inherits the status,
evidence, and owner of its primary AR. Supporting ARs remain available in the independently
verified bidirectional traceability CSV; the candidate records waive none.

The equal totals are the result of reassessment, not a retained author target. The same five hard
properties remain paper/design-analysis unknown in each candidate: `AR-DUR-005`, `AR-WSP-003`,
`AR-SEC-003`, `AR-SEC-004`, and `AR-PKG-001`. The same two empirical mechanism questions remain
architecture-blocking: `AR-EXE-003` descendant/process-tree containment and `AR-SEC-006`
protected-entry feasibility. `AR-DUR-003` is now `SATISFIED_BY_DESIGN` in each candidate because
each contains an explicit intent/attempt/correlation/readback and known/failed/unknown recovery
bridge without claiming global atomicity. `AR-FUT-001` and `AR-FUT-002` are satisfied only at the
hard compatibility-seam floor; extraction cost and elegance remain unscored preferences.
`AR-TST-002` remains satisfied only because field 25 now exposes the complete family-level matrix,
EP-CTL-016, and all 16 mandatory dangerous compositions for every candidate.

## 5. Preferences remain preferences

Every candidate characterizes the same six preferences without assigning weights or values:

| Preference | Candidate evidence that E2-003 may later examine |
|---|---|
| `AR-PRF-001` interactive/control latency | Local invocation/IPC/append and projection paths; no latency result exists. |
| `AR-PRF-002` operational/maintenance complexity | Components, ownership, lifecycle, failure propagation, state/recovery concepts and documentation burden. |
| `AR-PRF-003` migration/reversibility | Replaceable boundaries, state export/import, costly commitments, rollback limits and reversal triggers. |
| `AR-PRF-004` future remote/concurrency adaptation | Serializable interfaces, owner/version scopes and the work deliberately left for future transport/scheduling. |
| `AR-PRF-005` evidence/large-output overhead | Store/journal/payload/reference topology and future comparable measurement seams. |
| `AR-PRF-006` contributor/local packaging burden | Setup, process count, infrastructure, platform assumptions, local tests, debugging and bounded-component ownership. |

Weights remain `UNASSIGNED`. E2-003 owns any prospective comparison governance and must preserve
the verified correlation and sensitivity rules before candidate-specific scoring could occur.

## 6. Security, protected entry, approval, and effects

Field 5 in every candidate instantiates `TB-01..20` with trust/assets, authority, allowed and
forbidden flows, enforcement, fail-closed behavior, evidence, and recovery/replay. Each names
fully privileged host compromise as unsupported and makes missing enforcement a support
limitation or blocker. No row relies on “the model will follow policy.”

Field 18 assigns structural control ownership to policy/command kernels, workspace brokers,
execution supervisors and fences, capability/Git/network/provider/evidence gateways, and a
dedicated protected-entry broker/controller. In every candidate protected entry:

1. is distinct from ordinary chat/model/context/event capture;
2. authenticates a human takeover and exact recipient/use;
3. suspends or excludes ordinary observation/capture;
4. keeps the raw value out of transcript, model context, authoritative state, journal, logs,
   screenshots, summaries, evidence, and artifacts;
5. fails to `WAITING_FOR_USER` or a hard blocker if protection is unavailable;
6. emits only a non-secret durable receipt/provenance record; and
7. revalidates and reacquires after recovery without replaying the raw value.

The shared protected-acquisition/capture problem is separated from each candidate's delivery seam:

- **C01:** acquisition and one-use exact-recipient delivery remain inside the integrated trusted
  runtime boundary but outside ordinary command, model, transcript, logging, screenshot, and
  evidence pipelines.
- **C02:** protected entry begins in the authenticated client capture-exclusion controller. Raw
  bytes bypass the ordinary client command and service persistence/projection paths; the service
  validates only the non-secret recipient/use/operation/fence grant, and a protected delivery
  endpoint carries the transient value directly to the leased worker's exact recipient. The
  ordinary IPC router, command store, scheduler, projections, logs, telemetry, model context, and
  evidence system are forbidden from seeing it. Worker replacement revokes the old endpoint;
  crash ambiguity requires reacquisition rather than replay.
- **C03:** the journal may admit only non-secret protected intent, recipient/use, correlation,
  expiry, capture-state, and receipt metadata. Raw bytes never enter event history, payloads,
  snapshots, projections, model context, telemetry, or evidence; a transient out-of-event broker
  routes them to the fenced recipient. Intent-persisted/delivery-failed and
  delivery-succeeded/receipt-persist-failed crash points resolve to known-not-delivered,
  known-delivered, or `OUTCOME_UNCERTAIN` by correlation/readback, never guessed atomicity or raw
  replay.

Field 12 keeps `INTENT`, `APPROVAL`, `ATTEMPT`, `OBSERVED_EFFECT`, `CONFIRMED_EFFECT`, and
`UNKNOWN_EFFECT` distinct. Durable exact-scope approvals have principal, versions, full action,
target, expiry, revocation, one-shot consumption, replay protection and recovery rules. A response
is observation, not proof. Authoritative readback establishes known success or known non-success;
acknowledgement loss remains unknown and blocks completion and blind retry.

C01's “transactional” guarantee is explicitly limited to records under its embedded persistence
authority. It does not cover arbitrary filesystem writes, child processes, Git remotes, external
APIs, provider dispatch, or other external targets. C02 separately labels control-plane
lease/fencing, local process-tree containment, and remote-effect fencing; none proves either of the
others. C03 distinguishes the authoritative journal head/normative reducer from disposable
projections, and no effect may be admitted from stale projection state.

## 7. Task, state, recovery, context, and evidence

All candidates provide stable request/task/attempt/operation/workspace/approval/effect/artifact/
verification identities; first-outcome duplicate handling; versioned task/plan/predicate/policy;
orthogonal task axes; current ownership/fencing; finite prospective limits; durable pause, stop,
redirect and resume; retirement; and restart revalidation. Model context is always bounded and
non-authoritative.

The five required lifetime concepts are explicit in field 2 of every candidate:

| Lifetime | Shared product rule | Candidate-specific execution consequence |
|---|---|---|
| `CLIENT_LIFETIME` | Presentation attachment is non-authoritative and may end without cancellation or state loss. | C01 detaches from its task-bound integrated runtime; C02 detaches from the service; C03 drops a projection subscription. |
| `CONTROL_AUTHORITY_LIFETIME` | Durable authority outlives clients and must be reconstructable. | C01's task-bound core may safely continue/suspend and later recover; C02's service stays authoritative; C03's journal plus reducer rules remain authority even without a live coordinator. |
| `EXECUTION_OWNER_LIFETIME` | Ownership is fenced, policy-bounded, and durable enough to reconcile in-flight operations. | C01 uses its co-resident supervisor; C02 leases disposable workers; C03 leases a task-bound coordinator/executor that may be replaced by replay. |
| `TASK_LIFETIME` | Task state outlives every UI and process instance until a truthful terminal or retained nonterminal disposition. | Completion never depends on a client process in any candidate. |
| `WORKSPACE_LIFETIME` | Workspace state survives client/process loss until actual mutations/effects are reconciled and cleanup is safely authorized. | Each candidate retains pinned identity, operation records, evidence and fresh readback before cleanup. |

Client-only interruption (`EP-CTL-016`) is therefore distinct from deliberate full-system
shutdown in all candidates. No stale reconnecting client automatically recovers an old lease,
approval, or authority. C01 and C03 may have no live owner after full runtime/coordinator loss; in
that interval they authorize no new dispatch and make no real-time deadline-enforcement claim.
Restart immediately fences old ownership, classifies overdue/nonterminal work, rereads actual
state, and records a truthful recovery disposition.

Each candidate classifies task, operation, approvals, effects, verification, evidence, artifacts,
conversation/history, context summaries, and routing provenance as authoritative, derived,
ephemeral, or lossy. Summaries retain source/version/trust/omission provenance and cannot erase or
replace security, approval, effect, evidence, predicate, verification, or completion facts.

Every recovery model covers application crash, host restart, worker failure, model timeout, tool
timeout, lost tool result, partial write/corruption, stale workspace, duplicate operation,
duplicate effect, external acknowledgement loss, stop/force/fence, stale approval, stale
verification, waited-event delivery, protected-entry non-replay, and agent retirement. No model
uses guessed success.

Workspace recovery now separately covers process death during a write, an existing partial file,
interrupted rename/replace, a partially completed multi-file edit, unexpected Git index versus
working-tree divergence, a partially generated artifact, and startup with uncertain filesystem
state. No candidate assumes global filesystem atomicity. Each rereads the real workspace/Git
state, reconciles it against the pinned base and recorded operations, preserves partial/uncertain
evidence, invalidates stale verification, and returns `BLOCKED`, `UNVERIFIED`, `PARTIAL`, or an
explicit known/unknown outcome when truth cannot be safely established. An intended operation
record is never proof that a write succeeded.

### Isolation taxonomy and AQ-003

The candidate set uses one technology-neutral taxonomy and selects no container, VM, process
sandbox, worktree, or product:

| Tier | Semantic meaning |
|---|---|
| `TIER_0_LOGICAL_SCOPE_ONLY` | Identity/policy labels only; no enforceable process, filesystem, network, or secret boundary. Insufficient for untrusted execution. |
| `TIER_1_BROKERED_PROCESS_PATH_AND_EFFECT_CONTAINMENT` | Supported operations cross accountable path/process/network/effect/secret brokers, but arbitrary descendants are not yet proven confined against bypass. |
| `TIER_2_OS_ENFORCED_EXECUTION_ISOLATION` | The declared host enforces process-tree, filesystem, network/resource, and credential boundaries for the supported workload class, including descendants and owner loss. |
| `TIER_3_STRONGER_WORKLOAD_BOUNDARY` | Stronger separately administered workload/blast-radius properties beyond frozen E1; not required or assumed for v0.1. |

All three candidates declare Tier 1 as the minimum for brokered non-executing operations and
assume the semantic properties of Tier 2 for untrusted descendant-spawning code. This assumption
supports `AR-WSP-002/003`, `AR-EXE-003/004`, and `AR-SEC-002/003/004`; it does not claim protection
from a compromised administrator/kernel/firmware/media, cross-tenant isolation, side-channel
resistance, or Tier 3. Filesystem access is limited to admitted task objects; network sends zero
bytes without an exact revalidated grant; descendant identity/effects remain accountable; raw
secrets are neither ambient nor inherited. `AQ-003` is consistent across candidates: the semantic
tier and support declaration are analysis-resolvable, supported-host descendant containment is
shared empirical question `SPQ-E2-002-01`, and the concrete mechanism remains an implementation
detail. Logical lease/fence semantics alone do not satisfy the process-tree property.

Evidence and verification are structurally separate from executor narration. The verifier can
read the underlying authoritative state and target readbacks, rerun deterministic checks, assess
predicate adequacy, observe infrastructure error distinctly, and bind immutable runs to the exact
candidate/revision. Any material mutation invalidates the current pass while preserving historical
runs.

## 8. E1 suite testability

Field 25 in each candidate maps all frozen suite asset families to candidate-specific injection
and decisive-readback seams. Across the set, the design records expose or simulate:

- crashes before/after acknowledgement, append, dispatch, result and readback;
- process, worker, model, provider, transport and tool timeout/failure/cancellation;
- lost, duplicated, stale, reordered, substituted or malformed commands/results;
- stale owner, workspace, repository revision, approval, summary, evidence, and verification;
- protected marker secrets and capture-state surfaces;
- repository/path/Git mutation and cleanup races;
- external-effect acknowledgement loss and ambiguous target state;
- verifier error, predicate inadequacy, evidence gap/tamper and post-pass mutation; and
- raw timestamps, counters, limits, usage, cost, strata and missingness for the eight protocols.

Each candidate now contains exactly nine bounded family-level rows rather than 170 duplicated
case rows: 170 evaluation cases, 18 oracle classes, 11 fixture families, 23 security-negative
families, 16 repository-condition families, 30 Git/effect classifications, nine
predicate-adequacy variants, 16 dangerous compositions, and eight reliability protocols. Every
row records the architecture seam, injectable condition, observable state/evidence, oracle access
path, candidate limitation, unsupported condition, and the E2/E3/E4/E5 instrumentation stage.

Each candidate also contains one explicit `EP_CTL_016` mapping and 16 individually named
composition mappings (`COMP-01` through `COMP-16`). These cover approval/crash, external-effect
crash/stop/lost-ack duplication, redirect plus stale verification, dirty-repository recovery,
secret-path and symlink attacks, malicious output as evidence, stale approval after restart,
post-verification mutation, Git-hook effects, package-script egress, force-stop partial filesystem
mutation, provider fallback at a cost ceiling, and instruction-driven capability escalation.

Underlying store/journal/repository/effect state is decisive. An executor, client, projection,
model, or telemetry summary cannot be the sole oracle. Unsupported host/repository/capability
classes are explicit and cannot count as a pass.

## 9. Level B dispositions

Every candidate dispositions all 19 verified Level B families as `USED`, `NOT_USED`, `DEFERRED`,
or `SUBSUMED`, gives the independent E1 reason, and identifies excluded Level C detail. This is a
pattern inventory, not a merit count.

| Family | EP-ARCH-C01 | EP-ARCH-C02 | EP-ARCH-C03 |
|---|---|---|---|
| LB-01 canonical authority/checkpoints/roots/migration | USED | USED | USED |
| LB-02 content-addressed identity/referents | NOT_USED | NOT_USED | NOT_USED |
| LB-03 derived projections/rebuilding | USED | USED | USED |
| LB-04 authority/history persistence alternatives | USED — transactional hybrid | USED — service transactional hybrid | USED — event history |
| LB-05 operation journal/recovery | USED | USED | SUBSUMED by material event journal |
| LB-06 typed failure registry | USED | USED | USED |
| LB-07 typed process ports/owned boundaries | USED | USED | USED |
| LB-08 provider/router abstraction | USED | USED | USED |
| LB-09 explicit task/execution state | USED | USED | SUBSUMED by typed events/reducers |
| LB-10 structured approvals/capability receipts | USED | USED | USED |
| LB-11 local/remote execution abstraction | USED, local port only | USED, local worker interface | USED, local dispatch/result events |
| LB-12 long-running/cloud-agent lifecycle | SUBSUMED; cloud deferred | USED locally; cloud deferred | SUBSUMED; cloud deferred |
| LB-13 context compaction/summary blocks | USED | USED | USED |
| LB-14 direct adapters versus capability gateway | USED — central gateway | USED — service gateway | USED — command-policy gateway |
| LB-15 concurrency/multi-writer safety | USED — version/epoch | USED — version/lease/fence | USED — sequence/owner/fence |
| LB-16 telemetry/audit/evidence/presentation topology | USED | USED | USED |
| LB-17 corruption quarantine/salvage/migration | USED | USED | USED |
| LB-18 evidence packets/manifests/anchors/drift | USED | USED | USED |
| LB-19 extension/vertical-package boundary | USED as reserved contract | USED as reserved contract | USED as reserved contract |

Identical dispositions are retained where E1 supplies the same hard floor or where E2 deliberately
leaves the same technology choice open. In particular, LB-02 is `NOT_USED` in all candidates
because stable identity plus integrity meets the hard evidence floor and content addressing would
introduce privacy/retention/deletion questions without defining any candidate's authority shape.
LB-14 is `USED` in all candidates because no ordinary adapter may grant itself authority, but its
placement differs: an in-process integrated gateway in C01, a service-owned gateway plus separate
protected raw-value route in C02, and current-head policy/event admission before adapters in C03.
These shared dispositions are constraints/non-decisions, not evidence that the shapes converged.

The candidate set also rechecks charter §19's architecture subjects without forcing artificial
variation. It meaningfully varies authority ownership, client/runtime boundaries, long-running
topology, durable-state model, event/history authority, operation scheduling, recovery
reconstruction, executor replaceability, projection status, external-effect admission, future
remote seams, migration lock-in, and contributor burden. It intentionally does not vary hard
security, truthfulness, isolation-floor, protected-entry, approval, independent-verification, or
no-hidden-provider requirements merely to create cosmetic diversity. Level B disposition counts
are not scores.

## 10. Uncertainties and possible E2-004 work

Field 27 classifies candidate-local uncertainty as
`ANALYSIS_RESOLVABLE_E2_003`, `ARCHITECTURE_BLOCKING_SPIKE_E2_004`,
`E3_VALIDATION_OBLIGATION`, `E4_IMPLEMENTATION_DETAIL`, or `FUTURE_PRODUCT`. No spike was run.

The normalized model contains **five unique questions**: two
`SHARED_ARCHITECTURE_SPIKE` questions and three
`CANDIDATE_SPECIFIC_ARCHITECTURE_SPIKE` questions. Candidate records reference the two shared
questions plus their one delivery question, for nine references without creating three duplicate
acquisition or process-containment spikes. All five have `run_status: NOT_RUN`.

**SPQ-E2-002-01 — shared descendant/process-tree containment**

- `property_being_tested`: supported-host descendant/process-tree containment after cancel,
  force, fence, owner loss, and client-independent execution.
- `affected_ARs`: `AR-EXE-003`; `affected_candidates`: C01, C02, C03;
  `shared_or_candidate_specific`: `SHARED_ARCHITECTURE_SPIKE`.
- `why_analysis_is_insufficient`: logical lease/epoch fencing cannot prove actual descendants stop,
  lose effects, or remain contained.
- `minimal_mechanism_under_test`: one technology-neutral process-tree adapter, controlled
  descendants, cancel/force/fence/owner-loss fault points, and an effect canary through each
  topology.
- `success_criterion`: every descendant terminates or loses productive/effect authority within the
  declared bound, stale output cannot commit, and the full tree is evidenced;
  `failure_criterion`: any unaccounted descendant, post-fence effect, stale commit, or
  topology-specific bypass.
- `architecture_blocking_reason`: Tier 2 support and `AR-EXE-003` cannot be claimed without
  empirical feasibility; `reusable_result_scope`: host primitive/process behavior across all
  candidates, with topology assertions kept separate; `decision_linkage`: E2-003 may classify and
  E2-004 alone may run it, with failure returned to affected candidate work.

**SPQ-E2-002-02 — shared protected acquisition/capture exclusion**

- `property_being_tested`: protected human acquisition excludes ordinary keystroke, clipboard,
  screen/accessibility, terminal, model, transcript, log, and evidence capture.
- `affected_ARs`: `AR-SEC-006`; `affected_candidates`: C01, C02, C03;
  `shared_or_candidate_specific`: `SHARED_ARCHITECTURE_SPIKE`.
- `why_analysis_is_insufficient`: a paper boundary cannot demonstrate exclusion across real client
  and host observation surfaces.
- `minimal_mechanism_under_test`: synthetic marker entry with capture suspension and observers on
  every mandatory surface; no provider or real secret.
- `success_criterion`: the marker appears only at the protected endpoint and failure closes to
  waiting/blocked with a non-secret receipt; `failure_criterion`: any exposure, persistence,
  ordinary replay, or bypass.
- `architecture_blocking_reason`: capture exclusion is a hard protected-entry boundary;
  `reusable_result_scope`: acquisition is shared while routing remains candidate-specific;
  `decision_linkage`: E2-003 may classify and E2-004 alone may run it without selecting a client
  technology.

**SPQ-E2-002-03 — C01 integrated protected delivery**

- `property_being_tested`: exact one-use protected delivery within C01 reaches only the integrated
  recipient/use without entering ordinary core pipelines.
- `affected_ARs`: `AR-SEC-003`, `AR-SEC-006`; `affected_candidates`: C01;
  `shared_or_candidate_specific`: `CANDIDATE_SPECIFIC_ARCHITECTURE_SPIKE`.
- `why_analysis_is_insufficient`: colocation could expose raw input to ordinary command, model,
  logging, screenshot, or evidence paths.
- `minimal_mechanism_under_test`: recipient/use/fence-scoped synthetic handoff with crash points and
  forbidden-pipeline observers.
- `success_criterion`: one transient revocable consumption and no forbidden-surface appearance;
  `failure_criterion`: visibility, second/post-fence use, persistence, or replay.
- `architecture_blocking_reason`: C01-specific delivery half of protected-entry feasibility;
  `reusable_result_scope`: C01 routing only, with shared capture from SPQ-02;
  `decision_linkage`: E2-003 may freeze a bounded C01 variant and E2-004 alone may execute it.

**SPQ-E2-002-04 — C02 client-to-worker protected delivery**

- `property_being_tested`: protected client input reaches one C02 leased worker recipient without
  exposure to ordinary client/service/IPC/worker pipelines.
- `affected_ARs`: `AR-SEC-003`, `AR-SEC-006`; `affected_candidates`: C02;
  `shared_or_candidate_specific`: `CANDIDATE_SPECIFIC_ARCHITECTURE_SPIKE`.
- `why_analysis_is_insufficient`: service/worker replacement and IPC crash boundaries require
  observed raw-value lifetime, visibility, fencing, and no-replay behavior.
- `minimal_mechanism_under_test`: synthetic marker, non-secret service authorization, one-use
  delivery endpoint, worker replacement/fence, and crashes before/during receipt.
- `success_criterion`: only the intended current worker recipient consumes once and every
  intermediate observer remains marker-free; `failure_criterion`: service persistence/visibility,
  stale-worker use, duplicate delivery, raw replay, or uncorrelated receipt.
- `architecture_blocking_reason`: C02-specific delivery half of protected-entry feasibility;
  `reusable_result_scope`: C02 service/worker routing only, with shared capture from SPQ-02;
  `decision_linkage`: E2-003 may freeze a bounded C02 variant and E2-004 alone may execute it.

**SPQ-E2-002-05 — C03 out-of-event protected delivery**

- `property_being_tested`: C03 preserves intent/receipt/recovery truth while raw protected bytes
  bypass journal, payload, projection, model, and telemetry capture.
- `affected_ARs`: `AR-SEC-003`, `AR-SEC-006`; `affected_candidates`: C03;
  `shared_or_candidate_specific`: `CANDIDATE_SPECIFIC_ARCHITECTURE_SPIKE`.
- `why_analysis_is_insufficient`: event-before-delivery metadata, transient routing, append/delivery
  crash points, and no replay need observed behavior.
- `minimal_mechanism_under_test`: synthetic one-use intent/correlation, out-of-event broker,
  recipient/fence observer, and crashes around delivery/non-secret receipt append.
- `success_criterion`: only the named recipient consumes once, raw bytes remain absent from durable
  and derived surfaces, and every crash becomes known-not-delivered, known-delivered, or explicit
  unknown; `failure_criterion`: capture, stale/duplicate/replayed use, guessed outcome, or
  uncorrelated receipt.
- `architecture_blocking_reason`: C03-specific delivery half of protected-entry feasibility;
  `reusable_result_scope`: C03 ordering/routing only, with shared capture from SPQ-02;
  `decision_linkage`: E2-003 may freeze a bounded C03 variant and E2-004 alone may execute it.

E2-003 must independently determine whether each listed item truly requires a bounded E2-004
spike and freeze any allowed spike contract. E2-002 did not run one and does not optimistically
score any unknown.

Candidate-local uncertainty records total **28**: 10 analysis-resolvable records, nine normalized
spike references (five unique questions), three E3-obligation records, three E4-detail records,
and three future-product records. C01 has 9 records, C02 has 9, and C03 has 10. No uncertainty is
treated as favorable evidence, and the duplicated references to shared SPQ-01/SPQ-02 do not create
additional E2-004 questions.

## 11. E3 handoff

Field 30 in every candidate maps `E3V-001..008` to candidate-specific focused evidence, accountable
owner class, E4/E5 remainder, architecture-handback condition, implementation/configuration
condition, and an unpopulated proposed-ADR link. No ADR link exists unless E2-005 later creates one
for the candidate selected after verified comparison and blocker closure.

The handback boundary is unchanged:

- reproducible architectural inability to provide the required durable, control, isolation,
  provider, evidence/verifier, security/protected-entry, or instrumentation property reopens E2;
- an adapter, fixture, validator, policy wiring, ordinary configuration, or implementation defect
  remains correction work while the selected property is still feasible; and
- model/provider/configuration failure leaves a logical role unassigned unless a future ADR made
  the now-impossible capability indispensable with no compliant replacement.

E3 may validate a selected shape; it may not silently redesign it.

## 12. Contributor burden and migration

Candidate-local contributor analyses cover setup, process/service count, infrastructure, supported
platform assumptions, toolchain/dependencies, local test execution, failure reproduction,
debugging, bounded component ownership, and documentation. These are preference evidence, not a
“simplest wins” rule.

Migration records identify easy-to-replace adapters/projections and costly authority/state
commitments. In all candidates, provider/model occupants remain replaceable behind neutral
contracts. Client replacement must reproduce authentication, control, approval, protected-entry,
and evidence semantics. Local-to-remote evolution always requires future authentication,
transport, delivery, failure, ownership, and reconciliation design; no candidate pretends that
serializable interfaces already implement a distributed system.

The costly commitments differ structurally:

- EP-ARCH-C01: integrated single-writer core and chosen transactional authoritative records;
- EP-ARCH-C02: control-service lifecycle/store and service-worker lease/effect protocol; and
- EP-ARCH-C03: canonical event identities, meanings, ordering, evolution, reducers, and the
  journal/payload authority boundary.

This distinction is factual and unranked.

## 13. Future scope boundary

All three candidates classify v0.1 task/durability/workspace/execution/Git/approval/provider/
context/evidence/verification/security/local-interaction capabilities as `REQUIRED_NOW` subject to
the future gates. They reserve only interfaces and ownership/version scopes for remote execution,
cloud workers, concurrent tasks, multiple agents/clients, skills/routines, and connectors. Actual
remote/cloud/concurrent/multi-agent/multi-client/extension implementations, General Edition,
Finance Edition, and SaaS remain `DEFERRED_TO_LATER_STAGE` or future product scope.

No distributed consensus, remote transport, worker fleet, connector loader, multi-tenancy,
vertical schema, SaaS control plane, or provider/model role assignment was introduced.

## 14. Generation disposition

Candidate count: **3**

Candidate IDs: `EP-ARCH-C01`, `EP-ARCH-C02`, `EP-ARCH-C03`

Architecture selected: **NO**

Preferred candidate: **NONE**

Accepted ADRs: **0**

Architecture spikes run: **0**

Application code created: **NO**

Evaluation cases run: **0**

Model benchmarks run: **0**

Paid API calls: **0**

Autonomy eligible: **NOT_ELIGIBLE**

Autonomous build authorized: **NO**

E2-002 remains author-produced and **NOT VERIFIED**. Independent challenge/fix/verification must
precede any `VERIFIED` transition or release of E2-003. This fixer pass addresses
`F-E2-002-01..09`, leaves the candidate set at three unranked shapes, and returns E2-002 to
`READY_FOR_REVIEW`. E2-003 remains `BACKLOG` and dependency-blocked; the E2 gate remains
`NOT_EVALUATED`.
