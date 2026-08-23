# S1-001 customer-workflow scorecard and falsification plan

Status: FIXER PASS — READY FOR INDEPENDENT REVIEW; NOT VERIFIED

Research date: 2026-08-23

Scored data: `03_product/S1-001_SCORED_HYPOTHESES.csv`

Current-workaround research: `02_research/S1-001_CURRENT_WORKAROUND_EVIDENCE_2026-08-23.md`

## Outcome first

**CONFIRMED GOVERNANCE STATE — D-012:** H1 and H2 are co-equal discovery candidates. Neither is validated, selected as the final beachhead, or authorized for implementation. H8 is formally scored as a challenger-added hypothesis but is not automatically elevated to co-equal discovery status.

**VERIFIED REPOSITORY FACT:** `CUSTOMER_EVIDENCE = ZERO` for every hypothesis. There are no customer interviews, customer artifacts, observed workflows, usage records, pilot commitments, willingness-to-pay observations, payments, traction, or retention records in the repository.

**CORRECTED SCORE RESULT:** under the corrected weights H1 scores `60.4`, H2 `57.4`, H8 `57.0`, H6 `56.4`, H3/H4 `51.8`, H5 `50.4`, and H7 `48.6`. These are structured analyst judgments, not measured market differences. Alternative weightings change ranks: H8 leads under competition/WTP-heavy weights, and H2 ties H6 under feasibility-heavy weights. The score does not support a single winner.

**DISCOVERY ALLOCATION:** give H1 and H2 the same interview count, artifact request, concept-test sequence, pilot threshold, price-test form, sampling-bias control, and review standard. Let customer evidence determine which survives.

## Historical audit trail and D-012

1. The original AUTHOR ranking scored H2 `76.8` and H1 `75.6`, called them a directional tie, then gave H1 the first discovery slot under D-011.
2. The independent CHALLENGER found the H1/H2 choice too sensitive, the H1 substitute screen incomplete, the H2 market screen incomplete, and parts of the H1 tie-break already represented in scored feasibility criteria.
3. The founder issued D-012. It supersedes D-011 **only for current discovery allocation**. D-011 remains historical and provisional.
4. Current state: H1 and H2 are co-equal discovery candidates; neither is selected. D-006 and D-007 remain PROVISIONAL.

No H1-only quota, contract, build position, or incumbent advantage remains in the current plan.

## Evidence and claim discipline

| Class | Meaning in this artifact |
|---|---|
| `E` | Current public evidence or repository fact supports the input. Public product evidence is competition evidence, never customer evidence. |
| `J` | Analyst or founder judgment maps structure/evidence to the rubric. It is not an observed fact. |
| `U` | Evidence is unknown or insufficient. A wholly unknown criterion defaults to neutral `3` and cannot receive `4` or `5`. |

Every scored cell has an adjacent `_basis` cell in the CSV beginning with one or more of `E`, `J`, or `U`, followed by a source ID or concise rationale. `E+J` means evidence exists but score mapping remains judgment. `U+J` means a neutral or conservative judgment is used because customer evidence is missing.

The CSV is the per-cell provenance record. The score is not numerical precision about a population; it is a reproducible comparison under declared assumptions.

## Corrected scoring method

Each hypothesis receives an integer `1`–`5` for each of 15 criteria:

- `1`: structurally unfavorable for a first wedge
- `2`: material weakness
- `3`: mixed, neutral, or substantially unknown
- `4`: favorable structure with an explicit evidence or judgment basis, still unvalidated
- `5`: unusually favorable structure with a strong non-customer basis; never used to impute missing demand evidence

The corrected total is:

```text
sum(score × corrected_weight) / 5
```

### Failure direction correction

The ambiguous `cost_of_failure` criterion is renamed **failure safety**.

**Higher = safer / lower consequence of agent failure under the bounded pilot contract.**

