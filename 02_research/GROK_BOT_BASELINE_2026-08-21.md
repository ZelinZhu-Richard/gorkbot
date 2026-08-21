# Grok Bot Feature and Evidence Baseline

## Record status

- Task: `S0-002`
- Author status: `READY_FOR_REVIEW`
- Research date: 2026-08-21
- Reference product: Grok Bot
- Official documentation version context: the reviewed Grok Bot pages display `Last updated: August 11, 2026`
- Installed application build: UNKNOWN; no product account or installed app was available to this author run
- Account, plan, region, and rollout context: UNKNOWN
- Black-box runs completed: 0

This is a current official-documentation baseline, not proof of runtime reliability. A first-party product statement is a `VERIFIED FACT` about what the vendor currently documents. It is not a reproduced observation unless a black-box record says so.

## Evidence labels

- `VERIFIED FACT — DOCUMENTED`: directly supported by a current official page reopened on 2026-08-21.
- `STRONG INFERENCE`: a bounded interpretation of several documented facts; it is not an implementation claim.
- `OPEN QUESTION`: not established by the reviewed sources or dependent on account rollout or direct testing.
- `DESIGN PROPOSAL`: an independent product recommendation. No architecture proposal is made in this Stage 0 record.

## Source freshness result

The official Grok Bot navigation and the thirteen pages cited below were reopened on 2026-08-21. Each cited product page was reachable on `docs.x.ai`, and each displayed an August 11, 2026 update date. The prepared source map was therefore useful but was not treated as proof of freshness.

The documentation repeatedly uses rollout qualifiers. In particular, search, default-model selection, Auto Review, teach-by-demonstration, notifications, event triggers, usage views, and some team controls can vary by account or be gradually enabled. Those features remain rollout-dependent until tested on an identified account.

## Current documented feature baseline

