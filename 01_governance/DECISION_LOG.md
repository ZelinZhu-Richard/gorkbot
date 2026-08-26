# Decision Log

## Decision status

- CONFIRMED: explicitly decided by the founder
- PROVISIONAL: working choice pending evidence
- DEFERRED: intentionally postponed
- REJECTED: considered and not selected

## D-001: Build toward a multi-tenant SaaS

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: The long-term target is a SaaS product other people can use.
- Consequence: tenant, authorization, billing, audit, and data-boundary concerns must remain architecturally possible even if not built in the first prototype.

## D-002: Use Grok Bot as a clean-room capability benchmark

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: Target functional parity or better without copying branding, proprietary implementation, or exact assets.
- Consequence: maintain a sourced parity matrix and independent product identity.

## D-003: Begin with one extremely capable persistent agent

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: Build core persistence, execution, approvals, observability, artifacts, and verification before visible agent teams.
- Consequence: group chat, many agents, skills, and routines are later stages.

## D-004: Support multiple model providers

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: GPT, Claude, DeepSeek, and future models should be replaceable through a model abstraction and routing layer.
- Consequence: no provider-specific behavior may define core task state, memory, approvals, or authorization.

## D-005: Use repository files as shared model state

- Date: 2026-08-21
- Status: CONFIRMED
- Decision: GPT, Claude, and execution models coordinate through versioned files and task records.
- Consequence: chat memory and verbal summaries are non-authoritative.

## D-006: Initial beachhead customer

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: Begin discovery with technical founders and small startup teams while comparing research and engineering workflows.
- Evidence required: interviews, pilot willingness, workflow access, measurable pain, and technical feasibility.

## D-007: Primary differentiation

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: Test verified completion and model-transparent orchestration as the primary wedge, with stronger isolation as a secondary advantage.
- Evidence required: customer value, technical performance, cost, and competitive comparison.

## D-008: First client surface

- Date: 2026-08-21
- Status: PROVISIONAL
- Decision: A web control plane may precede native desktop and mobile applications.
- Evidence required: whether the first workflow requires local takeover, deep OS integration, or mobile supervision.

## D-009: S0-003 out-of-scope file modification

- Date: 2026-08-21
- Status: CONFIRMED
- Decision type: PROCESS_EXCEPTION
- Founder decision: Do not retroactively modify S0-003's `allowed_files_to_change`.

S0-003 modified governance files outside its originally authorized file scope. The modifications were relevant to the task, but the process deviation should remain visible rather than being erased by retroactively broadening the task definition.

The existing changes are accepted as a one-time documented exception.

Going forward:

1. A task must not modify files outside `allowed_files_to_change`.
2. If additional files become necessary, the task scope must be amended before modifying them.
3. The reason for the scope amendment must be recorded.
4. Reviewers should flag unauthorized changes even when the content itself is correct.

## D-010: Initial Stage 0 author runtime

- Date: 2026-08-21
- Status: CONFIRMED
- Decision type: EXECUTION_PROVENANCE
- Founder confirmation: The original `MODE: INITIALIZE` author pass for Stage 0 was executed in Codex, not directly in the ChatGPT interface using GPT-5.6 Sol.

Consequence:
- Stage 0 provenance should identify the author runtime as Codex.
- Any more specific underlying model identifier should remain unknown unless it was explicitly exposed by the Codex runtime.
- Do not retroactively label the author as GPT-5.6 Sol without evidence.

## D-011: S1-001 provisional discovery beachhead