| Score | Failure-safety meaning |
|---:|---|
| 1 | Failure could cause serious or difficult-to-recover external harm even with proposed controls. |
| 2 | Significant security, decision, or recovery cost remains plausible. |
| 3 | Mixed: work is reviewable, but failure can still create material rework or risk. |
| 4 | Primarily read-only/reversible with a clear approval boundary; false signals still have a cost. |
| 5 | Isolated, synthetic, and readily reversible with negligible external consequence. |

All hypotheses were rescored in this direction. The old values and totals were not preserved.

### Corrected weights and double-counting audit

| Criterion | Original | Corrected | Corrected rationale |
|---|---:|---:|---|
| Pain and urgency | 11 | 13 | Core demand question; neutral while customer evidence is absent. |
| Current-workaround gap | 5 | 9 | Competition and actual switching motivation were underweighted. |
| Workflow frequency | 7 | 8 | Recurrence matters, but software cadence is not customer frequency. |
| Economic value | 8 | 10 | Makes value/WTP evidence more influential. |
| Failure safety | 5 | 5 | Necessary risk screen with corrected favorable direction. |
| Willingness to delegate | 6 | 6 | Separate from pain; cannot exceed neutral without evidence. |
| Integration tractability | 7 | 5 | Reduced to limit feasibility dominance. |
| Security manageability | 6 | 5 | Reduced; still a gating constraint. |
| Sales-cycle speed | 7 | 5 | Unknown sales-cycle guesses receive less leverage. |
| Ease of reaching users | 8 | 7 | Founder access remains useful but is not customer demand. |
| Prototype feasibility | 10 | 7 | Reduced to avoid selecting a merely easy demo. |
| Differentiation | 8 | 9 | Strong substitutes require more weight. |
| Expansion potential | 4 | 4 | Retained as a secondary platform-path judgment. |
| Bootstrap revenue potential | 5 | 5 | WTP proxy remains neutral until price evidence exists. |
| Investor relevance | 3 | 2 | Lowest priority before customer evidence. |
| **Total** | **100** | **100** | |

Original feasibility/safety factors (`failure safety + integration + security + prototype`) held `28` weight; corrected weight is `22`. Original competition/WTP proxies (`gap + differentiation + bootstrap revenue`) held `18`; corrected weight is `23`. Core demand (`pain + frequency + economic value`) rises from `26` to `31`. Distribution (`sales cycle + reach`) falls from `15` to `12`. This does not eliminate correlation, so sensitivity analysis is mandatory.

Platform necessity is deliberately **not** another positive score. It is analyzed separately as a constraint so a workflow is not rewarded merely because a persistent-agent platform can technically perform it.

## Corrected score table

| Corrected rank | ID | Customer × workflow | Corrected total | Discovery status | Evidence confidence | Customer evidence |
|---:|---|---|---:|---|---|---|
| 1 | H1 | Small B2B SaaS team × official-source competitor-change decision ledger | 60.4 | CO-EQUAL DISCOVERY CANDIDATE under D-012 | LOW | 0_NONE |
| 2 | H2 | Small software team × bounded issue to tested PR with independently checked completion evidence | 57.4 | CO-EQUAL DISCOVERY CANDIDATE under D-012 | LOW | 0_NONE |
| 3 | H8 | Small software team × independent PR reproduce-and-verify evidence bundle | 57.0 | CHALLENGER_ADDED; retain as H2 refinement pending review/discovery | LOW | 0_NONE |
| 4 | H6 | Small web agency × bounded website change to checked preview | 56.4 | SCORED BACKUP; NOT SELECTED | LOW | 0_NONE |
| 5T | H3 | Data/analytics team × reproducible data-quality decision report | 51.8 | SCORED BACKUP; NOT SELECTED | LOW | 0_NONE |
| 5T | H4 | Product/user-research team × traceable interview synthesis | 51.8 | SCORED BACKUP; NOT SELECTED | LOW | 0_NONE |
| 7 | H5 | Applied research team × literature intelligence workspace | 50.4 | SCORED BACKUP; NOT SELECTED | LOW | 0_NONE |
| 8 | H7 | Operations-heavy small business × browser record reconciliation | 48.6 | SCORED BACKUP; NOT SELECTED | LOW | 0_NONE |