| ID | Capability | Evidence status | Current documented behavior | Source IDs | Important limit or unknown |
|---|---|---|---|---|---|
| GBF-001 | Persistent named agents | VERIFIED FACT — DOCUMENTED | A Bot has a name, job, conversation, profile, and working context that develops over time. | SRC-001, SRC-002 | Actual memory accuracy, retention duration, and correction behavior are untested. |
| GBF-002 | Bot roster and lifecycle | VERIFIED FACT — DOCUMENTED | Users can create, edit, pin, hide, duplicate, and delete Bots. An account can have up to 50 Bots and group chats combined. | SRC-002 | Account-specific enforcement and deletion timing are untested. |
| GBF-003 | Duplication semantics | VERIFIED FACT — DOCUMENTED | A duplicate carries profile, settings, enabled skills, routines, and avatar, but not conversation history, learned memory, or chat attachments. | SRC-002 | File and login remnants follow the shared-computer boundary. |
| GBF-004 | Memory guidance | VERIFIED FACT — DOCUMENTED | A Bot may retain stable preferences, important facts, and work summaries; the documentation warns users to reopen authoritative sources for changing facts. | SRC-002 | Memory schema, provenance, capacity, expiration, and retrieval algorithm are unknown. |
| GBF-005 | Persistent cloud computer | VERIFIED FACT — DOCUMENTED | Grok Bot works from a persistent cloud computer with browser, command line, files, and connected tools; work does not depend on the user's laptop remaining open. | SRC-001, SRC-008, SRC-013 | Runtime, scheduler, checkpoint, and VM implementation details are unknown. |
| GBF-006 | User-scoped shared-computer boundary | VERIFIED FACT — DOCUMENTED | Every Bot on one account shares the same cloud computer, files, browser sessions, sign-ins, and command-line credentials. Team documentation describes one managed Linux VM per member. | SRC-001, SRC-005, SRC-006, SRC-013 | This is not a Bot-level security boundary. Tenant-isolation implementation and contractual controls require separate evidence. |
| GBF-007 | Parallel computer work | VERIFIED FACT — DOCUMENTED | Each Bot gets its own screen on the shared computer; multiple Bots can work in parallel, while one Bot can run one computer-use task on its screen at a time. | SRC-001, SRC-008, SRC-013 | Resource contention and cross-screen interference are untested. |
| GBF-008 | Browser, terminal, files, connectors, and GUI fallback | VERIFIED FACT — DOCUMENTED | Bots can use the browser, command line, shared workspace, Plugins/connectors or MCP, and computer use for sites without a structured integration. | SRC-001, SRC-013 | Connector catalog, tool permissions, browser compatibility, and success rates are account- and site-dependent. |
| GBF-009 | Local-computer execution | VERIFIED FACT — DOCUMENTED | Cloud execution is separate from local Mac/Windows execution. Local commands use a policy with Ask every time as the documented default, plus Always allowed or Never allowed choices. | SRC-005, SRC-006, SRC-013 | Team-level ceilings are described as rollout-dependent or coming soon; enforcement has not been tested. |
| GBF-010 | Background continuation | VERIFIED FACT — DOCUMENTED | Closing the desktop app, laptop, iPhone app, or iPhone does not stop a background turn or routine. | SRC-008, SRC-013, SRC-015, SRC-016 | Maximum task duration, lease behavior, idle termination, and exact resumption semantics are unknown. |
| GBF-011 | Recovery and reset | VERIFIED FACT — DOCUMENTED | Recover and Update Agent Computer are documented as preserving durable state; Reset returns to a durable snapshot and can lose recent or unsynced work. | SRC-007, SRC-013, SRC-016 | The precise durable-state boundary and recovery-point objective are unknown. |
| GBF-012 | Attachments | VERIFIED FACT — DOCUMENTED | Desktop accepts up to six attachments; documents, images, and audio can be up to 25 MB each and video up to 200 MB. Listed formats include common documents, data files, code, notebooks, audio, images, and video. | SRC-012, SRC-016 | Parsing quality, encrypted-file behavior beyond rejection, and mobile limits require testing. |
| GBF-013 | Artifacts and evidence | VERIFIED FACT — DOCUMENTED | Files, images, links, and tool results appear as cards; users can preview or save supported outputs. The docs recommend source links, screenshots, timestamps, filenames, action logs, and explicit unverifiable items. | SRC-012 | The product is not documented as automatically enforcing a completion predicate or independent verification. |
| GBF-014 | Activity visibility | VERIFIED FACT — DOCUMENTED | The transcript can show tool activity, computer use, created files, questions, and approval requests. The computer preview shows current clicks, typing, navigation, and status. | SRC-003, SRC-013 | Audit completeness, export, tamper resistance, and retention are unknown. |
| GBF-015 | Redirect and stop | VERIFIED FACT — DOCUMENTED | A direct user message can redirect work in progress; a direct `Stop now` message requests immediate stop and does not undo completed actions. | SRC-003, SRC-016 | Cancellation latency, in-flight action semantics, and partial-result preservation require black-box testing. |
| GBF-016 | Groups and routing | VERIFIED FACT — DOCUMENTED | A group contains two to six Bots. Users can rely on participant routing or mention one or several Bots or `@everyone`; groups support threads and reactions. | SRC-003 | Unmentioned-message ownership, duplicate-response prevention, and routing algorithms are unknown. |
| GBF-017 | Agent handoffs | VERIFIED FACT — DOCUMENTED | Bots can send asynchronous messages, wake another Bot, pass work, and make handoffs visible in the conversation. Bot-to-group handoff messages are currently text-only. | SRC-003 | Ownership representation, delivery guarantees, retry semantics, and context payloads are unknown. |
| GBF-018 | Skills | VERIFIED FACT — DOCUMENTED | A skill is a reusable set of instructions including inputs, sequence, validation, result, and approval boundaries; skills are available across Bots subject to access and enablement. | SRC-004 | Versioning, portability, tests, provenance, and conflict resolution are unknown. |
| GBF-019 | Teach by demonstration | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | When available, a user can record up to ten minutes of visible browser interaction and receive a draft skill to review and test. | SRC-004, SRC-008, SRC-015 | Availability is gradual; generalization and safety are not established by documentation. |
| GBF-020 | Routines and event triggers | VERIFIED FACT — DOCUMENTED, PARTLY ROLLOUT-DEPENDENT | A routine binds a workflow to one Bot on a schedule or, where supported, an event. Background routines can run with the laptop closed. | SRC-004 | Supported events, delivery guarantees, retry behavior, and account availability are unknown. |
| GBF-021 | Routine management and limits | VERIFIED FACT — DOCUMENTED | A Bot can own up to 50 routines; the app keeps 20 recent run records per routine. Users can test, enable, pause, edit, inspect, and delete routines. Long unattended absence may prompt or pause routines. | SRC-004 | Retention beyond 20 runs, idempotency enforcement, and exact unattended limits are unknown. |
| GBF-022 | Action approvals | VERIFIED FACT — DOCUMENTED | Approval cards show a proposed operation and inputs. Desktop offers Allow once, Deny, and saved matching allow rules; iPhone offers Approve once and Deny. | SRC-005 | Coverage of all consequential actions and bypass resistance require testing. |
| GBF-023 | Auto Review | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | When available, model-based Auto Review evaluates tool and computer actions. Require Approval wins over Always Allow; official guidance says it complements rather than replaces least privilege. | SRC-005, SRC-007 | Model, false-negative rate, policy language, synchronization, and enforcement boundary are unknown. |
| GBF-024 | Human takeover and secret entry | VERIFIED FACT — DOCUMENTED | Users are told to take control for passwords, passkeys, two-factor codes, CAPTCHAs, payments, and identity checks. Supported secure secret requests are masked, excluded from the transcript, and not shown to the model. | SRC-005, SRC-013, SRC-014 | Supported secret-request integrations, storage, revocation, and leakage resistance are untested. |
| GBF-025 | Search | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | Search or the command palette can find conversations and available messages, files, links, and routines; cross-conversation results may vary during rollout. | SRC-003, SRC-015 | Index freshness, scope, authorization, and recall are unknown. |
| GBF-026 | Notifications and attention | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | The product distinguishes needs-attention, unread, and working states. Per-Bot desktop/mobile notifications can cover results or needed input; mobile push is rolling out. | SRC-007, SRC-015 | Delivery reliability, latency, and group-notification behavior require testing. |
| GBF-027 | iPhone supervision | VERIFIED FACT — DOCUMENTED | iPhone on iOS 18+ can start work, message, approve, inspect/take over the shared computer, review results, and pause/resume routines. Some routine editing and teach workflows require desktop. | SRC-015 | iPad and Android are not supported in the documented initial launch. |
| GBF-028 | Desktop platforms and access prerequisites | VERIFIED FACT — DOCUMENTED | Desktop is documented for macOS (Apple silicon and Intel) and Windows (x64 and Arm64), not Linux. Eligible plans are documented as SuperGrok Heavy, Cursor Ultra, or Cursor Teams Premium, using Cursor sign-in. | SRC-008, SRC-014 | Actual project account eligibility, geographic access, usage allowance, and billing are unverified. |
| GBF-029 | Team and enterprise controls | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | Team members use a managed Linux VM per member and Cursor identity/SSO; docs describe plugins/MCP, organization computer management, team rules, local execution controls, and network options. | SRC-006 | Availability and required plans vary; several controls are described as coming soon or account-team managed. |
| GBF-030 | Deletion and retained shared state | VERIFIED FACT — DOCUMENTED | Deleting a Bot removes its active profile, conversation, and routines from Grok Bot, but files and sign-ins may remain on the shared computer; backend retention follows applicable Cursor terms. | SRC-002, SRC-005, SRC-008 | Deletion latency, backups, and contractual retention were not verified in this task. |

