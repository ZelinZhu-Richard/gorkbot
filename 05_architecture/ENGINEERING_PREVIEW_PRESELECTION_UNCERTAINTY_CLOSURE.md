# Engineering Preview preselection uncertainty closure

Status: **E2-004 AUTHOR PASS — READY_FOR_REVIEW; NOT VERIFIED**

Task: `E2-004`

Closure version: `EP-ARCH-PRESELECTION-CLOSURE-0.1`

Authoring base commit: `7b4b0d51db54a52b6ce8fe49c65bfd7406b11b47`

Closure verdict: **`NO_PRESELECTION_SPIKE_REQUIRED`**

Architecture selection: **`NOT_SELECTED`**

Preferred candidate: **`NONE`**

Accepted architecture ADRs: **0**

Experiments run / architecture spikes run / evaluation cases run / model benchmarks run / paid API calls: **0 / 0 / 0 / 0 / 0**

This is an author-produced uncertainty-closure record, not independent verification, a spike result, an architecture decision, an ADR, implementation evidence, or E3 evidence. E2-005 remains blocked until a fresh challenger and a separate verifier complete the E2-004 lifecycle.

## 1. Question, authority, and method

The question is:

> Does any architecture-blocking empirical uncertainty still require a preselection experiment before E2-005 may propose the architecture/ADR baseline?

The answer from this independent author re-derivation is **no**. The conclusion is not based on trusting the E2-003 label. It follows from a fresh reconciliation of:

- the frozen E1 product, correctness, evaluation, and release-acceptance contracts;
- the independently verified 59-hard-requirement E2-001 architecture contract;
- all three independently verified E2-002 candidate records and their 28 source uncertainty records;
- the verified E2-003 comparison, 195-cell matrix, normalized 28-item uncertainty register, and author/challenger/fixer/verifier lifecycle;
- `AR-EXE-003`, `AR-SEC-003`, `AR-SEC-006`, `AQ-003`, `AQ-004`, `AQ-010`, and canonical `E3V-001..008` contracts;
- all five historical `SPQ-E2-002-01..05` questions;
- D-016, charter §19, risks R-009/R-030, the verified reference audit/adoption matrix, and the reusable `SP-C01..SP-C10` library; and
- searches for hidden feasibility uncertainty across durability, effects, workspaces, process/client lifecycle, protected entry, evidence, verification, packaging, authority loss, fencing, resources, and testability.

Repository authority is resolved in this order: frozen E1 semantics; verified E2-001 requirement and canonical E3 obligation definitions; verified E2-002 candidate structure; verified E2-003 comparison/disposition; this E2-004 closure. Compact downstream summaries do not redefine a canonical E3V ID.

No experiment was run because the re-derived E2 preselection set is empty. The absence of a run is the required consequence of the evidence, not a favorable result.

## 2. Recomputed uncertainty universe

### 2.1 Source and normalized counts

The candidate source records and normalized register both contain 28 records, but normalization deduplicates four repeated shared-SPQ references, splits three mixed technical/model bundles, and adds one cross-candidate preference-authority record.

| View | Category | Count | Current state / owner |
|---|---|---:|---|
| E2-002 source | `ANALYSIS_RESOLVABLE_E2_003` | 10 | All resolved by E2-003 analysis; none remains analysis-owned. |
| E2-002 source | `ARCHITECTURE_BLOCKING_SPIKE_E2_004` references | 9 | Five unique historical questions, all preserved and reclassified; 0 retained in E2. |
| E2-002 source | `E3_VALIDATION_OBLIGATION` | 3 | Split into three technical bundles and three model/configuration bundles. |
| E2-002 source | `E4_IMPLEMENTATION_DETAIL` | 3 | E4 technology/configuration bundles. |
| E2-002 source | `FUTURE_PRODUCT` | 3 | Deferred product scope. |
| E2-002 source | **Total** | **28** | 9 C01 + 9 C02 + 10 C03. |
| Normalized | `PAPER_RESOLVABLE` | 10 | 10 `RESOLVED`; analytic distribution 5 tradeoff / 2 supports-property / 3 seam-present-E3-required. |
| Normalized | `E2_PRESELECTION_SPIKE_REQUIRED` | **0** | Final preselection set is empty. |
| Normalized | `E3_POSTSELECTION_TECHNICAL_VALIDATION` | 8 | S01, S02, three protected-delivery records, and three candidate technical bundles. |
| Normalized | `E3_MODEL_OR_CONFIGURATION_BENCHMARK` | 3 | One `E3V-008` bundle per candidate; all unrun and roles unassigned. |
| Normalized | E4 implementation | 3 | `E4U-C01-IMPLEMENTATION`, `E4U-C02-IMPLEMENTATION`, `E4U-C03-IMPLEMENTATION`. |
| Normalized | Future product | 3 | `FUTU-C01-PRODUCT`, `FUTU-C02-PRODUCT`, `FUTU-C03-PRODUCT`. |
| Normalized | E2-005 preference authority | 1 | `E2U-PREFERENCE-WEIGHTS`; no current weights or scores. |
| Normalized | **Total** | **28** | 10 + 0 + 8 + 3 + 3 + 3 + 1. |

The E2-003 aggregate partition `10 / 0 / 8 / 3 / 7` is therefore reproduced exactly: the final seven deferred items are three E4 bundles, three future-product bundles, and one E2-005 preference-authority item.

### 2.2 Full historical source-record reconciliation

No source uncertainty disappeared. Shared historical questions map repeatedly to one deduplicated normalized record; mixed E3 bundles map to two normalized owners.

