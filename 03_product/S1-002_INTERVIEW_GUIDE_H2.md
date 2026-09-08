# S1-002 interview guide — H2 issue-to-PR verification workflow

Status: FIXED DRAFT PROTOCOL — NOT EXECUTED; NOT VERIFIED

Protocol version: `S1-002-H2-v2`

Target duration: 45 minutes

Companion plan: `03_product/S1-002_CUSTOMER_DISCOVERY_PLAN.md`

## Interviewer rules

1. Do not lead with “AI agent,” independent verification, evidence bundles, or better trust.
2. Ask about the last bounded issue/PR and the current completion decision before presenting a concept.
3. Treat issue-to-PR generation, tests, CI, review, logs, and proof artifacts as existing alternatives, not assumed differentiation.
4. Capture delegation behavior before both contracts, after Contract A, and after Contract B; a rating change without an action change is not material lift.
5. Record negative evidence without persuasion. Do not rescue H2 by shifting the conversation to faster code generation.
6. One structurally qualified participant counts in the denominator even when the workflow is rare, current tools are adequate, or delegation is rejected.
7. Do not store repository names, URLs, source code, credentials, recordings, or identifiable confidential material in the public repository.
8. Never interpret praise, referrals, waitlist interest, or “try me later” as a pilot or WTP commitment.

## Opening and consent — 0 to 3 minutes

Suggested script:

> I am researching how small software teams decide whether bounded issue and pull-request work is actually complete. This is not a sales call, and I want to understand the current process before discussing any concept. I will take notes. You can skip any question and should not share source code, credentials, customer data, or anything confidential.

Ask and record:

1. May I take notes?
2. May I record this conversation? If no, continue with notes only.
3. May I later use a sanitized quotation? A yes is optional and separate from recording permission.
4. If you show a PR or workflow, may I record only a sanitized description and evidence reference? Do not copy code or private links into the repository.

## Structural screening — 3 to 7 minutes

These questions establish the ICP only. Do not qualify on pain, agent usage, frequency, dissatisfaction, trust, or interest.

1. What is your current role, and which engineering decisions do you personally own?
2. Is this an operating commercial software team or product?
3. How many active developers work on the relevant codebase?
4. Does the team use a Git-based pull-request workflow?
5. Is there a runnable test, build, preview, or reproduction path for at least some bounded issues?
6. In the last 12 months, were you directly responsible for issue triage, PR review, or deciding whether bounded work was complete?
7. Who can authorize repository access and a small workflow pilot? Who controls that budget?

Screen outcome:

- `ICP_QUALIFIED`: operating commercial software team, 2–20 developers, Git/PR workflow, at least one bounded runnable test path, and direct responsibility in the last 12 months.
- `SCREEN_FAIL`: a structural criterion is not met. End politely; do not count the interview.
- Do not screen out participants because they do not use coding agents, have no recent pain, trust current CI, refuse delegation, or would not pay.

## Behavioral interview — 7 to 19 minutes

Mandatory behavior checkpoint begins here. Do not show either concept contract yet.

1. Tell me about the last bounded issue or pull request whose completion you personally had to judge.
2. What triggered the work, and when did it happen?
3. What did “done” mean before work started? Who wrote or understood that acceptance condition?
4. Who or what performed the implementation?
5. Walk me through every step from issue selection to your final decision.
6. Which repository, environment, dependencies, tests, CI checks, preview, or external behavior mattered?
7. What evidence did the author or tool provide?
8. What did you independently check yourself?
9. Did the base, PR head, environment, or remote CI state change while the work was underway?
10. Did anything fail, become flaky, contradict another signal, or remain unknown? If not, record none.
11. Was the issue reopened, returned for rework, delayed, or later found incomplete? If so, what was the consequence; if not, record none.
12. How did you decide it was safe enough to merge or reject? Who had final authority?

Artifact prompt, without pressure:

> If it is safe and permitted, could you show a redacted issue, PR/check summary, test log, review artifact, or the workflow you used? Please hide code, names, URLs, secrets, or customer information.

Record `artifacts_observed=FALSE` when nothing is shown. A promised artifact does not count.

## Frequency and cost — 19 to 24 minutes

