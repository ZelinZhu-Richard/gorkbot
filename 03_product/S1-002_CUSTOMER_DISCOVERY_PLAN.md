# S1-002 symmetric customer-discovery experiment plan

Status: AUTHOR PASS — READY FOR INDEPENDENT REVIEW; NOT VERIFIED

Planning date: 2026-08-23

Authority: `MODE: PLAN_STAGE_1` founder instruction and confirmed D-012

Execution task: S1-003, blocked until this plan is independently verified and the founder separately authorizes outreach and resolves the incentive decision

## Outcome first

This artifact defines a falsifiable, behavior-first experiment for H1 and H2. It does not execute discovery.

- **VERIFIED REPOSITORY FACT:** S1-001 is independently VERIFIED.
- **CONFIRMED GOVERNANCE STATE:** H1 and H2 are co-equal discovery candidates under D-012. Neither is selected.
- **VERIFIED REPOSITORY FACT:** `CUSTOMER_EVIDENCE = ZERO`. No interview, customer artifact, pilot, price acceptance, payment, usage, or retention evidence exists in the repository.
- **DESIGN PROPOSAL — NOT TESTED:** the first wave is 8 ICP-qualified interviews for H1 and 8 for H2, using comparable procedures and hard gates.
- **H8 TREATMENT:** H8 is the independently reproduced verification/evidence mechanism inside H2. It receives no separate quota.
- **OUTREACH/SPEND STATE:** no outreach, recruitment, interview, incentive purchase, or spend is authorized or performed by S1-002.

No result in this plan confirms D-006 or D-007 or selects a customer, workflow, differentiator, MVP, price, architecture, integration, or model role.

## Research question

> Which workflow has enough demonstrated pain, recurrence, current-alternative dissatisfaction, delegability, measurable value, willingness to pilot, and willingness to pay to deserve becoming the provisional beachhead?

The unit of analysis is one ICP-qualified participant from one independent organization. A statement, contact, company, or artifact may not be counted more than once or for both hypotheses.

## Claim and denominator discipline

The following definitions apply before recruitment begins:

- **ICP-qualified interview:** the participant meets the structural company, role, and direct-responsibility screen. Recent pain, high frequency, tool dissatisfaction, pilot interest, and WTP are outcomes, never screening requirements.
- **Behaviorally anchored interview:** an ICP-qualified participant can recount a specific occurrence, or explicitly confirms after a bounded lookback that no occurrence happened. A lack of a recent occurrence is disconfirming evidence and remains in the denominator.
- **Artifact-backed:** the participant permits the interviewer to inspect a redacted artifact or walk through the live process. Only a sanitized observation and evidence reference may enter this public repository.
- **Valid denominator:** all completed ICP-qualified interviews, including negative, rare, satisfied, non-delegable, and unwilling-to-pay cases. Missing answers, refusal to show an artifact, and conditional interest do not disappear from the denominator.
- **Administrative invalidation:** an interview may be replaced only when the participant fails the structural screen, leaves before the behavioral section begins, or a documented interviewer/recording failure prevents use. It may not be excluded because its evidence is unfavorable.
- **One-organization rule:** one participant per organization across the entire first wave. An overlapping H1/H2 participant is assigned before concept exposure and can count toward only one quota.

This definition deliberately avoids selecting only people who already perform the workflow frequently.

**Prospective refinement of S1-001:** the verified S1-001 scorecard used “qualified interview” to require a real occurrence in the target time window. S1-002 narrows that term into `ICP-qualified` and `behaviorally anchored` before execution. S1-003 must use the structural `ICP-qualified` denominator above so absence of a recent occurrence can falsify pain/frequency gates rather than disappear through screening. This does not rewrite S1-001's historical artifact; if S1-002 is independently verified, it prospectively governs S1-003.

## H1 hypothesis contract

Every item below is a **DESIGN PROPOSAL / HYPOTHESIS — NOT TESTED**, except descriptions of public alternatives already verified by S1-001.