| Source candidate | Historical source ID | Normalized record(s) | Final class / owner | Closure rationale |
|---|---|---|---|---|
| C01 | `C01-U01` | `E2U-PAPER-C01-U01` | Analysis, resolved tradeoff | Ports make bounded testing possible; broad-core coupling remains an unscored preference tradeoff. |
| C01 | `C01-U02` | `E2U-PAPER-C01-U02` | Analysis, resolved tradeoff | Remote/concurrency seam exists; extraction and migration burden is explicit preference evidence. |
| C01 | `C01-U03` | `E2U-PAPER-C01-U03` | Analysis, seam present; `E3V-001/003/006` | Persistence, workspace, exact-recipient, network, and packaging structures exist; selected mechanisms remain later validation. |
| C01 | `SPQ-E2-002-01` | `E2U-S01-DESCENDANT-CONTAINMENT` | `E3V-002` | Shared host/process mechanism validation; provenance retained. |
| C01 | `SPQ-E2-002-02` | `E2U-S02-PROTECTED-ACQUISITION` | `E3V-006` | Selected-client capture validation; provenance retained. |
| C01 | `SPQ-E2-002-03` | `E3U-C01-PROTECTED-DELIVERY` | `E3V-006` | C01 exact-recipient implementation validation after selection. |
| C01 | `C01-U04` | `E3U-C01-TECHNICAL`; `E3U-C01-MODEL-CONFIGURATION` | `E3V-001..007`; `E3V-008` | Mixed source bundle split so technical validation and model eligibility cannot be conflated. |
| C01 | `C01-U05` | `E4U-C01-IMPLEMENTATION` | E4 implementation | Concrete client/runtime/store/process/isolation/provider/package choices. |
| C01 | `C01-U06` | `FUTU-C01-PRODUCT` | Future product governance | Remote/cloud, multi-agent/client, extensions, General/Finance, SaaS remain deferred. |
| C02 | `C02-U01` | `E2U-PAPER-C02-U01` | Analysis, resolved tradeoff | Service/worker clarity trades against IPC, lease, lifecycle, and contributor burden. |
| C02 | `C02-U02` | `E2U-PAPER-C02-U02` | Analysis, supports property | Visible service lifecycle/auth/update responsibilities meet the no-hidden-state packaging floor. |
| C02 | `C02-U03` | `E2U-PAPER-C02-U03` | Analysis, seam present; `E3V-001/003/006` | Includes V-E2-002-01 `AR-DUR-005` reconciliation; selected host/toolchain/client validation remains later. |
| C02 | `SPQ-E2-002-01` | `E2U-S01-DESCENDANT-CONTAINMENT` | `E3V-002` | Deduplicated shared question. |
| C02 | `SPQ-E2-002-02` | `E2U-S02-PROTECTED-ACQUISITION` | `E3V-006` | Deduplicated shared question. |
| C02 | `SPQ-E2-002-04` | `E3U-C02-PROTECTED-DELIVERY` | `E3V-006` | C02 exact worker/use/lease/fence validation after selection. |
| C02 | `C02-U04` | `E3U-C02-TECHNICAL`; `E3U-C02-MODEL-CONFIGURATION` | `E3V-001..007`; `E3V-008` | Technical and model eligibility work remain separate. |
| C02 | `C02-U05` | `E4U-C02-IMPLEMENTATION` | E4 implementation | Concrete service/client/IPC/store/worker/isolation/provider/package choices. |
| C02 | `C02-U06` | `FUTU-C02-PRODUCT` | Future product governance | Remote/cloud/concurrency/agents/clients/extensions/verticals/SaaS deferred. |
| C03 | `C03-U01` | `E2U-PAPER-C03-U01` | Analysis, resolved tradeoff | Replay/reconstruction benefits trade against event/reducer/checkpoint/contributor burden. |
| C03 | `C03-U02` | `E2U-PAPER-C03-U02` | Analysis, resolved tradeoff | Retention/redaction/deletion/evidence semantics are coherent at design level; operational burden remains explicit. |
| C03 | `C03-U03` | `E2U-PAPER-C03-U03` | Analysis, supports property | Visible runtime/journal/reducer/projection/migration tools meet the packaging floor. |
| C03 | `C03-U04` | `E2U-PAPER-C03-U04` | Analysis, seam present; `E3V-001/003/006` | Includes V-E2-002-01 `AR-DUR-005` reconciliation; selected mechanisms remain later validation. |
| C03 | `SPQ-E2-002-01` | `E2U-S01-DESCENDANT-CONTAINMENT` | `E3V-002` | Deduplicated shared question. |
| C03 | `SPQ-E2-002-02` | `E2U-S02-PROTECTED-ACQUISITION` | `E3V-006` | Deduplicated shared question. |
| C03 | `SPQ-E2-002-05` | `E3U-C03-PROTECTED-DELIVERY` | `E3V-006` | C03 out-of-event delivery validation after selection. |
| C03 | `C03-U05` | `E3U-C03-TECHNICAL`; `E3U-C03-MODEL-CONFIGURATION` | `E3V-001..007`; `E3V-008` | Technical and model eligibility work remain separate. |
| C03 | `C03-U06` | `E4U-C03-IMPLEMENTATION` | E4 implementation | Concrete runtime/journal/schema/reducer/projection/executor/provider/package choices. |
| C03 | `C03-U07` | `FUTU-C03-PRODUCT` | Future product governance | Remote/cloud/concurrency/agents/clients/extensions/verticals/SaaS deferred. |

The cross-candidate `E2U-PREFERENCE-WEIGHTS` record is the one normalized record not copied from a candidate-local source row. Its owner is E2-005 accountable decision authority, with founder priority input if needed. Missing priority authorizes no score, rank, favorite, or preferred candidate.

## 3. Nine-condition no-spike closure

| # | Condition | Result | Exact evidence and conclusion |
|---:|---|---|---|
| 1 | All analysis-owned unknowns are resolved. | **PASS** | The register contains 10 `PAPER_RESOLVABLE` records and all 10 have `state: RESOLVED`: 5 `RESOLVED_TRADEOFF`, 2 `RESOLVED_SUPPORTS_PROPERTY`, 3 `RESOLVED_ARCHITECTURE_SEAM_PRESENT_E3_VALIDATION_REQUIRED`, 0 remaining. Comparison §§4.2, 4.5, 13, 16 and the source ledger above preserve their findings. |
| 2 | No architecture-blocking empirical uncertainty remains. | **PASS** | The matrix has 0 `ARCHITECTURE_BLOCKING_SPIKE` cells and 0 known violations. The only unvalidated hard properties are `AR-EXE-003` and `AR-SEC-006`; each has the required seam in all candidates and its empirical question depends on an unselected host/process or client/execution mechanism. The final `E2_PRESELECTION_SPIKE_REQUIRED` set is `[]`. |
| 3 | Empirical residuals are legitimately owned by E3/E4. | **PASS** | All 11 E3 residuals map to canonical `E3V-001..008`; all three E4 bundles are technology/configuration choices behind already-defined interfaces; three future bundles remain policy scope; preference authority remains E2-005. None asks E3 or E4 to invent an architecture seam or change E1 semantics. |
| 4 | Every deferred hard property has a structural architecture seam. | **PASS** | Recomputed 59 hard ARs per candidate: 57 structural requirements confirmed and 2 explicit seam/E3-outstanding properties. Candidate f02–f20/f23/f25/f30 and the matrix identify authority, boundary, fail-closed action, evidence/readback, recovery, and replaceable implementation ports. The exhaustive table in §4 records every hard AR. |
| 5 | Every E3 deferral has explicit evidence and tested-scope requirements. | **PASS** | Canonical E2-001 §9 defines property, focused owner/protocol, evidence, E4/E5 remainder, validating result, and handback for `E3V-001..008`. The complete ledger in §9 restates selected-architecture dependency, required evidence, bounded scope, and architecture-selection timing. `E3V-002` and `E3V-006` have additional concrete contracts in §§6–8. |
| 6 | Every E3 deferral fails closed. | **PASS** | Missing/failed/inconclusive evidence yields waiting, blocked, unsupported, `UNKNOWN_OUTCOME`, verification unsatisfied, or role unassigned. No tested scope broadens by analogy. `AR-EXE-003` keeps execution fenced/blocked; `AR-SEC-006` stays `WAITING_FOR_USER`/blocked with no ordinary-input fallback. |
| 7 | Every E3 deferral has an E2/ADR handback trigger. | **PASS** | Canonical §9 and the ledger distinguish implementation/configuration correction from structural contradiction. Structural inability to realize a hard property required by a linked proposed/accepted ADR stops E3 and returns evidence to E2-005/E2-006 and the E2 gate; E3 cannot redesign silently. |
| 8 | Missing evidence receives no favorable interpretation. | **PASS** | Matrix seam cells say “not empirically proven”; comparison result vocabulary grants no empirical credit; register policy sets `unknown_receives_favorable_credit: false`; all consequence profiles specify `EVIDENCE_MISSING_FAIL_CLOSED`; preferences are unweighted/unscored. |
| 9 | No preselection spike was skipped merely for convenience. | **PASS** | Every historical SPQ and every listed hidden-risk theme was rechecked against the plan §13 stage test. An experiment now would have to choose an arbitrary host/client/runtime/store/adapter that E2 has intentionally not selected, so it would test that implementation/configuration rather than candidate architecture. Relevant `SP-C01/C04/C05` contracts were reviewed but not executed because the verified E2 blocker set is empty; the absence of cost/time is not the rationale. |