1. In the last 30 days, how many bounded issues did you personally triage for implementation?
2. How many human- or agent-authored PRs did you personally review?
3. How many required manual reproduction or checks beyond ordinary CI?
4. For the last case, how many active minutes did implementation review and verification take you and others?
5. What was the elapsed issue/PR delay?
6. Was there rework, reopen time, or incident/defect cost? If so, how much; if not, record none.
7. Which coding, review, or CI tools are paid for now, and what is the approximate spend if known?
8. Do you ever accept a completion claim without additional checking? What happened the last time? If that does not occur, record none.

Do not use the number of automated tasks as the participant's human workflow frequency.

## Current workaround and alternatives — 24 to 30 minutes

Ask unaided first:

1. What do you use today to move a bounded issue to a merge decision?
2. What is adequate about that stack?
3. Which checks are performed by the person or tool that made the change, and which are performed by someone or something else?
4. Which checks, if any, are performed by someone or something other than the author or authoring tool?
5. Is any repeated manual verification step, reopen, correction, or stale-state check still unsatisfactory? If none, what is adequate enough to keep?
6. Have you tried replacing this process? What did you actually try, and what happened?
7. If the process improved, is there an exact step you would stop doing? If none, record none.

Only after unaided answers, use the standardized recognition list:

> Have you used or seriously evaluated any of these categories: manual peer review and reproduction, CI/security checks, GitHub Copilot cloud agent or code review, Codex cloud/review, Claude Code/Code Review, Cursor Cloud Agents/Bugbot, Devin/Devin Review, Jules, or another issue-to-PR or AI-review system? For each one you recognize, what happened in actual use?

Do not imply that a vendor lacks verification. Record `ADEQUATE` when the current combination is sufficient.

## Delegation, trust, access, and failure tolerance — 30 to 35 minutes

Begin with past behavior:

1. Tell me about the last time you delegated repository work to a person or coding tool.
2. What repository/data/secret access did you allow, and what did you block?
3. What branch, review, or approval controls were in place?
4. What did you still check manually before merge?
5. What would you never delegate?
6. Would you permit a no-merge test on an authorized repo or fixture with immutable base/head commits and a runnable setup/test path? Why or why not?
7. Would production credentials, deployment access, or merge authority be required for first value?
8. Describe a false assurance or missed defect that would be tolerable and one that would not be.
9. Are explicit `UNKNOWN`, flaky-test, or verifier-disagreement results acceptable? When are they not?
10. What evidence must exist before you grant branch write, draft-PR, or broader scope?

Record `delegation_tier_before_concept` now, based on specific permitted actions rather than a 1–10 trust rating.

## Contract A / Contract B test, including H8 — 35 to 40 minutes

### Commodity baseline

Read first:

> Contract A starts from a bounded issue, creates a change on a branch, runs the available tests, and prepares a draft PR with the author run's logs and current CI/check results. A human still reviews and controls merge.

Ask:

1. How different is Contract A from what you already have?
2. For the last case, would Contract A change any exact step, permission, or delegation decision? If so, which one; if not, record none.
3. Would Contract A alone adequately solve the job? Why or why not?

Record `delegation_tier_after_contract_a`. Do not count interest, novelty, or time savings in Contract A as support for H2's differentiation.

### H8 residual contract

Read second:

> Contract B adds a separate verifier after the author run stops. It receives the acceptance condition independently, freezes the base and PR-head commits, starts in a clean environment, reproduces the relevant behavior and tests, rereads the current remote PR and CI/check state, and returns a source-linked bundle that preserves contradictions and unknowns. It cannot merge or deploy.

Ask:

1. For the last case, what specific review or merge decision would Contract B change, if any?
2. Would any permission change only with Contract B? If so, which one; if not, record none.
3. Would you remove or shorten any manual check? If so, which one and how would that be measured; if not, record none.
4. Which existing evidence is already sufficient, and would the second run be operationally independent in your environment or merely duplicate the authoring system?
5. Would you use or pilot verification without issue-to-code generation? What action, if any, would that change, and what setup, latency, flakiness, cost, or ignored evidence would prevent it?