## Feature-parity evidence map

`Reference documented` means the official documentation supports the public capability claim. It does not mean our product has selected or implemented it.

| Capability family | Reference status | Evidence IDs | Clean-room status |
|---|---|---|---|
| Persistent agent identity and role | Reference documented | GBF-001–GBF-004 | No design selected; no implementation. |
| Persistent/background execution | Reference documented; runtime limits unknown | GBF-005, GBF-010, GBF-011 | No design selected; no implementation. |
| Browser, terminal, files, connectors, GUI | Reference documented; reliability unknown | GBF-008, GBF-012, GBF-013 | No design selected; no implementation. |
| User-scoped computer and isolation | Reference documented; contractual tenant boundary incomplete | GBF-006, GBF-007, GBF-009 | Comparison input only; do not copy the security boundary by default. |
| Steering, cancellation, and recovery | Reference partial | GBF-011, GBF-015 | Semantics require black-box evidence before parity can be claimed. |
| Approvals and human takeover | Reference documented; enforcement untested | GBF-022–GBF-024 | No policy architecture selected. |
| Activity, artifacts, and evidence | Reference documented; automatic verification unknown | GBF-013, GBF-014 | Verified-completion differentiation remains a founder hypothesis. |
| Multi-Bot groups and handoffs | Reference documented; ownership internals unknown | GBF-016, GBF-017 | Later-stage capability, outside first MVP by current decisions. |
| Skills and routines | Reference documented; several rollouts unknown | GBF-018–GBF-021 | Later-stage capability, outside first MVP by current decisions. |
| Search, notifications, and mobile supervision | Reference documented; rollout-dependent | GBF-025–GBF-027 | Surface selection remains provisional. |
| Team administration | Reference partial and rollout-dependent | GBF-029 | Later-stage capability; no enterprise architecture selected. |
| Metering and billing | Reference partial | GBF-028 and FAQ billing text in SRC-008 | Exact pricing, allowance, metering, and account terms are unknown. |
| Audit and retention | Reference partial | GBF-014, GBF-030 | Audit export, immutability, and contractual retention remain unknown. |

## Strong inferences

