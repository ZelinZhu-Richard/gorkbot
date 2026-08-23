# S1-001 customer-workflow scorecard and evidence plan

Status: AUTHOR DRAFT — READY FOR INDEPENDENT CHALLENGER REVIEW

Research date: 2026-08-23

Scored data: `03_product/S1-001_SCORED_HYPOTHESES.csv`

Current-workaround research: `02_research/S1-001_CURRENT_WORKAROUND_EVIDENCE_2026-08-23.md`

## Outcome first

**DESIGN PROPOSAL — provisional discovery beachhead:** prioritize discovery for a founder, head of product, or product-marketing lead at a **3–30 person B2B SaaS company with 5–15 named competitors and no dedicated competitive-intelligence analyst**. Test one narrow workflow: a **verification-first weekly ledger of material product, pricing, and changelog changes from an explicit official-source allowlist**, followed by a cited delta brief and an approval-gated update to the customer's master record.

This is **not a validated customer selection**. It is the hypothesis to test first.

The raw scorecard ranks H2, GitHub issue to reviewed pull-request candidate, first at `76.8/100` and H1, the competitor-change workflow, second at `75.6/100`. The `1.2`-point gap is smaller than a one-level change in any moderately weighted criterion, so the author treats them as a directional tie. H1 is selected for discovery because it offers a read-only, lower-sensitivity first test, a simpler external completion predicate, and alignment with the founder's stated reach hypothesis. H2 remains the explicit counter-hypothesis.

**VERIFIED FACT — evidence state:** the repository contains zero customer interviews, usage records, pilot commitments, payments, or retention evidence. Every demand-side score is therefore low-confidence and provisional.

**VERIFIED FACT — founder preference:** D-006 and the founder brief prefer starting discovery with technical founders and small startup teams. That is evidence of founder preference and proposed reach, not customer demand.

**VERIFIED FACT — current alternatives:** first-party pages document strong adjacent products in every shortlisted workflow. GitHub Copilot and Codex cover asynchronous coding work; ChatGPT deep research, Klue, and Crayon cover cited research or competitor monitoring; Hex, Dovetail, and Elicit cover analytics, customer research, and literature workflows; Vercel covers preview deployments; Power Automate covers browser automation. See SRC-064 through SRC-074.

**OPEN QUESTION:** whether any target customer values a verification-first delta ledger enough to switch, pilot, or pay.

## Evidence and claim discipline

| Evidence class | What exists | What it permits |
|---|---|---|
| Repository-verified project state | Stage 0 verified; no customer evidence; D-006/D-007 provisional; A-001/A-002/A-005 open | State constraints and explicit founder preference only |
| Current first-party product pages | Documented product positioning and capabilities in SRC-064 through SRC-074 | Alternative/product-availability and workflow-crowding screen only |
| Prepared founder materials | Workflow descriptions, completion predicates, and founder intent | Hypothesis generation and prototype-fit judgment only |
| Author scoring | Seven scored combinations with explicit weights | A transparent order for discovery; not a market fact |
| Missing evidence | Interviews, observed work, artifacts, pilots, payment, retention | No claim of pain, demand, willingness to pay, or product-market fit |

No market size, customer count, conversion rate, willingness to pay, or traction is asserted.

## Scoring method

Each hypothesis receives an integer score from `1` to `5` for each criterion:

- `1`: structurally unfavorable for a first wedge
- `2`: material weakness
- `3`: mixed, neutral, or substantially unknown
- `4`: promising but unvalidated
- `5`: unusually favorable as a hypothesis

For `integration tractability`, `security manageability`, and `sales-cycle speed`, a higher score is more favorable: fewer or easier integrations, less sensitive data, and a shorter hypothesized sales cycle. A high score is not a claim that the real customer condition has been observed.

The weighted total is:

```text
sum(criterion score × criterion weight) / 5
```