Record `delegation_tier_after_concept` after Contract B. Set both `contract_b_material_action_lift=TRUE` and `h8_material_trust_lift=TRUE` only when a named action, permission, workflow step, or recent decision changes over Contract A under the plan's definition. A rating increase alone is false. Record `h8_verification_only_interest` separately from lift.

Distinct H8 reconsideration is not decided in the interview: the plan requires 4/8 action-level lifts, 4/8 verification-only interest, and at least 3 of the same participants satisfying both plus the written pilot commitment, followed by independent review. No separate H8 quota is created.

## Pilot commitment — 40 to 42 minutes

Ask in order and record exact answers:

1. Would you test Contract B on a real authorized bounded issue/PR for two cycles, with no merge or deploy?
2. Which repository/fixture and bounded cases would you use?
3. Can you provide immutable base/head commits, setup/test commands, and PR/CI read access without production credentials?
4. Who would own the pilot?
5. What start date within the next 30 days could you commit to?
6. What completion criterion and before/after metric would decide whether it worked?
7. Would you test verification-only without issue-to-code generation?
8. May I send a written pilot scope for you or the budget owner to accept?

Classification:

- `WRITTEN_QUALIFYING` only when owner, authorized input/access, start date, two-cycle scope, and completion criterion are accepted in writing.
- Set `h8_pilot_commitment=TRUE` only when that qualifying written commitment explicitly covers verification-only Contract B without issue-to-code generation; verbal or conditional verification-only interest remains false.
- A verbal yes, sandbox suggestion, referral, or “when it supports our stack” is not qualifying.

## Pricing and WTP — 42 to 44 minutes

Ask behavioral budget questions first:

1. What does the current process cost in tools, review time, rework, or delay, if known?
2. Who approved the last comparable engineering tool or service purchase?
3. What budget would this come from?

Then read the identical standardized price test:

> The first-wave price test is USD 500 for a four-week, two-cycle pilot with the bounded no-merge scope just described and no automatic continuation. Would your organization accept that scope and price in writing?

Follow-ups:

1. Is that `yes`, `no`, or conditional on a named approval?
2. What makes that price acceptable or unacceptable?
3. If no, what would you use or do instead?
4. If you propose a different price, what scope and approval would that include?

Only explicit written acceptance of the standardized offer satisfies G10. Code it `WRITTEN_500_ACCEPTANCE` and Level 4 at most. A conversational “yes” or “USD 500 sounds reasonable” is `PRICE_REACTION_ONLY`; only payment/deposit, a signed paid-pilot order, or an equivalent binding signed commitment naming amount, budget owner, and execution date is Level 5 / `ECONOMIC_COMMITMENT`. Record counteroffers separately; do not negotiate during the interview.

## Mandatory closing disconfirmation — 44 to 45 minutes

Ask both; they are not optional:

1. What observed evidence from your workflow most contradicts the idea that Contract B's independent-reproduction problem is real?
2. What is the strongest reason not to build Contract B for your team?

If time remains, ask whether current CI/review is already adequate, whether the pain is generation speed rather than verification, what access/latency/failure boundary blocks the workflow, and who in the company would disagree.

Thank the participant. Do not promise a product, pilot slot, incentive, follow-up, or timeline beyond S1-003's explicit authority.

## Post-interview coding checklist

- Confirm `qualification` from structural facts only.
- Record no recent occurrence as disconfirming evidence, not a screen failure.
- Separate issue/PR volume from the participant's direct triage/review frequency.
- Record actual tools before the recognition list.
- Identify a replaceable verification step or mark none.
- Record allowed/blocked actions, environment requirements, and forbidden access.
- Compare delegation tiers before contracts, after Contract A, and after Contract B using actions, not ratings.
- Code Contract B / H8 lift only from a B-over-A action change tied to the recent case.
- Record H8 verification-only interest and qualifying pilot commitment separately.
- Code pilot and WTP using exact commitment enums.
- Record `interview_completion`; truncated ICP-qualified interviews remain in the denominator with unasked gates as non-successes.
- Assign evidence levels per claim, preserve contradictions, and store only field-level sanitized data plus an opaque restricted source-reference ID; `pilot_owner` is a role and `pilot_input` is generic.
