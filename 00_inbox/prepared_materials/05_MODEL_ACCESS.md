# Model Access and Provider Assumptions

Baseline date: 2026-08-21

This file distinguishes personal development access from production API access. A consumer subscription does not automatically supply API credits, commercial deployment rights, service guarantees, or suitable rate limits.

## Founder-reported personal access

| Provider or tool | Founder-reported access | Intended development role | Production status |
|---|---|---|---|
| ChatGPT Pro | GPT-5.6 Sol and high-effort reasoning | planning, synthesis, architecture, review | verify API access separately |
| Codex | available through OpenAI plan or tooling | bounded implementation and repository work | verify exact version and limits |
| Claude Max | Claude Fable 5 Max | independent challenge, architecture, coding | verify API access separately |
| Claude Code | available | repository execution and review | verify usage and commercial terms |
| DeepSeek | DeepSeek V4 | lower-cost exploration, execution, long context | verify exact hosted or local access |
| Local development | MacBook Pro, Apple silicon, 48 GB memory | orchestration, development, tests, small local models | not a production hosting plan |

No credentials belong in this file.

## Current official model-family baseline

### OpenAI

Official current material describes the GPT-5.6 family:

- Sol: flagship tier
- Terra: balanced lower-cost tier
- Luna: fastest and most economical tier

The family is described as available across ChatGPT, Codex, and the OpenAI API. Exact API model identifiers, effort controls, prices, regional availability, quotas, and retention terms must be captured from the current API account before implementation.

### Anthropic

Claude Fable 5 is founder-selected for high-capability planning and review. Official Anthropic material states that Fable 5 returned to global availability in July 2026 across Claude products and the Claude Platform, subject to plan and usage rules.

Exact model identifiers, pricing, context limits, tool support, computer-use interfaces, provider availability, and data terms must be checked in current Anthropic documentation and the founder's account.

### DeepSeek

Official DeepSeek API material lists V4-Pro and V4-Flash model families through OpenAI-compatible and Anthropic-compatible interfaces. Exact availability, open-weight artifacts, licensing, prices, rate limits, function calling, context behavior, and data handling must be verified before routing production tasks.

## Required production provider adapters

The architecture should expose logical capabilities rather than vendor names:

```text
PLANNER
EXECUTOR
CODER
VISION_INTERPRETER
COMPUTER_CONTROLLER
VERIFIER
SECURITY_REVIEWER
MEMORY_EXTRACTOR
SUMMARIZER
ROUTER
```

Each provider adapter should record:

- exact model and version
- supported modalities
- structured output
- tool calling
- streaming
- context and output limits
- reasoning controls
- timeout behavior
- retry behavior
- usage accounting
- input and output costs
- rate limits
- regional and data-residency options
- retention and training terms
- commercial-use constraints
- known failures

## Initial routing hypotheses

These are hypotheses to benchmark, not permanent assignments.

| Task | Primary candidate | Challenger or verifier | Lower-cost candidate |
|---|---|---|---|
| product and system architecture | GPT-5.6 Sol Pro | Claude Fable 5 | DeepSeek V4-Pro |
| architecture challenge | Claude Fable 5 | GPT-5.6 Sol Pro | DeepSeek V4-Pro |
| bounded coding | Codex with Sol, Terra, or specialized coding model | Claude Code or separate Codex run | Luna or DeepSeek V4 where reliable |
| long-context source synthesis | Fable 5 or Sol | independent alternative provider | DeepSeek V4 |
| deterministic extraction | schema-constrained lower-cost model | sampled strong-model audit | Luna, Terra, or V4-Flash |
| external-state verification | different provider or deterministic tool | strong model on ambiguous cases | task-dependent |
| memory extraction | low-cost structured-output model | periodic stronger audit | Luna, Terra, or V4-Flash |

## Required project benchmark

Before architecture locks model roles, evaluate each accessible model on:

- source fidelity
- long-horizon planning
- repository comprehension
- backend coding
- frontend coding
- infrastructure code
- browser and computer action selection
- debugging
- test generation
- security review
- structured output validity
- context consistency
- latency
- cost per successful task

## Missing access facts

The founder must later add, without exposing credentials:

- which API accounts are funded
- monthly experimental API budget
- organization or account rate limits
- approved data-retention settings
- cloud providers available
- whether local open-weight inference is required
- whether customers can supply their own model keys
- whether the SaaS will resell inference or pass through provider billing