| # | Required item | H1 definition |
|---:|---|---|
| 1 | Exact ICP | An operating B2B SaaS company with 3–30 employees, a live product, 5–15 named direct competitors, no full-time competitive-intelligence analyst, and a founder, head of product, or product-marketing lead who directly owns a competitor-informed pricing, positioning, roadmap, launch, or enablement decision. |
| 2 | Buyer | The founder/CEO when they hold the budget, otherwise the head of product or product-marketing leader with authority to approve a USD 500 design-partner pilot. Buyer identity and actual authority must be observed, not inferred from title. |
| 3 | Daily user | The primary operator who gathers, compares, interprets, and records competitor changes. “Daily user” means operational user; daily usage is not assumed. |
| 4 | Trigger | Either a named decision that requires a fresh comparison or a new interval since the last accepted snapshot. Interviews must distinguish event-triggered research, machine-check cadence, and human review cadence. |
| 5 | Job to be done | When a competitor-informed decision arises, establish what materially changed across the named set, what did not, what could not be checked, and what record should be updated so the owner can act without redoing the research. |
| 6 | Current workaround | Manual page checks, search alerts, spreadsheets/docs, ad hoc LLM research, scheduled assistants, SMB page monitors, and/or CI suites such as the categories verified in S1-001. The participant's actual named stack controls the comparison. |
| 7 | Expected workflow frequency | Hypothesis: the human performs a decision-linked comparison at least twice in 60 days. Software polling and digest cadence do not count as human workflow frequency. |
| 8 | Pain hypothesis | Recent comparisons are missed, stale, noisy, or labor-intensive enough to cause a concrete decision delay, rework, lost confidence, missed response, or repeated manual burden. |
| 9 | Economic-value hypothesis | A governed comparison can reduce active research/correction time or shorten a named pricing, positioning, launch, roadmap, or sales-enablement decision. The participant must supply the baseline and metric. |
| 10 | Trust/delegation hypothesis | The owner will permit a real public watchlist and prior accepted snapshot for read-only work, while specifying allowed and blocked actions and retaining approval over any master-record write. |
| 11 | Existing-alternative dissatisfaction hypothesis | The actual monitor/CI/manual stack leaves a repeated manual reconciliation, coverage-state, materiality, or decision-record step that the owner wants to replace. Generic preference for “better summaries” is insufficient. |
| 12 | Pilot hypothesis | At least three of eight will make a written two-cycle commitment using their own permitted watchlist, with an owner, input, start date within 30 days, and completion criterion. |
| 13 | Willingness-to-pay hypothesis | At least three of eight, including one outside the founder's first-degree network, will explicitly accept in writing the standardized USD 500/four-week pilot scope. This is a lower-bound price test, not final pricing. |
| 14 | Required-integration hypothesis | At least six of eight can receive first value from public URLs, a customer-supplied watchlist/prior snapshot, CSV or memo output, and an approval-gated test ledger; no more than two require authenticated, private, regulated, or production-system access. |
| 15 | Failure-tolerance hypothesis | At least five of eight accept explicit unknown/unavailable states, human review, no silent write, and a declared false-positive/false-negative review process; no more than two require an unsupported near-zero miss rate. |
| 16 | Differentiation hypothesis | Beyond already available detection, diffs, timestamps, summaries, scoring, and digests, a customer-owned materiality rule, explicit coverage/unknown state, approval-gated record proposal, and readback materially change a real decision or delegation choice. |
| 17 | Disconfirming evidence | Rare or non-decision-linked use; current solution considered adequate; no replaceable step; interest only in ordinary monitoring; unwillingness to delegate a public watchlist; first value requires private sources; low consequence; no pilot; no written price acceptance. |
| 18 | Kill criteria | Kill the current H1 formulation if any hard gate fails. In particular, kill it if scheduled monitoring plus the current workflow is adequate, if the residual governed-record layer changes no real decision, or if pilot/WTP gates fail. Do not preserve H1 merely because it is easy to prototype. |
| 19 | Advance criteria | H1 advances only if every hard gate in the predeclared decision table passes. Passing creates a provisional beachhead candidate for independent review; it does not validate demand, set final pricing, or authorize a build. |

## H2 hypothesis contract

Every item below is a **DESIGN PROPOSAL / HYPOTHESIS — NOT TESTED**, except descriptions of public alternatives already verified by S1-001.

