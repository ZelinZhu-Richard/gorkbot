# S1-002 interview guide — H1 competitor-change workflow

Status: FIXED DRAFT PROTOCOL — NOT EXECUTED; NOT VERIFIED

Protocol version: `S1-002-H1-v2`

Target duration: 45 minutes

Companion plan: `03_product/S1-002_CUSTOMER_DISCOVERY_PLAN.md`

## Interviewer rules

1. Do not describe an AI agent, verification-first product, or proposed solution before the concept checkpoint.
2. Ask for the last actual occurrence before opinions about an ideal workflow.
3. Ask unaided questions before naming alternatives.
4. Record “none,” “adequate,” “would not delegate,” “would not pilot,” and “would not pay” without persuasion.
5. Do not teach the participant why the residual concept should matter.
6. One structurally qualified participant counts in the denominator even if no recent occurrence exists.
7. Do not store names, contact details, recordings, private links, or identifiable confidential material in the public repository.
8. Never interpret “interesting,” “keep me posted,” a referral, or a rating as a commitment.

## Opening and consent — 0 to 3 minutes

Suggested script:

> I am researching how small B2B SaaS teams actually track competitor changes and use them in decisions. This is not a sales call, and I want to understand the current process before discussing any concept. I will take notes. You can skip any question and should not share secrets or customer-confidential information.

Ask and record:

1. May I take notes?
2. May I record this conversation? If no, continue with notes only.
3. May I later use a sanitized quotation? A yes is optional and separate from recording permission.
4. If you show an artifact, may I record only a sanitized description and evidence reference? Do not copy the artifact into the repository.

## Structural screening — 3 to 7 minutes

These questions establish the ICP only. Recent pain, frequency, dissatisfaction, and interest are not qualification criteria.

1. What is your current role, and what decisions do you personally own?
2. What does the company sell, and is the product currently live?
3. Approximately how many employees are at the company?
4. Roughly how many named competitors does the team actively track?
5. Is anyone a full-time competitive-intelligence analyst?
6. In the last 12 months, were you directly responsible for gathering or approving competitor information for a pricing, positioning, roadmap, launch, or sales-enablement decision?
7. Who controls the budget for a small workflow pilot like this? Is that you, or someone else?

Screen outcome:

- `ICP_QUALIFIED`: live B2B SaaS, 3–30 employees, 5–15 named competitors, no full-time CI analyst, and direct workflow responsibility in the last 12 months.
- `SCREEN_FAIL`: a structural criterion is not met. End politely; do not count the interview.
- Do not screen out a participant because the workflow is rare, painless, well served, non-delegable, or not worth paying for.

## Behavioral interview — 7 to 19 minutes

Mandatory behavior checkpoint begins here. Do not show the concept until this section and the workaround section are complete.

1. Tell me about the last time you needed current competitor information for a real decision.
2. What was the decision, and what triggered the need?
3. When did this happen? If nothing happened in the last 90 days, what was the most recent case in the last 12 months?
4. What did you personally do, step by step?
5. Who else was involved, and where did ownership change hands?
6. Which competitor pages, sources, files, or systems did you check?
7. How did you compare the current state with what you previously believed?
8. What did you produce or update at the end?
9. How did you decide the research was complete enough to use?
10. Was anything unavailable, uncertain, stale, or contradictory? If not, record none.
11. What happened after the research? Which decision or action changed, if any?
12. What happened, or would have happened, if you did nothing?

Artifact prompt, without pressure:

> If it is safe and permitted, could you show me a redacted example of the watchlist, prior report, spreadsheet, battlecard, decision memo, alert, or live process? Please hide names or information you should not share.

Record `artifacts_observed=FALSE` if nothing is shown. A promised later artifact does not count as observed.

## Frequency and cost — 19 to 24 minutes

Keep the three H1 clocks separate.

