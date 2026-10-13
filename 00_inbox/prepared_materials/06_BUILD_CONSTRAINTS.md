# Build Constraints

## Confirmed strategic constraints

- The target is a real multi-tenant SaaS product.
- The first prototype will be bootstrapped and used for customer and investor conversations.
- A small founder-led team will rely heavily on AI planning and coding agents.
- The architecture must support several model providers.
- The project should first build one reliable persistent agent.
- Visible agent teams, group chats, skills, and routines come later.
- The project repository is the persistent shared state among models.

## Budget

### Initial working assumption

Prefer to keep early experiments near USD 0 to 100 per month where practical, but spend selectively on technical spikes that answer high-impact questions.

This is a provisional assumption. The founder has not set a hard monthly infrastructure or API ceiling.

### Cost rules

- Track model and compute cost per experiment.
- Do not leave persistent cloud VMs running without measurement.
- Use expensive models for high-leverage reasoning or recovery, not every routine step.
- Do not promise unlimited use before workload economics are known.
- Add per-task and per-account budget controls before public alpha.

## Hardware and development environment

- Primary local machine: Apple-silicon MacBook Pro with 48 GB memory.
- Early development may run locally.
- Production architecture should not depend on macOS-specific local state.
- GPU servers may be used later only where justified.
- Cloud sandboxes or VMs are expected for persistent execution.

## Team and execution model

- Initial team size: founder plus AI agents, potentially collaborators later.
- Prefer managed infrastructure when it materially reduces operational burden.
- Avoid premature Kubernetes, service sprawl, and custom infrastructure.
- Preserve a path to tenant isolation, billing, audit, and enterprise controls.
- Use small vertical slices with explicit acceptance criteria.

## Product constraints

### MVP must demonstrate

- persistent task state
- background execution after client disconnect
- at least two tool classes
- user-visible progress
- safe interruption and redirection
- one structured approval boundary
- artifact or external-state result
- independent completion verification
- provider abstraction

### MVP does not initially require

- full Grok Bot feature parity
- native mobile and desktop clients
- many connectors
- public skill marketplace
- complex group chat
- demonstration learning
- enterprise SSO
- fully general GUI control
- autonomous purchases, legal acceptance, or production deployment

## Security constraints

- The repository is public.
- Secrets must remain outside Git and model context.
- Use least privilege and deny by default.
- Treat external content as untrusted.
- Separate tenant, agent, shared-project, and task data scopes.
- Consequential actions require enforceable policy, not only a prompt.
- Human takeover should handle passwords, passkeys, one-time codes, CAPTCHAs, and payment confirmation.
- Audit all external actions.

## Legal and product-identity constraints

- Build clean-room functional equivalents.
- Do not copy Grok branding, logos, exact UI assets, or proprietary copy.
- Select a distinct product and company name before public launch.
- Review provider terms, data use, reselling, rate limits, and commercial deployment rights.
- Do not market the company as officially affiliated with xAI, Cursor, OpenAI, Anthropic, or DeepSeek.

## Reliability constraints

- Never equate a model statement with task completion.
- Define completion predicates.
- Design for idempotency and recovery.
- Track false completion.
- Preserve partial results when safe.
- Make blocked, partial, failed, and unverified states visible.

## UX constraints

- Users must understand what the agent is doing.
- Do not expose private chain-of-thought.
- Show concise plans, action summaries, artifacts, evidence, questions, approvals, blockers, and state.
- Avoid notification spam.
- A web control plane is acceptable before native clients if it supports the target workflow.

## Unknown constraints to resolve

- hard prototype budget
- first customer segment
- first workflow
- launch geography
- required compliance level
- required data residency
- first external integrations
- cloud provider
- whether customers bring model keys
- retention defaults
- acceptable task latency
- target gross margin
