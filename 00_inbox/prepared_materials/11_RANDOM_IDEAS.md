# Idea Backlog

Ideas remain hypotheses until customer, technical, and economic evidence supports them.

## Core product ideas

### Model-transparent agent policy

Let customers define provider preferences, allowed models, privacy requirements, latency targets, and task budgets. Show which model performed which role.

Risk: too much choice may confuse users. The default must be strong.

### Verified completion bundles

Every completed task can return:

- requested outcome
- completion predicate
- external-state checks
- sources
- artifacts
- action log
- unresolved uncertainty
- verifier result

Potential wedge: trust rather than personality.

### Isolated agent workspaces with explicit sharing

Separate:

- tenant workspace
- agent-private workspace
- task sandbox
- shared project artifacts
- scoped credentials

Potential advantage: clearer security boundary than every agent sharing all user-level computer state.

### Branch, review, and merge for knowledge work

Apply software-development patterns to agent work:

- branch a task
- create draft artifacts
- request specialist review
- compare changes
- merge accepted results
- preserve provenance and rollback

### Portable agents

Export agent profile, memory, skills, artifacts, tool requirements, and model policy in a documented format.

Risk: portability reduces lock-in but can build trust and ecosystem adoption.

### Cost-aware orchestration

Estimate task cost before execution and escalate model capability only when needed.

Possible policy:

```text
cheap structured extractor
→ normal executor
→ strong planner on ambiguity
→ independent verifier on consequential completion
```

### Reliability benchmark as product asset

Build a continuously growing evaluation suite around real customer workflows, browser changes, interruptions, credential expiration, and false completion.

Potential moat: execution data and regression infrastructure.

### Agent team templates

Later, ship tested role sets for specific workflows rather than generic personas.

Examples:

- founder operating review
- software release team
- research synthesis team
- analytics investigation team

Risk: roleplay without reliable ownership and tools is cosmetic.

## Product wedges to test

1. Persistent engineering teammate for small teams
2. Research and competitive-intelligence teammate
3. Data-analysis and reporting teammate
4. Agent operating system for technical power users
5. Secure, model-governed agent platform for teams

## Distribution ideas

- founder-led design partnerships
- public reliability benchmark
- open agent portability specification
- workflow templates tied to measurable outcomes
- developer-first GitHub integration
- research-team pilot program
- transparent cost and completion metrics

## Investor narrative candidates

Do not use until evidence exists:

- AI employees are becoming persistent software infrastructure rather than chat sessions.
- Model intelligence is commoditizing faster than trustworthy execution.
- The control plane for model, tool, memory, permission, and verification may be more durable than any one model.
- Customers need accountable outcomes, not more chat windows.

## Ideas to reject unless evidence changes

- launch with dozens of agents
- build a marketplace before skills are reliable
- copy Grok Bot branding or interface
- claim every knowledge worker as the initial customer
- build native apps before workflow value is proven
- market model debate as a core benefit
- offer unrestricted autonomy
- promise unlimited usage
