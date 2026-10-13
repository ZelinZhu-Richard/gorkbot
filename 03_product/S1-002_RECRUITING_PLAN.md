# S1-002 recruiting plan for H1/H2 discovery

Status: FIXED DRAFT-ONLY DESIGN PROPOSAL — NO OUTREACH AUTHORIZED OR SENT

Planning date: 2026-08-23

Execution task: S1-003, currently BLOCKED

## Objective and boundary

Recruit a first wave of 8 ICP-qualified H1 participants and 8 ICP-qualified H2 participants from 16 distinct organizations without privileging either hypothesis or screening away negative evidence.

This plan contains channel assessments and draft copy only. It does not authorize anyone to identify private contact details, connect an account, send a message, post in a community, book an interview, buy an incentive, or spend money.

## Fixed sample requirements

| Dimension | H1 | H2 |
|---|---|---|
| Counted interviews | 8 ICP-qualified | 8 ICP-qualified |
| Organization independence | One participant per organization across both groups | Same |
| Outside-network minimum | At least 4/8 outside founder first-degree network | Same |
| Buyer/budget coverage | Target at least 4/8 buyer-operators or confirmed budget owners | Same |
| Alternative-use target | At least 4/8 current/recent direct-tool users; no more than 4/8 primarily manual | Same |
| Size balance | Avoid more than 5/8 in either 3–10 or 11–30 employee band | Avoid more than 5/8 in either 2–7 or 8–20 developer band |
| Interview | 45 minutes, behavior first | Same |
| Artifact request | Redacted watchlist/report/process | Redacted issue/PR/check/process |
| Pilot/price ask | Two cycles; USD 500/four weeks | Same |

Recent pain, high frequency, dissatisfaction, delegation, pilot interest, and WTP are measured outcomes and may not be used to qualify a lead.

## ICP screening summary

### H1

- Operating B2B SaaS company, 3–30 employees, live product.
- Tracks 5–15 named competitors.
- No full-time competitive-intelligence analyst.
- Participant directly owned competitor-informed pricing, positioning, roadmap, launch, or enablement work within the last 12 months.
- Target titles: founder/CEO, head/VP/director of product, head/lead of product marketing. A title alone is insufficient; direct responsibility must be confirmed.

### H2

- Operating commercial software team with 2–20 active developers.
- Uses a Git-based pull-request workflow and has at least one bounded runnable test/build/preview path.
- Participant directly owned issue triage, PR review, or completion decisions within the last 12 months.
- Target titles: technical founder, CTO, VP/head/director of engineering, engineering lead/manager with direct review responsibility.

### Exclusions for the counted wave

- Duplicate person or organization.
- No direct workflow responsibility in the last 12 months.
- Consultant/agency reporting client behavior rather than the participant's own organization.
- Direct monitoring/CI vendor employee for H1 or coding-agent/review vendor employee for H2.
- Outside the size limits, hobby/student project, non-operating product, or no relevant workflow infrastructure.
- Expert-only calls may be useful later but cannot enter the first-wave denominator.

## Prospect and overlap handling

- Keep prospect identity/contact data outside this public repository in a founder-approved restricted recruiting tracker.
- Assign pseudonymous prospect and organization keys before interview notes enter the repository.
- Dedupe by organization domain and participant identity in the restricted tracker.
- If a participant qualifies for both H1 and H2, assign them before concept exposure by alternating toward the group with fewer completed valid interviews while respecting quotas.
- Do not expose both concepts, count one interview twice, or use secondary remarks in the other hypothesis's gate calculation.
- Keep screen failures and declines in the restricted funnel log so reach and sampling bias remain visible; do not create fake scorecard rows for people never interviewed.

## Channel assessment

All response probabilities below are **DESIGN ESTIMATES, NOT OBSERVED PROJECT RESULTS**. They are directional planning ranges for a personalized invitation and one follow-up, not promises.