The corrected rank does not override D-012. A `3.0`-point H1/H2 difference is only three one-level judgment changes on weight-5 criteria, and the demand cells are uniformly unobserved.

## Sensitivity analysis

All scenarios below use the **corrected scores**, including corrected failure-safety direction. “Original” means the original AUTHOR weights applied to corrected scores; it does not reuse the defective original cells.

Abbreviations: `P` pain, `G` workaround gap, `F` frequency, `V` economic value, `S` failure safety, `Dg` delegation, `I` integration, `Sec` security, `Sa` sales cycle, `R` reach, `Pr` prototype, `Df` differentiation, `E` expansion, `B` bootstrap revenue, `Iv` investor relevance.

| Weighting scheme | P | G | F | V | S | Dg | I | Sec | Sa | R | Pr | Df | E | B | Iv | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Original AUTHOR | 11 | 5 | 7 | 8 | 5 | 6 | 7 | 6 | 7 | 8 | 10 | 8 | 4 | 5 | 3 | 100 |
| Corrected balanced | 13 | 9 | 8 | 10 | 5 | 6 | 5 | 5 | 5 | 7 | 7 | 9 | 4 | 5 | 2 | 100 |
| Demand-heavy | 20 | 12 | 15 | 15 | 3 | 8 | 3 | 3 | 4 | 5 | 3 | 5 | 2 | 1 | 1 | 100 |
| Feasibility-heavy | 6 | 4 | 5 | 5 | 10 | 4 | 12 | 10 | 4 | 4 | 18 | 4 | 4 | 5 | 5 | 100 |
| Competition/WTP-heavy | 10 | 18 | 6 | 13 | 3 | 5 | 3 | 3 | 5 | 5 | 4 | 18 | 2 | 4 | 1 | 100 |

| Scheme | Ordered corrected totals |
|---|---|
| Original AUTHOR weights | H1 62.4; H2 58.4; H6 57.6; H8 57.2; H4 52.2; H3 51.6; H5 51.0; H7 45.8 |
| Corrected balanced | H1 60.4; H2 57.4; H8 57.0; H6 56.4; H3/H4 51.8; H5 50.4; H7 48.6 |
| Demand-heavy | H1 58.8; H2/H8 57.0; H6 56.4; H4 53.6; H3 53.4; H7 52.6; H5 51.0 |
| Feasibility-heavy | H1 67.4; H2/H6 59.0; H8 55.4; H4 53.2; H5 52.8; H3 51.2; H7 39.2 |
| Competition/WTP-heavy | H8 55.6; H1 55.2; H2 53.2; H6 52.8; H7 52.0; H3 49.4; H4 49.2; H5 48.2 |

**MATERIAL SENSITIVITY:** H8 moves from fourth under original weights to first under competition/WTP-heavy weights; H2 ties H6 under feasibility-heavy weights; H7 moves sharply when competition is emphasized. Since demand evidence is zero and rankings change, the score cannot select a single winner.

## Corrected hypothesis briefs

### H1 — small B2B SaaS competitor-change decision ledger

**PROVISIONAL HYPOTHESIS:** a directly responsible founder, product lead, or product-marketing lead at a 3–30 person B2B SaaS company with 5–15 named competitors and no dedicated CI analyst may value a governed decision ledger beyond current monitoring products.

- Current alternatives already provide page monitoring, before/after diffs, URLs/timestamps, importance scoring, reports, integrations, and multi-competitor views, often at self-serve prices (SRC-067, SRC-068, SRC-075–SRC-090, SRC-105).
- Corrected `current_workaround_gap = 2` and `differentiation = 2`.
- Residual differentiator to test: customer-owned materiality rule, explicit coverage/unknown state, approval-gated master-record proposal, and exact readback after an approved update. It is not established as unique or valuable.
- Minimum sufficient runtime for most value: **scheduled automation**. A multi-tool persistent agent is optional unless governed record maintenance proves valuable.
- Pain, meaningful-event frequency, active time, dissatisfaction, delegation, pilot interest, and WTP are all UNKNOWN/NOT_TESTED.