| # | Required item | H2 definition |
|---:|---|---|
| 1 | Exact ICP | A commercial software team with 2–20 active developers, a Git-based pull-request workflow, runnable tests for at least some bounded changes, and a technical founder, CTO, or engineering lead who directly owns issue triage or PR completion decisions. |
| 2 | Buyer | The technical founder/CTO or engineering leader with authority to approve repository access and a USD 500 design-partner pilot. Buyer identity and actual authority must be observed. |
| 3 | Daily user | The person who triages bounded issues, reviews human- or agent-authored PRs, checks tests/CI, and decides whether completion evidence is sufficient. “Daily user” does not assert daily usage. |
| 4 | Trigger | A bounded issue selected for delegation or an incoming human/agent PR whose claimed completion must be accepted, rejected, or returned for rework. |
| 5 | Job to be done | When bounded engineering work is delegated, determine whether the issue was actually resolved in the declared environment and current PR state, expose contradictions/unknowns, and prepare a human-controlled merge decision without redoing all verification manually. |
| 6 | Current workaround | Manual reproduction and review, CI, author-run tests, peer review, issue-to-PR agents, AI code review, logs, screenshots/video, and security checks. The participant's actual Git/CI/coding-agent stack controls the comparison. |
| 7 | Expected workflow frequency | Hypothesis: the participant personally triages or reviews at least four bounded issues/PRs in 30 days. Coding-agent task volume alone does not count. |
| 8 | Pain hypothesis | A recent bounded issue/PR produced measurable delay, rework, reopen, false completion, redundant verification effort, or an escaped defect that current tools did not satisfactorily prevent. |
| 9 | Economic-value hypothesis | Independent evidence can reduce review/reproduction time, shorten issue cycle time, reduce reopen/rework, or prevent a measurable failure. The participant supplies the baseline and success metric. |
| 10 | Trust/delegation hypothesis | The owner will permit an authorized repository or fixture, immutable base/head commits, setup/test commands, and read access to PR/CI state for a no-merge/no-deploy test, with explicit allowed and blocked actions. |
| 11 | Existing-alternative dissatisfaction hypothesis | The actual coding-agent/CI/review stack leaves a repeated manual check, untrusted author assertion, environment mismatch, stale remote state, or completion ambiguity the owner wants to replace. Desire for faster code generation alone does not support H2. |
| 12 | Pilot hypothesis | At least three of eight will make a written two-cycle commitment using an authorized bounded issue/PR and runnable environment, with owner, input, start date within 30 days, and completion criterion. |
| 13 | Willingness-to-pay hypothesis | At least three of eight, including one outside the founder's first-degree network, will explicitly accept in writing the same USD 500/four-week pilot scope. This is not final pricing. |
| 14 | Required-integration hypothesis | At least six of eight can receive first value from one Git repo/fixture, immutable commits, a reproducible setup/test path, and PR/CI read access; no more than two require production credentials or merge/deploy authority. |
| 15 | Failure-tolerance hypothesis | At least five of eight accept no merge/deploy, explicit unknowns, human review, and visible verifier disagreement; no more than two demand autonomous merge/deploy or an unsupported near-zero defect rate. |
| 16 | Differentiation hypothesis | The residual value is not issue-to-PR generation. A separately provisioned verifier that independently receives the acceptance predicate, reproduces relevant behavior/tests after the author stops, rereads current remote PR/CI state, and preserves contradictions materially changes a real delegation or merge decision. This is H8 inside H2. |
| 17 | Disconfirming evidence | Current agent/CI/review evidence is sufficient; verification is not a recurring burden; participants value generation but not independent reproduction; repository/access requirements are unacceptable; evidence does not alter a decision; no pilot; no written price acceptance. |
| 18 | Kill criteria | Kill the current H2 differentiation if the issue-to-PR commodity layer is the only valued benefit, if independent reproduction produces no behaviorally anchored trust/delegation lift, or if any hard gate fails. Do not preserve H2 merely because the platform narrative is strong. |
| 19 | Advance criteria | H2 advances only if every hard gate passes, including the H8 incremental-value condition inside the differentiation gate. Passing creates a provisional beachhead candidate for independent review, not a build authorization. |

## H8 treatment inside H2

**HYPOTHESIS — NOT TESTED:**

> Does an independently reproduced verification/evidence bundle materially increase trust or willingness to delegate issue-to-PR work?

H8 receives no separate quota, buyer, score, price, or interview. Every H2 interview records delegation before the residual concept and after the separate-reproduction concept.