The weights sum to `100`. Scores and weights are author judgments subject to challenger review and customer evidence.

| Criterion | Weight | Why it matters at Stage 1 |
|---|---:|---|
| Pain and urgency | 11 | A wedge must displace a painful job, not create novelty work. |
| Current-workaround gap | 5 | Strong existing solutions lower switching motivation. |
| Workflow frequency | 7 | Repetition supports learning and retention. |
| Economic value | 8 | The result must justify product and service cost. |
| Cost of failure | 5 | Failure cost shapes trust, verification, and buyer urgency. |
| Willingness to delegate | 6 | A painful job is not useful if customers refuse delegation. |
| Integration tractability | 7 | Fewer, safer integrations reduce prototype risk. |
| Security manageability | 6 | Low-sensitivity inputs permit faster responsible learning. |
| Sales-cycle speed | 7 | A small team needs fast design-partner feedback and revenue tests. |
| Ease of reaching users | 8 | Founder-led discovery depends on access to qualified users. |
| Prototype feasibility | 10 | The first demo must be repeatable and objectively verifiable. |
| Differentiation | 8 | The wedge must be more than a generic agent or existing feature. |
| Expansion potential | 4 | The narrow wedge should lead to adjacent durable workflows. |
| Bootstrap revenue potential | 5 | Early paid pilots should be possible without enterprise scale. |
| Investor relevance | 3 | A credible platform path helps, but customer evidence comes first. |
| **Total** | **100** | |

## Ranked hypotheses

| Rank | ID | Customer × workflow | Total | Evidence confidence | Customer evidence |
|---:|---|---|---:|---|---|
| 1 | H2 | Small software team × bounded GitHub issue to tested, reviewed PR candidate | 76.8 | LOW | 0 — none |
| 2 | H1 | Small B2B SaaS team × verification-first official-source competitor-change ledger | 75.6 | LOW | 0 — none |
| 3 | H3 | Data/analytics team × reproducible data-quality and decision report | 68.8 | LOW | 0 — none |
| 4 | H6 | Small web agency × bounded website change to checked preview | 67.8 | LOW | 0 — none |
| 5 | H7 | Operations-heavy small business × browser record reconciliation with proposed updates | 66.2 | LOW | 0 — none |
| 6 | H4 | Product/user-research team × traceable interview synthesis | 63.0 | LOW | 0 — none |
| 7 | H5 | Applied research team × literature intelligence workspace | 62.8 | LOW | 0 — none |

The complete criterion-level values are in the CSV. The ranking is a prioritization instrument, not measurement of a population.

## Sensitivity and selection rule

- H2 leads H1 by `1.2` points. A one-level change in a criterion weighted `6` changes the total by `1.2`; a one-level change in an `8`-weight criterion changes it by `1.6`. The top two are therefore not meaningfully separated by this author-only score.
- H2's structural pain, frequency, and economic-value hypothesis are strong, but SRC-064 and SRC-065 show that the core issue-to-PR sequence is already directly served. Its differentiation score is `2`.
- H1 also faces strong alternatives: SRC-066 provides cited deep research and SRC-067/SRC-068 provide competitor monitoring. Its proposed edge is narrower—verified delta state and approval-gated record updates—not generic citations.
- H1 receives the first discovery slot because the founder's stated target and proposed founder-led outreach make qualified-user access more plausible, while public-source-only inputs make an initial concierge test lower sensitivity. Neither point is customer evidence.
- If the H1 problem or payment gates fail, or H2 produces stronger artifact, pilot, and payment evidence, reopen D-011 and prefer H2 or another candidate. Do not defend the author ranking.

## Hypothesis briefs

### H1 — small B2B SaaS competitor-change intelligence

**PROVISIONAL HYPOTHESIS:** a founder or product/product-marketing lead at a 3–30 person B2B SaaS company, tracking 5–15 named competitors without a dedicated CI analyst, performs material competitor-change research at least monthly and will delegate a weekly public-source change ledger when every material claim is independently inspectable.