#### H1 trigger and three clocks

- Trigger: a new interval since the last accepted snapshot, or a named decision requiring a fresh comparison.
- Software check cadence: DESIGN PROPOSAL—daily for ordinary allowlisted pages, with any faster cadence tested only when justified.
- Human reporting cadence: DESIGN PROPOSAL—weekly digest plus an exceptional material alert.
- Strategically meaningful change/pain frequency: UNKNOWN. Interview evidence must establish it; machine checks and weekly reports do not count as customer pain frequency.

### H2 — bounded issue to tested PR with independently checked evidence

**PROVISIONAL HYPOTHESIS:** a technical founder or engineering lead at a 2–20 developer team may delegate bounded GitHub issues when merge remains human-controlled and completion evidence is independently checked.

- GitHub Copilot, Codex, Claude Code, Cursor, Devin, and Jules materially overlap task-to-code, autonomous execution, tests, PRs, background work, review, CI follow-up, approvals, and evidence artifacts (SRC-064, SRC-065, SRC-091–SRC-104).
- Corrected `current_workaround_gap = 2` and `differentiation = 2`.
- Potential differentiator to test, not a market fact: **independently verified completion evidence** from a separately provisioned reproducer that checks the declared acceptance predicate, relevant tests/behavior, and current remote PR/CI state after the author run stops.
- Do not claim that competitors lack verification. Current products document second opinions, multi-agent review, verification steps, logs, artifacts, and video proof. The narrower separate-reproduction gap is UNKNOWN.
- Minimum sufficient runtime: **multi-tool persistent agent**, which current coding-agent products already provide.
- Pain, delegation, dissatisfaction, pilot interest, WTP, and acceptable failure contract are UNKNOWN/NOT_TESTED.

### H8 — independent PR reproduce-and-verify evidence bundle

Origin: `CHALLENGER_ADDED_HYPOTHESIS`.

**PROVISIONAL HYPOTHESIS:** the same small-team buyer may want a read-mostly verifier for a human- or agent-authored PR: freeze base/head commits and acceptance predicate, provision a clean environment, reproduce relevant tests/behavior, check remote PR/CI state, and emit a contradiction-preserving evidence bundle without merging.

- Corrected total `57.0`; close to H2 and first under competition/WTP-heavy weights.
- Not clearly dominated, so it requires explicit challenger/verifier discussion.
- Same buyer, systems, and completion decision as H2; current classification is **retain as an H2 refinement**, not a separate co-equal discovery candidate or quota.
- Minimum sufficient runtime: **multi-tool persistent agent**, though incumbent review/coding products may absorb it as a feature.
- Customer evidence and all gates: `ZERO / NOT_TESTED`.

### H3–H7

| ID | Key structural judgment | Minimum sufficient runtime | Primary falsifier |
|---|---|---|---|
| H3 | Reproducible data report is verifiable, but Hex/notebooks are strong substitutes and live data can be sensitive. | Product feature or scheduled automation | Analysts prefer direct notebook control or correction cost exceeds savings. |
| H4 | Traceable synthesis is feasible on redacted transcripts, but Dovetail covers provenance/memory and PII is central. | Product feature | Security/consent blocks delegation or current repository is satisfactory. |
| H5 | Fixed public corpora are tractable, but Elicit covers screening/extraction/alerts and budgets/frequency are unknown. | Scheduled automation | Existing tools satisfy the job or required accuracy makes correction prohibitive. |
| H6 | Code-to-preview is tractable on a known stack, but coding agents plus Vercel already serve most of the flow. | Multi-tool persistent agent | Existing code/preview process is satisfactory or stack variance destroys repeatability. |
| H7 | Browser/record work has the strongest runtime need but the worst safety, security, and prototype profile. | Multi-tool persistent agent | No repeatable vertical process, setup exceeds value, or customers reject credential handling. |