| Channel | Expected participant quality | Main bias | Founder effort | Estimated positive-response probability | Best fit | Use conditions |
|---|---|---|---|---|---|---|
| Founder first-degree network | High when direct responsibility is known | Courtesy/relationship and founder-belief bias | Low | 30–60% | Both; likely H2-heavy | Cap at 4/8 per hypothesis; do not treat warmth as demand. |
| Warm introductions | High; referrer can confirm role | Referral/network homophily and positive framing | Medium | 20–50% | Both | Give referrer neutral copy; no product endorsement in the intro. |
| LinkedIn targeted outreach | Medium-high if title/company/workflow are checked | Title inflation, public-profile selection, platform-message fatigue | Medium-high | 5–15% | H1 strong; H2 also appropriate | Manual personalization; comply with platform rules; no scraping or mass automation. |
| GitHub public profiles/repositories | High H2 workflow relevance when company/role is confirmable | Open-source, developer-tool, and public-code bias | High | 3–10% | H2 | Use only public professional contact paths; never open an issue or PR for recruiting. |
| X | Mixed; useful for founder/operator reach | Public-posting, AI-enthusiast, and audience-size bias | Medium | 2–8% | Both; H2 likely stronger | Prefer targeted direct invitations over broad “who wants AI?” posts. |
| Relevant Slack/Discord communities | Medium-high in well-defined communities | Community/tool enthusiasm and administrator-selection bias | Medium | 5–15% | H1 in PMM/product communities; H2 in founder/engineering communities | Obtain admin permission before posting; one neutral post; no repeated solicitation. |
| Startup/founder communities | Medium | Very-early-stage and founder-only bias | Medium | 5–15% | Both | Screen for operating product, exact company/team size, and direct workflow ownership. |
| Direct email | Medium-high with careful company/role selection | Non-response and availability bias | High | 3–10% | Both | Use public professional addresses lawfully; one follow-up maximum; honor opt-outs. |

Response probability is a distribution/recruiting signal only. It is not proof of pain or WTP.

## Recommended channel mix

For each hypothesis, begin only after authorization with:

1. up to 4 first-degree/warm-intro candidates;
2. at least 4 outside-network participants recruited through two or more cold/community channels;
3. no more than 5 counted interviews from any one recruitment channel;
4. at least 4 participants with current/recent experience of a direct alternative, identified without requiring dissatisfaction.

Recommended H1 emphasis: LinkedIn, PMM/product communities, warm founder/product introductions, and careful direct email.

Recommended H2 emphasis: founder/engineering network, GitHub-derived public professional paths, engineering communities, LinkedIn, and direct email.

## Funnel arithmetic, batches, and time box

All values in this section are **DESIGN PROPOSAL / DESIGN ESTIMATES — NOT OBSERVED PROJECT RESULTS**. The funnel is measured separately for H1 and H2 as:

```text
unique prospects contacted
→ positive/opt-in responses
→ structural screens completed
→ ICP-qualified screens
→ interviews scheduled
→ ICP-qualified interviews completed
```

Declines, non-responses, screen failures, scheduling failures, and no-shows remain in the restricted funnel. None is a G1–G11 market result.

### Cap adequacy scenarios

The former 40-prospect cap cannot plausibly yield eight completed qualified interviews under the channel ranges above. The revised maximum is 120 unique targeted prospects **per hypothesis**, using a planning mix of up to 16 known/warm prospects and at least 104 outside-first-degree prospects if the full cap is needed. These scenarios show the arithmetic; they do not predict actual performance.

| Hypothesis/scenario | Response assumptions | Screen-completion | ICP-qualified among screened | Schedule among qualified | Complete among scheduled | Expected funnel at 120: responses → screened → qualified → scheduled → completed | Expected outside-network completions |
|---|---|---:|---:|---:|---:|---|---:|
| H1 base design | 35% of 16 known/warm; 10% of 104 outside | 85% | 75% | 90% | 90% | 16.0 → 13.6 → 10.2 → 9.2 → **8.3** | 5.4 |
| H1 downside | 20% known/warm; 3% outside | 75% | 60% | 80% | 80% | 6.3 → 4.7 → 2.8 → 2.3 → **1.8** | 0.9 |
| H2 base design | 45% of 16 known/warm; 10% of 104 outside | 90% | 80% | 90% | 90% | 17.6 → 15.8 → 12.7 → 11.4 → **10.3** | 6.1 |
| H2 downside | 30% known/warm; 3% outside | 80% | 70% | 80% | 80% | 7.9 → 6.3 → 4.4 → 3.5 → **2.8** | 1.1 |

