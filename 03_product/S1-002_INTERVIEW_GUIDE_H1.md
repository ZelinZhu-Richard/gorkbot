# S1-002 interview guide — H1 competitor-change workflow

Status: DRAFT PROTOCOL — NOT EXECUTED; NOT VERIFIED

Protocol version: `S1-002-H1-v1`

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

## Behavioral interview — 7 to 20 minutes

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
10. What was unavailable, uncertain, stale, or contradictory?
11. What happened after the research? Which decision or action changed, if any?
12. What happened, or would have happened, if you did nothing?

Artifact prompt, without pressure:

> If it is safe and permitted, could you show me a redacted example of the watchlist, prior report, spreadsheet, battlecard, decision memo, alert, or live process? Please hide names or information you should not share.

Record `artifacts_observed=FALSE` if nothing is shown. A promised later artifact does not count as observed.

## Frequency and cost — 20 to 25 minutes

Keep the three H1 clocks separate.

1. In the last 60 days, how many times did you personally perform a competitor comparison for a decision?
2. How often do tools check sources automatically, if at all?
3. How often does a person actually read or act on a report?
4. How often was there a strategically meaningful change rather than routine page noise?
5. For the last case, roughly how many active minutes did you spend? What was the elapsed delay?
6. Did anyone else spend time on it? How much?
7. What tools or services are paid for now, and what is the approximate current spend if you know it?
8. What correction, delay, missed response, or decision cost resulted from the last failure or stale state?

Do not convert software polling frequency into customer workflow frequency.

## Current workaround and alternatives — 25 to 31 minutes

Ask unaided first:

1. What are you using now?
2. Why did you choose that process?
3. What is adequate about it?
4. What repeated step, missed state, or correction is still unsatisfactory?
5. Have you tried replacing the process? What did you actually try, and what happened?
6. Which exact step would you stop doing if the process improved?

Only after unaided answers, use the standardized recognition list:

> Have you used or seriously evaluated any of these categories: manual page checks or spreadsheets, Google Alerts, scheduled assistants, page monitors such as Visualping/PageCrawl/ChangeTower/Distill, competitor trackers such as Competiflow/Competitors.app, or larger CI suites such as Klue/Crayon/Kompyte? For each one you recognize, what happened in actual use?

Do not imply that every named product is appropriate or deficient. Record `ADEQUATE` when the participant considers the current solution good enough.

## Delegation, trust, access, and failure tolerance — 31 to 36 minutes

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

## Concept test — 36 to 40 minutes

Read the neutral contract once. Do not add benefit claims.

> Imagine a bounded two-cycle service. You provide 5–15 competitors, public URLs, a prior accepted snapshot, and your own materiality rules. Each cycle returns a coverage manifest showing checked, unchanged, changed, and unavailable sources; source-linked before/after evidence; a short decision memo; and proposed changes to a master record. Nothing is written externally without approval, and any approved test-record change is reread. The service can return unknowns and does not claim to replace every monitoring tool.

Ask:

1. In your current process, what exact step would this change, if any?
2. What would remain unchanged?
3. Which current tool would it replace, supplement, or duplicate?
4. Think about the last case you described. Would this output have changed the decision, timing, or confidence? How?
5. Which part is already handled well by your current tool?
6. Is the coverage/unknown state or approval-gated record proposal useful enough to act differently, or merely nice to have?
7. What evidence in the bundle would you ignore?
8. If a standard page monitor plus your current summary process produced the same outcome, would you still need this service?
9. What is the strongest reason this should not be built for your team?

A claimed decision change counts only when tied to the named recent workflow.

## Pilot commitment — 40 to 43 minutes

Ask in order and record exact answers:

1. Would you test this on a real, permitted watchlist for two cycles?
2. Which watchlist and prior snapshot would you use?
3. Who would own the pilot?
4. What start date within the next 30 days could you commit to?
5. What one completion criterion and one before/after metric would decide whether it worked?
6. What access or approval would block the start?
7. May I send a written pilot scope for you or the budget owner to accept?

Classification:

- `WRITTEN_QUALIFYING` only when owner, permitted input, start date, two-cycle scope, and completion criterion are all accepted in writing.
- A verbal yes, referral, scheduling suggestion, or “after you build it” is not a qualifying commitment.

## Pricing and WTP — 43 to 45 minutes

Ask behavioral budget questions before stating the test price:

1. What does the current process cost in tools and labor, if known?
2. Who approved the last comparable tool or service purchase?
3. What budget would this come from?

Then read the standardized price test without discounting or negotiation:

> The first-wave price test is USD 500 for a four-week, two-cycle pilot with the bounded scope just described and no automatic continuation. Would your organization accept that scope and price in writing?

Follow-ups:

1. Is that `yes`, `no`, or conditional on a named approval?
2. What makes that price acceptable or unacceptable?
3. If no, what would you do instead?
4. If you propose a different price, what scope and approval would that include?

Only an explicit written acceptance of the standardized offer counts for G10. Record counteroffers separately; do not negotiate during the interview.

## Closing disconfirmation

If time remains:

1. What evidence from your own workflow most contradicts the idea that this is a real problem?
2. Is this job too rare, too low-stakes, or already solved?
3. What required access or failure mode makes delegation unacceptable?
4. Who else in the company would disagree with your answers, and why?

Thank the participant. Do not promise a product, pilot slot, incentive, follow-up, or timeline beyond what S1-003 has explicitly authorized.

## Post-interview coding checklist

- Confirm `qualification` from structural facts only.
- Record absence of a 90-day occurrence as disconfirming evidence, not a screen failure.
- Separate machine cadence, human report cadence, and decision-linked frequency.
- Record actual tools before the recognition list.
- Identify a replaceable step or mark none.
- Record allowed/blocked actions and forbidden access requirements.
- Code pilot and WTP using exact commitment enums.
- Assign evidence levels per claim, then record the maximum interview level.
- Preserve contradictions and exact negative evidence.
- Store only pseudonymous/sanitized data and a restricted source-reference ID.