No hypothesis currently requires a multi-agent team. Ability to use multiple agents is not scored as customer value.

## Comparable H1/H2 discovery gates

Every threshold below is a **DESIGN PROPOSAL** for falsification. Every result is `NOT_TESTED`. Thresholds are not customer observations.

### Equivalent discovery effort

| Dimension | H1 | H2 |
|---|---|---|
| Qualified interviews | 8 | 8 |
| Participant independence | One person per organization; at least 4/8 outside founder first-degree network | Same |
| Interview length/procedure | 45 minutes; last actual workflow first, neutral concepts later | Same |
| Artifact request | Permitted recent watchlist, prior report/ledger, or live process walk-through | Permitted recent bounded issue, PR/review artifact, or live process walk-through |
| Concept comparison | Current alternative vs residual governed evidence contract | Current alternative vs residual independent-reproduction contract |
| Sample cycle | One operator-run, no-external-write sample after interview | Same |
| Pilot ask | Two cycles, named owner/input/date/criterion | Same |
| Written price test | USD 500 for four weeks | Same |

If service effort differs, record operator minutes and cost; do not secretly give either candidate more support or count it as stronger demand.

### Predeclared falsification table

| Dimension | H1 observable pass criterion | H2 observable pass criterion | Current result |
|---|---|---|---|
| Customer pain | At least 5/8 describe a specific decision-linked missed/stale/research burden in the preceding 90 days and a concrete consequence; at least 4/8 anchor it to a permitted artifact or walk-through. | At least 5/8 describe a specific bounded-issue/review failure or delay in the preceding 90 days and a concrete consequence; at least 4/8 anchor it to a permitted artifact or walk-through. | NOT_TESTED |
| Workflow frequency | At least 5/8 personally performed the decision-linked comparison at least twice in the preceding 60 days. Machine checks and report cadence do not count. | At least 5/8 personally triaged at least four bounded issues or agent/human PR reviews in the preceding 30 days. | NOT_TESTED |
| Current-workaround dissatisfaction | At least 4/8 show one repeated manual step, missed state, or correction in their actual named stack and explicitly identify the step they would replace; neutral comparison includes current page monitors/CI suites. | At least 4/8 show one repeated manual check, reopen, CI/review gap, or correction in their actual named stack and identify the step they would replace; neutral comparison includes current coding/review agents. | NOT_TESTED |
| Willingness to delegate | At least 5/8 specify an own-work public watchlist they would permit for read-only testing and name allowed/blocked actions. | At least 5/8 specify an authorized repository/fixture they would permit for a no-merge, bounded test and name allowed/blocked actions. | NOT_TESTED |
| Measurable value | At least 4/8 provide a recent baseline for active time, correction time, missed-change consequence, or decision delay and agree to one before/after success metric. | At least 4/8 provide a recent baseline for issue cycle time, review time, reopen/rework, escaped defect, or verification effort and agree to one success metric. | NOT_TESTED |
| Willingness to pilot | At least 3/8 make a written two-cycle commitment with permitted input, named owner, start date within 30 days, and completion criterion. | Same, using an authorized bounded issue/PR and runnable environment. | NOT_TESTED |
| Willingness to pay | At least 3/8 explicitly accept in writing a USD 500/four-week paid-pilot offer with scope and terms, including at least one organization outside the founder's first-degree network. A payment is stronger evidence; enthusiasm is not acceptance. | Same. | NOT_TESTED |
| Required integrations | At least 6/8 can receive first value from public URLs plus CSV/memo and an approval-gated test ledger; fewer than 3/8 require private/authenticated/regulated sources for first value. | At least 6/8 can receive first value from one Git repo, reproducible test command/environment, and PR/CI read access; fewer than 3/8 require production credentials or deployment/merge authority. | NOT_TESTED |
| Failure tolerance | At least 5/8 accept explicit unknowns, human approval before any record write, and the predefined false-positive/false-negative review process; fewer than 3/8 require an unsupported near-zero miss rate for first value. | At least 5/8 accept no-merge/no-deploy operation, explicit unknowns, human review, and verifier disagreement; fewer than 3/8 require autonomous merge/deploy or an unsupported near-zero defect rate. | NOT_TESTED |
| Competitive differentiation | After the neutral actual-alternative comparison and sample, at least 4/8 say the residual contract would change a real workflow decision **and** at least 3 of those 4 make the written pilot commitment. | Same for separate reproduction/current-state evidence versus their actual coding-agent/CI/review stack. | NOT_TESTED |

