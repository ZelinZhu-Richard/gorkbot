# Engineering Preview architecture alternatives

Status: **E2-002 AUTHOR PASS — READY_FOR_REVIEW; NOT VERIFIED**

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
| `SATISFIED_BY_DESIGN` | `SATISFIED_BY_DESIGN` | The described system shape contains a structural path; E3/E4 evidence is still absent. |
| `PLAUSIBLY_SATISFIABLE_BUT_REQUIRES_E2_003_ANALYSIS` | `UNKNOWN` | E2-003 must analyze it; it receives no favorable surrogate. |
| `UNKNOWN_REQUIRING_SPIKE` | `UNKNOWN` | Selection is blocked until E2-004 closes it for the affected candidate. |
| `VIOLATED` | `FAILED_HARD` | Candidate is inadmissible unless revised and independently reviewed. |
| `PREFERENCE_CHARACTERIZED_UNSCORED` | `UNKNOWN` for the preference entry | Comparative evidence remains for E2-003; no weight or score exists. |

`SATISFIED_BY_DESIGN` is not an implementation, evaluation, benchmark, release, or runtime-pass
claim. Every canonical E1 runtime result remains `SPECIFIED_NOT_IMPLEMENTED_NOT_RUN`; every
`SLO-*` or `MET-*` protocol remains `PROTOCOL_SPECIFIED_NOT_RUN`.

## 2. Candidate set

### EP-ARCH-C01 — Integrated Transactional Local Core

One persistent local application core owns policy, orchestration, canonical writes, embedded
transactional state/history, recovery, provider/capability routing, client projections, and
evidence. Untrusted execution and independent verification use owned child-process and separate
workspace/context boundaries. No mandatory daemon or external service exists.

Full contract: [`candidates/EP-ARCH-C01.yaml`](candidates/EP-ARCH-C01.yaml)

### EP-ARCH-C02 — Local Control Service with Replaceable Workers

A persistent user-local control service is the sole authority. Authenticated thin clients submit
idempotent commands and render projections. Leased, fenced execution and verifier workers are
disposable and have no direct canonical write access. The local service owns persistence,
scheduling, recovery, approvals/effects, routing, evidence, and worker fencing.

Full contract: [`candidates/EP-ARCH-C02.yaml`](candidates/EP-ARCH-C02.yaml)

### EP-ARCH-C03 — Durable Event and Workflow Core with Rebuildable Projections

An append-only material event journal plus immutable referenced payloads is authoritative.
Deterministic reducers create rebuildable task, client, transcript, search, and evidence
projections. Coordinator process lifetime is not task identity. Fenced execution, provider,
protected-entry, and verifier adapters submit typed commands/events through one policy and append
boundary.

Full contract: [`candidates/EP-ARCH-C03.yaml`](candidates/EP-ARCH-C03.yaml)

## 3. Structural distinctions only

This table identifies system-shape differences. It is not a comparison result, preference,
ranking, or recommendation.

| Architecture dimension | EP-ARCH-C01 | EP-ARCH-C02 | EP-ARCH-C03 |
|---|---|---|---|
| Authority owner | Single-writer integrated local core | Persistent user-local control service | Journal append gate plus deterministic workflow reducer |
| Client boundary | Integrated local interaction in the core process boundary | Thin authenticated client over local service boundary | Projection client over command/event boundary |
| Required long-running topology | One core while the application is active | One service plus an active client | No mandatory separate daemon; coordinator may remain active while work runs |
| Execution boundary | Owned child process tree behind core supervisor | Leased/fenced disposable execution worker | Fenced adapter consuming durable workflow dispatch |
| Verification boundary | Fresh separate process/context and review workspace | Separately leased verifier worker | Separate verifier adapter that independently replays/rereads and appends immutable run events |
| Persistence authority | Transactional current state plus material history and operation/effect ledgers | Service-owned transactional state/history plus command, dispatch, result, and effect inbox/outbox | Append-only material event journal plus immutable payloads; snapshots/projections are derived |
| Scheduling model | In-core scheduler under one owner epoch | Service scheduler grants worker leases/fences | Reducer derives eligible work; coordinator grants leases/fences from durable events |
| Recovery reconstruction | Validate transactional store, rebuild projections, reconcile nonterminal ledgers | Restart service epoch, invalidate leases/IPC, reconcile inbox/outbox/effects | Validate/replay journal and payloads, rebuild projections, reconcile nonterminal workflows |
| External-effect seam | Core approval/effect ledger around adapters | Service dispatch/result/effect bridge around workers | Ordered intent/approval/dispatch/observation/readback workflow events |
| Remote-evolution boundary | Executor port must be extracted from colocated core | Worker lease/request/result interface already crosses a service boundary | Serializable dispatch/result/fence event contract; transport remains absent |
| Principal architectural commitment | Integrated single-writer core and transactional record semantics | Local control-service lifecycle and lease/effect protocol | Canonical event meanings, ordering, evolution, journal/payload boundary and reducers |

