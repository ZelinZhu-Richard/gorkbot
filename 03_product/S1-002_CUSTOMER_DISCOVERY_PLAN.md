# S1-002 symmetric customer-discovery experiment plan

Status: FIXER PASS — READY FOR INDEPENDENT POST-FIX REVIEW; NOT VERIFIED

Planning date: 2026-08-23

Fix date: 2026-08-23

Authority: `MODE: PLAN_STAGE_1` author instruction, `MODE: FIX_TASK_S1-002` fixer instruction, and confirmed D-012

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
- **Valid denominator:** every ICP-qualified interview whose behavioral section begins, whether complete or truncated, including negative, rare, satisfied, non-delegable, and unwilling-to-pay cases. Missing/unasked answers, refusal to show an artifact, and conditional interest do not disappear from the denominator.
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
| 16 | Differentiation hypothesis | Interest in scheduled monitoring, detection, before/after diffs, source URLs/timestamps, summaries, importance scoring, alerts, digests, and ordinary reports is commodity Contract A interest and does not count. Contract B adds only the residual: cross-competitor synthesis tied to a named decision, a customer-owned materiality rule, a governed/canonical change ledger with explicit coverage/unknown state and provenance, an approval-gated record proposal, and readback. H1 is supported only if Contract B changes a real decision, permission, removed step, pilot commitment, or economic commitment beyond Contract A. |
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

> Relative to commodity issue-to-PR generation and ordinary author/CI evidence, does an independently reproduced verification/evidence bundle change a real permission or decision, reduce a named manual review burden, or create a qualifying pilot or economic commitment?

H8 receives no separate quota, ICP, buyer, score, price, interview, or discovery allocation. Every H2 interview measures Contract B over Contract A and separately records whether the participant would use or pilot verification without issue-to-code generation.

A **material H8 lift** requires behaviorally anchored evidence of at least one of the following:

1. the participant grants a specific permission or real-workflow scope only with the independent bundle;
2. the participant identifies a named recent PR decision that the bundle would have changed and explains how;
3. the participant removes or shortens a specific manual verification step and commits to measure it; or
4. the participant changes from no/conditional pilot intent to a qualifying written pilot commitment because of the bundle.

A numeric trust-rating increase or “I would trust it more” without a changed action is Level 0 and does not count. General interest in Contract A does not count.

H2's in-wave residual gate requires at least 4/8 action-level Contract-B-over-A lifts and at least 3 of those same participants making the standard written pilot commitment to Contract B.

For the narrower question of reopening a **distinct H8 allocation**, S1-002 prospectively operationalizes A-018 as a conjunction: at least 4/8 must show the action-level lift above, at least 4/8 must explicitly prefer or accept a verification-only pilot without commodity generation, and at least 3 participants must satisfy both conditions and make the qualifying written pilot commitment. This stricter operational definition governs S1-003; it interprets A-018's “verification-only value” as changed behavior rather than opinion. Even if met, H8 is only eligible for independent challenger/verifier review of whether its buyer, trigger, job, workflow, or value proposition is materially distinct. It is never automatically elevated.

## Comparable interview procedure

Both guides are authoritative and use the same 45-minute sequence and evidence rules:

| Minutes | Phase | Rule |
|---:|---|---|
| 0–3 | Consent | Obtain separate note, recording, quotation, and artifact permissions. |
| 3–7 | Structural screen | Confirm role/company/direct responsibility. Do not screen on pain, frequency, dissatisfaction, or interest. |
| 7–19 | Last actual occurrence | Ask for the last real workflow, trigger, people, tools, errors, consequence, completion check, and artifact. Do not describe either contract. |
| 19–24 | Frequency and cost | Capture human frequency, active/elapsed time, spend, failure, and consequence without presupposing pain. |
| 24–30 | Current workaround | Capture unaided alternatives first; then use the standardized recognition list. Ask what is adequate and what is not. |
| 30–35 | Delegation and failure boundary | Start with past delegation behavior, then permitted data/actions and unacceptable failures. Record the pre-contract delegation tier. |
| 35–40 | Contract A / Contract B test | Present the candidate-specific commodity baseline first and residual second. Record A and B separately; count only B-over-A action lift. |
| 40–42 | Pilot | Ask for a concrete two-cycle commitment to Contract B. |
| 42–44 | Price | Use the identical USD 500/four-week instrument after behavioral budget questions. |
| 44–45 | Mandatory disconfirmation | Ask what observed evidence most contradicts the problem and the strongest reason not to build this for the team. |

