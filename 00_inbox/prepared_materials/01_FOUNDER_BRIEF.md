# Founder Brief

## Status labels

- CONFIRMED: directly stated by the founder
- PROVISIONAL: useful working hypothesis that requires validation
- UNKNOWN: unresolved and should not be guessed

## Founder and project intent

**CONFIRMED**

The founder wants to build a real SaaS company, not a toy clone or portfolio demo.

The long-term product is a model-agnostic platform for persistent AI teammates. Its clean-room capability benchmark is Grok Bot or better. Customers should eventually be able to create named agents with durable roles, memory, tools, permissions, cloud execution, collaboration, group conversations, reusable skills, routines, and human approval boundaries.

The product should support several model providers. Current candidates include GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, Claude Fable 5, DeepSeek V4, Codex, Claude Code, and future models. Model choice should be based on measured task performance, reliability, cost, latency, privacy, and access, not loyalty to one provider.

The founder plans to use highly capable reasoning models to create the product strategy, research, architecture, stage plans, and verification criteria. Later coding models will execute bounded implementation tasks. Models will share state through repository files and return to those files at every stage.

The first build stage should focus on one extremely capable persistent agent. Visible multi-agent teams and group chat are later stages after the core runtime is reliable.

The founder intends to bootstrap a credible prototype and use product evidence to pitch investors.

## Product vision

Build a system in which a customer can delegate a meaningful result rather than micromanage clicks.

A successful agent should be able to:

- receive a goal and constraints
- identify the authoritative sources and tools
- plan and execute multi-step work
- use browser, terminal, files, structured APIs, connectors, and GUI fallback
- continue after the user's client disconnects
- show concise progress and blockers
- ask for approval before consequential actions
- accept interruption and redirection
- recover from common failures
- produce artifacts and action evidence
- verify the requested external state before declaring completion
- retain useful role-specific context without treating memory as current truth

## Product philosophy

**CONFIRMED**

- Begin with one reliable agent, then add internal multi-model collaboration, then multiple user-visible agents.
- Build model-provider independence into the architecture.
- Let strong reasoning models decide the model-role allocation after benchmarking.
- Preserve project state in files rather than relying on chat memory.
- Build toward a complete SaaS product with multi-tenant architecture.

**PROVISIONAL, REQUIRES VALIDATION**

- Initial beachhead customer: technical founders and small startup teams.
- Initial differentiation: verified completion plus model-transparent orchestration.
- Secondary differentiation: stronger workspace and credential isolation than a shared-computer model.
- Initial sales motion: founder-led outreach and design partnerships.

These are starting hypotheses, not settled facts.

## Business objective

The company should eventually have:

- an understandable high-value workflow
- measurable customer outcomes
- reliable execution rather than impressive chat
- a viable gross-margin model
- model and infrastructure cost controls
- a credible security posture
- a path from individual users to teams
- defensibility beyond connecting several model APIs

## What the company is not

- a Grok-branded product
- a copied interface
- a generic chat wrapper
- a collection of prompts called a multi-agent system
- an unrestricted autonomous system that hides consequential actions
- a product whose main advantage disappears when model vendors add a feature
- an enterprise settings page without a reliable core workflow

## First prototype objective

Build a narrow end-to-end demonstration in which one persistent agent:

1. accepts a real multi-step task
2. uses at least two classes of tools
3. keeps working in the cloud after the client disconnects
4. encounters a controlled approval or authentication boundary
5. accepts user intervention
6. resumes safely
7. creates a useful artifact or changes an external state
8. verifies the result
9. returns an evidence bundle and concise action log

The workflow must be stable enough to demonstrate repeatedly. Reliability matters more than theatrical breadth.

## Founder resources

**CONFIRMED FROM CURRENT PROJECT CONTEXT**

- MacBook Pro with Apple silicon and 48 GB memory for local development
- ChatGPT Pro access
- Claude Max access
- DeepSeek access
- willingness to use cloud infrastructure when justified
- willingness to use AI coding agents extensively
- initial small-team or solo-founder execution model

Exact API credits, model IDs, quotas, legal terms, and production access must be verified separately.

## Initial success milestones

### Research milestone

- current reference-product baseline sourced
- five customer-workflow hypotheses
- one provisional wedge
- top architectural risks identified

### Technical milestone

- durable task survives client disconnect and worker restart
- at least two model providers work behind one abstraction
- browser or computer action is verified
- sensitive action is intercepted by policy
- artifact is stored and returned

### Product milestone

- at least five design partners complete the target workflow
- the workflow has measurable value
- false-completion rate is tracked
- cost per successful task is known
- users understand the activity and approval interface

### Fundraising milestone

- repeatable live demo
- verified task metrics
- evidence from real users
- clear wedge and expansion path
- honest cost model
- defensible technical or workflow insight

## Open founder decisions

The founder should eventually decide, using evidence:

- first paying customer segment
- first workflow
- acceptable prototype cloud budget
- whether web is sufficient before desktop
- which external integrations are essential
- initial geographic and regulatory scope
- whether the product stores customer data or primarily operates in customer-controlled systems
- desired level of agent portability
- pricing unit: seat, task, compute, usage, outcome, or hybrid
