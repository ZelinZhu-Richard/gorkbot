# Product Reference Links

Research baseline date: 2026-08-21

This file is a starting source map, not a completed teardown. Current planning models must reopen primary sources and record access dates because product behavior may change.

## Official Grok Bot documentation

### Core concept

- Overview: https://docs.x.ai/grok-bot/overview
  - persistent named agents
  - persistent cloud computer
  - browser, filesystem, and terminal
  - connectors or MCP plus computer use
  - multi-Bot collaboration
  - durable state

### Bot lifecycle and memory

- Create and manage Bots: https://docs.x.ai/grok-bot/bots
  - roles and profiles
  - Bot limits
  - duplication behavior
  - deletion behavior
  - durable memory guidance
  - separation between Bot conversation and shared computer

### Conversations, groups, and handoffs

- Message and collaborate: https://docs.x.ai/grok-bot/chat-and-collaboration
  - progress activity
  - redirection and stopping
  - two-to-six-Bot groups
  - mentions
  - asynchronous handoffs
  - threads and reactions

### Files and computer execution

- Files and results: https://docs.x.ai/grok-bot/files-and-results
- Use the computer and apps: https://docs.x.ai/grok-bot/computer-and-apps

Verify exact current behavior for:

- file persistence
- artifact previews
- downloads and uploads
- terminal permissions
- browser sessions
- local-computer access
- parallel screens
- reset and recovery

### Skills, routines, and automation

- Skills and routines: https://docs.x.ai/grok-bot/skills-routines-and-automations
  - reusable instructions
  - scheduled and event-triggered routines
  - validation and safety boundaries
  - routine limits and run history
  - workflow demonstration behavior

### Security and approvals

- Approvals, security, and privacy: https://docs.x.ai/grok-bot/approvals-security-and-privacy
  - approval boundaries
  - auto-review rules
  - human takeover for passwords and verification
  - local-computer permissions
  - shared-computer security boundary
  - least privilege

### Teams and enterprise

- Teams and enterprises: https://docs.x.ai/grok-bot/teams-and-enterprises
  - one managed Linux computer per member
  - user-level shared computer
  - team and organization controls
  - local execution controls
  - admin computer management
  - model and provider policy limits

### Notifications, mobile, and support

- Settings and notifications: https://docs.x.ai/grok-bot/settings-and-notifications
- FAQ: https://docs.x.ai/grok-bot/faq
- iOS: https://docs.x.ai/grok-bot/mobile
- Troubleshooting: https://docs.x.ai/grok-bot/troubleshooting
- Use cases: https://docs.x.ai/grok-bot/use-cases
- Get started: https://docs.x.ai/grok-bot/get-started

Some URL slugs should be verified before relying on them. The overview navigation is the authoritative index.

## Official model references

### OpenAI

- GPT-5.6 announcement: https://openai.com/index/gpt-5-6/
- API model documentation: https://platform.openai.com/docs/models
- API pricing: https://openai.com/api/pricing/

Current family labels include Sol, Terra, and Luna. Exact production identifiers, effort controls, account access, and prices must be checked at implementation time.

### Anthropic

- Fable 5 availability update: https://www.anthropic.com/news/redeploying-fable-5
- Anthropic model documentation: https://docs.anthropic.com/en/docs/about-claude/models/overview
- Claude Code documentation: https://docs.anthropic.com/en/docs/claude-code
- MCP documentation: https://docs.anthropic.com/en/docs/mcp

Verify API availability, model identifiers, usage-credit rules, computer-use support, and data terms.

### DeepSeek

- API updates: https://api-docs.deepseek.com/updates
- API quick start and model names: https://api-docs.deepseek.com/quick_start/pricing-details-usd/
- Transparency and model reports: https://www.deepseek.com/en/transparency/

Current V4 API labels should be verified before implementation. Separate open-weight availability from hosted API access and commercial deployment terms.

## Black-box evidence policy

For each observed product behavior, record:

- exact product and version context
- date
- account or rollout conditions
- input prompt
- initial state
- actions observed
- output
- timing
- permissions or approvals
- failure or recovery behavior
- screenshots or recording paths
- whether the result was reproduced

Do not infer architecture from a single screenshot. Do not treat a marketing demo as proof of reliability.

## Claims requiring direct testing

- how long tasks can run
- what persists across app restart, VM reset, and account reset
- exact concurrency behavior
- how agent-to-agent context is represented
- whether agents receive complete group history
- browser and filesystem isolation
- credential persistence
- failure recovery
- cancellation semantics
- cost or usage accounting
- workflow-learning generalization
- event-trigger availability
- model selection and failover
- limits by account tier