If time is short, optional follow-ups are shortened; the two mandatory disconfirmation questions are never dropped. The interviewer may not convert praise, a waitlist signup, a referral, or “keep me posted” into a pilot or WTP signal.

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

A plain written “yes” to the standardized USD 500 scope is `WRITTEN_500_ACCEPTANCE`, satisfies G10 when timely, and is **Level 4 at most**. It becomes Level 5 / `ECONOMIC_COMMITMENT` only when backed by payment or deposit, a signed paid-pilot order, or an equivalent binding signed commitment that names the amount, budget owner, and execution date. “USD 500 sounds reasonable,” verbal price acceptance, or an unsigned budget statement is `PRICE_REACTION_ONLY`, not G10 and not Level 5.

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
- `interview_completion` records the last completed phase using mutually exclusive values: `COMPLETE`, `TRUNCATED_DURING_BEHAVIOR`, `TRUNCATED_BEFORE_CONTRACTS`, `TRUNCATED_DURING_CONTRACT_A`, `TRUNCATED_AFTER_CONTRACT_A`, `TRUNCATED_AFTER_CONTRACT_B_BEFORE_PILOT`, `TRUNCATED_BEFORE_PRICING`, or `TRUNCATED_BEFORE_DISCONFIRMATION`. A structurally qualified truncated interview remains in the denominator; every unasked gate field is a non-success.
- `network_tier`: `FIRST_DEGREE`, `WARM_INTRO`, or `OUTSIDE_NETWORK`.
- `buyer`: `SELF_CONFIRMED`, `OTHER_ROLE_CONFIRMED`, or `UNKNOWN`; `daily_user`: `PARTICIPANT_OPERATOR`, `OTHER_ROLE_OPERATOR`, or `UNKNOWN`. Neither field contains a person's name or exact title.
- `current_alternative_satisfaction`: `ADEQUATE`, `MIXED`, `INADEQUATE`, or `NOT_USED`.
- `pain_score`: `0` no recent occurrence/consequence; `1` inconvenience only; `2` recurring burden without quantified consequence; `3` measurable time/delay/rework/decision consequence; `4` artifact-backed material consequence. Gate calculations use the underlying fields, not an average pain score.
- `delegation_tier_before_concept`, `delegation_tier_after_contract_a`, and `delegation_tier_after_concept` (after Contract B): `0` no real input; `1` synthetic/redacted only; `2` real read-only input; `3` reversible draft/branch write with human review; `4` consequential write only behind explicit approval. No autonomous merge/deploy is offered.
- `contract_b_material_action_lift`: `TRUE` only when Contract B, beyond Contract A, changes a named decision, permission, removed/shortened step, or qualifying pilot commitment. `contract_b_lift_basis` records the sanitized action category and recent-case anchor. H2 additionally records the same result as `h8_material_trust_lift` for compatibility with A-018; H1 never receives H8 status.
- For H2 only, `h8_verification_only_interest=TRUE` means the participant explicitly prefers, would use, or would pilot Contract B without commodity issue-to-code generation; this interest alone is not a material action lift. `h8_pilot_commitment=TRUE` only when the qualifying written pilot commitment itself covers verification-only Contract B without issue-to-code generation. H1 records both fields as `NOT_ASKED`.
- `pilot_commitment`: `NO`, `VERBAL_ONLY`, `CONDITIONAL`, or `WRITTEN_QUALIFYING`.
- `wtp_signal`: `NONE`, `PRICE_REACTION_ONLY`, `COUNTEROFFER`, `WRITTEN_500_ACCEPTANCE`, or `ECONOMIC_COMMITMENT`.
- `evidence_level`: integer `0`–`6` from the hierarchy above.
- Boolean fields use `TRUE`, `FALSE`, or `NOT_ASKED`; `NOT_ASKED` cannot count as success.