- **Pain, frequency, value, and failure:** OPEN QUESTIONS. Scores assume missed or stale product/pricing changes can create planning or positioning rework; no occurrence or cost is evidenced.
- **Current workaround:** general cited research and purpose-built CI monitoring exist (SRC-066 through SRC-068). Actual small-team use remains unknown.
- **Delegation:** read-only public research appears structurally delegable, but interviews must identify sources and decisions users will not delegate.
- **Required integrations:** initial test needs an allowlisted browser/web fetcher plus CSV/spreadsheet and memo artifacts. CRM, Slack, email, authenticated sources, and automatic schedules are non-goals for the first test.
- **Security:** use public official sources and a customer-supplied non-secret watchlist; no credentials, private customer data, or external publishing.
- **Sales and reach:** founder-led access is a founder preference, not verified recruiting reach. The hypothesized buyer can approve a small pilot without enterprise procurement; this must be tested.
- **Prototype feasibility:** high because the result can be compared against a prior snapshot and a manually curated source set.
- **Differentiation:** the proposed verification contract is a hypothesis. Citations alone are not differentiated.
- **Expansion:** recurring monitoring, customer-supplied sources, product-marketing distribution, win/loss evidence, and operating intelligence are later possibilities only after the narrow workflow retains users.
- **Falsifier:** insufficient observed frequency/artifacts, satisfaction with existing tools, no value placed on delta evidence, authenticated/private-source dependence, or failure to obtain paid-pilot commitments.

### H2 — small software team issue to reviewed PR candidate

**PROVISIONAL HYPOTHESIS:** a technical founder or engineering lead at a 2–20 developer team will delegate bounded, well-tested repository issues when the system reproduces the problem, records tests and review evidence, and never merges without approval.

- **Pain, frequency, value, and failure:** structurally promising but unobserved in target teams.
- **Current workaround:** GitHub Copilot cloud agent and Codex already cover issue delegation, pull requests, cloud work, testing, and review (SRC-064, SRC-065).
- **Delegation and security:** repository access, code, dependency installation, CI, secrets, and write permissions create higher trust and isolation requirements than H1.
- **Required integrations:** GitHub, terminal/test environment, dependency registry, and optional preview environment.
- **Sales and reach:** technical founders match D-006, but access and purchasing authority are untested.
- **Prototype feasibility:** high for well-instrumented repositories; environment reproduction and flaky tests reduce repeatability.
- **Differentiation:** weak unless independent verification materially outperforms current coding agents on a customer-owned task.
- **Expansion:** code review, maintenance, release preparation, incident follow-up, and engineering operations.
- **Falsifier:** qualified teams already trust existing agents, will not grant repository access, cannot provide runnable test environments, or see no improvement in verified completion.

### H3 — boutique or internal analytics team data report

**PROVISIONAL HYPOTHESIS:** an analyst responsible for recurring decisions will delegate data-quality checks and a reproducible report when calculations, filters, units, charts, and caveats can be re-run and independently checked.

- **Pain, frequency, value, and failure:** potentially high but no observed jobs, time, error, or buyer evidence exists.
- **Current workaround:** spreadsheets/notebooks and a purpose-built agentic analytics platform such as Hex (SRC-069).
- **Delegation and security:** customer exports, warehouse schemas, commercial metrics, and PII may be sensitive.
- **Required integrations:** file ingestion and notebook/terminal initially; warehouse, BI, and semantic-model integrations later.
- **Sales and reach:** analytics practitioners are in the recruiting brief, but founder reach is unknown.
- **Prototype feasibility:** strong with scrubbed exports and fixed questions; weaker with live warehouse ambiguity.
- **Differentiation:** reproducibility and independent calculation checks must beat existing governed notebook workflows.
- **Expansion:** recurring reporting, metric diagnostics, planning, and decision support.
- **Falsifier:** analysts prefer direct notebook control, cannot share safe fixtures, or corrections consume more time than the delegated work saves.