- Date: 2026-08-23
- Status: PROVISIONAL
- Decision: Test first with a founder, head of product, or product-marketing lead at a 3–30 person B2B SaaS company that tracks 5–15 named competitors without a dedicated competitive-intelligence analyst. The narrow job is a verification-first weekly ledger of material official-source product, pricing, documentation, and changelog changes, with an approval-gated master-record update. Keep the small-software-team GitHub issue-to-reviewed-PR workflow as the explicit counter-hypothesis.
- Scoring context: H2 scored `76.8/100` and H1 scored `75.6/100`; the author treats the 1.2-point gap as a directional tie because one level on a weight-6 criterion changes the total by 1.2 points. H1 receives the first discovery slot based on lower-sensitivity initial inputs and founder-stated reach, neither of which is customer evidence.
- Primary differentiation hypothesis: test verified before/after delta evidence, explicit unknown states, approval, and external-state readback. Citations alone are not differentiated, and model transparency is not assumed to be a purchasing driver.
- Evidence required: the predeclared problem, delegation/differentiation, commitment/payment, and prototype-feasibility gates in `03_product/S1-001_CUSTOMER_WORKFLOW_SCORECARD.md`.
- Reversal rule: reopen this decision if any H1 problem gate fails, current alternatives are satisfactory without a material gap, the paid-pilot gate fails, authenticated/private sources are required for the first valuable version, or H2 produces stronger artifact, pilot, or payment evidence.
- Non-decision: D-006 and D-007 remain provisional. No final segment, workflow, pricing, architecture, model/provider role, benchmark, application implementation, market demand, or traction is confirmed.

Historical status note — 2026-08-23 S1-001 fixer pass:

- This original author ranking and first-slot rationale are preserved as the historical decision record.
- The independent challenger found the top-two ordering too sensitive, the H1 substitute screen incomplete, and the first-slot rationale partly duplicative of scored feasibility factors.
- Confirmed founder decision D-012 supersedes D-011 **only for current discovery allocation**. H1 no longer has an incumbent quota, contract, or priority: H1 and H2 are co-equal discovery candidates under comparable gates, and neither is validated or selected.
- The corrected scorecard does not retroactively rewrite the original `76.8/75.6` author scores. Customer evidence remains zero; customer evidence must determine which candidate survives.

## D-012: Stage 1 discovery allocation after S1-001 challenger review

- Date: 2026-08-23
- Status: CONFIRMED
- Decision type: FOUNDER_DISCOVERY_ALLOCATION
- Supersedes: D-011 only with respect to provisional discovery prioritization.

### Decision

H1 and H2 will proceed as co-equal discovery candidates.

Neither H1 nor H2 is selected as the final beachhead customer/workflow.

H1:
Verification-first competitor-change workflow for small B2B SaaS teams.

H2:
Verification-first software-engineering workflow centered on independently verified completion evidence around issue-to-PR work.

H8:
The challenger-added independent PR reproduce-and-verify hypothesis should be formally scored and evaluated during the S1-001 fix, but is not yet elevated to co-equal discovery status.

### Rationale

The S1-001 challenger found that:

1. H2 scored slightly above H1 in the original model.
2. The H1/H2 ranking is highly sensitive to small scoring changes.
3. H1's original differentiation was weakened by current SMB competitive-monitoring products.
4. H1's original preference was partly driven by feasibility and founder-access assumptions already represented in the score.
5. H2's issue-to-PR market is also highly competitive, but independently verified completion evidence remains an unresolved potential differentiator.
6. There is currently zero direct customer evidence for either hypothesis.

Therefore the evidence is insufficient to privilege either H1 or H2 before customer discovery.

### Consequences

- S1-001 must not portray H1 as the sole provisional beachhead.
- The scoring model must be corrected and sensitivity made explicit.
- H1 and H2 must receive comparable discovery effort and falsification criteria.
- Customer evidence, not founder preference or small score differences, should determine which survives.
- D-006 and D-007 remain PROVISIONAL.
- No final customer, MVP workflow, pricing, architecture, or model role is selected.

## D-013: S1-003 founder execution authorization and product-scope clarification

- Date: 2026-08-24
- Status: CONFIRMED
- Decision type: CUSTOMER_DISCOVERY_EXECUTION_AUTHORIZATION

### Long-term product scope

The long-term product remains a clean-room Grok Bot-class multi-tenant SaaS platform with functional parity or better.