Each record must preserve disconfirming evidence and contradictions. The interviewer and coder may not collapse conflicting statements into a positive summary.

### Coding authority and audit

- The assigned interviewer is the **primary coder** and completes the structured record from the restricted notes within 24 hours. Screen failures may be single-coded; every counted `ICP_QUALIFIED` row requires a nonempty `reviewer_id` before the gate-counting freeze.
- A second reviewer independently recodes every gate-relevant interpretive field from the restricted source record: structural qualification, recent consequential pain, decision linkage, alternative satisfaction/replaceable step, measurable baseline, delegation tiers, integration/access boundary, failure tolerance, Contract-B-over-A lift, pilot/WTP classification, and evidence level. The independent S1-003 challenger or verifier may serve this bounded role.
- Direct observations are transcribed, not upgraded by judgment: reported counts/dates, artifact seen/not seen, stated allowed/blocked actions, written pilot elements, standardized written price acceptance, signed order, and payment/deposit. Interpretive fields include `pain_score`, `decision_linked_workflow`, `current_alternative_satisfaction`, `replaceable_step`, delegation tiers, `contract_b_material_action_lift`, `failure_tolerance`, and `evidence_level`.
- The restricted notes, observed artifact, and written commitment control over summaries. If coders disagree and the direct record does not resolve the ambiguity, record both readings in `contradictions` and use `UNKNOWN`, `FALSE`, the lower evidence level, or the non-qualifying commitment class for gate calculation. Favorable intent may not resolve ambiguity.
- Every coding change is appended in the restricted audit log with interview ID, field, old value, new value, actor/reviewer ID, timestamp, reason, and opaque source reference. The public CSV contains the frozen sanitized result, not the private audit trail. A post-freeze correction is retained as a correction but cannot change this wave's gate result.
- AI may assist only with consented transcription or structured extraction inside the founder-approved restricted environment and under the founder's recorded S1-003 AI-role policy. AI may not conduct unsupervised outreach/interviews, make the final evidence classification, resolve coder disagreement, or upgrade a gate. A named accountable coder and reviewer make the final entries.

### Field-level public-repository policy

Every public CSV header has exactly one treatment below. Values that cannot be safely sanitized are `REDACTED_UNKNOWN` and do not count as gate successes.

- **PUBLIC_SAFE:** `interview_id` and `organization_key` (new random opaque keys only); `protocol_version`; `sample_wave`; `hypothesis`; `network_tier`; `recruitment_channel` (broad enum); `qualification`; `interview_completion`; `buyer`; `daily_user`; `alternative_usage_stratum`; `workflow_observed`; `decision_linked_workflow`; `recent_occurrence_window_met`; `frequency`; `frequency_window_days`; `machine_check_cadence`; `report_cadence`; `currency`; `current_alternative_satisfaction`; `pain_score`; `delegation_willingness`; `delegation_tier_before_concept`; `delegation_tier_after_contract_a`; `delegation_tier_after_concept`; `forbidden_access_required`; `contract_b_material_action_lift`; `pilot_interest`; `pilot_commitment`; `pilot_two_cycle_commitment`; `wtp_signal`; `written_price_acceptance`; `economic_commitment`; `h8_material_trust_lift`; `h8_verification_only_interest`; `h8_pilot_commitment`; `artifacts_observed`; `artifact_type` (broad enum); `evidence_level`; `permission_to_record`; `permission_to_quote`; `interviewer_id`; and `reviewer_id` (opaque role IDs, not personal names).
- **PUBLIC_SANITIZED:** `interview_date` and `pilot_start_date` at month precision only; `qualification_reason` as a controlled reason code; `role` as a broad role bucket; `company_type` as a broad category; `company_size` and `team_size` as predeclared bands, never exact counts when identifying; `trigger`, `last_occurrence`, `time_cost`, `money_cost`, `current_tools`, `current_workaround`, `replaceable_step`, `failure_cost`, `economic_value_baseline`, `allowed_actions`, `blocked_actions`, `trust_constraints`, `integration_requirements`, `failure_tolerance`, `contract_b_lift_basis`, `pilot_owner`, `pilot_input`, `pilot_completion_criterion`, `price_reaction_sanitized`, `disconfirming_evidence`, `contradictions`, and `notes`. Use controlled categories or short paraphrases only: `pilot_owner` is a role, never a name; `pilot_input` is generic (for example, “own public 12-competitor watchlist” or “authorized backend-service fixture”), never competitor/company/repository names; `current_tools` uses product categories unless a named public product is non-identifying; no public field contains a verbatim customer quotation.
- **OPAQUE_REFERENCE_ONLY:** `source_recording_or_notes` contains only a random restricted-record ID. It may not contain a filename, storage path, URL, email, handle, organization key derivation, or share link.
- **PRIVATE_ONLY — no public CSV header or value:** names, emails, handles, phone numbers, employer/domain, exact interview timestamp, exact payment/incentive delivery details, raw title where identifying, raw notes/transcripts/recordings, verbatim quotations, consent records, exact competitor/watchlist entries, private repository names/URLs/source code, screenshots, internal documents, proprietary workflow details, budgets, credentials, customer data, and raw artifacts.