All nine conditions pass. No `FAIL`, `PARTIAL`, or material `NOT_APPLICABLE` remains, so the author closure verdict is `NO_PRESELECTION_SPIKE_REQUIRED`.

## 4. All 59 hard architecture requirements

Abbreviations in this table:

- `CONFIRMED` = `CONFIRMED_SATISFIED_FOR_COMPARISON`, a design-level structural result with implementation/release evidence still outstanding.
- `SEAM / E3V-nnn` = `ARCHITECTURE_SEAM_CONFIRMED_E3_VALIDATION_OUTSTANDING`, no empirical credit.

| Hard AR | C01 | C02 | C03 | Residual owner / closure note |
|---|---|---|---|---|
| `AR-COR-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; stable IDs and duplicate-first-outcome seams. |
| `AR-COR-002` | CONFIRMED | CONFIRMED | CONFIRMED | Direct architecture constraint; versioned admitted task/plan. |
| `AR-COR-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; nine-axis authoritative state separation. |
| `AR-COR-004` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; non-compensating completion gate. |
| `AR-COR-005` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; predicate authority/adequacy seam. |
| `AR-COR-006` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; exact revision binding and stale invalidation. |
| `AR-COR-007` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; one owner plus stale-writer rejection. |
| `AR-DUR-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; durable acknowledgement boundary explicit. |
| `AR-DUR-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; restart/reconciliation owner explicit. |
| `AR-DUR-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; intent/attempt/readback/unknown bridge, no global atomicity claim. |
| `AR-DUR-004` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-002`; durable control ordering and bounds. |
| `AR-DUR-005` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; paper-closed corruption/partial/migration structure, empirical faults later. |
| `AR-DUR-006` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; retention/hold/cleanup ownership explicit. |
| `AR-DAT-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; authoritative/derived/ephemeral/lossy separation. |
| `AR-DAT-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; causal history/integrity state. |
| `AR-CTX-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; durable continuity outside model context. |
| `AR-CTX-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; source-linked compaction and invalidation. |
| `AR-WSP-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; read-only admission/support disposition. |
| `AR-WSP-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; bind-before-mutation isolation. |
| `AR-WSP-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; paper-closed broker/fail-closed seam; host negatives later. |
| `AR-WSP-004` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; original/dirty user-state protection. |
| `AR-WSP-005` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; stale detection and scoped cleanup readback. |
| `AR-EXE-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; versioned capability boundary. |
| `AR-EXE-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-002`; operation lifecycle/output bounds. |
| `AR-EXE-003` | **SEAM / E3V-002** | **SEAM / E3V-002** | **SEAM / E3V-002** | Process-tree control and authority fencing explicit; selected host/process mechanism unvalidated. |
| `AR-EXE-004` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; untrusted surfaces classified outside LLM judgment. |
| `AR-GIT-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; 30-row Git/effect enforcement seam. |
| `AR-GIT-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; exact Git state/review-package truth. |
| `AR-SEC-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; closed trust/authority precedence. |
| `AR-SEC-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; deny-by-default scoped capabilities. |
| `AR-SEC-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; exact-recipient seam paper-closed; delivery implementation later. |
| `AR-SEC-006` | **SEAM / E3V-006** | **SEAM / E3V-006** | **SEAM / E3V-006** | Protected acquisition/capture-exclusion seam explicit; selected client/configuration unvalidated. |
| `AR-SEC-004` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; destination/data/credential/redirect/zero-send boundary. |
| `AR-SEC-005` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; clean-room/provenance structural enforcement. |
| `AR-APR-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; durable exact-scope grant lifecycle. |
| `AR-APR-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; effect observation/readback/uncertainty. |
| `AR-APR-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; prohibited action remains non-overridable. |
| `AR-MOD-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-004`; provider/role-neutral product truth. |
| `AR-MOD-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-004`; purpose/eligibility/capability/zero-dispatch. |
| `AR-MOD-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-004`; explicit fallback/provider semantics. |
| `AR-EVD-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; versioned outcome-profile bundle. |
| `AR-EVD-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; stable identity/provenance/reference/redaction. |
| `AR-EVD-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; evidence integrity separate from telemetry. |
| `AR-VER-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; structurally independent verifier boundary. |
| `AR-VER-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; deterministic replay/bounded context/adequacy. |
| `AR-VER-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; verifier error/correction/stale invalidation. |
| `AR-OBS-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-007`; structured raw measurement inputs. |
| `AR-OBS-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-005`; evidence-linked explanation, no private reasoning dependency. |
| `AR-FAIL-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; typed semantic failures and retry ownership. |
| `AR-FAIL-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-007`; finite ceilings and safety reserve. |
| `AR-TST-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; fault injection/readback seams. |
| `AR-TST-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; all frozen asset-family seams, `EP-CTL-016`, 16 compositions. |
| `AR-TST-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-007`; measurement protocol without invented thresholds. |
| `AR-PERF-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-007`; finite resource/time/output/network/cost enforcement. |
| `AR-PERF-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-007`; latency/cost/output instrumentation seam. |
| `AR-PKG-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-003`; visible local packaging/no-hidden-service floor paper-closed. |
| `AR-FUT-001` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-001`; serializable replaceable boundaries, not remote implementation. |
| `AR-FUT-002` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-006`; explicit ownership scope/no global singleton floor. |
| `AR-FUT-003` | CONFIRMED | CONFIRMED | CONFIRMED | `E3V-004`; versioned extension/domain-neutral core seam. |

Recomputed per candidate: **59 hard = 57 CONFIRMED + 2 SEAM/E3 + 0 analysis remaining + 0 E2 preselection spike + 0 known violation**. No other hard AR contains a hidden empirical architecture-feasibility claim. Design confirmation is not implementation or release validation.

## 5. Hidden-preselection search

| Question tested for hidden architecture uncertainty | Classification | Basis |
|---|---|---|
| Can the architecture represent stable identity, authoritative state, versions, and single-owner writes? | `ANALYSIS_ALREADY_CLOSED` | `AR-COR-001..007`, f06/f07/f23; topology-specific writer/epoch/sequence is explicit. |
| Can acknowledged persistence and recovery preserve truth? | `ANALYSIS_ALREADY_CLOSED`; exact faults `E3_VALIDATION` | Acknowledgement, history, recovery owner, quarantine, and migration seams exist; `E3V-001` validates selected mechanisms. |
| Can partial filesystem writes be recovered without invented atomicity? | `ANALYSIS_ALREADY_CLOSED`; exact faults `E3_VALIDATION` | Every candidate itemizes actual-byte/Git readback and partial/blocked outcomes; `E3V-001/003/005`. |
| Can external effects survive lost/ambiguous acknowledgement without duplicate action? | `ANALYSIS_ALREADY_CLOSED`; exact adapters `E3_VALIDATION` | Intent/attempt/receipt/readback/unknown and no-blind-replay are explicit for C01/C02/C03; `E3V-001`. |
| Can workspace isolation and original-state protection be expressed? | `ANALYSIS_ALREADY_CLOSED`; selected host `E3_VALIDATION` | Broker, bind-before-mutation, path identity, support matrix, canaries, cleanup seams exist; `E3V-003/006`. |
| Can descendants be controlled and stale work fenced? | `E3_VALIDATION` | Residual `AR-EXE-003` is owned by `E3V-002`; §6 supplies the full contract. |
| Is client-only interruption distinct from authority loss? | `ANALYSIS_ALREADY_CLOSED` | All five lifetimes and `EP-CTL-016` are explicit; no client is authority. |
| Can protected acquisition and exact-recipient delivery be expressed? | `E3_VALIDATION` | Residual `AR-SEC-006` and delivery mechanisms are `E3V-006`; §§7–8. |
| Can evidence remain authoritative, gap-aware, exact-revision-bound, and independent of telemetry? | `ANALYSIS_ALREADY_CLOSED`; mechanism `E3_VALIDATION` | Evidence/artifact/verifier interfaces exist in all candidates; `E3V-005`. |
| Can verification reject author/executor claims independently? | `ANALYSIS_ALREADY_CLOSED`; mechanism `E3_VALIDATION` | Separate verifier context, source readback, predicate adequacy, rerun/error/stale rules exist; `E3V-005`. |
| Can provider routing preserve semantics without a selected provider? | `ANALYSIS_ALREADY_CLOSED`; adapter `E3_VALIDATION` | Neutral gateway, purpose/eligibility, explicit fallback and provenance exist; `E3V-004`; roles remain unassigned. |
| Can local packaging be explicit and contributor-operable? | `ANALYSIS_ALREADY_CLOSED`; exact setup `E3_VALIDATION` | Each candidate declares components/state/lifecycle and no hidden cloud; `E3V-003`. |
| Can authority recover after core/service/coordinator loss? | `ANALYSIS_ALREADY_CLOSED`; fault behavior `E3_VALIDATION` | New epoch/lease/owner, no-live-owner stop on dispatch, reconciliation, and unknown effect are explicit; `E3V-001/002`. |
| Can stale projections or stale service/worker results mutate authority? | `ANALYSIS_ALREADY_CLOSED`; negative proof `E3_VALIDATION` | Projections are derived and owner/fence/version checks reject stale writes; `E3V-001/005`. |
| Can resource limits and protocol inputs be represented? | `ANALYSIS_ALREADY_CLOSED`; actual values/results `E3_VALIDATION` | Counters/timestamps/ceilings are structural; `E3V-007` validates exact instrumentation. |
| Which concrete store, IPC, runtime, process API, isolation mechanism, schema, package tool, or provider SDK is used? | `E4_IMPLEMENTATION_DETAIL` | These choices sit behind the already-defined E2 boundaries and cannot relax E3 hard-property evidence. |
| Which remote/cloud/multi-agent/multi-client/extension/General/Finance/SaaS behavior is built? | `FUTURE_PRODUCT` | Compatibility seams only; behavior is outside v0.1 and unauthorized. |
| Which model/provider occupies a logical role? | `E3_VALIDATION` (`E3V-008`) | Separate benchmark authorization; failure leaves the role unassigned. |

Hidden `E2_PRESELECTION_SPIKE_REQUIRED` findings: **0**.

## 6. `AR-EXE-003` / `E3V-002` recheck

### 6.1 Architecture semantics already decided

All candidates already require, without relying on LLM cooperation:

- explicit execution authority: C01 core owner epoch, C02 service lease/fence, C03 workflow owner/fence;
- explicit supervisor ownership of parent, child, and descendant process trees;
- a process-tree containment boundary separate from control-authority fencing;
- durable pause/stop/cancel ordering and bounded settlement;
- stale execution/result/effect rejection after epoch/lease/owner fence change;
- cooperative cancellation followed by safe/available force termination or durable authority fencing;
- fail-closed blocking/unsupported scope when force termination cannot safely be supplied, never false completion;
- survivor/orphan, output, effect, and uncertainty accounting; and
- restart discovery, reconciliation, new-owner establishment, and exact outcome classification.

No candidate claims a logical fence is proof of physical descendant termination. No candidate permits a model, executor, or stale worker to self-authorize continued work or completion.

### 6.2 E3 validation contract

`E3V-002` must freeze and record the exact selected host/platform/process/configuration class, representative parent/descendant mechanisms, process-tree membership, cancellation/force attempts and permissions, monotonic timeline, owner/fence state, stale result/approval/effect rejection, survivor/orphan discovery, recovery/readback, supported scope, unsupported scope, and limitations.

Outcomes are:

- **SUCCESS:** validates only the exact tested class and configuration.
- **IMPLEMENTATION_CONFIGURATION_FAILURE:** the chosen supervisor/adapter/bounds are wrong while another conforming realization remains; correct or replace and revalidate.
- **PRODUCT_CLASS_UNSUPPORTED:** no demonstrated safe mechanism exists for that class; keep it unsupported and execution blocked/fenced.
- **ARCHITECTURE_ASSUMPTION_DISPROVEN / E3_HAND_BACK_TO_E2:** no conforming realization can provide required `AR-EXE-003` semantics for a class required by the linked `ADR-E2-003/004` baseline; stop E3 and reopen E2.
- **EVIDENCE_MISSING_FAIL_CLOSED:** missing, invalid, incomplete, or inconclusive evidence cannot broaden support; execution remains blocked/fenced.

Failure of one process-control implementation does **not** necessarily invalidate C01, C02, or C03. No candidate's architectural shape lacks the containment/fencing seam. Therefore this is not a preselection architecture spike.

## 7. `AR-SEC-006` / `E3V-006` recheck

### 7.1 Architecture semantics already decided

Every candidate already requires:

- a protected human-acquisition/takeover boundary distinct from ordinary chat, model context, repository content, tool/terminal input, transcript, logs, telemetry, evidence, and artifacts;
- suspension or exclusion of ordinary keystroke, clipboard, screen/screenshot, accessibility, terminal, model, transcript, logging, and evidence capture where required;
- exact task, operation, recipient, use, lease/epoch/fence, expiry, and one-use scope;
- raw-value exclusion from every unauthorized surface and from recovery state;
- a durable non-secret intent/authorization/receipt/provenance record only;
- cancellation, expiry, replacement, revocation, recovery, and reacquisition semantics;
- no raw replay; and
- `WAITING_FOR_USER`/blocked behavior with no ordinary-input fallback whenever safe acquisition or delivery cannot be guaranteed.

C01 places a transient protected path outside ordinary integrated pipelines; C02 uses non-secret service authorization plus direct protected client-to-current-recipient delivery; C03 keeps raw bytes outside journal/payload/projection paths and persists only non-secret causal facts.

### 7.2 E3 validation contract

A meaningful validation requires a selected client and execution configuration. E2 deliberately has neither, so a preselection prototype could not inspect the eventual capture surfaces and would create arbitrary implementation evidence.

`E3V-006` must use a synthetic sentinel only—never a real secret—and record the complete selected-surface observer inventory, exact binding, one-use delivery, capture state, raw-value absence scans, crash/cancel/replacement/revocation/expiry/recovery/reacquisition, non-secret receipt/readback, exact supported scope, unsupported scope, and independent review.

Outcomes are:

- **SUCCESS:** validates only the tested client/execution configuration.
- **IMPLEMENTATION_CONFIGURATION_FAILURE:** repair or replace the mechanism when the architecture seam remains realizable.
- **PRODUCT_CLASS_UNSUPPORTED:** fail to `WAITING_FOR_USER`/blocked and narrow that client/platform class.
- **ARCHITECTURE_ASSUMPTION_DISPROVEN / E3_HAND_BACK_TO_E2:** no conforming realization can satisfy a hard protected-entry property required by linked `ADR-E2-001/005`.
- **EVIDENCE_MISSING_FAIL_CLOSED:** remain `WAITING_FOR_USER`/blocked; never improvise ordinary entry or claim safety.

Failure of one concrete protected-input mechanism invalidates that mechanism/configuration, not automatically the architecture. Structural impossibility with no conforming realization is the distinct handback case.

## 8. Historical `SPQ-E2-002-01..05` dispositions

| Historical question | Final class / owner | Existing architecture seam | Why E2 selection does not need an experiment now | E3 evidence | Fail-closed / configuration failure / handback |
|---|---|---|---|---|---|
| `SPQ-E2-002-01`: Can descendants terminate or lose productive/effect authority after cancel, owner loss, or fence? | `E3_VALIDATION`, `E3V-002` | Supervisor-owned process identity/tree plus distinct epoch/lease/workflow fence in every candidate. | Host primitive is unselected and candidate-invariant; one mechanism failure cannot distinguish architecture shape. | Exact host/process/config, tree/timeline/force permissions, fence/effect rejection, recovery, scope, limitations. | Missing/unsafe class stays blocked/fenced; adapter failure is configuration correction; no conforming required realization hands back `ADR-E2-003/004`. |
| `SPQ-E2-002-02`: Can protected acquisition exclude ordinary capture and fail closed? | `E3_VALIDATION`, `E3V-006` | Distinct protected boundary, capture-exclusion interface, exact recipient, receipt, no replay, fail-to-WAIT in every candidate. | No client surface is selected, so a preselection harness cannot observe the final surfaces or distinguish candidates. | Synthetic sentinel, complete capture inventory/scans, exact binding, recovery/reacquisition, receipt, supported/unsupported scope. | Missing/unsafe evidence stays `WAITING_FOR_USER`/blocked; mechanism failure is correction/unsupported class; no conforming required realization hands back `ADR-E2-001/005`. |
| `SPQ-E2-002-03`: Can C01 deliver once to its co-resident exact recipient without ordinary capture? | `E3_VALIDATION`, `E3V-006` | C01 transient recipient/use/fence path outside ordinary core/model/log/evidence capture. | Architecture has already chosen the boundary; behavior depends on selected client/runtime mechanism. | Delivery/capture/crash/revocation/recovery/forbidden-surface/receipt/no-replay evidence. | Fail to WAIT; mechanism/config failure first; structural inability reopens `ADR-E2-005`. |
| `SPQ-E2-002-04`: Can C02 preserve exact recipient/use/lease/fence through client-to-current-worker delivery? | `E3_VALIDATION`, `E3V-006` | Non-secret service authorization, direct protected path, current lease/fence, revocation and reacquisition. | Testing requires selected client, IPC/auth, worker, and protected carrier; an arbitrary prototype is not topology proof. | Authorization, direct delivery, replacement/crash/revocation, forbidden surfaces, receipt and no replay. | Fail to WAIT; bad carrier/IPC/config is correction; no conforming C02 realization reopens `ADR-E2-005`. |
| `SPQ-E2-002-05`: Can C03 keep raw delivery outside events/payloads/projections and preserve truthful recovery? | `E3_VALIDATION`, `E3V-006` | Out-of-event broker, exact recipient/fence, non-secret causal receipt/recovery, no raw replay. | Testing requires selected journal/payload/broker/client/runtime mechanisms; architecture ordering and exclusion seams already exist. | Broker/recipient/crash/append ordering, absence scans, receipt/readback, recovery truth, no replay. | Fail to WAIT; broker/config error is correction; no conforming C03 realization reopens `ADR-E2-005`. |

All five questions retain their original IDs and source candidate references. None is deleted, passed, or represented as a successful experiment.

## 9. E2 versus E3 boundary and complete E3 ledger

E2 decides **what** exists: structure, authority, interfaces, trust boundaries, containment/protected-entry seams, recovery, evidence, and verification architecture. E3 validates **how** a proposed selected baseline realizes those seams for a named mechanism/configuration and bounded support class. E3 may not change the E2 contract or silently redesign it.

The canonical meaning of each `E3V` ID below is the independently verified E2-001 §9 register. E2-003 candidate f30 records and the comparison provide candidate-specific focus, but do not redefine those IDs.

| E3V | Exact property and selected-baseline dependency | Required evidence and bounded scope | Failure / missing evidence / handback | May E2-005 propose before it runs? |
|---|---|---|---|---|
| `E3V-001` | Selected persistence/recovery mechanism preserves acknowledgements, ownership, partial writes, duplicates, resume revalidation, and ambiguous effects. Depends on chosen state/history/operation/effect boundaries. | Exact baseline/mechanism/config IDs; prospective fault schedule; before/after authority; duplicate first outcome; dispatch/receipt/readback; preserved raw evidence; limitations; representative focused subset only. | Adapter/store defect is correction. Acknowledged loss, stale acceptance, duplicate effect, fabricated continuity, or architecture-incapable recovery hands back linked `ADR-E2-002/003/004/005`. Missing evidence leaves recovery unvalidated/blocked/unknown. | **YES**, if ADR records this obligation and handback. |
| `E3V-002` | Selected process/control mechanism supplies truthful pause/stop/force-or-fence, descendants, output/effect bounds, recovery. Depends on selected host/process classes. | §6 contract: exact host/config, tree, timeline, force primitive/permissions, fence rejection, survivors, recovery, support/unsupported scope. | Config/adapter correction; unsupported class blocked/fenced; structural inability for required class hands back `ADR-E2-003/004`; missing evidence fail-closed. | **YES**; no candidate-discriminating mechanism exists before selection. |
| `E3V-003` | Selected workspace/isolation/Git/local-package boundary protects user state and is contributor-operable. Depends on selected runtime, platform, package, workspace mechanisms and support matrix. | Representative admitted repository/path/topology/dirty/stale/cleanup/setup cases; inventories, canaries, bind ordering, readback, support matrix, reproducibility, limitations. | Local adapter/docs/config defect is correction; narrow unsupported scope; structural root/user-state escape or undeclared mandatory service hands back `ADR-E2-001/004/009`; missing scope unsupported. | **YES**; E2 qualitative burden is sufficient for proposal, exact mechanism is not selected. |
| `E3V-004` | Selected provider boundary preserves product truth, purpose/eligibility, fallback, provider-specific result/failure/cancel, data policy, provenance, usage/cost. Depends on chosen gateway/adapter contract. | Begin with controlled offline provider-shape replays; manifest, requested/resolved routes, capability/eligibility, zero-dispatch, stream/tool/failure/cancel/fallback, usage/cost, limitations. Live calls separately gated. | Provider/config/adapter failure is correction/ineligibility; interface inability to preserve required semantics hands back `ADR-E2-001/005/006/008`; missing evidence means no dispatch/eligibility claim. | **YES**; no provider or role occupant is assumed. |
| `E3V-005` | Selected state/evidence/verifier mechanism preserves authority/derived separation, exact revision binding, gaps/tamper/staleness, replay, adequacy, verifier error/correction. Depends on chosen state/evidence/artifact/verifier structures. | Exact candidate/revision/schema/actor identities; representative stale/gap/tamper/adequacy/verifier-failure faults; bundles/references; independent readbacks/replay; limitations. | Validator/projection defect is correction. Executor-self-report dependence, stale-pass acceptance, telemetry authority, nondeterministic authority, or unavoidable evidence loss hands back `ADR-E2-002/003/005/007/008`; missing evidence keeps verification/completion unsatisfied. | **YES**, with explicit obligation and no claim of current verification. |
| `E3V-006` | Selected trust/capability/approval/secret/protected-entry boundary denies unauthorized flow/effect and provides safe protected acquisition/delivery. Depends on every selected enforcement point and client/execution configuration. | §7 contract plus focused threat/enforcement map, synthetic canaries, positive/negative requests, zero-dispatch/effect readback, approval/revocation/replay, clean-room/path/process/network, independently reviewed scope/limitations. | Policy/adapter/fixture/config correction; unsafe class unsupported/WAITING; structural inability hands back `ADR-E2-001/004/005/008`; missing evidence fails closed. | **YES**, because required seams are defined and no selected mechanism exists earlier. |
| `E3V-007` | Selected instrumentation/limit mechanism produces protocol inputs and enforces finite ceilings without redefining results. Depends on selected instrumentation, limits, reference environment, and workload. | Exact mechanism/config/environment/workload; raw timestamps/outcomes/usage/cost/limits; sample derivations; ceiling denials; uncertainty/missingness; focused slices of eight protocols; no post-result definition change. | Instrumentation/config correction or truthful performance miss does not automatically reopen ADR. Unrepresentable required inputs or unenforceable ceilings hand back `ADR-E2-002/007/008/009`; missing evidence grants no SLO/limit claim. | **YES**; preselection measurement would conflate architecture with arbitrary implementation. |
| `E3V-008` | Candidate systems/configurations may occupy logical roles only through separately authorized benchmark evidence. Depends on provider-neutral routing baseline and frozen model/role/configuration protocol. | Exact route/model/tool/config/task evidence, raw outputs/failures/refusals, cost/latency, grader/verifier, eligibility and limitations; separate budget/data/credential authorization. | Failure/missing leaves role unassigned; alternate configuration may be evaluated. Hand back `ADR-E2-006` only if an indispensable ADR capability is structurally impossible with no compliant route. | **YES**, provided ADR assumes no occupant and no indispensable unvalidated capability. |

### 9.1 Normalized E3-deferral mapping

| Normalized residual(s) | E3 owner |
|---|---|
| `E2U-S01-DESCENDANT-CONTAINMENT` | `E3V-002` |
| `E2U-S02-PROTECTED-ACQUISITION` | `E3V-006` |
| `E3U-C01-PROTECTED-DELIVERY`; `E3U-C02-PROTECTED-DELIVERY`; `E3U-C03-PROTECTED-DELIVERY` | `E3V-006` candidate-scoped selected configuration |
| `E3U-C01-TECHNICAL`; `E3U-C02-TECHNICAL`; `E3U-C03-TECHNICAL` | Candidate-specific `E3V-001..007` focused validation plan |
| `E3U-C01-MODEL-CONFIGURATION`; `E3U-C02-MODEL-CONFIGURATION`; `E3U-C03-MODEL-CONFIGURATION` | Candidate-specific `E3V-008`; roles remain unassigned |

No E3V contains hidden preselection feasibility. E3V results may reveal configuration cost, performance, or a structural contradiction later; before mechanism selection, a prototype would not produce architecture-valid comparative evidence. Structural contradiction is deliberately preserved as handback rather than assumed away.

## 10. E4 and future-product boundary

### 10.1 E4 implementation ledger

| E4 record | Concrete items | Why legitimate E4 detail | Guardrail |
|---|---|---|---|
| `E4U-C01-IMPLEMENTATION` | client/runtime; embedded store; schema/codec; process API; isolation mechanism; provider SDKs/adapters; package/update tooling | Choices implement C01's already-defined ports, authority, persistence, supervisor, gateways, and packaging boundary. | E4 cannot weaken E1/E2, claim a support class without E3, or turn an adapter failure into architecture success. |
| `E4U-C02-IMPLEMENTATION` | service/client/runtime; IPC/auth; store/schema; worker supervisor; isolation mechanism; provider adapters; installer/updater | Choices implement the already-defined service/worker/lease and direct protected-delivery seams. | Same guardrail; E3 validation precedes support/eligibility claims. |
| `E4U-C03-IMPLEMENTATION` | runtime/journal/payload; event/schema/reducer; projections/checkpoints; executor/isolation; provider adapters; client/package | Choices implement the already-defined journal/reducer authority and out-of-event protected path. | Same guardrail; projection/event implementation cannot redefine canonical authority. |

Additional canonical E4 detail includes concrete finite defaults under an independently reviewed policy, adapter-specific time/output limits, supported build/package configuration, module organization, tuning, and migration tooling. E2-005 must register accountable ownership/review for finite verification-rerun, deterministic-repetition, and correction-attempt ceilings before scored freeze. E4 inherits no unresolved architecture feasibility or product semantics.

### 10.2 Future-product and other deferred ledger

| Record | Deferred items | Current consequence |
|---|---|---|
| `FUTU-C01-PRODUCT` | remote/cloud workers; multi-agent/client; skills/connectors; General/Finance; SaaS | Preserve versioned seams only; no behavior or implementation authorized. |
| `FUTU-C02-PRODUCT` | remote/cloud workers; actual concurrency/agents/clients; extensions/verticals/SaaS | Same. |
| `FUTU-C03-PRODUCT` | remote/cloud workers; actual concurrency/agents/clients; extensions/verticals/SaaS | Same. |
| `E2U-PREFERENCE-WEIGHTS` | priority/weight policy for six preferences | E2-005 accountable decision authority only; absent policy means no score/rank/preferred candidate. |

## 11. Unified consequence, fail-closed, and handback model

| Outcome | Required consequence |
|---|---|
| `SUCCESS` | Validate only the exact selected mechanism/configuration/tested scope. Do not generalize to another host, client, workload, provider, model, or product class. |
| `IMPLEMENTATION_CONFIGURATION_FAILURE` | Correct or replace the adapter/mechanism/fixture/wiring/configuration and independently revalidate. Do not automatically invalidate an architecture or select another candidate. |
| `PRODUCT_CLASS_UNSUPPORTED` | Narrow the host/client/workload/effect class and remain blocked, waiting, denied, or unsupported. It becomes architecture handback only when a linked ADR requires the class/property and no conforming alternative remains. |
| `ARCHITECTURE_ASSUMPTION_DISPROVEN` | Evidence shows the selected structure/interface cannot satisfy a required hard property and no conforming realization remains. Stop affected E3 work. |
| `E3_HAND_BACK_TO_E2` | Return exact evidence to E2-005/E2-006, revise/rechallenge/reverify proposed ADRs/baseline, and reevaluate the E2 gate as applicable. E3 cannot redesign silently. |
| `EVIDENCE_MISSING_FAIL_CLOSED` | Missing, invalid, incomplete, or inconclusive evidence grants no success credit and cannot broaden support: wait/block/deny/unknown/unverified/unassigned as the property requires. |

No failure state falls through to continued build or false completion.

## 12. Decision-neutrality and candidate viability

### 12.1 Deferred-question decision neutrality

| Deferred area | Could a valid preselection result favor or eliminate only one candidate now? | Conclusion |
|---|---|---|
| Descendant containment / force / fence | **No.** All candidates require the same host primitive class plus topology-specific authority token; no concrete host mechanism is selected. | `E3V-002`; one mechanism failure is not architecture elimination. |
| Protected acquisition/capture | **No.** Acquisition surface is shared and no client is selected. | `E3V-006`; fail to WAIT until selected-config evidence. |
| Candidate protected delivery | **No architecture-valid preselection result.** The seams differ, but a run requires arbitrary client/runtime/IPC/journal/broker technology and would test that choice. | Candidate-scoped `E3V-006`; structural impossibility later hands back. |
| Durability/recovery/effects | **No current architecture blocker.** Abstract acknowledgement, ownership, effect, recovery, and readback semantics are complete; a prototype would instantiate arbitrary stores/adapters. | `E3V-001`; qualitative topology/reversibility differences already recorded. |
| Workspace/package/provider/evidence mechanisms | **No current architecture blocker.** Exact platform/toolchain/adapter evidence depends on selection. | `E3V-003/004/005/006`; failures retain correction/unsupported/handback split. |
| Instrumentation, latency, resource, overhead | A concrete implementation could measure differently, but a preselection measurement would be implementation-confounded and cannot prove architecture viability or a stable preference value. | `E3V-007`; E2-003 retains qualitative tradeoffs only. |
| Model/provider role eligibility | **No.** Gateway shape is neutral and no occupant is assumed. | `E3V-008`; failure leaves role unassigned. |

Zero spikes is therefore decision-neutral for architecture viability. It does not claim that future configurations will pass.

### 12.2 Candidate viability

| Candidate | Known hard violation | Analysis-owned unknown | E2 preselection empirical question | E3 residual | E4 detail | Readiness |
|---|---:|---:|---:|---|---|---|
| `EP-ARCH-C01` | 0 | 0 | 0 | `E3V-001..008`, including C01 protected delivery | `E4U-C01-IMPLEMENTATION` | `ANALYTICALLY_VIABLE`; `READY_FOR_E2_005_AFTER_E2_004_INDEPENDENT_VERIFICATION` |
| `EP-ARCH-C02` | 0 | 0 | 0 | `E3V-001..008`, including C02 protected delivery | `E4U-C02-IMPLEMENTATION` | `ANALYTICALLY_VIABLE`; `READY_FOR_E2_005_AFTER_E2_004_INDEPENDENT_VERIFICATION` |
| `EP-ARCH-C03` | 0 | 0 | 0 | `E3V-001..008`, including C03 protected delivery | `E4U-C03-IMPLEMENTATION` | `ANALYTICALLY_VIABLE`; `READY_FOR_E2_005_AFTER_E2_004_INDEPENDENT_VERIFICATION` |

This table is not a rank, score, recommendation, favorite, or selection.

## 13. ADR input readiness

E2-005 may propose—never accept—the ADR set after E2-004 is independently verified. Each row already has viable alternatives, hard constraints, qualitative preference evidence, risk, reversibility, E3 obligation, and handback. E3 results are not prerequisites unless the ADR would assume the unvalidated result rather than attach it as an obligation.

| Future ADR | Comparison/alternatives ready | Constraints, risk, reversibility | Required attached validation / handback | E2-005 input status |
|---|---|---|---|---|
| `ADR-E2-001` system/client/core | C01 integrated core; C02 service/workers; C03 command/event core. | Client non-authority, durable acknowledgement, local-first; topology migration and client/platform risk explicit. | `E3V-003/004/006`; hand back if required authority/trust boundary cannot be realized. | **READY AFTER INDEPENDENT E2-004 VERIFICATION** |
| `ADR-E2-002` state/persistence/history/projections/migration | Transactional core, service store, event/journal alternatives. | Truth, acknowledgement, partial-write, integrity, retention, migration; foundational lock-in explicit. | `E3V-001/005/007`; hand back on structural truth/recovery/evidence failure. | Same. |
| `ADR-E2-003` orchestration/ownership/recovery/idempotency | Epoch owner, service leases, workflow owner/fence. | Stale-writer, duplicate/effect, lifecycle, future-owner scopes; token migration explicit. | `E3V-001/002/005`; hand back on unrealizable ownership/fencing/recovery. | Same. |
| `ADR-E2-004` workspace/process/isolation/Git/local-remote | Supervisor port, worker interface, command/event adapter. | Isolation-before-mutation, process tree, 30 Git rows, support matrix; adapter portability explicit. | `E3V-001/002/003/006`; hand back if a required class cannot be safely contained. | Same. |
| `ADR-E2-005` capability/approval/secret/effect/reconciliation | Integrated authority, service authority/direct raw path, command admission/out-of-event broker. | Exact authority, no replay, unknown effects, protected capture/recipient; client/adapter replacement implications explicit. | `E3V-001/004/005/006`; hand back when no conforming protected/effect realization remains. | Same. |
| `ADR-E2-006` model/provider/routing/context | Embedded, service, or command/event gateway with bounded context. | Provider neutrality, purpose/eligibility, fallback, provenance, no occupant assumed. | `E3V-004/005/008`; role remains unassigned on failure; structural gateway contradiction hands back. | Same. |
| `ADR-E2-007` verification/evidence/artifacts | Integrated manifests, service evidence, journal-position evidence. | Independent verification, revision binding, integrity, large-output/migration portability. | `E3V-005/007`; hand back on structural evidence/verifier impossibility. | Same. |
| `ADR-E2-008` observability/audit/metering/failure | Integrated semantic separation, service telemetry, journal plus derived telemetry. | Telemetry not authority, stable failures, metering inputs, redaction; schema evolution explicit. | `E3V-004/005/007`; hand back only on hard structural contradiction. | Same. |
| `ADR-E2-009` packaging/future seams | Integrated package, visible service package, local journal/runtime package. | No hidden service/cloud, contributor workflow, bounded future interfaces, Finance/SaaS deferred. | `E3V-003/006/007`; hand back on required local/support-boundary impossibility. | Same. |

No ADR is created or accepted here. Preferred candidate remains `NONE`.

## 14. No-favorable-unknown audit

The comparison, matrix, uncertainty register, E2-003 handoff, R-009/R-030, PROJECT_STATE, and TASK_REGISTRY were searched for language equivalent to “assumed supported,” “likely works,” “expected to pass,” “probably available,” “safe enough,” or “implementation should handle.” No outstanding empirical property receives such treatment.

The active language instead states:

- implementation conformance remains unproven;
- `AR-EXE-003` and `AR-SEC-006` are `ARCHITECTURE_SEAM_CONFIRMED_E3_VALIDATION_OUTSTANDING`;
- supported host/client scope is not empirically proven;
- missing evidence is `EVIDENCE_MISSING_FAIL_CLOSED`;
- model/provider roles remain unassigned;
- no weights, scores, rank, favorite, or preferred candidate exist; and
- E2-005 remains blocked by the missing independent E2-004 verification.

Candidate source `candidate_assumptions` remain proposals/unknowns, not comparison passes; the matrix separately records design structure and future validation. This closure does not upgrade them.

## 15. E2-003 verifier NOTE carry-forward

| Note | E2-004 disposition |
|---|---|
| `V-E2-003-N1` README refresh | Already handled by the founder commit at the current base; no E2-004 work. |
| `V-E2-003-N2` hard-cell category labels | Non-material classification convenience; this closure does not use them as preference groups or weights. |
| `V-E2-003-N3` SP-C library | Relevant `SP-C01/C04/C05` contracts were reviewed. With no retained E2 spike, reuse is not applicable now; E2-005 must reuse or explicitly distinguish relevant contracts when freezing E3 work. |
| `V-E2-003-N4` compact E3 technical bundles inherit evidence/handback | Material carry-forward accepted. This closure uses canonical E2-001 §9 meanings and makes evidence, scope, failure, missing-evidence, and handback explicit for every `E3V`. E2-005 must preserve them as explicit fields rather than rely on bundle inheritance. |
| `V-E2-003-N5` `AR-SEC-003` paper result plus E3 delivery | Preserved exactly; no action. |
| `V-E2-003-N6` stricter seam/outstanding status | Preserved exactly; no empirical credit. |
| `V-E2-003-N7` historical timestamps/commit wording | Historical record only; no closure impact. |
| `V-E2-003-N8` shared no-live-owner interval | Rechecked under authority-loss/lifecycle audit; candidly represented and not a hidden candidate-specific hard violation. |

Historical verifier records are unchanged.

## 16. Closure record and governance consequence

| Field | Author result |
|---|---|
| Base commit | `7b4b0d51db54a52b6ce8fe49c65bfd7406b11b47` |
| Nine closure conditions | `PASS / PASS / PASS / PASS / PASS / PASS / PASS / PASS / PASS` |
| Final preselection spike IDs | `[]` |
| Final preselection spike count | `0` |
| Experiments run | `0` |
| Architecture spikes executed | `0` |
| Paid calls / external effects | `0 / 0` |
| Application code | `NONE` |
| Evaluation cases / model benchmarks | `0 / 0` |
| Candidate viability | C01/C02/C03 `ANALYTICALLY_VIABLE`, unranked |
| E2-005 | `BACKLOG`; blocked by `E2_004_NOT_INDEPENDENTLY_VERIFIED` |
| E2 gate | `NOT_EVALUATED` |
| Architecture / preferred candidate / accepted ADRs | `NOT_SELECTED / NONE / 0` |
| Autonomy | `NOT_ELIGIBLE`; autonomous build `NOT_AUTHORIZED` |
| S1-003 | `DEFERRED_NOT_EXECUTED` |

Author result: **`NO_PRESELECTION_SPIKE_REQUIRED`**.

Required next lifecycle action: **`MODE: REVIEW_TASK_E2-004`**. A fresh challenger must try to falsify this rationale and a separate verifier must independently reconcile the full set before E2-004 can become `VERIFIED` or E2-005 can become `READY`.
