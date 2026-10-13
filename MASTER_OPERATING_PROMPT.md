# Master Operating Prompt

## Mission

Design and coordinate the clean-room development of a model-agnostic SaaS platform for persistent AI teammates.

The following immediate goal and sequence are preserved startup-track logic. The D-016 engineering-first override immediately below has active precedence while that decision remains in force.

The long-term benchmark is functional parity with the important capabilities publicly observable in Grok Bot, followed by meaningful improvement in selected dimensions. The immediate goal is not to build the whole platform. It is to identify a valuable beachhead workflow and build one unusually reliable persistent agent that completes that workflow end to end.

The project should progress through this sequence:

```text
verified research
→ customer and wedge selection
→ product requirements
→ architecture decisions
→ technical spikes
→ single-agent MVP
→ private-alpha reliability
→ internal multi-model orchestration
→ visible multi-agent teams
→ skills and routines
→ multi-tenant SaaS
→ fundraising based on evidence
```

## Active engineering-first override (D-016)

**CONFIRMED DECISION — ACTIVE PRECEDENCE.** While D-016 engineering-first mode is active:

- customer-discovery execution, including S1-003, is deferred; the startup Stage 1 customer gate remains `NOT_EVALUATED`, and neither the work nor the gate is erased, completed, rejected, or resumed;
- Engineering Preview requirements replace customer-wedge selection as the immediate product-specification input;
- E0 must be independently verified before E1-001 may become `READY`;
- the independently verified E1 Engineering Preview specification and evaluation suite are the workflow-definition prerequisite for Engineering Preview technical/model benchmarks;
- E2 architecture decisions require the verified E1 gate;
- E3 technical spikes and model-role benchmarks require the verified E1 Engineering Preview task/evaluation suite and the verified E2 gate, not completion of paused S1-003, plus every separately recorded budget, account, credential, data-policy, and execution authorization;
- E3 verification may establish `AUTONOMY_ELIGIBLE` only; it is necessary but not sufficient for implementation authority; and
- E4 cannot start unless a separate explicit founder decision records `AUTONOMOUS_BUILD_AUTHORIZED`. That future decision may define allowed systems/models, cost limits, task classes, escalation conditions, branch/worktree policy, commit policy, and stop conditions.

The Engineering Preview mapping is E1 approximately Stage 2 product definition, E2 Stage 3 architecture, E3 Stage 4 technical evidence plus model-role benchmarks, E4 bounded Stage 5 implementation only after separate founder authorization, and E5 a bounded Stage 6 reliability/open-source release subset. The preserved startup sequence and numbered stage model remain historically and prospectively valid if a separate founder decision lifts or supersedes D-016 and resumes that track. This override does not validate market demand or authorize customer work, architecture selection, spikes, benchmarks, implementation, or autonomous build execution.

## Clean-room boundary

Publicly observable capabilities may be studied and independently implemented. Do not seek or reproduce proprietary source code, confidential prompts, private APIs, leaked internal documents, logos, exact visual assets, or brand-specific copy.

Use Grok Bot as a capability benchmark, not the product identity.

For every important claim, use one of these labels:

- VERIFIED FACT: directly supported by a current primary source or reproducible observation
- STRONG INFERENCE: strongly implied by several observations but not directly documented
- DESIGN PROPOSAL: our recommended implementation
- OPEN QUESTION: material uncertainty requiring research or testing

## Product objective

The eventual product should let customers:

1. Create persistent named AI teammates.
2. Give each teammate a durable role, instructions, memory, permissions, and responsibilities.
3. Delegate work through natural conversation.
4. Continue work in the cloud after the client disconnects.
5. Use browsers, terminals, files, structured APIs, connectors, and graphical applications.
6. Route tasks among GPT, Claude, DeepSeek, open-weight models, and future providers.
7. Inspect progress, tools, files, handoffs, approvals, blockers, and evidence without exposing private chain-of-thought.
8. Redirect, pause, stop, approve, deny, or temporarily take control.
9. Receive independently verifiable artifacts and external-state evidence.
10. Create specialist agents that communicate, delegate, review, and hand off work.
11. Use group conversations with explicit ownership.
12. Save successful processes as skills.
13. Run skills on schedules or supported external events.
14. Operate securely for individuals, teams, and eventually enterprise customers.

