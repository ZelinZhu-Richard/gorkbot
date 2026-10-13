# Target Workflows

These workflows translate the platform vision into testable jobs. They are not all MVP scope.

## Selection criteria

A strong first workflow should:

- be painful and frequent
- produce an objectively checkable result
- require more than chat generation
- use a manageable number of integrations
- tolerate early product limitations
- have customers who can buy quickly
- demonstrate persistence, approval, and verification
- avoid high regulatory or irreversible risk

## Workflow 1: source-backed competitive intelligence

**User request**

Research a defined set of companies using official sites, funding announcements, product documentation, public repositories, and recent news. Produce a cited spreadsheet and a concise strategy report.

**Capabilities**

- browser research
- source ledger
- structured extraction
- deduplication
- spreadsheet and document artifacts
- long-running execution
- verification

**Completion predicate**

- required companies covered
- every material claim has a source
- spreadsheet schema validates
- duplicate records handled
- report and spreadsheet open successfully

**MVP fit:** high

## Workflow 2: GitHub issue to reviewed pull request

**User request**

Inspect a repository issue, reproduce the problem, implement a bounded fix, run tests, obtain independent model review, and prepare a pull request for human approval.

**Capabilities**

- repository access
- terminal
- coding model routing
- tests
- verifier
- external-action approval

**Completion predicate**

- issue reproduced or inability documented
- patch exists
- required tests pass
- reviewer findings addressed or recorded
- PR draft exists only after approval

**MVP fit:** high if GitHub is the first integration

## Workflow 3: literature intelligence workspace

**User request**

Analyze a collection of research papers, extract claims, methods, datasets, limitations, and citations, then maintain a structured literature database and research-gap memo.

**Capabilities**

- file processing
- PDF extraction
- long-context reasoning
- database or spreadsheet artifacts
- source provenance
- iterative updates

**Completion predicate**

- every paper accounted for
- extracted fields pass spot checks
- claims link to pages or sections
- uncertain extraction is flagged
- database and memo are consistent

**MVP fit:** medium to high, depending on PDF reliability

## Workflow 4: recurring opportunity intelligence

**User request**

Monitor selected opportunity sources, update a master database, identify new or materially changed records, and produce a weekly change report.

**Capabilities**

- scheduled routine
- web research
- durable database state
- change detection
- deduplication
- evidence and alerts

**Completion predicate**

- run history recorded
- changed records linked to sources
- no duplicate identifiers
- stale or unavailable sources flagged
- update is idempotent

**MVP fit:** medium, better after routine support

## Workflow 5: startup operating review

**User request**

Pull product, support, sales, and engineering signals; summarize risks, decisions, and next actions; leave drafts rather than sending external communications.

**Capabilities**

- multiple connectors
- memory of operating cadence
- source reconciliation
- approval boundaries
- recurring workflow

**Completion predicate**

- required systems checked
- metrics use defined formulas
- inconsistencies flagged
- recommendations link to evidence
- no external communication sent

**MVP fit:** medium

## Workflow 6: customer-research synthesis

**User request**

Ingest interview transcripts and notes, identify recurring pains, contradictory evidence, existing workarounds, willingness-to-pay signals, and recommended next interviews.

**Capabilities**

- file ingestion
- qualitative coding
- evidence traceability
- memory and updates

**Completion predicate**

- every interview represented
- themes link to source excerpts or timestamps
- dissenting evidence included
- no invented quotations

**MVP fit:** high

## Workflow 7: data-analysis report

**User request**

Inspect a dataset, validate quality, answer a defined business question, create charts, and produce a reproducible report with calculations and caveats.

**Capabilities**

- terminal or notebook
- file handling
- data validation
- artifact generation
- independent calculation checks

**Completion predicate**

- data-quality report exists
- analysis is reproducible
- units and filters are documented
- charts match calculations
- limitations are explicit

**MVP fit:** high

## Workflow 8: website release preparation

**User request**

Inspect a website repository, implement a bounded content or UI change, run checks, create preview evidence, and prepare deployment for approval.

**Capabilities**

- repository and terminal
- browser preview
- visual verification
- approval before deployment

**Completion predicate**

- requested change visible in preview
- tests and build pass
- accessibility checks run where relevant
- production remains unchanged until approval

**MVP fit:** high

## Workflow 9: browser-only operations task

**User request**

Collect records from a web application lacking an API, reconcile them against a local file, and prepare proposed updates without committing them.

**Capabilities**

- browser control
- structured extraction
- reconciliation
- screenshots
- approval boundary

**Completion predicate**

- every intended record accounted for
- proposed changes are reviewable
- no unauthorized write occurred
- UI extraction errors are flagged

**MVP fit:** medium because GUI reliability is a central risk

## Workflow 10: persistent inbox and task triage

**User request**

Classify new messages, connect them to existing projects, draft responses, and escalate only items that need human judgment. Do not send without approval.

**Capabilities**

- event trigger
- email connector
- memory
- draft artifacts
- approval

**Completion predicate**

- messages classified using defined rules
- uncertain messages escalated
- drafts preserve context
- no message sent automatically

**MVP fit:** later unless email is selected as beachhead

## Workflow 11: multi-agent research-to-build pipeline

**User request**

A research agent gathers evidence, an architect turns it into decisions, an engineer implements a bounded slice, and a verifier tests it.

**Capabilities**

- agent roles
- structured handoffs
- ownership
- artifacts
- review

**Completion predicate**

- no duplicate ownership
- every handoff has an output contract
- implementation traces to requirements
- verifier uses independent evidence

**MVP fit:** later

## Workflow 12: recurring learned workflow

**User request**

Observe a user perform a safe browser workflow, convert it into a draft reusable skill, test it with different inputs, and schedule it after approval.

**Capabilities**

- demonstration capture
- workflow abstraction
- skill representation
- routine scheduler
- safe testing

**Completion predicate**

- variables separated from constants
- uncertain branches exposed
- workflow passes safe test cases
- user explicitly enables automation

**MVP fit:** much later

## Recommended MVP shortlist

These should be tested with potential users before selection:

1. GitHub issue to reviewed pull request
2. Source-backed competitive intelligence
3. Data-analysis report
4. Customer-research synthesis
5. Website release preparation

## Provisional recommendation

Start customer discovery with technical founders and small software teams. Compare two concrete wedges:

- persistent engineering teammate for bounded repository work
- persistent research and operating-intelligence teammate

Do not decide from model preference. Decide from interviews, workflow access, repeatability, measurable value, and technical spike results.