### H4 — product/user-research interview synthesis

**PROVISIONAL HYPOTHESIS:** a product or research team will delegate first-pass coding and synthesis if every theme links to permitted source excerpts or timestamps and dissenting evidence remains visible.

- **Pain, frequency, value, and failure:** unobserved; transcript volume and decision impact must be measured.
- **Current workaround:** Dovetail already positions evidence-linked clips, research memory, PII controls, and purpose-built analysis (SRC-070).
- **Delegation and security:** recordings, participant PII, consent, and confidential roadmap context create high sensitivity.
- **Required integrations:** transcript/file ingestion initially; meeting, support, and repository connectors later.
- **Sales and reach:** product researchers are recruitable in principle but no channel conversion is known.
- **Prototype feasibility:** high on permitted redacted transcripts; real data handling is the gating risk.
- **Differentiation:** weak unless cross-tool portability or an independently verified evidence graph solves a documented switching problem.
- **Expansion:** research repository, feedback triage, roadmap evidence, and recurring voice-of-customer synthesis.
- **Falsifier:** PII/security blocks cloud delegation, purpose-built repositories are satisfactory, or researchers reject model-generated coding even with provenance.

### H5 — applied-research literature intelligence

**PROVISIONAL HYPOTHESIS:** an applied research team will delegate paper accounting, extraction, and a research-gap memo when each claim maps to page/section evidence and uncertain extraction is flagged.

- **Pain, frequency, value, and failure:** systematic evidence work can be intensive, but target-team behavior and budget are unknown.
- **Current workaround:** Elicit documents reports, review screening/extraction, libraries, alerts, and sentence-level citations (SRC-071).
- **Delegation and security:** public papers are manageable; unpublished manuscripts, clinical data, or licensed corpora are not in initial scope.
- **Required integrations:** PDF/file processing and bibliography/spreadsheet output; database and publisher access later.
- **Sales and reach:** academic procurement may be slow; applied or commercial research teams may differ. Both are open questions.
- **Prototype feasibility:** moderate to high on a fixed public corpus, constrained by PDF and table extraction reliability.
- **Differentiation:** weak without a validated domain or workflow that existing literature tools do not cover.
- **Expansion:** alerts, evidence maintenance, protocol support, and regulated evidence workflows only with appropriate controls.
- **Falsifier:** existing products satisfy the job, budgets are individual/low, or required accuracy demands make correction cost prohibitive.

### H6 — small web agency website-release preparation

**PROVISIONAL HYPOTHESIS:** a small agency or founder will delegate bounded site changes when the agent produces a checked preview and cannot deploy production without explicit approval.

- **Pain, frequency, value, and failure:** plausible but unobserved; the job may already be fast enough with existing tools.
- **Current workaround:** coding agents cover changes and Vercel provides automatic pull-request previews and production-after-merge workflows (SRC-065, SRC-072).
- **Delegation and security:** repository and preview access are sensitive, but production can remain blocked.
- **Required integrations:** Git provider, build/test toolchain, browser preview, and one preview host.
- **Sales and reach:** agencies may buy quickly, but founder reach and pricing are unknown.
- **Prototype feasibility:** high for a known stack and fixture site.
- **Differentiation:** weak unless visual, accessibility, and external-state verification remove a measured review bottleneck.
- **Expansion:** multi-site maintenance, content operations, accessibility remediation, and release coordination.
- **Falsifier:** existing coding/preview flow is satisfactory, stack diversity destroys repeatability, or preview QA still requires full manual work.

### H7 — operations-heavy SMB browser record reconciliation

**PROVISIONAL HYPOTHESIS:** an operations user working across a browser-only application and spreadsheets will delegate read-only extraction and reconciliation if all proposed writes are reviewable and blocked pending approval.