Before any row is committed, a reviewer performs a field-by-field privacy check plus a quasi-identifier check over role, size band, month, channel, tools, and narrative fields. If the combination could reasonably identify the participant or organization, coarsen or suppress it. Private evidence and payment/incentive records remain in the founder-approved restricted tracker; only opaque references and aggregate spend may appear publicly.

## Protocol freeze and amendment rule

### Protocol freeze before contact

Before the first prospect is contacted, S1-003 must record one repository commit SHA containing the independently verified versions of this plan, both guides, the CSV header, the recruiting plan, and the S1-002/S1-003 registry entries. The same authorization record must name the approved channels/accounts, incentive decision and cap (including USD 0), restricted evidence/consent location, assigned interviewer, and explicit AI-role policy. No draft or working-tree version may govern a contacted prospect.

At that point the following become immutable for the first wave: ICP and exclusion rules; quotas and sampling controls; question order and mandatory questions; recognition lists; Contract A and Contract B wording; artifact request; pilot scope; USD 500/four-week price instrument; evidence levels; CSV fields/enums; coding and privacy rules; G1–G11 definitions and thresholds; missing-data treatment; early-stop math; recruiting batch triggers/caps; terminal-state vocabulary; tie/selection rules; and both freeze dates. In particular, G9/G10 definitions, commitment elements, price, counting window, and Level 4/5 boundary cannot change after any response is visible.

### Permitted corrections and amendments

- Consent withdrawal, safety stops, PII redaction, and removal of an accidentally exposed secret occur immediately and do not require symmetry. The affected evidence becomes unavailable/non-success; it is never replaced by a favorable inference.
- An obvious typo, broken reference, or formatting defect may be corrected only when meaning, burden, timing, coding, and threshold remain unchanged. Log the before/after text, reason, timestamp, actor, affected interviews, and why comparability is unchanged.
- Any substantive change is a prospective **protocol amendment**. Log it in the restricted deviation/audit record and summarize it publicly in the S1-003 handoff with the old rule, new rule, reason, timestamp, affected hypothesis/interviews, and original-rule result. A common defect must receive the same amendment for H1 and H2. A hypothesis-specific safety correction must be justified and cannot improve that hypothesis's gate count.
- A substantive amendment after first contact invalidates direct first-wave comparability from the first affected interview. Report both original and amended results, select no beachhead from the amended evidence, and require a newly authorized symmetric wave under one verified protocol.

### Gate-counting freeze