H1 and H2 are candidate initial customer-workflow wedges. They do not redefine or limit the long-term platform scope.

Customer discovery will determine which workflow, if either, should become the first packaged use case, prototype demonstration, and customer-acquisition wedge.

Neither H1 nor H2 is currently selected.

TAM/SAM/SOM analysis is deferred until customer discovery produces a provisional ICP, workflow, buyer, pricing hypothesis, and evidence of willingness to pilot or pay.

### Outreach authorization

Manual, personalized, one-to-one outreach is authorized for the verified S1-003 discovery protocol.

Automated bulk outreach is not authorized during the first wave.

### Outreach scaling policy

Outreach quantity may increase later only after personalization quality, factual accuracy, tone, relevance, and protocol compliance have been tested and shown to remain stable.

Every message must:

1. Be based on verified company-specific and role-relevant context.
2. Demonstrate genuine understanding of why the recipient is relevant.
3. Avoid fabricated facts, compliments, familiarity, or personalization.
4. Avoid generic or obviously AI-generated language.
5. Be individually relevant even when a reusable structural template is used.
6. Comply with applicable platform, community, and email rules.

The scaling sequence is:

1. Founder-reviewed individual drafting.
2. AI-assisted personalized batches with founder approval.
3. Controlled higher-volume production after a documented quality gate.
4. Automated sending only after separate founder authorization and appropriate compliance, deliverability, suppression, audit, and quality controls exist.

Increasing quantity must not reduce the required personalization standard.

### Approved initial channels

The following channels are authorized for individualized outreach where contextually appropriate:

- founder email
- LinkedIn
- X
- GitHub
- warm introductions
- relevant startup or technical communities whose rules permit recruiting
- direct email based on legitimately obtained public business contact information

The following are not authorized during the first wave:

- purchased lead lists
- mass scraping for outreach
- automated bulk messaging
- indiscriminate community posting
- deceptive identity or false familiarity

### Incentives

The first-wave incentive budget is USD 0.

The prior proposal of up to USD 50 per interview and USD 800 total remains unapproved.

Incentives may be reconsidered after evidence from the initial unincentivized recruiting effort.

### Evidence storage and consent

Raw and identifying customer-discovery evidence must remain in approved private storage.

The public repository may contain only sanitized structured evidence or opaque references.

Recording is off by default.

Any recording requires the participant's explicit prior consent.

### Interviewer

The founder is the primary interviewer for the initial discovery wave.

### AI role

AI may:

- research prospects using permitted public information
- draft personalized outreach for founder approval
- prepare interview briefs
- check protocol compliance
- structure founder-provided notes
- extract candidate evidence
- conduct second-pass coding
- identify contradictions
- calculate predeclared gates
- analyze results

AI may not:

- autonomously conduct first-wave interviews
- send bulk outreach
- fabricate or infer missing customer evidence
- change frozen discovery gates after results appear
- independently select H1 or H2 as the winner
- place private evidence in the public repository

## D-014: Shared core platform with a provisional Finance Edition

- Date: 2026-08-24
- Status: PROVISIONAL
- Decision type: PRODUCT_LINE_AND_VERTICALIZATION_STRATEGY

### Decision

The project will continue toward one shared, model-agnostic, Grok Bot-class persistent-agent platform.

The intended product-line structure is:

1. General Edition
2. Finance Edition

These editions must share the same core agent runtime, task state, model abstraction, tool system, memory architecture, approval engine, security controls, audit system, and multi-agent protocol.

They must not become separate duplicated codebases.

### General Edition

The General Edition remains the clean-room Grok Bot-class product for persistent AI teammates, tools, cloud execution, skills, routines, and multi-agent collaboration.

### Finance Edition

The Finance Edition is a provisional future vertical built on the same platform.

Its initial scope should focus on finance-specialized research, analysis, modeling, reproducible backtesting, portfolio monitoring, risk analysis, evidence provenance, and human-approved workflows.