- **Pain, frequency, value, and failure:** potentially high and recurring, but no actual SMB workflow has been observed.
- **Current workaround:** manual work and RPA are hypotheses; Power Automate publicly documents browser automation capabilities and concrete control failures (SRC-073, SRC-074).
- **Delegation and security:** customer records, account credentials, PII, and write actions create high sensitivity.
- **Required integrations:** browser control, spreadsheet/file reconciliation, authentication takeover, and approval interception.
- **Sales and reach:** the buyer and distribution path are unclear, and setup may become services-heavy.
- **Prototype feasibility:** lowest in the set because UI variability and account-specific state are central to the workflow.
- **Differentiation:** verified proposed changes and robust exception handling could matter, but neither is customer-validated.
- **Expansion:** broader back-office operations and recurring routines if one vertical is selected.
- **Falsifier:** no repeatable vertical process is found, setup cost exceeds value, browser reliability is inadequate, or customers reject cloud credential handling.

## Provisional beachhead contract

### Customer

Founder, head of product, or product-marketing lead at a 3–30 person B2B SaaS company that tracks 5–15 named competitors and has no dedicated CI analyst.

### Trigger and job

At a weekly review or before a positioning/release decision, determine what materially changed on allowlisted official competitor product, pricing, documentation, and changelog pages since the prior accepted snapshot.

### Narrow first output

1. A machine-checkable CSV change ledger with company, source URL, source type, prior observed value, current observed value, retrieved-at time, materiality classification, confidence, and status.
2. A short cited delta memo covering only material changes and explicit unknowns.
3. A proposed update to the customer's master ledger, held for approval.
4. After approval in a test environment, a readback proving the intended record and exact values changed once.

### Completion predicate

- every allowlisted source is covered or marked unavailable;
- every material claim links to current source evidence and the prior accepted snapshot;
- no unsupported material claim appears;
- duplicate records are rejected;
- CSV schema and memo-to-ledger consistency checks pass;
- no external publication, message, or master-record update occurs without approval;
- any approved test update is re-read and exactly verified;
- uncertainty and source failure remain visible rather than being converted into a change claim.

### Primary differentiator to test

**PROVISIONAL HYPOTHESIS:** verification-first delta evidence and explicit completion state are more valuable than a generic cited report. Model transparency is secondary and is not assumed to be a purchasing driver. This narrows D-007 for testing without confirming it.

### Prototype demo proposal

Use a synthetic or founder-created prior snapshot and five public competitor sites. Run one change cycle, identify a seeded mix of changed, unchanged, duplicate, and unavailable sources, produce the ledger and memo, block a master-ledger update for approval, accept one user correction, apply the approved update in a test record, and re-read it. This is a proposed demo definition, not an implementation or observed result.

### Expansion path

Only if the narrow workflow retains users: scheduled monitoring, authenticated customer-supplied sources, team distribution, win/loss evidence, product-planning context, and a broader recurring operating-intelligence teammate. No expansion item is MVP scope today.

## Falsification plan

### H1 problem gate — eight qualified interviews

Pass only if all of the following occur:

1. At least `5/8` participants personally performed the defined competitor-change job at least twice in the preceding 60 days.
2. At least `4/8` provide a permitted redacted prior artifact, source list, or live process walk-through; hypothetical interest alone does not count.
3. At least `4/8` report two or more hours of active work per cycle and can connect that estimate to the observed steps or artifact.
4. At least `3/8` describe a specific missed or stale change in the preceding 90 days and a concrete consequence; generalized fear does not count.

Failing any item falsifies the initial pain/frequency framing and removes H1 from the build queue pending a revised segment or job.

### Delegation and differentiation gate

Pass only if:

1. At least `5/8` will test read-only delegation on their own public watchlist.
2. At least `4/8`, after comparing a generic cited report with the proposed delta ledger, select the inspectable before/after and completion-state evidence as materially useful for a real decision.
3. Fewer than `3/8` require authenticated, private, or regulated sources for the first valuable version.
4. Fewer than `5/8` describe their current alternative as satisfactory with no material unsolved gap.

If generic citations are sufficient, or existing CI products solve the job, verified completion is not a wedge for this workflow even if participants like the concept.

### Commitment and payment gate

Pass only if:

1. At least `3/8` provide a permitted watchlist plus prior artifact and commit in writing to a two-cycle concierge pilot.
2. After reviewing one sample cycle, at least `2/8` accept a written price test of `USD 500` for a four-week pilot. The number is a DESIGN PROPOSAL for falsification, not a price decision or willingness-to-pay claim.

Interest, compliments, waitlist signup, or an unpaid trial without artifact access do not satisfy payment evidence. If pain passes and payment fails, do not call the wedge commercially validated; test a different buyer, outcome, or candidate.

### Prototype feasibility gate — after customer evidence authorizes a build

On three permitted customer-supplied or equivalently representative watchlists across two consecutive cycles:

- `100%` of material claims have accessible source and prior-state evidence;
- `0` unsupported material claims;
- at least `90%` precision and `90%` recall against an independently curated material-change set;
- `0` unauthorized external writes or messages;
- approved test updates are applied exactly once and pass readback;
- median human correction time is no more than 15 minutes per cycle;
- task cost, latency, unavailable-source rate, and false-completion rate are recorded rather than assumed.

These thresholds are proposed acceptance tests. No run has occurred.

### Counter-hypothesis rule

Run at least four artifact-led H2 interviews in the same discovery wave. Reopen the selection if H2 produces more qualified artifacts, stronger pilot commitments, or stronger payment evidence than H1, despite its lower differentiation score. H1 receives no incumbent advantage.

## Interview recruiting plan

### Objective and timing

**DESIGN PROPOSAL:** recruit and complete `20` discovery interviews between `2026-08-24` and `2026-09-13`, subject to founder availability and approval. This stays within A-001's `15–25` interview evidence target and deliberately covers multiple segments.

No outreach has been sent, no participant has been recruited, and no incentive is authorized in this task.

### Sampling quotas

| Quota | Candidate group | Qualification screen | Main hypotheses |
|---:|---|---|---|
| 8 | B2B SaaS founders, heads of product, or product-marketing leads | 3–30 staff; 5–15 named competitors; personally touched competitor research in last 60 days; no dedicated CI analyst | H1 |
| 4 | Technical founders or engineering leads | 2–20 developers; maintains a GitHub repository; personally triages bounded issues | H2 |
| 3 | Internal or boutique data analysts | Produced a decision report from an export/notebook in the last 60 days | H3 |
| 3 | Product/user researchers or applied research leads | Synthesized interviews or literature into a decision artifact in the last 90 days | H4 or H5 |
| 2 | Operations leads in small businesses or professional-services teams | Reconciles records between a browser-only system and spreadsheet at least monthly | H7 |
| **20** | | One participant per organization in the first wave | |

H6 remains a scored backup but receives no first-wave quota unless recruiting evidence or challenger review raises it.

### Channel plan

Use channels in this order, recording attempted and qualified counts without implying conversion:

1. Founder first-degree network and prior colleagues, if the founder confirms relevant contacts.
2. Targeted introductions through accelerator, founder, product, engineering, analytics, research, and operations communities where outreach is permitted.
3. Direct role-based outreach to publicly identifiable professionals on company sites or professional networks; do not scrape private contact data or send bulk unsolicited messages.
4. Customer referrals requested only after an interview, with no disclosure of the prior participant's statements.

At least half of completed interviews should come from outside the founder's first-degree network to reduce preference bias. If that quota cannot be met, record the skew rather than relaxing it silently.

### Proposed outreach copy