A **material H8 lift** requires behaviorally anchored evidence of at least one of the following:

1. the participant grants a specific permission or real-workflow scope only with the independent bundle;
2. the participant identifies a named recent PR decision that the bundle would have changed and explains how;
3. the participant removes or shortens a specific manual verification step and commits to measure it; or
4. the participant changes from no/conditional pilot intent to a qualifying written pilot commitment because of the bundle.

A numeric trust-rating increase or “I would trust it more” without a changed action is Level 0 and does not count.

H8's in-H2 threshold is at least 4/8 material lifts and at least 3 of those participants making the standard written pilot commitment. H8 can be reconsidered as a distinct allocation only after this threshold is met and an independent challenger/verifier determines that the buyer, trigger, job, workflow, or value proposition is materially distinct. It is not automatically elevated.

## Comparable interview procedure

Both guides use the same 45-minute sequence and evidence rules:

| Minutes | Phase | Rule |
|---:|---|---|
| 0–5 | Consent and structural screen | Confirm role/company/direct responsibility. Do not screen on pain, frequency, dissatisfaction, or interest. |
| 5–23 | Last actual occurrence | Ask for the last real workflow, trigger, people, tools, time, errors, consequence, completion check, and artifact. Do not describe the concept. |
| 23–30 | Current workaround | Capture unaided alternatives first; then use the standardized recognition list. Ask what is adequate and what is not. |
| 30–35 | Delegation and failure boundary | Start with past delegation behavior, then permitted data/actions and unacceptable failures. |
| 35–40 | Residual concept test | Present the candidate-specific neutral contract only after the behavior checkpoint. Ask what actual step or decision changes. |
| 40–45 | Pilot, price, and disconfirmation | Ask for a concrete two-cycle commitment, then the identical USD 500/four-week price test, then reasons not to proceed. |

The interviewer may not convert praise, a waitlist signup, a referral, or “keep me posted” into a pilot or WTP signal.

## Evidence hierarchy

Evidence is classified per claim/dimension, not only once per interview. An interview's `evidence_level` records the strongest level reached but never substitutes for the hard gates.

| Level | Name | Required evidence | Does not qualify |
|---:|---|---|---|
| 0 | Opinion | General belief, feature preference, rating, or hypothetical interest without a specific past case or action. | “That sounds cool,” a high trust score, waitlist interest, or willingness if it were free. |
| 1 | Specific behavior | A dated or bounded remembered occurrence naming trigger, tools, people, steps, and outcome. | Generic “we do this a lot.” |
| 2 | Repeated measured behavior | More than one occurrence in the declared window plus a concrete time, money, delay, rework, or failure baseline. Corroboration method is recorded. | An unbounded estimate with no examples. |
| 3 | Direct artifact/workflow observation | Redacted artifact, logs, calendar/ticket history, report, PR, or live walkthrough corroborates the behavior and baseline. | A promised artifact that was not shown. |
| 4 | Operational commitment | Written two-cycle pilot commitment naming owner, real permitted input/access, start date within 30 days, and success criterion. | Verbal interest, a meeting request, or a conditional “maybe.” |
| 5 | Economic commitment | Payment/deposit, signed paid-pilot order, or an equivalent signed commitment naming amount, budget owner, and execution date. A generic non-binding LOI is Level 4 at most. | A price reaction or unsigned budget claim. |
| 6 | Repeated economic behavior | Repeated paid use, renewal, expansion, or retained workflow usage. | Not expected in the first interview wave. |

Strength modifiers must remain visible: direct observation is stronger than participant interpretation; recent evidence is stronger than remote memory; actual action is stronger than stated intent; independent organizations are stronger than duplicated/network-linked evidence.

## First-wave sample design

### Size and symmetry

- 8 ICP-qualified interviews for H1.
- 8 ICP-qualified interviews for H2.
- 16 organizations maximum in the first wave; one participant and one counted hypothesis per organization.
- 45 minutes per interview, the same artifact request, concept timing, pilot ask, price test, and evidence rubric.
- H8 is tested inside the 8 H2 interviews.
- H3–H7 receive no first-wave quota. Restoring a backup probe requires a separate task amendment and may not reduce H1/H2 symmetry.

### Within-hypothesis controls

For each hypothesis:

- at least 4/8 must be outside the founder's first-degree network;
- at least 4/8 should be buyer-operators or confirmed budget owners; titles alone do not prove authority;
- target at least 4/8 current/recent users of a direct product alternative and no more than 4/8 primarily manual-workaround users;
- avoid having more than 5/8 in one size sub-band (H1: 3–10 vs 11–30 employees; H2: 2–7 vs 8–20 developers);
- recruit one person per organization and record recruitment channel/network tier.

The alternative-use and size controls are sampling targets. If they are missed, report the skew and do not silently redefine the ICP or gates.

### Overlap handling

A technical founder at a 3–30 person B2B SaaS company may qualify for both hypotheses. Before any concept is shown, assign overlapping candidates by alternating to the group with fewer valid interviews, while respecting quotas. Record `overlap_eligible=true` in restricted recruitment notes. The participant sees only the assigned concept. Secondary comments may be noted but cannot enter the other denominator, evidence count, or quotation set.

### Exclusions

Exclude from the decision sample:

- people without direct responsibility for the workflow within the last 12 months;
- consultants/agencies describing client work rather than their own organization's workflow;
- H1 companies with a dedicated full-time CI analyst or outside the 3–30 employee range;
- H2 teams without a Git/PR workflow, without any bounded test path, or outside the 2–20 developer range;
- hobby projects, student exercises, and pre-product teams without an operating workflow;
- employees of direct monitoring/CI or coding-agent/review vendors when discussing their own product category;
- duplicate participants or organizations.

Experts outside the ICP may be interviewed under a future task but cannot be counted in S1-003.

## Scorecard and coding rules

The header-only schema is in `03_product/S1-002_DISCOVERY_SCORECARD.csv`. S1-002 must leave it with exactly zero customer rows.

Core enums:

- `hypothesis`: `H1` or `H2`; never `H8`.
- `qualification`: `ICP_QUALIFIED`, `SCREEN_FAIL`, or `ADMIN_INVALID`. Only `ICP_QUALIFIED` enters the eight-person denominator; a negative workflow result is not a screen failure.
- `network_tier`: `FIRST_DEGREE`, `WARM_INTRO`, or `OUTSIDE_NETWORK`.
- `current_alternative_satisfaction`: `ADEQUATE`, `MIXED`, `INADEQUATE`, or `NOT_USED`.
- `pain_score`: `0` no recent occurrence/consequence; `1` inconvenience only; `2` recurring burden without quantified consequence; `3` measurable time/delay/rework/decision consequence; `4` artifact-backed material consequence. Gate calculations use the underlying fields, not an average pain score.
- `delegation_tier_before_concept` and `delegation_tier_after_concept`: `0` no real input; `1` synthetic/redacted only; `2` real read-only input; `3` reversible draft/branch write with human review; `4` consequential write only behind explicit approval. No autonomous merge/deploy is offered.
- `pilot_commitment`: `NO`, `VERBAL_ONLY`, `CONDITIONAL`, or `WRITTEN_QUALIFYING`.
- `wtp_signal`: `NONE`, `PRICE_REACTION_ONLY`, `COUNTEROFFER`, `WRITTEN_500_ACCEPTANCE`, or `ECONOMIC_COMMITMENT`.
- `evidence_level`: integer `0`–`6` from the hierarchy above.
- Boolean fields use `TRUE`, `FALSE`, or `NOT_ASKED`; `NOT_ASKED` cannot count as success.

Each record must preserve disconfirming evidence and contradictions. The interviewer and coder may not collapse conflicting statements into a positive summary.

## Predeclared hard gates

Every threshold below is a **DESIGN PROPOSAL — NOT TESTED**. All gates are hard: a strong result on one cannot compensate for a fatal weakness on another.