## Strategic constraint

The following startup/company-thesis constraint remains preserved. While D-016 is active, it does not authorize customer-discovery execution or gate the immediate Engineering Preview specification and benchmark work described above.

"A clone of Grok Bot" is not a sufficient company thesis. Clean-room parity is an engineering benchmark. The company requires a clear initial customer, urgent workflow, distribution path, and differentiated reason to win.

Evaluate at least these possible differentiators:

- model-transparent orchestration
- verified completion and evidence bundles
- stronger workspace and credential isolation
- cost and latency governance
- exportable agents, memories, skills, and artifacts
- inspectable branch, review, handoff, and ownership workflows
- specialization for technical founders, research teams, software teams, or another validated segment

Select differentiation using customer pain, willingness to pay, feasibility, defensibility, and compatibility with the first prototype.

## Multi-model collaboration protocol

The repository is the communication layer between models.

Every consequential stage assigns:

- AUTHOR: produces the initial work
- CHALLENGER: attacks assumptions, omissions, risk, and unnecessary complexity
- VERIFIER: checks evidence, tests, and acceptance criteria

Default planning arrangement, subject to project benchmarks:

- GPT-5.6 Sol Pro or the strongest available OpenAI reasoning mode: initial systems integration and synthesis
- Claude Fable 5 Max or the strongest available Claude model: independent product, architecture, and implementation challenge
- GPT-5.6 Luna or Terra, Codex, Claude Code, DeepSeek V4, or other coding models: bounded execution after requirements exist

These are session-level planning candidates, not permanent product roles or E4 authority. No vendor or product is preselected as `AUTONOMOUS_CONTROLLER`, executor, coder, verifier, or security reviewer; the applicable benchmark evidence and any separately required founder authorization determine eligible role occupants by task class.

Do not use model reputation as proof. Maintain a model registry and run project-specific evaluations.

Avoid consensus theater. For major decisions use one author proposal, one challenger review, one revision, and one verifier decision. Record unresolved dissent rather than creating endless model debate.

## Operating modes

Every project instruction begins with one mode:

- `INITIALIZE`: inspect inputs, verify sources, establish Stage 0 artifacts and tasks
- `STATUS`: report repository state, blockers, and next action without unrelated work
- `PLAN_STAGE_<N>`: create or revise one stage's task graph
- `EXECUTE_TASK_<ID>`: execute one bounded task
- `REVIEW_TASK_<ID>`: independently review one task
- `FIX_TASK_<ID>`: address verified findings
- `VERIFY_TASK_<ID>`: independently verify one task after the author/fixer cycle
- `VERIFY_STAGE_<N>`: verify the full stage gate
- `ADVANCE_STAGE`: advance only after verification
- `AUDIT_ARCHITECTURE`: inspect coherence, coupling, reversibility, and operational risk
- `AUDIT_SECURITY`: inspect threats and hard controls
- `AUDIT_PRODUCT`: test whether the project solves a valuable customer problem
- `BENCHMARK_MODELS`: update project-specific model evidence
- `PREPARE_VC`: produce investor materials only from verified evidence
- `RESUME`: continue from the latest verified repository checkpoint

## Repository state

Before work, read:

1. `01_governance/PROJECT_STATE.yaml`
2. `01_governance/TASK_REGISTRY.yaml`
3. `01_governance/DECISION_LOG.md`
4. `01_governance/ASSUMPTION_REGISTER.md`
5. `01_governance/RISK_REGISTER.md`
6. `01_governance/MODEL_REGISTRY.yaml`
7. `01_governance/SOURCE_LEDGER.csv`

Do not infer project state from conversation memory.

## Stage 0: intake, governance, and reference research

Objective: establish a trustworthy foundation.

Required work:

- inventory every available file
- preserve original evidence
- verify current Grok Bot behavior from primary sources
- build a feature inventory and evidence ledger
- separate verified behavior from design inference
- identify rollout-dependent or unknown behavior
- establish model, assumption, risk, decision, task, and project-state records
- prepare a black-box product test plan

Gate:

- consequential product claims are sourced or labeled
- current product version and research date are explicit
- no fabricated observations exist
- unresolved high-impact questions are visible
- governance files agree with one another

## Stage 1: customer, wedge, and company thesis

This is preserved startup-track logic. While D-016 is active, Stage 1 customer-discovery execution is deferred, S1-003 remains paused, and this gate is not a prerequisite for the Engineering Preview E1/E2/E3 sequence. It applies again only after a separate founder decision resumes the startup track.

Generate at least five customer-workflow combinations. Evaluate:

- pain and urgency
- current workaround
- workflow frequency
- economic value
- cost of failure
- willingness to delegate
- required integrations
- security sensitivity
- sales cycle
- ease of reaching users
- prototype feasibility
- differentiation
- expansion potential
- bootstrap revenue potential
- investor relevance

Write falsifiable hypotheses. Do not fabricate market size or demand.

Gate:

- one provisional beachhead customer
- one primary workflow
- one primary differentiator
- one narrow prototype demo
- one expansion path
- a concrete customer evidence plan

## Stage 2: product definition and parity map

Create a functional-parity matrix covering:

- persistent agents
- durable roles and memory
- cloud execution
- browser, terminal, files, APIs, and GUI use
- background work
- user steering and cancellation
- approvals and human takeover
- artifacts and evidence
- handoffs and groups
- skills and routines
- notifications and mobile supervision
- team administration
- audit, metering, and billing

Classify each capability as:

- reference verified
- reference partial
- reference unknown
- MVP
- later release
- intentionally different
- out of scope

Each MVP requirement must define user, trigger, expected behavior, failure behavior, permissions, returned evidence, and measurable acceptance criteria.

Gate: MVP and full platform are clearly separated and the first release does not require user-visible multi-agent teams.

## Stage 3: architecture options and decisions

Compare alternatives for:

- client surfaces
- authentication and tenants
- conversation and task services
- durable workflows
- agent runtime
- model abstraction and routing
- tools and connectors
- browser and computer use
- sandboxes and VMs
- files and artifacts
- memory
- approvals
- eventing
- notifications
- observability
- metering and billing
- audit and retention

Required architecture comparisons:

### Compute isolation

- one VM per user
- one VM per agent
- one sandbox per task
- persistent user workspace plus ephemeral task sandboxes
- isolated agent workspaces plus explicitly shared project storage

### Durable execution

- custom queue
- database-backed state machine
- Temporal or an equivalent workflow engine
- managed cloud queues and workers

### Computer control

- structured API or connector
- Playwright or browser automation
- DOM and accessibility tree
- Chrome DevTools Protocol
- screenshot-based vision
- native desktop control
- hybrid structured plus visual control

### Agent orchestration

- one loop
- planner-executor
- planner-executor-verifier
- actor model
- event-driven agents
- manager-worker hierarchy
- shared blackboard
- hybrid durable actor model

Every major decision requires an ADR with requirements, alternatives, choice, rationale, tradeoffs, migration path, reversal cost, and missing evidence.

Gate: tenant, credential, execution, and data boundaries are explicit; model providers are replaceable; uncertain technologies have spikes.

## Stage 4: technical spikes

Test the highest-risk assumptions before application breadth:

- persistent sandbox lifecycle
- realistic browser workflow
- recovery from unexpected UI state
- terminal and file operations
- pause, resume, checkpoint, and worker restart
- user interruption and redirection
- provider abstraction across at least two providers
- tool-call normalization
- realtime activity streaming
- secure authentication takeover
- approval interception
- artifact storage and retrieval
- external-state verification
- latency and cost

Every spike records hypothesis, environment, model, implementation, test cases, result, failures, cost, latency, security impact, and architecture consequence.

Gate: the central execution loop is demonstrated with evidence, not only diagrams or mocks.

## Stage 5: single persistent-agent MVP

Build one credible AI teammate with:

- account and isolated workspace
- persistent agent identity and conversation
- durable instructions and permissions
- task planning and execution
- browser, terminal, files, and at least one structured integration
- background continuation after client disconnect
- progress checkpoints and worker recovery
- pause, stop, redirect, approval, and human login takeover
- concise plan and activity visibility
- artifact creation
- source and action evidence
- external-state verification
- provider abstraction with primary and fallback models

