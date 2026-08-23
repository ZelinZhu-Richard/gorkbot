# S1-002 interview guide — H2 issue-to-PR verification workflow

Status: DRAFT PROTOCOL — NOT EXECUTED; NOT VERIFIED

Protocol version: `S1-002-H2-v1`

Target duration: 45 minutes

Companion plan: `03_product/S1-002_CUSTOMER_DISCOVERY_PLAN.md`

## Interviewer rules

1. Do not lead with “AI agent,” independent verification, evidence bundles, or better trust.
2. Ask about the last bounded issue/PR and the current completion decision before presenting a concept.
3. Treat issue-to-PR generation, tests, CI, review, logs, and proof artifacts as existing alternatives, not assumed differentiation.
4. Capture delegation behavior before and after the H8 residual concept; a rating change without an action change is not material lift.
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

## Behavioral interview — 7 to 20 minutes

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
10. What failed, was flaky, contradicted another signal, or remained unknown?
11. Was the issue reopened, returned for rework, delayed, or later found incomplete? What was the consequence?
12. How did you decide it was safe enough to merge or reject? Who had final authority?

Artifact prompt, without pressure:

> If it is safe and permitted, could you show a redacted issue, PR/check summary, test log, review artifact, or the workflow you used? Please hide code, names, URLs, secrets, or customer information.

Record `artifacts_observed=FALSE` when nothing is shown. A promised artifact does not count.

## Frequency and cost — 20 to 25 minutes

1. In the last 30 days, how many bounded issues did you personally triage for implementation?
2. How many human- or agent-authored PRs did you personally review?
3. How many required manual reproduction or checks beyond ordinary CI?
4. For the last case, how many active minutes did implementation review and verification take you and others?
5. What was the elapsed issue/PR delay?
6. How much rework, reopen time, or incident/defect cost resulted?
7. Which coding, review, or CI tools are paid for now, and what is the approximate spend if known?
8. What happens when you accept the author's completion claim without additional checking?

Do not use the number of automated tasks as the participant's human workflow frequency.

## Current workaround and alternatives — 25 to 31 minutes

Ask unaided first:

1. What do you use today to move a bounded issue to a merge decision?
2. What is adequate about that stack?
3. Where is evidence generated by the same authoring system?
4. Who or what provides a genuinely independent check, if anyone?
5. What repeated manual verification step, reopen, correction, or stale-state check is still unsatisfactory?
6. Have you tried replacing this process? What did you actually try, and what happened?
7. Which exact step would you stop doing if the process improved?

Only after unaided answers, use the standardized recognition list:

> Have you used or seriously evaluated any of these categories: manual peer review and reproduction, CI/security checks, GitHub Copilot cloud agent or code review, Codex cloud/review, Claude Code/Code Review, Cursor Cloud Agents/Bugbot, Devin/Devin Review, Jules, or another issue-to-PR or AI-review system? For each one you recognize, what happened in actual use?

Do not imply that a vendor lacks verification. Record `ADEQUATE` when the current combination is sufficient.

## Delegation, trust, access, and failure tolerance — 31 to 36 minutes

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

## Concept test, including H8 — 36 to 40 minutes

### Commodity baseline

Read first:

> Contract A starts from a bounded issue, creates a change on a branch, runs the available tests, and prepares a draft PR with the author run's logs and current CI/check results. A human still reviews and controls merge.

Ask:

1. How different is Contract A from what you already have?
2. For the last case you described, what would Contract A change?
3. Would it change any permission or delegation decision? Which one?

Do not count interest in Contract A as support for H2's differentiation.

### H8 residual contract

Read second:

> Contract B adds a separate verifier after the author run stops. It receives the acceptance condition independently, freezes the base and PR-head commits, starts in a clean environment, reproduces the relevant behavior and tests, rereads the current remote PR and CI/check state, and returns a source-linked bundle that preserves contradictions and unknowns. It cannot merge or deploy.

Ask:

1. For the last case, what specific review or merge decision would Contract B change, if any?
2. Which permission would you grant only with Contract B?
3. Which manual check would you remove or shorten? How would we measure that?
4. Which evidence is already sufficient: ordinary CI, author logs, video, code review, human test, or something else?
5. What makes the second run meaningfully independent in your environment? What would make it theater?
6. What evidence in Contract B would you ignore?
7. Would clean reproduction create too much setup, latency, flakiness, or cost?
8. Would you buy verification without buying issue-to-code generation? Why or why not?
9. What is the strongest reason this should not be built for your team?

Record `delegation_tier_after_concept`. `h8_material_trust_lift=TRUE` only when a named action, permission, workflow step, or recent decision changes under the plan's definition. A rating increase alone is false.

## Pilot commitment — 40 to 43 minutes

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
- A verbal yes, sandbox suggestion, referral, or “when it supports our stack” is not qualifying.

## Pricing and WTP — 43 to 45 minutes

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

Only explicit written acceptance of the standardized offer satisfies G10. Record counteroffers separately; do not negotiate during the interview.

## Closing disconfirmation

If time remains:

1. What evidence from your workflow most contradicts the idea that independent reproduction is a real problem?
2. Is current CI/review already adequate?
3. Is the pain generation speed rather than verification? If so, record this against H2's differentiation.
4. What required access, latency, or failure mode makes the workflow unacceptable?
5. Who else in the company would disagree with your answers, and why?

Thank the participant. Do not promise a product, pilot slot, incentive, follow-up, or timeline beyond S1-003's explicit authority.

## Post-interview coding checklist

- Confirm `qualification` from structural facts only.
- Record no recent occurrence as disconfirming evidence, not a screen failure.
- Separate issue/PR volume from the participant's direct triage/review frequency.
- Record actual tools before the recognition list.
- Identify a replaceable verification step or mark none.
- Record allowed/blocked actions, environment requirements, and forbidden access.
- Compare delegation tiers before/after Contract B using actions, not ratings.
- Record H8 verification-only interest and qualifying pilot commitment separately.
- Code pilot and WTP using exact commitment enums.
- Assign evidence levels per claim, preserve contradictions, and store only sanitized data plus a restricted source-reference ID.