| Gate | H1 pass condition | H2 pass condition |
|---|---|---|
| G1 Recent consequential pain | At least 5/8 describe a decision-linked missed/stale/manual burden in the prior 90 days with a concrete consequence. | At least 5/8 describe a bounded-issue/review failure or delay in the prior 90 days with a concrete consequence. |
| G2 Recurring human workflow | At least 5/8 personally performed the decision-linked comparison at least twice in 60 days; machine/report cadence excluded. | At least 5/8 personally triaged/reviewed at least four bounded issues/PRs in 30 days. |
| G3 Alternative dissatisfaction | At least 4/8 identify a repeated step or failure in their actual named monitor/CI/manual stack that they would replace. | At least 4/8 identify a repeated check, reopen, CI/review gap, or correction in their actual named stack that they would replace. |
| G4 Measurable economic value | At least 4/8 provide a recent time/money/delay/failure baseline and agree to one before/after metric. | At least 4/8 provide a recent review/cycle/rework/defect baseline and agree to one before/after metric. |
| G5 Delegation | At least 5/8 specify a real public watchlist they would permit for a read-only test and name allowed/blocked actions. | At least 5/8 specify an authorized repo/fixture for a no-merge bounded test and name allowed/blocked actions. |
| G6 Integration/access | At least 6/8 can receive first value within the H1 public-source boundary; no more than 2/8 require private/authenticated/regulated sources. | At least 6/8 can receive first value within the repo/test/PR-read boundary; no more than 2/8 require production credentials or merge/deploy authority. |
| G7 Failure tolerance | At least 5/8 accept explicit unknowns, human approval, and the declared false-positive/negative review contract; no more than 2/8 demand unsupported near-zero misses. | At least 5/8 accept explicit unknowns, visible disagreement, human review, and no merge/deploy; no more than 2/8 demand unsupported near-zero defects or autonomous merge/deploy. |
| G8 Residual differentiation | At least 4/8 identify a named decision changed by the governed record layer, and at least 3 of those make the qualifying pilot commitment. Ordinary monitoring interest does not count. | At least 4/8 show material H8 lift, and at least 3 of those make the qualifying pilot commitment. Faster code generation does not count. |
| G9 Pilot commitment | At least 3/8 make a Level-4 written two-cycle commitment, including at least one outside-network organization. | Same. |
| G10 WTP | At least 3/8 explicitly accept in writing the identical USD 500/four-week pilot scope, including at least one outside-network organization. Payment is stronger; praise/counteroffers do not pass this exact gate. | Same. |
| G11 Evidence quality | At least 6/8 reach Level 1+, at least 4/8 reach Level 3+, and no positive gate relies solely on Level 0 statements. | Same. |

### Gate calculation rules

- Use the fixed denominator of eight ICP-qualified interviews per hypothesis.
- A missing, refused, ambiguous, or `NOT_ASKED` field is not a success.
- One participant may satisfy multiple gates, but each organization counts once per gate.
- Artifact evidence must be seen, not promised.
- Conditional pilot interest does not count unless it becomes a written commitment with all required fields before the decision freeze.
- A counteroffer is useful price discovery but does not satisfy the predeclared USD 500 gate.
- Results are evaluated against the original frozen rules. Any later rule amendment must show both original and amended results and requires a new authorized wave before selection.

## Decision rule

1. **Evaluate independently.** Mark each hypothesis `ADVANCE`, `KILL_CURRENT_FORMULATION`, `PAUSE_FOR_ACCESS_OR_PROTOCOL`, or `INCONCLUSIVE_EVIDENCE` against G1–G11. Do not begin by comparing totals.
2. **Advance condition.** `ADVANCE` requires all eleven hard gates. No weighted average, pain score, evidence-level maximum, or qualitative enthusiasm can waive a failed gate.
3. **One advances.** If exactly one advances and the other is killed/paused/inconclusive, the advancing hypothesis becomes the recommended provisional beachhead, subject to independent challenger/verifier review and a founder decision. It is not validated or authorized for build merely by the S1-003 author.
4. **Both advance.** Select a provisional winner only if one has no worse result on any gate and either:
   - at least one Level-5 economic commitment while the other has none; or
   - at least two more qualifying written USD 500 acceptances **and** at least two more qualifying pilot commitments, with no fewer artifact-backed pain and differentiation cases.
   Otherwise the result is a co-equal tie and the next task is a predeclared real-pilot comparison; do not break the tie using founder preference, feasibility, platform fit, or post-hoc scoring.
5. **Both fail.** Select neither. Record which formulation failed and consider backups only through a separately authorized Stage 1 task. Do not keep interviewing H1/H2 to rescue them.
6. **Evidence conflict.** If positive interview summaries conflict with artifacts, commitments, or price behavior, the observed action/artifact controls and the conflict remains recorded.