> I'm researching how small teams handle [specific recurring job]. I'm not selling a finished product. Could I spend 45 minutes learning about the last time you did it, the artifacts and tools involved, and what went wrong? I will not ask you to share confidential data; a redacted example or screen walk-through is optional. With your permission, I may invite you to test a narrow prototype later.

Do not lead with “persistent agents,” multi-model orchestration, or the proposed differentiator. Ask about past behavior before presenting concepts.

### Interview procedure

1. Use `00_inbox/prepared_materials/10_CUSTOMER_NOTES/INTERVIEW_TEMPLATE.md`.
2. Reconfirm role, company size, workflow recency, and direct responsibility.
3. Walk through the last actual occurrence: trigger, tools, people, handoffs, elapsed and active time, errors, completion state, and approval boundary.
4. Request a permitted redacted artifact or live process map; absence is recorded.
5. Ask what has already been tried and why it remains in use or was abandoned.
6. Only after evidence capture, show two neutral output concepts: a generic cited report and a verification-first delta ledger. Randomize presentation order across interviews.
7. Ask for a concrete next action: watchlist/artifact access, scheduled pilot date, and written price response. Record “no” and conditions exactly.
8. Capture disconfirming evidence before author interpretation.

### Evidence recording and privacy

- Default to notes only. Record audio/video only with explicit permission.
- Do not commit participant names, emails, recordings, private company data, credentials, or identifiable quotations to this public repository.
- Store only sanitized notes or aggregate evidence in the repository; keep authorized originals in an approved private location and reference them by non-identifying ID.
- Separate exact permitted quotation, observed artifact, participant report, interviewer inference, and product proposal.
- One interview is one evidence unit; do not count multiple employees from one company as independent market observations in the first wave.
- A pilot commitment requires a named owner, permitted input, start date, completion criterion, and explicit yes. A payment signal requires a written price response or payment, not enthusiasm.

### Incentive proposal and unresolved authority

**DESIGN PROPOSAL:** offer up to `USD 50` for a 45-minute interview, with a maximum discovery incentive budget of `USD 1,000`, only after founder approval. The task does not authorize spending or outreach. If no budget is approved, record incentive-free recruiting and its sampling bias.

### Weekly evidence review

- After each batch of five interviews, update a hypothesis evidence table with support, contradiction, unknowns, artifact availability, and next sampling gap.
- Do not change the hypothesis because of one memorable quote.
- After 20 interviews, apply the predeclared gates before revising the recommendation.
- Independent challenger review should test whether the coding counter-hypothesis or another segment was under-sampled.

## Decisions and non-decisions

### Provisional decisions

- Test H1 first and H2 as the explicit counter-hypothesis.
- Test verified delta completion as the primary differentiator; do not assume model transparency is a buyer benefit.
- Keep the first H1 test public-source-only and read-only until approval for a test record update.

### Not decided

- No final customer segment, workflow, differentiator, pricing, market size, sales motion, architecture, integration stack, model provider, model role, benchmark shortlist, application code, or production scope is selected.
- D-006 and D-007 remain provisional.
- S0-004 and S0-005 remain unchanged and blocked under their recorded boundaries.
- The independent challenger test has not run; the author may not mark this work verified.

## Required independent challenge

The reviewer should at minimum:

1. Recompute every weighted total from the CSV and verify rank ordering.
2. Challenge scores and weights, especially H1 vs H2, with an alternative weighting or at least three one-level perturbations.
3. Check every public-workaround statement against SRC-064 through SRC-074 and reject vendor outcome claims presented as demand evidence.
4. Verify that all four S1-001 deliverables and acceptance criteria are present.
5. Attack the H1 segment definition, thresholds, recruiting bias, artifact requirements, payment test, and kill rules.
6. Confirm no architecture, application code, paid benchmark, model-role lock, or customer evidence was fabricated.
7. Return findings and a verdict without marking the author's artifact verified unless a later independent verifier satisfies the repository rules.