Explicit MVP non-goals unless Stage 1 evidence changes them:

- full native mobile app
- many visible agents
- public skill marketplace
- enterprise SSO
- every connector
- general-purpose perfect computer use
- workflow learning from demonstration
- unlimited persistent VMs
- autonomous consequential financial or legal actions

Success means a narrow set of real workflows complete reliably. Chat functioning is not success. A plausible answer is not success. A model claiming completion is not success.

## Stage 6: private alpha and reliability

Harden:

- tenant isolation
- permissions and approvals
- secret handling
- prompt injection defenses
- idempotency and duplicate prevention
- timeouts and retries
- browser, worker, provider, and connector recovery
- rate and spend limits
- usage metering
- observability
- privacy and retention
- support and incident handling

Track:

- task success
- verified completion
- false completion
- human interventions
- approval violations
- recovery
- duplicate actions
- cost per task
- p50 and p95 latency
- user correction
- artifact acceptance
- retention by workflow

Do not multiply unreliable behavior by adding more agents.

## Stage 7: internal multi-model orchestration

A single user-visible agent may use internal roles:

```text
classifier → router → planner → executor/coder → verifier → integrator
```

Use multiple models only when they improve success, verified completion, cost, latency, security, or maintainability compared with the best single-model baseline.

Prevent endless debate, duplicate work, uncontrolled token use, incompatible schemas, and verification that merely restates the author.

## Stage 8: multiple persistent agents and group conversations

Add visible specialist agents only after runtime reliability.

Each agent needs identity, role, instructions, memory scope, workspace scope, tool and credential scopes, approval policy, skills, routines, active tasks, inbox, status, and model policy.

Support structured primitives:

- SEND_MESSAGE
- DELEGATE_TASK
- REQUEST_REVIEW
- RETURN_RESULT
- TRANSFER_OWNERSHIP
- ESCALATE_BLOCKER
- BROADCAST_UPDATE
- CANCEL_DELEGATION

Every handoff needs a single owner, expected output, constraints, evidence, artifacts, deadline, and correlation ID.

Prevent recursive delegation, circular waiting, duplicate ownership, response storms, uncontrolled context replication, and token explosions.

A group containing several chatbots is not sufficient. The system must demonstrate reliable ownership transfer and useful specialization.

## Stage 9: skills, routines, and workflow learning

A skill is a versioned reusable procedure with purpose, triggers, inputs, permissions, tools, steps, decisions, validation, output contract, approvals, failures, stale-data policy, examples, tests, and provenance.

A routine binds a trigger to an owning agent, skill or task, inputs, execution policy, approvals, result destination, retry policy, budget, and run history.

Workflow learning from demonstration is later-stage. A demonstration creates a draft skill, not a trusted automation. It must identify variables, uncertainty, and exceptions, then pass user review and safe testing.

## Stage 10: multi-tenant SaaS

Implement organizations, roles, workspaces, RBAC, tenant isolation, shared agents and skills, credential governance, model policies, spend limits, usage analytics, billing, quotas, export, deletion, retention, audit, support, and onboarding.

Plan for enterprise controls without building enterprise theater before product-market evidence.

## Stage 11: product surfaces

Choose web, desktop, and mobile surfaces based on workflow need.

The first prototype may use a strong web control plane. Mobile should initially focus on remote supervision: task entry, notifications, questions, approvals, status, results, pause, and stop.

## Stage 12: fundraising readiness

Create investor material only from verified product and customer evidence.

The pitch must cover customer pain, why assistants fail, initial wedge, demo, why now, technical insight, differentiation, model strategy, security, business model, evidence, competition, defensibility, milestones, use of funds, risks, and founder fit.

Several LLM APIs are not a moat. Defensibility may develop through workflow data, evaluations, reliability, integrations, distribution, security, customer-specific memory and skills, switching costs, and operational learning.

## Agent runtime requirements

Model the runtime as a durable state machine with at least:

```text
CREATED
QUEUED
ANALYZING
PLANNING
READY_TO_EXECUTE
EXECUTING
OBSERVING
VERIFYING
DELEGATING
WAITING_FOR_AGENT
WAITING_FOR_USER
WAITING_FOR_APPROVAL
WAITING_FOR_EXTERNAL_EVENT
PAUSED
RETRYING
BLOCKED
COMPLETED
FAILED
CANCELLED
```

Define legal transitions, persisted state, leases, heartbeats, checkpoints, retries, cancellation, redirection, idempotency, partial completion, recovery, and terminal conditions.

## Completion standard

Define a completion predicate for every task.

Examples:

- A document task requires the file to exist, open, contain the required sections, preserve sources, and pass quality checks.
- A CRM task requires rereading the changed record, confirming exact values, and recording the action.
- A coding task requires the requested behavior, tests, static checks, documented limitations, and a reviewable patch or commit.

Track false completion as a first-class failure.

## Security requirements

Threat-model malicious webpages, emails, documents, connectors, MCP servers, prompt injection, credential leakage, tenant leakage, agent leakage, command injection, sandbox escape, privilege escalation, destructive actions, social engineering, malicious downloads, recursive attacks, memory poisoning, approval manipulation, billing abuse, and denial of service.

Required principles:

- least privilege
- deny by default
- scoped credentials
- secrets outside model context
- explicit shared resources
- structured approvals
- immutable audit events
- network and command controls
- input validation and output sanitization
- provenance and revocation
- incident response and deletion

Model review may supplement hard controls but never replace them.

## Model routing

Maintain logical roles rather than hardcoding vendors:

- AUTONOMOUS_CONTROLLER
- PLANNER
- EXECUTOR
- CODER
- COMPUTER_CONTROLLER
- VISION_INTERPRETER
- VERIFIER
- SECURITY_REVIEWER
- MEMORY_EXTRACTOR
- SUMMARIZER
- ROUTER

Use the least expensive model that has demonstrated sufficient reliability, with stronger verification when failure is costly. Record exact model version, access method, cost, latency, capabilities, constraints, and benchmark evidence.

## Task execution rules

For `EXECUTE_TASK_<ID>`:

1. Read project state and the task.
2. Confirm dependencies are verified.
3. Read canonical files and inspect existing code.
4. Implement only the bounded task.
5. Add or update tests.
6. Run required checks.
7. Record commands and exact results.
8. Update relevant documentation.
9. Mark `READY_FOR_REVIEW`, not `VERIFIED`.
10. Create a factual handoff.

Do not silently replace architecture, delete tests, hide failures, expose secrets, weaken controls, or claim mocked behavior is real.

## Review rules

Classify findings as BLOCKER, HIGH, MEDIUM, LOW, or NOTE. Each finding needs affected requirement, evidence, consequence, correction, and verification method.

Block approval for acceptance failure, security-boundary violations, tenant leakage, missing authorization, secret exposure, false completion, data-loss risk, destructive untested migration, or material architectural contradiction.

## Initial investor demonstration

The first demo should show one narrow task that ordinary chatbots cannot reliably finish:

1. natural-language delegation
2. persistent execution
3. real tools or applications
4. continued work after client disconnect
5. a blocked sensitive step or approval
6. user intervention
7. resumption
8. a finished artifact or changed external state
9. verified final state
10. concise action log

Avoid fake traces, prewritten results, hidden manual work, and unstable dependencies.

## INITIALIZE output

When run in `INITIALIZE` mode for the preserved startup track, use the following output. While D-016 is active, follow the Engineering Preview E-track, task registry, and charter instead; do not re-run beachhead selection or customer work merely because this historical startup-mode procedure exists.

1. Inventory files.
2. Verify source freshness.
3. Reconcile governance records.
4. Expand the source ledger and parity map.
5. Establish the current reference-product baseline.
6. Propose at least five customer-workflow combinations.
7. Recommend one provisional beachhead and falsification plan.
8. Assign author, challenger, and verifier roles.
9. Create the next bounded tasks.
10. Do not begin application implementation.

End with:

```text
MODE COMPLETED:
CURRENT STAGE:
GATE STATUS:
FILES CREATED:
FILES MODIFIED:
UNRESOLVED BLOCKERS:
NEXT COMMAND:
```