1. `STRONG INFERENCE`: the user-scoped shared computer reduces handoff friction because Bots can reuse files and sessions, while also creating a deliberately coarse Bot-to-Bot credential boundary. This follows from SRC-001, SRC-005, SRC-006, and SRC-013; it is not a claim about undocumented internal authorization.
2. `STRONG INFERENCE`: documentation encourages evidence-rich outputs but does not establish that Grok Bot independently verifies every completion claim. External-state verification reliability therefore remains an open comparison dimension.
3. `STRONG INFERENCE`: rollout qualifiers are material enough that a documentation-only parity claim would overstate what any particular account can use.

## Open questions requiring direct testing or contractual sources

- Installed app version/build and the exact feature set on an eligible project account.
- End-to-end success, false-completion, intervention, and recovery rates on representative workflows.
- Maximum task and routine duration, idle limits, usage exhaustion behavior, and task concurrency.
- Stop latency, cancellation of in-flight browser/tool actions, redirect ordering, and partial-result handling.
- Durable-state boundaries across app restart, computer recovery, update, reset, and account deletion.
- Cross-Bot file, browser, command-line credential, connector, and group-context visibility.
- Handoff payloads, delivery guarantees, ownership semantics, recursion controls, and duplicate prevention.
- Which model executes each role, whether users can select models, and model failover behavior.
- Complete approval interception coverage and resistance to prompt injection or malicious tools.
- Secure-secret storage, supported connections, revocation, retention, and audit behavior.
- Exact account pricing, included usage, on-demand rates, metering units, and plan/region rollout.
- Current contractual encryption, subprocess isolation, retention, deletion, training, and incident terms under the linked Cursor policies.
- Audit-log completeness, export, immutability, and administrator visibility.
- Skill representation, versioning, provenance, portability, evaluation, and demonstration generalization.

## Prioritized black-box plan

No tests below were run in this author pass because no eligible account, installed build, plan, or region was documented. Use the existing experiment template and preserve exact prompts, initial state, timestamps, screenshots/recordings, external-state checks, and reproduction count.

### P0 — gate-critical

| Priority | Existing test ID | Why it is first | Minimum evidence |
|---|---|---|---|
| 1 | Account preflight (new metadata-only record) | Establishes product build, plan, region, rollout, and safe test accounts before interpreting behavior. | About/version capture, plan, OS, region, enabled controls; secrets redacted. |
| 2 | GB-006 and GB-007 | Verifies the central background-continuation claim. | Server-side timestamps, client closure timeline, artifact/external-state verification; repeat twice. |
| 3 | GB-009 and GB-010 | Defines redirect and stop semantics before consequential tasks. | Last action before/after message, cancellation latency, partial artifacts; repeat twice. |
| 4 | GB-011 and GB-012 | Tests approval presentation, denial, and whether external state remains unchanged. | Approval card, exact target/arguments, independent external-state readback. |
| 5 | GB-013 and GB-014 | Tests takeover and session persistence without exposing credentials. | Redacted recording, session state after return of control and later task. |
| 6 | GB-023 | Confirms the documented shared-computer boundary. | Harmless canary files and non-secret session state across Bots; no real credentials. |
| 7 | GB-029 | Measures recovery/update/reset preservation and loss. | Before/after hashes, file/session inventory, exact recovery action, repeat where safe. |
| 8 | GB-034 | Tests false completion, the core proposed differentiator. | Controlled silent external failure and independent state check. |
| 9 | GB-033 | Tests prompt-injection handling at the approval and tool boundary. | Authorized controlled page, visible decision trace, no real secrets or external writes. |
| 10 | GB-035 | Establishes usage, duration, and limit behavior. | Account usage before/after, elapsed time, interruption behavior, exact plan context. |

### P1 — collaboration and automation

- GB-017 through GB-023: shared files, asynchronous handoffs, ownership, group routing, mentions, concurrency, and isolation.
- GB-024 through GB-028: skill creation/reuse, routine scheduling/failure, and teach-by-demonstration generalization.
- GB-030 through GB-032: search, notifications, and iOS supervision.

### Reproduction and acceptance rules

- Repeat each P0 behavior at least twice; use three runs for timing or recovery claims.
- A vendor UI claim is not the completion check. Verify files by hashes/schema and external actions by rereading the target system.
- Record failures and rollout absence as results, not as missing data to be discarded.
- Do not use production accounts, private customer data, real secrets, irreversible actions, or unauthorized security tests.
- A black-box result applies only to the recorded build, plan, region, initial state, and date.

## Stage 0 conclusion

The current official documentation supports a broad capability baseline for persistent named Bots, one shared user/member cloud computer, browser/terminal/files/connectors, background work, collaboration, skills, routines, approvals, takeover, mobile supervision, and team controls. It does not establish reliability, complete rollout, internal architecture, or this project's access. Those gaps are explicit and block a verified parity claim.

No final architecture, MVP workflow, or customer wedge is selected by this record.