Each hypothesis reaches a data-collection terminal when it completes eight valid interviews, hits a predeclared mathematical/protocol stop, or reaches the recruiting cap/time box. The **common gate-counting freeze** is 23:59 America/New_York on the earlier of (a) seven calendar days after the later of the H1 and H2 terminal timestamps and (b) 42 calendar days after the first authorized outreach. Before first contact, S1-003 records this immutable formula, the authorized first-outreach date, and the resulting day-42 cap. As soon as the later H1/H2 terminal occurs, S1-003 mechanically calculates and logs the exact common timestamp from the frozen formula; it may not choose or move the timestamp based on observed results. Written pilot or USD 500 acceptances received by that timestamp may count if all frozen elements are present; anything received later is recorded as later evidence but cannot change this wave's G9/G10 or decision state.

## Predeclared hard gates

Every threshold below is a **DESIGN PROPOSAL — NOT TESTED**. All gates are hard: a strong result on one cannot compensate for a fatal weakness on another.

| Gate | H1 pass condition | H2 pass condition |
|---|---|---|
| G1 Recent consequential pain | At least 5/8 describe a decision-linked missed/stale/manual burden in the prior 90 days with a concrete consequence. | At least 5/8 describe a bounded-issue/review failure or delay in the prior 90 days with a concrete consequence. |
| G2 Recurring human workflow | At least 5/8 personally performed the decision-linked comparison at least twice in 60 days; machine/report cadence excluded. | At least 5/8 personally triaged and/or reviewed at least four distinct bounded issues/PRs in 30 days; the two guide counts are summed without double-counting the same item. |
| G3 Alternative dissatisfaction | At least 4/8 identify a repeated step or failure in their actual named monitor/CI/manual stack that they would replace. | At least 4/8 identify a repeated check, reopen, CI/review gap, or correction in their actual named stack that they would replace. |
| G4 Measurable economic value | At least 4/8 provide a recent time/money/delay/failure baseline and agree to one before/after metric. | At least 4/8 provide a recent review/cycle/rework/defect baseline and agree to one before/after metric. |
| G5 Delegation | At least 5/8 specify a real public watchlist they would permit for a read-only test and name allowed/blocked actions. | At least 5/8 specify an authorized repo/fixture for a no-merge bounded test and name allowed/blocked actions. |
| G6 Integration/access | At least 6/8 can receive first value within the H1 public-source boundary; no more than 2/8 require private/authenticated/regulated sources. | At least 6/8 can receive first value within the repo/test/PR-read boundary; no more than 2/8 require production credentials or merge/deploy authority. |
| G7 Failure tolerance | At least 5/8 accept explicit unknowns, human approval, and the declared false-positive/negative review contract; no more than 2/8 demand unsupported near-zero misses. | At least 5/8 accept explicit unknowns, visible disagreement, human review, and no merge/deploy; no more than 2/8 demand unsupported near-zero defects or autonomous merge/deploy. |
| G8 Residual differentiation | At least 4/8 show an action-level Contract-B-over-A lift tied to a named decision, permission, or removed step, and at least 3 of those same participants make the qualifying Contract B pilot commitment. Interest in ordinary monitoring, diffs, summaries, alerts, or reports does not count. | At least 4/8 show the defined action-level H8 / Contract-B-over-A lift, and at least 3 of those same participants make the qualifying Contract B pilot commitment. Faster code generation or general Contract A interest does not count. |
| G9 Pilot commitment | At least 3/8 make a Level-4 written two-cycle commitment, including at least one outside-network organization. | Same. |
| G10 WTP | At least 3/8 explicitly accept in writing the identical USD 500/four-week pilot scope, including at least one outside-network organization. Payment is stronger; praise/counteroffers do not pass this exact gate. | Same. |
| G11 Evidence quality | At least 6/8 reach Level 1+, at least 4/8 reach Level 3+, and no positive gate relies solely on Level 0 statements. | Same. |

### Gate calculation rules

- Use the fixed denominator of eight ICP-qualified interviews per hypothesis.
- A missing, refused, ambiguous, or `NOT_ASKED` field is not a success.
- One participant may satisfy multiple gates, but each organization counts once per gate.
- Artifact evidence must be seen, not promised.
- Conditional pilot interest does not count unless it becomes a written commitment with all required fields before the common gate-counting freeze defined above.
- A counteroffer is useful price discovery but does not satisfy the predeclared USD 500 gate.
- Every counted row must complete the second-coder and public-row privacy checks before freeze; an unresolved ambiguous field remains non-success.
- Results are evaluated against the original frozen rules. Any later rule amendment must show both original and amended results and requires a new authorized wave before selection.