The base scenarios support the eight-interview and four-outside targets; the downside scenarios do not. Reaching 120 without filling a quota therefore means `PAUSE_RECRUITING_FAILED`, not customer-market rejection. The response, screen, schedule, and completion assumptions must be replaced by actual funnel values as S1-003 proceeds, without changing G1–G11.

### Predeclared staged release

- **Batch 1:** up to 40 unique prospects per hypothesis, with at least 28 outside the founder's first-degree network and at least two approved channels.
- **Batch 2:** on or after day 7, release up to 40 more for a hypothesis only if its completed-qualified plus already-screened-and-scheduled qualified pipeline is below 8, or its outside-network completed/scheduled pipeline is below 4.
- **Batch 3:** on or after day 14, apply the same trigger for up to 40 more. Change channel emphasis toward the better observed recruiting conversion only within founder-approved channels; do not change the ICP or screen.
- Send one personalized initial invitation and at most one follow-up 5–7 days later.
- Stop outreach after 35 calendar days from the first authorized invitation or 120 unique prospects for that hypothesis, whichever comes first. Any extension requires a new founder-authorized task before comparison; it is not granted post hoc.
- Schedule H1 and H2 in parallel and keep completed-valid counts within two interviews when feasible. If one quota fills first, pause its recruiting while the other catches up.
- Screen structurally before booking where practical, but do not ask whether the problem is painful, frequent, unsolved, delegable, or worth paying for.
- If quotas or sampling controls are missed, report every funnel stage, channel mix, and bias; do not expand the ICP, exceed eight valid interviews, or interpret recruiting friction as a failed customer gate.

## Draft screening form

Use the same neutral introduction for both groups. The form should request no secrets and no private artifacts.

Common fields:

- role/title;
- company/product type;
- company employee count or developer-team count as applicable;
- direct responsibility for the named workflow in the last 12 months;
- buyer/budget authority: self, named role, or unknown;
- network relationship and recruitment channel;
- consent to a 45-minute research conversation and optional redacted workflow walkthrough.

H1-only structural fields:

- number of named competitors tracked;
- whether a full-time CI analyst exists.

H2-only structural fields:

- Git/pull-request workflow present;
- bounded runnable test/build/preview path present.

Do not ask “How painful is this?”, “Would you use an AI agent?”, “Do you want independent verification?”, or “Would you pay?” in the screen.

## Draft outreach templates — do not send

### H1 personalized invitation

Subject: Research on how small SaaS teams track competitor changes

> Hi [first name] — I am researching how 3–30 person B2B SaaS teams actually track competitor changes for pricing, positioning, roadmap, launch, or sales decisions. I am looking for a 45-minute workflow interview, not a product pitch. I would ask you to walk through the last real example and the tools/process you used; no confidential information is needed. If you are directly responsible for this work and your team tracks roughly 5–15 competitors without a full-time CI analyst, would you be open to a conversation? [Authorized incentive sentence, if any.] A no is completely fine.

### H2 personalized invitation

Subject: Research on how small engineering teams verify issue/PR completion

> Hi [first name] — I am researching how 2–20 developer software teams decide whether bounded issue and pull-request work is actually complete. I am looking for a 45-minute workflow interview, not a product pitch. I would ask you to walk through the last real example and the tools/checks you used; no code, credentials, or confidential information is needed. If you directly triage issues or review PRs in a Git-based workflow with runnable checks for some bounded changes, would you be open to a conversation? [Authorized incentive sentence, if any.] A no is completely fine.

### Warm-introduction request

> Could you introduce me to someone who directly owns [competitor-informed product/positioning decisions OR bounded issue/PR completion] at a team matching the short screen below? Please describe this as workflow research, not as an AI product or endorsement. I will ask about past behavior before discussing any concept, and a no is completely fine.