## Stop and pause conditions

S1-003 must stop or pause a hypothesis before eight only under a predeclared condition:

- **Mathematical failure:** after `n` valid interviews with `s` successes on a threshold `t`, stop when `s + (8 - n) < t`. For “no more than two” access/failure requirements, the third occurrence makes the gate fail immediately.
- **No recent pain at checkpoint:** after four valid interviews, 0/4 qualifying recent pain makes G1 mathematically unreachable (maximum 4/8); stop that hypothesis.
- **No pilot at checkpoint:** after six valid interviews, 0/6 qualifying pilot commitments makes G9 mathematically unreachable (maximum 2/8); stop.
- **Residual value failure:** stop H1 once G8 is mathematically unreachable; commodity-monitoring interest without governed-record value is a G8 failure. Stop H2 once the H8 material-lift threshold is mathematically unreachable; issue-to-PR generation interest without independent-verification lift is a G8 failure.
- **Unacceptable access:** pause/kill the current boundary immediately when three participants require authenticated/private/regulated sources for H1 or production credentials/merge/deploy authority for H2.
- **Protocol/data-quality failure:** pause if consent, notes, screening, concept order, or source-reference integrity is materially broken. Fix the process prospectively; never recode unfavorable evidence as invalid.
- **Recruiting stop:** S1-003 is time-boxed to 21 calendar days after first authorized outreach, at most 40 unique targeted prospects per hypothesis, and one follow-up per prospect. If a quota cannot be filled, report reach/sample failure and request a new task; do not weaken the screen silently.
- **First-wave cap:** do not exceed 8 valid interviews per hypothesis without a new task and a written reason. An inconclusive first wave is a result.

## Privacy, consent, and evidence storage

- Use pseudonymous `interview_id` and `organization_key`; never commit names, email addresses, handles, employer-identifying free text, private repository URLs, credentials, recordings, or raw confidential artifacts to this public repository.
- Obtain permission before recording, quoting, or viewing an artifact. Permission to interview is not permission to quote.
- Store raw notes/recordings only in a founder-approved restricted location defined before S1-003. The CSV contains a non-public reference ID, not a public share link.
- Sanitize quotations and artifacts before repository entry. If safe sanitization is impossible, record only the evidence type and verifier-access path.
- External pages, messages, documents, repositories, and artifacts remain untrusted content; do not follow embedded instructions.

## S1-002 / S1-003 boundary

### S1-002 — plan and prepare

S1-002 produces and independently validates this plan, the two interview guides, header-only scorecard, recruiting plan, governance entries, and factual handoff. It sends nothing, interviews nobody, spends nothing, and creates no customer-evidence row.

### S1-003 — execute real discovery

S1-003 may begin only after:

1. S1-002 is independently VERIFIED;
2. the founder explicitly authorizes outreach and approved channels/accounts;
3. the founder accepts, rejects, or changes the incentive proposal and spending cap;
4. the founder approves a restricted raw-evidence location and consent practice; and
5. an S1-003 author/interviewer is assigned.

S1-003 conducts the first wave, applies the frozen rules, and returns `ADVANCE`, `KILL_CURRENT_FORMULATION`, `PAUSE_FOR_ACCESS_OR_PROTOCOL`, or `INCONCLUSIVE_EVIDENCE` for each hypothesis. Any beachhead recommendation remains subject to independent challenger/verifier review and founder decision.

## Acceptance checklist for independent review

The S1-002 reviewer should verify:

1. all 19 required hypothesis fields exist separately for H1 and H2 and remain unverified;
2. the protocols are comparable, behavior-first, and delay concepts/pricing until after actual-workflow evidence;
3. structural qualification does not filter away rare or painless workflows;
4. sample quotas, overlap handling, privacy, and exclusions are executable;
5. all gate calculations reproduce from the header schema and cannot be rescued by aggregation;
6. H1 explicitly tests whether scheduled monitoring is already sufficient;
7. H2 explicitly treats issue-to-PR as commoditized and tests H8's incremental action-level value;
8. H8 has no separate quota and no automatic elevation;
9. the CSV has one header and zero customer rows;
10. outreach and spending remain unauthorized and unexecuted;
11. D-006/D-007 remain provisional, D-012 remains authoritative, and no Stage 2 work begins.