## Decision rule

1. **Evaluate independently.** Assign one terminal state to each hypothesis before comparing them:
   - `ADVANCE`: the denominator is closed at exactly eight valid interviews, including any counted truncation under the rule above, and all G1–G11 pass. Positive thresholds reached early do not end the denominator early, and a truncated counted interview may not be replaced merely to improve a gate.
   - `KILL_MARKET_EVIDENCE`: a hard gate is legitimately evaluated and fails from counted customer behavior, access requirements, commitments, or economic evidence. A third participant requiring disallowed first-value access is a G6 market failure, not an operational pause.
   - `PAUSE_RECRUITING_FAILED`: the valid quota or outside-network control is not reached inside the frozen recruiting cap/time box.
   - `PAUSE_ACCESS_BLOCKED`: project-side permission, consent, or evidence-access conditions prevent valid evaluation; this does not include participants themselves rejecting the offered access boundary, which is gate evidence.
   - `PAUSE_PROTOCOL_FAILED`: consent, ordering, coding, privacy, or data integrity is materially broken.
   - `INCONCLUSIVE_INSUFFICIENT_SAMPLE`: the available valid sample cannot establish pass or mathematical failure for a reason not already classified above.
2. **Advance condition.** `ADVANCE` requires all eleven hard gates. No weighted average, pain score, evidence-level maximum, or qualitative enthusiasm can waive a failed gate.
3. **Exactly one advances.** If the rival is `KILL_MARKET_EVIDENCE`, the advancing hypothesis may be recommended as the provisional Stage 1 beachhead, subject to independent challenger/verifier review and a founder decision. If the rival is any `PAUSE_*` or `INCONCLUSIVE_*` state, label the result `PROMISING_ADVANCE_WITH_UNRESOLVED_RIVAL`: preserve the passing candidate as promising, preserve D-012 co-equality for the unresolved comparison, and claim no comparative winner. The required next evidence is a newly authorized task that remedies the named recruiting/access/protocol defect and completes or legitimately kills the rival under the same verified protocol. A founder may separately abandon the rival on reach or operational grounds, but that decision must be labeled non-market and cannot be reported as pain/demand falsification.
4. **Both advance.** Select a provisional winner only if one has no worse result on any gate and either:
   - at least one Level-5 economic commitment while the other has none; or
   - at least two more qualifying written USD 500 acceptances **and** at least two more qualifying pilot commitments, with no fewer artifact-backed pain and differentiation cases.
   Otherwise the result is a co-equal tie and the next task is a predeclared real-pilot comparison; do not break the tie using founder preference, feasibility, platform fit, or post-hoc scoring.
5. **Both killed.** Select neither. Record each failed formulation and consider backups only through a separately authorized Stage 1 task. Do not keep interviewing H1/H2 to rescue them.
6. **No advance with a pause/inconclusive state.** Select neither and remedy only the named execution/reach gap in a new task; do not recode it as a customer rejection.
7. **Evidence conflict.** If positive interview summaries conflict with artifacts, commitments, or price behavior, the observed action/artifact controls and the conflict remains recorded.

`KILL_MARKET_EVIDENCE` is a market/workflow signal. `PAUSE_RECRUITING_FAILED`, `PAUSE_ACCESS_BLOCKED`, `PAUSE_PROTOCOL_FAILED`, and `INCONCLUSIVE_INSUFFICIENT_SAMPLE` are execution or evidence-availability signals. Recruiting response, screen completion, scheduling, and no-show rates are reported in the funnel; they never enter G1–G11.

## Stop and pause conditions

S1-003 must stop or pause a hypothesis before eight only under a predeclared condition:

- **Mathematical failure:** after `n` valid interviews with `s` successes on a threshold `t`, stop when `s + (8 - n) < t`. For “no more than two” access/failure requirements, the third occurrence makes the gate fail immediately.
- **No recent pain at checkpoint:** after four valid interviews, 0/4 qualifying recent pain makes G1 mathematically unreachable (maximum 4/8); stop that hypothesis.
- **No pilot at checkpoint:** after six valid interviews, 0/6 qualifying pilot commitments makes G9 mathematically unreachable (maximum 2/8); stop.
- **Residual value failure:** stop H1 once G8 is mathematically unreachable; Contract A commodity-monitoring interest without Contract B lift is a G8 failure. Stop H2 once the H8/Contract B material-lift threshold is mathematically unreachable; issue-to-PR generation interest without independent-verification lift is a G8 failure.
- **Participant access rejection:** assign `KILL_MARKET_EVIDENCE` when three counted participants require authenticated/private/regulated sources for H1 or production credentials/merge/deploy authority for H2; that is a failed G6 boundary. Use `PAUSE_ACCESS_BLOCKED` only when the project cannot validly evaluate the boundary because its own permission, consent, or approved-storage condition is missing.
- **Protocol/data-quality failure:** assign `PAUSE_PROTOCOL_FAILED` if consent, notes, screening, contract order, coding, privacy, or source-reference integrity is materially broken. Fix only prospectively under the amendment rule; never recode unfavorable evidence as invalid.
- **Recruiting stop:** S1-003 may contact at most 120 unique targeted prospects per hypothesis in three predeclared batches of up to 40, over at most 35 calendar days after first authorized outreach, with one follow-up per prospect. The identical batch-release triggers are defined in the recruiting plan. If a quota or outside-network floor cannot be filled, assign `PAUSE_RECRUITING_FAILED`, report the full funnel, and request a new task; do not weaken the screen or interpret the shortfall as pain/demand evidence.
- **First-wave cap:** do not exceed 8 valid interviews per hypothesis without a new task and a written reason. An inconclusive first wave is a result.

## Privacy, consent, and evidence storage

- Use pseudonymous `interview_id` and `organization_key`; never commit names, email addresses, handles, employer-identifying free text, private repository URLs, credentials, recordings, or raw confidential artifacts to this public repository.
- Obtain permission before recording, quoting, or viewing an artifact. Permission to interview is not permission to quote.
- Store raw notes/recordings only in a founder-approved restricted location defined before S1-003. The CSV contains only an opaque random reference ID, never a path or public/private share link.
- Apply the field-level policy above before repository entry. No verbatim customer quotation enters the public scorecard; if safe sanitization is impossible, record only a broad evidence type and opaque restricted reference.
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
5. an S1-003 author/interviewer is assigned; and
6. the founder records the AI-role policy for outreach, interviewing, transcription, raw-evidence access, extraction, coding, and review. A recorded “no AI access” policy is valid.

S1-003 conducts the first wave, applies the frozen rules, and returns one of `ADVANCE`, `KILL_MARKET_EVIDENCE`, `PAUSE_RECRUITING_FAILED`, `PAUSE_ACCESS_BLOCKED`, `PAUSE_PROTOCOL_FAILED`, or `INCONCLUSIVE_INSUFFICIENT_SAMPLE` for each hypothesis. Any beachhead recommendation remains subject to independent challenger/verifier review and founder decision; an advanced candidate facing a paused/inconclusive rival is promising but not a comparative winner.

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
9. protocol and gate-counting freezes are exact, G9/G10 cannot move, and substantive amendments invalidate first-wave selection;
10. primary/second-coder authority, conservative disagreement handling, AI limits, and coding audit are reproducible;
11. every CSV header has one public privacy class, identity-prone fields have explicit transformations, and the CSV has one header with zero customer rows;
12. the 120-prospect/35-day staged funnel arithmetic is labeled as a design estimate and recruiting failure never becomes a customer gate;
13. the Level 4/5 price boundary, H8/A-018 conjunction, completion statuses, incentive symmetry, and private payment ledger agree across artifacts;
14. outreach and spending remain unauthorized and unexecuted; and
15. D-006/D-007 remain provisional, D-012 remains authoritative, S1-003 remains blocked, and no Stage 2 work begins.