### One permitted follow-up

> Following up once in case this workflow research is relevant. I am still looking for direct operators who fit the structural screen. There is no product pitch and no need to share confidential material. If it is not a fit, no response is needed and I will not follow up again.

Templates must be personalized and reviewed by the founder before use. Remove the incentive sentence unless the founder has authorized the budget and exact delivery method.

## Incentive design

**DETERMINATION / DESIGN PROPOSAL — NOT AUTHORIZED:** incentives are not necessary to begin with willing warm contacts, but an optional fixed incentive is likely useful for meeting the outside-network quota without relying only on favors. The recommended authorization is a reserve of up to USD 50 for a completed 45-minute ICP-qualified interview, with a maximum first-wave budget of USD 800 (`16 × USD 50`). The founder may approve USD 0, a lower reserve, or the full cap before outreach.

Rationale:

- Warm founder-network participants may participate without compensation, but outside-network operators often bear a real time cost.
- A modest, fixed interview incentive can improve attendance without tying compensation to positive answers, artifact sharing, pilot interest, or WTP.
- Incentive acceptance is not customer demand, economic value, pilot intent, or willingness to pay.

Controls:

- Founder must explicitly authorize the total cap, delivery method, eligible geography, and who can issue incentives before S1-003.
- The amount, eligibility, and delivery policy must be identical for H1 and H2 within the wave unless the founder records a concrete operational reason before any outreach; no observed response or interview result may trigger an asymmetric change.
- Incentives compensate time, not agreement. Never pay more for favorable evidence, artifact access, private data, pilot interest, or price acceptance. Pay the authorized amount for every completed structurally qualified interview even when the participant rejects the hypothesis.
- If the founder chooses USD 0, a lower cap, or an unpaid-warm-first stage, record that policy and its symmetric stage trigger before outreach. A staged option is not silently adopted as founder policy.
- The private incentive/payment ledger lives in the founder-approved restricted recruiting tracker and records only the opaque prospect key, eligibility, amount, currency, authorization reference, delivery date, and delivery method. Names, payment details, and delivery identifiers never enter Git; only aggregate authorized/paid totals are surfaced publicly.
- No incentive, gift card, software subscription, list purchase, ad spend, or other expenditure may occur under S1-002.

## Consent, privacy, and contact controls

- Use only founder-approved accounts and channels in S1-003.
- Do not scrape, bulk message, automate outreach, open GitHub issues/PRs for recruiting, or bypass community rules.
- Obtain community-admin permission before posting.
- Record opt-outs and do not contact them again.
- Keep names, contact details, employer-identifying notes, and raw consent records in an approved restricted system, not Git.
- Ask separate permission for recording, quoting, and artifact viewing.
- Do not request source code, credentials, customer data, private URLs, or production access during recruiting/interviews.
- Use pseudonymous keys in the public scorecard and an opaque random restricted-record ID, never a path or share link.

## Execution readiness checklist

S1-003 remains blocked until all are true:

- S1-002 independently VERIFIED;
- explicit founder outreach authorization recorded;
- approved channels/accounts recorded;
- incentive decision and maximum spend recorded (including a zero-budget decision if chosen);
- restricted prospect/raw-evidence storage location approved;
- consent language approved;
- S1-003 author/interviewer assigned;
- explicit AI-role policy recorded for outreach, interviews, transcription, raw evidence, extraction, coding, and review;
- independently verified protocol commit SHA and guide versions recorded before first contact;
- 35-day/120-prospect batch authority plus the frozen common-cutoff formula, authorized first-outreach date, and day-42 cap recorded before contact; the exact common freeze is mechanically logged when the later H1/H2 terminal occurs; and
- primary-coder responsibility accepted, with a second reviewer assigned no later than before the gate-counting freeze.

Current status: none of these S1-003 execution permissions is inferred from this document. Outreach sent: **ZERO**. Interviews conducted: **ZERO**. Spend: **USD 0**.