Failing any pain, frequency, dissatisfaction, delegation, pilot, or price gate removes that candidate from the build queue unless the segment/job is explicitly revised and re-reviewed. Passing interviews without the price gate is not commercial validation.

### H8 probes inside H2 discovery

H8 gets no separate quota. In every H2 interview, ask after the actual-workflow walkthrough:

1. Who or what currently verifies an agent/human PR independently of the author?
2. Would a clean-environment reproduction bundle change approval, merge, or review time?
3. Which evidence is already sufficient: CI, author logs, video, code review, human test, or separate reproduction?
4. Would the participant pilot/pay for verification without buying issue-to-code generation?

If at least 4/8 prefer verification-only and at least 3/8 make the same written pilot commitment, reopen whether H8 is a distinct workflow. This is a DESIGN PROPOSAL and remains NOT_TESTED.

## Making sample and feasibility gates executable

### Operational definitions

- **Qualified interview:** participant meets the candidate screen, directly owned the named workflow, and recounts a real occurrence in the specified time window. Interest without a real occurrence is unqualified.
- **Artifact-backed:** participant permits viewing a redacted artifact or live process. The repository stores only a sanitized evidence ID and observation, not confidential material.
- **Written pilot commitment:** explicit yes containing owner, permitted input, start date, two-cycle scope, and completion criterion.
- **Written price acceptance:** explicit acceptance of the proposed USD 500/four-week scope and terms. A counteroffer is recorded separately; praise, a waitlist signup, or “keep me posted” does not count.
- **Concierge cycle:** a named human operator performs the proposed bounded workflow once using participant-permitted historical or current inputs, records active minutes and corrections, and makes no external write/message/merge/deploy.
- **Independent truth-set curator:** a second person who did not operate the sample freezes and labels the comparison set before inspecting the sample output. Disagreements remain visible.

### H1 sample and truth set

1. Participant names the decision, 5–15 competitors, allowlisted pages, prior accepted snapshot/date, and material fields before the run.
2. Operator checks the frozen prior/current pages and produces the proposed ledger/memo without external writes.
3. Curator independently labels changed/unchanged/unavailable pages and material fields from the frozen source set using the participant's predeclared materiality rule.
4. Compare coverage, unsupported claims, precision/recall, correction minutes, and decision usefulness. Do not count software check volume as customer frequency.

### H2/H8 sample and truth set

1. Participant supplies an authorized historical or fixture issue/PR, immutable base/head commit IDs, setup command, test command, and acceptance predicate before the run.
2. Operator performs the evidence-only reproduction in a clean environment with no push, merge, deploy, or production credential.
3. Curator is the repository owner or an independent engineer who did not operate the sample; they freeze the expected acceptance/test set before viewing output.
4. Compare reproducibility, evidence coverage, contradictions, false-completion claims, correction minutes, and whether the bundle changes the participant's review decision.

### Prototype feasibility gates — only after customer evidence authorizes a build

All thresholds are DESIGN PROPOSALS and `NOT_RUN`.