## 4. Hard-constraint generation status

No candidate contains a known hard violation. Unknowns are explicit and receive no score or pass
credit. A candidate cannot be selected while its selection-blocking spike items remain open.

| Candidate | Hard total | `SATISFIED_BY_DESIGN` | Plausible, E2-003 analysis | `UNKNOWN_REQUIRING_SPIKE` | `VIOLATED` |
|---|---:|---:|---:|---:|---:|
| EP-ARCH-C01 | 59 | 50 | 7 | 2 | 0 |
| EP-ARCH-C02 | 59 | 52 | 5 | 2 | 0 |
| EP-ARCH-C03 | 59 | 51 | 6 | 2 | 0 |

The complete per-AR evidence and owner records are in field 23 of each candidate. The full 127-ID
E1 mapping in the same field enumerates every canonical ID exactly once and inherits the status,
evidence, and owner of its primary AR. Supporting ARs remain available in the independently
verified bidirectional traceability CSV; the candidate records waive none.

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

Field 12 keeps `INTENT`, `APPROVAL`, `ATTEMPT`, `OBSERVED_EFFECT`, `CONFIRMED_EFFECT`, and
`UNKNOWN_EFFECT` distinct. Durable exact-scope approvals have principal, versions, full action,
target, expiry, revocation, one-shot consumption, replay protection and recovery rules. A response
is observation, not proof. Authoritative readback establishes known success or known non-success;
acknowledgement loss remains unknown and blocks completion and blind retry.

## 7. Task, state, recovery, context, and evidence

All candidates provide stable request/task/attempt/operation/workspace/approval/effect/artifact/
verification identities; first-outcome duplicate handling; versioned task/plan/predicate/policy;
orthogonal task axes; current ownership/fencing; finite prospective limits; durable pause, stop,
redirect and resume; retirement; and restart revalidation. Model context is always bounded and
non-authoritative.

Each candidate classifies task, operation, approvals, effects, verification, evidence, artifacts,
conversation/history, context summaries, and routing provenance as authoritative, derived,
ephemeral, or lossy. Summaries retain source/version/trust/omission provenance and cannot erase or
replace security, approval, effect, evidence, predicate, verification, or completion facts.

Every recovery model covers application crash, host restart, worker failure, model timeout, tool
timeout, lost tool result, partial write/corruption, stale workspace, duplicate operation,
duplicate effect, external acknowledgement loss, stop/force/fence, stale approval, stale
verification, waited-event delivery, protected-entry non-replay, and agent retirement. No model
uses guessed success.

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

## 10. Uncertainties and possible E2-004 work

Field 27 classifies candidate-local uncertainty as
`ANALYSIS_RESOLVABLE_E2_003`, `ARCHITECTURE_BLOCKING_SPIKE_E2_004`,
`E3_VALIDATION_OBLIGATION`, `E4_IMPLEMENTATION_DETAIL`, or `FUTURE_PRODUCT`. No spike was run.

The current candidate-specific E2-004 spike candidates are:

| Candidate | Spike candidate | Hard ARs affected |
|---|---|---|
| EP-ARCH-C01 | Supported-host process-tree force termination or durable authority fencing from an integrated supervisor | `AR-EXE-003` |
| EP-ARCH-C01 | Capture-excluded protected input inside an integrated local client boundary | `AR-SEC-006` |
| EP-ARCH-C02 | Crash/lost-ack safety of the service dispatch-outbox, worker result, and effect-readback bridge | `AR-DUR-003` |
| EP-ARCH-C02 | Protected raw-input handoff across client, local IPC, service, worker, and exact recipient without ordinary capture | `AR-SEC-006` |
| EP-ARCH-C03 | Crash safety of the journal-to-external-effect intent/dispatch/observation/readback workflow | `AR-DUR-003` |
| EP-ARCH-C03 | Protected acquisition that bypasses ordinary command, event, payload, projection, model, and telemetry capture | `AR-SEC-006` |

E2-003 must independently determine whether each listed item truly requires a bounded E2-004
spike and freeze any allowed spike contract. E2-002 did not run one and does not optimistically
score any unknown.

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
precede any `VERIFIED` transition or release of E2-003.