The Finance Edition is not currently authorized to:

- manage external investor capital
- make unsupervised live trades
- provide unreviewed personalized investment advice
- represent itself publicly as an operating hedge fund
- claim improved returns or investment performance without evidence
- use a model fine-tune as a substitute for current data, deterministic calculations, backtesting, verification, or risk controls

### Fine-tuning policy

Finance-specific fine-tuning is deferred until:

1. A precise finance customer and workflow are defined.
2. Finance-specific evaluations exist.
3. Repeated failure modes are measured.
4. Retrieval, tools, skills, and prompting have been tested.
5. The project has lawful rights to use the proposed training data.
6. Fine-tuning demonstrates measurable improvement over the base-model system.

The initial Finance Edition should use strong base models with authoritative data retrieval, deterministic financial tools, reproducible code, finance-specific skills, and independent verification.

### Potential future investment-management entity

A future AI-native fund or investment adviser would be a separate strategic and legal undertaking from the SaaS Finance Edition.

It would require independent legal, compliance, risk, operational, custody, reporting, and live-capital authorization gates.

No such entity or live-capital operation is currently selected or authorized.

### Current Stage 1 consequence

H1 and H2 remain the only co-equal candidates in the currently verified S1-003 customer-discovery protocol.

The Finance Edition does not receive a current interview quota and does not delay S1-003.

A later bounded task should define and test:

- finance ICP
- buyer and user
- first finance workflow
- research versus execution boundary
- data requirements
- integration requirements
- willingness to pay
- regulatory and compliance boundaries
- whether the finance vertical should become an early product line or a later expansion

## D-015: Restricted customer-discovery evidence storage

- Date: 2026-08-25
- Status: CONFIRMED
- Decision type: CUSTOMER_DISCOVERY_DATA_GOVERNANCE

### Approved restricted storage location

Raw and identifying S1-003 customer-discovery evidence is approved to reside at:

`/Users/richardzhu/dev/grok_bot/private_customer_discovery`

This directory is outside the public Git repository:

`/Users/richardzhu/dev/grok_bot/gork_bot`

and is restricted to the founder's local macOS user.

### Storage structure

The approved private workspace contains:

- `raw_interviews/`
- `recordings/`
- `transcripts/`
- `private_artifacts/`
- `participant_registry/`

### Public repository boundary

The public repository may contain only:

- opaque interview IDs
- sanitized/de-identified structured evidence
- aggregate findings
- evidence classifications
- non-identifying workflow descriptions
- opaque references to restricted evidence

The public repository must not contain, unless separately and explicitly authorized:

- participant names
- personal email addresses
- identifying employer information
- raw interview notes
- recordings
- transcripts
- private screenshots
- proprietary code
- confidential company documents
- confidential workflows
- identifiable budget information
- payment information

### Evidence references

Private evidence should be referenced from public records using opaque identifiers such as:

`H1-INT-001`
`H2-INT-001`

Public records must not encode participant identity into those IDs.

### Recording policy

Recording remains OFF by default.

Any recording requires explicit prior participant consent and must be stored only in the restricted evidence location.

### Consequence

This decision satisfies the remaining S1-003 restricted-evidence-storage-location requirement.

It does not itself start outreach, interviews, recording, spending, or S1-003 execution.

## Stage 0 author reconciliation note — 2026-08-21

This note records scope, not a new decision:

- Provenance: written in the initial Stage 0 author batch under S0-001's `DECISION_LOG.md` allowance on behalf of the S0-002 and S0-003 research outcomes; attribution was clarified during F-S0-001-02 remediation. It changed no D-00x status.

- Current primary-source research does not change D-001 through D-005.
- D-006, D-007, and D-008 remain provisional founder hypotheses. No customer evidence was added by Stage 0.
- The reference product's documented shared-computer boundary is evidence about Grok Bot, not a selected architecture for this project.
- No final architecture, MVP workflow, customer wedge, or model-role assignment was selected.