| Check | H1 proposed threshold | H2/H8 proposed threshold |
|---|---|---|
| Representative cases | 3 authorized watchlists across 2 consecutive cycles | 3 authorized repos/fixtures with 2 bounded cases each |
| Evidence coverage | 100% of output claims link to prior/current source, or are explicit UNKNOWN | 100% of completion claims link to immutable commit/environment/test/log evidence, or are explicit UNKNOWN |
| Unsupported material claims | 0 | 0 |
| Truth-set performance | At least 90% precision and 90% recall on curated material changes | At least 90% agreement with curated acceptance/test outcomes; disagreements must be shown, never silently resolved |
| Unauthorized action | 0 writes/messages | 0 pushes/merges/deploys/production writes |
| External-state verification | Approved test-ledger update occurs exactly once and passes readback | Current remote PR head and CI/check state reread after verification; no claim based on stale local state |
| Human correction | Median no more than 15 active minutes/cycle | Median no more than 30 active minutes/case |
| Required recording | Cost, latency, unavailable-source rate, false positive/negative, corrections, false completion | Cost, latency, setup failure, flaky tests, contradictions, corrections, false completion |

Threshold values are proposals chosen to make the next test falsifiable. They are not benchmark results, customer requirements, or production-readiness claims.

## Interview recruiting plan

**DESIGN PROPOSAL:** 16 discovery interviews, 8 H1 and 8 H2, one participant per organization. No outreach, recruiting, incentive, or spend is authorized or executed by S1-001.

### Qualification screens

- H1: founder, product lead, or product-marketing lead; 3–30 staff; 5–15 named competitors; no dedicated CI analyst; personally performed the defined decision-linked workflow at least once in the preceding 60 days. Record one directly responsible owner per organization.
- H2: technical founder or engineering lead; 2–20 developers; maintains a Git repository with a runnable bounded test path; personally triaged a bounded issue or reviewed a PR in the preceding 30 days.

At least 4/8 in each group should be outside the founder's first-degree network. If the quota is missed, report the sampling skew; do not lower it silently. H8 is probed within H2. H3–H7 receive no first-wave allocation under D-012.

### Interview sequence

1. Reconfirm qualification, direct responsibility, and last actual occurrence.
2. Walk through trigger, active/elapsed time, tools, people, artifacts, errors, completion state, and approval boundary.
3. Record the actual named workaround and why it remains in use.
4. Request a permitted redacted artifact/live process; absence is recorded.
5. Only after behavior capture, compare the actual workaround with the residual concept. Randomize concept order.
6. Run or schedule at most one no-write concierge sample under the definitions above.
7. Ask for the exact pilot and price commitments; record “no,” conditions, counteroffers, and non-response.
8. Separate participant report, observed artifact, exact permitted quotation, analyst inference, and proposal.

Default to notes. Do not commit participant names, contact details, recordings, credentials, private data, or identifiable quotations to this public repository. A proposed interview incentive up to USD 50/person (maximum USD 800) requires separate founder approval; no budget or outreach is authorized here.

## Decisions and non-decisions

### Current decisions

- D-012 controls discovery allocation: H1 and H2 are co-equal.
- H8 is scored and retained as an H2 refinement requiring explicit reviewer discussion.
- H1/H2 have comparable, executable, predeclared gates and equal effort.
- Failure safety uses the explicit favorable direction above.
- Platform necessity is a qualitative constraint, not a score bonus.

### Not decided

- No final customer, beachhead, workflow, differentiator, MVP, price, market size, sales motion, architecture, integration stack, model/provider role, benchmark, application implementation, or production scope is selected.
- D-006 and D-007 remain PROVISIONAL.
- H1/H2/H8 remain NOT_TESTED; customer evidence remains zero.
- S0-004/S0-005 remain unchanged. S1-002 is not started.

## Required independent review

The next reviewer should:

1. Recompute the corrected total and all five weighting scenarios from the CSV.
2. Validate every score has an E/J/U basis and every cited source ID exists.
3. Challenge H1/H2 competitor matrices against the current primary sources.
4. Decide whether H8 remains an H2 refinement or warrants separate discovery, without treating its score as customer evidence.
5. Check H1/H2 gate equivalence, operational definitions, and threshold labels.
6. Confirm D-012, D-006, D-007, customer-evidence zero, and the no-build/no-MVP boundaries remain intact.
7. Do not mark S1-001 VERIFIED unless an independent verifier satisfies the repository completion rule.