1. In the last 60 days, how many times did you personally perform a competitor comparison for a decision?
2. How often do tools check sources automatically, if at all?
3. How often does a person actually read or act on a report?
4. How often was there a strategically meaningful change rather than routine page noise?
5. For the last case, roughly how many active minutes did you spend? What was the elapsed delay?
6. Did anyone else spend time on it? How much?
7. What tools or services are paid for now, and what is the approximate current spend if you know it?
8. Was there a failure, stale state, correction, delay, or missed response in that case? If so, what did it cost or change? If not, record none.

Do not convert software polling frequency into customer workflow frequency.

## Current workaround and alternatives — 24 to 30 minutes

Ask unaided first:

1. What are you using now?
2. Why did you choose that process?
3. What is adequate about it?
4. Is any repeated step, missed state, or correction still unsatisfactory? If none, what is adequate enough to keep?
5. Have you tried replacing the process? What did you actually try, and what happened?
6. If the process improved, is there an exact step you would stop doing? If none, record none.

Only after unaided answers, use the standardized recognition list:

> Have you used or seriously evaluated any of these categories: manual page checks or spreadsheets, Google Alerts, scheduled assistants, page monitors such as Visualping/PageCrawl/ChangeTower/Distill, competitor trackers such as Competiflow/Competitors.app, or larger CI suites such as Klue/Crayon/Kompyte? For each one you recognize, what happened in actual use?

Do not imply that every named product is appropriate or deficient. Record `ADEQUATE` when the participant considers the current solution good enough.

## Delegation, trust, access, and failure tolerance — 30 to 35 minutes

Begin with past behavior:

1. Have you delegated this research to a person, contractor, or tool before? Tell me about the last time.
2. What information or access did you provide?
3. What did you check yourself before using the result?
4. What would you never delegate?
5. Would you permit a test using your real public competitor watchlist and a prior accepted snapshot? Why or why not?
6. Which actions would be allowed: read public pages, save a draft memo, propose a spreadsheet change, write a test record after approval? Which are blocked?
7. Would authenticated pages, private data, or regulated sources be required for first value?
8. Describe a false positive that would be tolerable and one that would not be.
9. Describe a missed change that would be tolerable and one that would not be.
10. Is an explicit `UNKNOWN` or `SOURCE_UNAVAILABLE` result acceptable? When is it not?

Record the delegation tier before any concept is shown.

## Contract A / Contract B test — 35 to 40 minutes

Read each neutral contract once. Do not add benefit claims. The same Contract A is shown to monitor users and monitor-naive/manual participants so novelty attributable to ordinary monitoring is absorbed before Contract B.

### Contract A — commodity monitoring baseline

> Contract A uses capabilities already substantially available from monitoring products. It checks named public pages on a schedule, detects changes, returns source URLs and timestamps with before/after diffs, produces summaries or importance signals, and sends alerts, digests, or an ordinary recurring report. It does not maintain or update a governed canonical competitive record.

Ask:

1. How different is Contract A from what you already use or could configure today?
2. For the last case, would Contract A change any exact step, permission, or delegation decision? If so, which one; if not, record none.
3. Would Contract A alone adequately solve the job? Why or why not?

Record `delegation_tier_after_contract_a`. Interest, novelty, time savings, or willingness to try Contract A is commodity value and does **not** support H1's G8 residual differentiation.

### Contract B — H1 governed-record residual

> Contract B assumes Contract A's monitoring output already exists. It adds cross-competitor synthesis tied to your named decision and decision rules; a canonical change ledger that records checked, unchanged, changed, unavailable, and unknown state with source provenance; a proposed update to that record; explicit approval before any external record change; and readback of an approved test-record update. It adds no faster monitoring or extra alert volume.

Ask:

1. Beyond Contract A, would Contract B change any exact step, named decision, permission, or delegation choice in the last case? If so, which one; what would remain unchanged?
2. Would you remove or shorten any manual reconciliation or review step only with Contract B? If so, which one and how would that be measured; if not, record none.
3. Which part is already duplicated by your current stack, and would Contract B still add enough beyond your current monitoring to change an action?
4. Which evidence or ledger fields would you ignore, and what maintenance, latency, false-state, or approval burden would make Contract B worse than the current process?

Record `delegation_tier_after_concept` after Contract B. `contract_b_material_action_lift=TRUE` only when a named recent decision, permission, removed/shortened step, or qualifying pilot commitment changes **over Contract A**. If a participant values the bundle but cannot identify what B adds beyond A, code no residual lift.

## Pilot commitment — 40 to 42 minutes

Ask in order and record exact answers:

1. Would you test Contract B, layered on your current or Contract A monitoring, on a real permitted watchlist for two cycles?
2. Which watchlist and prior snapshot would you use?
3. Who would own the pilot?
4. What start date within the next 30 days could you commit to?
5. What one completion criterion and one before/after metric would decide whether it worked?
6. What access or approval would block the start?
7. May I send a written pilot scope for you or the budget owner to accept?

Classification:

- `WRITTEN_QUALIFYING` only when owner, permitted input, start date, two-cycle scope, and completion criterion are all accepted in writing.
- A verbal yes, referral, scheduling suggestion, or “after you build it” is not a qualifying commitment.

## Pricing and WTP — 42 to 44 minutes

Ask behavioral budget questions before stating the test price:

1. What does the current process cost in tools and labor, if known?
2. Who approved the last comparable tool or service purchase?
3. What budget would this come from?

Then read the standardized price test without discounting or negotiation:

> The first-wave price test is USD 500 for a four-week, two-cycle Contract B pilot with the bounded scope just described and no automatic continuation. Would your organization accept that scope and price in writing?

Follow-ups:

1. Is that `yes`, `no`, or conditional on a named approval?
2. What makes that price acceptable or unacceptable?
3. If no, what would you do instead?
4. If you propose a different price, what scope and approval would that include?

Only an explicit written acceptance of the standardized offer counts for G10. Code it `WRITTEN_500_ACCEPTANCE` and Level 4 at most. A conversational “yes” or “USD 500 sounds reasonable” is `PRICE_REACTION_ONLY`; only payment/deposit, a signed paid-pilot order, or an equivalent binding signed commitment naming amount, budget owner, and execution date is Level 5 / `ECONOMIC_COMMITMENT`. Record counteroffers separately; do not negotiate during the interview.

## Mandatory closing disconfirmation — 44 to 45 minutes

Ask both; they are not optional:

1. What observed evidence from your own workflow most contradicts the idea that the residual Contract B problem is real?
2. What is the strongest reason not to build Contract B for your team?

If time remains, ask whether the job is too rare, too low-stakes, already solved, or blocked by access/failure tolerance, and who in the company would disagree.

Thank the participant. Do not promise a product, pilot slot, incentive, follow-up, or timeline beyond what S1-003 has explicitly authorized.

## Post-interview coding checklist

- Confirm `qualification` from structural facts only.
- Record absence of a 90-day occurrence as disconfirming evidence, not a screen failure.
- Separate machine cadence, human report cadence, and decision-linked frequency.
- Record actual tools before the recognition list.
- Identify a replaceable step or mark none.
- Record separate delegation tiers before contracts, after Contract A, and after Contract B; commodity Contract A interest cannot count toward G8.
- Code `contract_b_material_action_lift` only from a B-over-A action change tied to the recent case.
- Record allowed/blocked actions and forbidden access requirements.
- Code pilot and WTP using exact commitment enums.
- Assign evidence levels per claim, then record the maximum interview level.
- Preserve contradictions and exact negative evidence.
- Record `interview_completion`; truncated ICP-qualified interviews remain in the denominator with unasked gates as non-successes.
- Store only field-level sanitized data and an opaque restricted source-reference ID; `pilot_owner` is a role and `pilot_input` is generic.
