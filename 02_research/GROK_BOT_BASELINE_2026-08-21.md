# Grok Bot Feature and Evidence Baseline

## Record status

- Task: `S0-002`
- Author status: `READY_FOR_REVIEW` (fixer pass complete; not independently verified)
- Research date: 2026-08-21 (original author pass)
- Current-source revalidation completed: `2026-08-22T03:07:34Z` (`2026-08-21T23:07:34-04:00`); final 24-source reachability window began at `2026-08-22T03:06:16Z`
- Reference product: Grok Bot
- Product status and launch context: vendor-labelled `beta` / `Early beta`, publicly launched 2026-08-11; Cursor's official help center says the beta label sets expectations for an early product and is not a statement that Cursor Beta Services terms apply (SRC-025, SRC-027, SRC-029, SRC-033)
- Publisher and account ecosystem: the documentation is branded SpaceXAI and the launch post is published by X.AI LLC; Grok Bot uses Cursor identity, billing, usage, privacy settings, and team administration (SRC-006, SRC-014, SRC-025, SRC-028, SRC-031)
- Official documentation version context: among the thirteen feature pages cited by the original baseline, nine display `Last updated: August 11, 2026` and four display `Last updated: August 20, 2026`; the official access-expansion post is dated August 21, 2026
- Known public app-version reference: Cursor Help says Sidebar Sections require Grok Bot `v1.2.0` or later; this is a minimum for one feature, not the current product version or evidence of the project account's installed build (SRC-029)
- Installed application build: UNKNOWN; no product account or installed app was available to this author run
- Account, plan, region, and rollout context: UNKNOWN
- Black-box runs completed: 0

This is a current official-documentation baseline, not proof of runtime reliability. A first-party product statement is a `VERIFIED FACT` about what the vendor currently documents. It is not a reproduced observation unless a black-box record says so.

## Evidence labels

- `VERIFIED FACT — DOCUMENTED`: directly supported by a current official page reopened during the fixer pass completed at `2026-08-22T03:07:34Z`.
- `STRONG INFERENCE`: a bounded interpretation of several documented facts; it is not an implementation claim.
- `OPEN QUESTION`: not established by the reviewed sources or dependent on account rollout or direct testing.
- `DESIGN PROPOSAL`: an independent product recommendation. No architecture proposal is made in this Stage 0 record.

## Source freshness result

The thirteen originally cited Grok Bot pages plus the official Use cases page were independently reopened from their live primary URLs during this fix pass; live-source revalidation completed at `2026-08-22T03:07:34Z`. All fourteen were reachable. The nine unchanged cited pages and Use cases display August 11, 2026. FAQ, Get started, Mobile, and Teams and enterprises display August 20, 2026 and expose JSON-LD `dateModified` values for that date.

`SOURCE DRIFT — OBSERVED AND PRESERVED`: the initial author handoff says all thirteen cited pages displayed August 11. That pass did not record a per-page access time. The challenger preserved Internet Archive copies dated August 12–19 that match the initial plan text, then observed the four live pages change on or about August 20/21. This revision corrects the current baseline and ledger without rewriting the historical handoff result as though it had always used the newer text. The August 21 official expansion post confirms that Grok Bot launched on August 11 and was then expanded to more plans (SRC-026).

The documentation still uses material rollout qualifiers for search, Auto Review, teach-by-demonstration, notifications, event triggers, some usage views, and team/enterprise access or controls. Model selection is no longer treated generically as rollout-dependent: the teams page documents product-managed model choice with no member/admin picker, while the settings page conditionally mentions a `Default Model` control. That remaining surface/account ambiguity is recorded under GBF-031 and the official-source inconsistencies below.

## Current documented feature baseline

| ID | Capability | Evidence status | Current documented behavior | Source IDs | Important limit or unknown |
|---|---|---|---|---|---|
| GBF-001 | Persistent named agents | VERIFIED FACT — DOCUMENTED | A Bot has a name, job, conversation, profile, and working context that develops over time. | SRC-001, SRC-002 | Actual memory accuracy, retention duration, and correction behavior are untested. |
| GBF-002 | Bot roster and lifecycle | VERIFIED FACT — DOCUMENTED | Users can create, edit, pin, hide, duplicate, and delete Bots. An account can have up to 50 Bots and group chats combined. | SRC-002 | Account-specific enforcement and deletion timing are untested. |
| GBF-003 | Duplication semantics | VERIFIED FACT — DOCUMENTED | A duplicate carries profile, settings, enabled skills, routines, and avatar, but not conversation history, learned memory, or chat attachments. | SRC-002 | File and login remnants follow the shared-computer boundary. |
| GBF-004 | Memory guidance | VERIFIED FACT — DOCUMENTED | A Bot may retain stable preferences, important facts, and work summaries; the documentation warns users to reopen authoritative sources for changing facts. | SRC-002 | Memory schema, provenance, capacity, expiration, and retrieval algorithm are unknown. |
| GBF-005 | Persistent cloud computer | VERIFIED FACT — DOCUMENTED | Grok Bot works from a persistent cloud computer with browser, command line, files, and connected tools; work does not depend on the user's laptop remaining open. | SRC-001, SRC-008, SRC-013, SRC-025 | Runtime, scheduler, checkpoint, and VM implementation details are unknown. SRC-001's per-Bot-VM wording conflicts with its own shared-computer wording; see DOC-A-001. |
| GBF-006 | User/member-scoped shared-computer boundary | VERIFIED FACT — DOCUMENTED | Every Bot on one individual account shares one user-assigned computer, files, browser sessions, sign-ins, and command-line credentials. For teams, each member gets one managed Linux VM shared by all that member's Bots and across every team the member belongs to. Separate screens are work surfaces, not security boundaries. | SRC-001, SRC-005, SRC-006, SRC-008, SRC-013, SRC-025 | The resolving reading is user/member scope, not Bot scope; see DOC-A-001. Tenant isolation, implementation, and contractual guarantees remain unknown. |
| GBF-007 | Parallel computer work | VERIFIED FACT — DOCUMENTED | Each Bot gets its own screen on the shared computer; multiple Bots can work in parallel, while one Bot can run one computer-use task on its screen at a time. | SRC-001, SRC-008, SRC-013 | Resource contention and cross-screen interference are untested. |
| GBF-008 | Browser, terminal, files, connectors, and GUI fallback | VERIFIED FACT — DOCUMENTED | Bots can use the browser, command line, shared workspace, Plugins/connectors or MCP, and computer use for sites without a structured integration. Installed connectors are account-wide. For hosted MCP, the teams page says sign-in tokens remain in Cursor's backend and the computer never stores those tokens. | SRC-001, SRC-006, SRC-013, SRC-032 | Connector catalog, per-tool authorization, browser compatibility, backend token handling beyond the documented claim, and success rates remain untested. |
| GBF-009 | Local-computer execution | VERIFIED FACT — DOCUMENTED | Cloud execution is separate from local Mac/Windows execution. Local commands use a policy with Ask every time as the documented default, plus Always allowed or Never allowed choices. | SRC-005, SRC-006, SRC-013 | Team-level ceilings are described as rollout-dependent or coming soon; enforcement has not been tested. |
| GBF-010 | Background continuation | VERIFIED FACT — DOCUMENTED | Closing the desktop app, laptop, iPhone app, or iPhone does not stop a background turn or routine. | SRC-008, SRC-013, SRC-015, SRC-016 | Maximum task duration, lease behavior, idle termination, and exact resumption semantics are unknown. |
| GBF-011 | Recovery, storage layers, and reset | VERIFIED FACT — DOCUMENTED | Recover and Update Agent Computer are documented as preserving durable state. Cursor Help says conversation history is outside the box filesystem and synced box data has a durable server copy. Reset recreates the computer from durable/synced state but can lose recent or unsynced work; local Mac/Windows files are outside that recovery. The teams FAQ warns that in-computer sign-in sessions can drop after computer recreation or a network-address change. | SRC-006, SRC-007, SRC-013, SRC-016, SRC-030 | Sync timing, exact durable-store contents, recovery-point objective, backups, and recovery reliability are unknown. The shorter teams-page statement that Reset “keeps its data” is qualified by the other sources; see DOC-A-003. |
| GBF-012 | Attachments | VERIFIED FACT — DOCUMENTED | Desktop accepts up to six attachments; documents, images, and audio can be up to 25 MB each and video up to 200 MB. Listed formats include common documents, data files, code, notebooks, audio, images, and video. | SRC-012, SRC-016 | Parsing quality, encrypted-file behavior beyond rejection, and mobile limits require testing. |
| GBF-013 | Artifacts and evidence | VERIFIED FACT — DOCUMENTED | Files, images, links, and tool results appear as cards; users can preview or save supported outputs. The docs recommend source links, screenshots, timestamps, filenames, action logs, and explicit unverifiable items. | SRC-012 | The product is not documented as automatically enforcing a completion predicate or independent verification. |
| GBF-014 | Activity visibility | VERIFIED FACT — DOCUMENTED | The transcript can show tool activity, computer use, created files, questions, and approval requests. The computer preview shows current clicks, typing, navigation, and status. | SRC-003, SRC-013 | Audit completeness, export, tamper resistance, and retention are unknown. |
| GBF-015 | Redirect and stop | VERIFIED FACT — DOCUMENTED | A direct user message can redirect work in progress; a direct `Stop now` message requests immediate stop and does not undo completed actions. | SRC-003, SRC-016 | Cancellation latency, in-flight action semantics, and partial-result preservation require black-box testing. |
| GBF-016 | Groups and routing | VERIFIED FACT — DOCUMENTED | A group contains two to six Bots. Users can rely on participant routing or mention one or several Bots or `@everyone`; groups support threads and reactions. | SRC-003 | Unmentioned-message ownership, duplicate-response prevention, and routing algorithms are unknown. |
| GBF-017 | Agent handoffs | VERIFIED FACT — DOCUMENTED | Bots can send asynchronous messages, wake another Bot, pass work, and make handoffs visible in the conversation. Bot-to-group handoff messages are currently text-only. | SRC-003 | Ownership representation, delivery guarantees, retry semantics, and context payloads are unknown. |
| GBF-018 | Skills | VERIFIED FACT — DOCUMENTED | A skill is a reusable set of instructions including inputs, sequence, validation, result, and approval boundaries; skills are available across Bots subject to access and enablement. | SRC-004 | Versioning, portability, tests, provenance, and conflict resolution are unknown. |
| GBF-019 | Teach by demonstration | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | When available, a user can record up to ten minutes of visible browser interaction and receive a draft skill to review and test. | SRC-004, SRC-008, SRC-015 | Availability is gradual; generalization and safety are not established. SRC-001's unqualified claim that a demonstrated path is persisted as a routine is broader than the procedural documentation; see DOC-A-002. |
| GBF-020 | Routines and event triggers | VERIFIED FACT — DOCUMENTED, PARTLY ROLLOUT-DEPENDENT | A routine binds a workflow to one Bot on a schedule or, where supported, an event. Background routines can run with the laptop closed. | SRC-004 | Supported events, delivery guarantees, retry behavior, and account availability are unknown. |
| GBF-021 | Routine management and limits | VERIFIED FACT — DOCUMENTED | A Bot can own up to 50 routines; the app keeps 20 recent run records per routine. Users can test, enable, pause, edit, inspect, and delete routines. Long unattended absence may prompt or pause routines. | SRC-004 | Retention beyond 20 runs, idempotency enforcement, and exact unattended limits are unknown. |
| GBF-022 | Action approvals | VERIFIED FACT — DOCUMENTED | Approval cards show a proposed operation and inputs. Desktop offers Allow once, Deny, and saved matching allow rules; iPhone offers Approve once and Deny. | SRC-005 | Coverage of all consequential actions and bypass resistance require testing. |
| GBF-023 | Auto Review | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | When available, model-based Auto Review evaluates tool and computer actions. Require Approval wins over Always Allow; official guidance says it complements rather than replaces least privilege. Personal rules are stored on the current desktop and synced to its Grok Bot computer, but are not an account-synchronized policy across every desktop. | SRC-005, SRC-007 | Model identity, false-negative rate, policy interpretation, propagation timing, and enforcement boundary remain unknown. |
| GBF-024 | Human takeover and secret entry | VERIFIED FACT — DOCUMENTED | Users are told to take control for passwords, passkeys, two-factor codes, CAPTCHAs, payments, and identity checks. Cursor Help says the user signs into sites and the agent does not see the password. Supported secure secret requests/cards are masked, excluded from the transcript, and not shown to the model; ordinary chat/files must not be used for credentials. | SRC-005, SRC-013, SRC-014, SRC-029, SRC-032 | Supported secret integrations, storage, revocation, implementation, and leakage resistance are untested. |
| GBF-025 | Search | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | Search or the command palette can find conversations and available messages, files, links, and routines; cross-conversation results may vary during rollout. | SRC-003, SRC-015 | Index freshness, scope, authorization, and recall are unknown. |
| GBF-026 | Notifications and attention | VERIFIED FACT — DOCUMENTED, ROLLOUT-DEPENDENT | The product distinguishes needs-attention, unread, and working states. Per-Bot desktop/mobile notifications can cover results or needed input; mobile push is rolling out. Group chats do not have the same per-Bot notification switch. | SRC-007, SRC-015 | Delivery reliability, latency, suppression, and the remaining group-notification semantics require testing. |
| GBF-027 | iPhone supervision | VERIFIED FACT — DOCUMENTED | iPhone on iOS 18+ can start work, message, approve, inspect/take over the shared computer, review results, and pause/resume routines. Some routine editing and teach workflows require desktop. | SRC-015 | iPad and Android are not supported in the documented initial launch. |
| GBF-028 | Platforms, plans, trial, and usage prerequisites | VERIFIED FACT — DOCUMENTED, CURRENT PLAN TEXT | Desktop is documented for macOS (Apple silicon and Intel) and Windows (x64 and Arm64), not Linux; iPhone requires iOS 18+. Current included paths are individual SuperGrok Plus/Heavy links, Cursor Pro+/Ultra, and Cursor Teams Standard/Premium. Cursor Pro, basic SuperGrok, and SuperGrok Team/Enterprise linking are not included. A one-time trial is a usage credit with a seven-day window; paid usage resets weekly and can continue through enabled on-demand spend. If both linked subscriptions exist, the FAQ says the product uses the one with more usage. Enterprise access is rolling out through the account team. Cursor Help also documents known persistent authentication errors and phone-verification blocks that can require support. | SRC-006, SRC-008, SRC-014, SRC-015, SRC-026, SRC-028, SRC-031, SRC-034 | The live eligibility text changed on August 20/21. Actual project entitlement, authentication state, region, allowance, trial credit, current build, metering, and billing remain unverified by account readback. |
| GBF-029 | Team, enterprise, and computer administration | VERIFIED FACT — DOCUMENTED, PARTLY ROLLOUT-DEPENDENT | Team members use a per-member managed Linux VM; the Bot runs non-root. Admin docs cover Cursor SSO/dashboard, team rules, MCP policy, a default-on Cloud Agents toggle, static egress, and organization-admin computer kill that deletes the running VM while retaining durable storage. The computer is shared across every team the member belongs to and is not enrolled in mobile device management (MDM) by default. Privacy Mode (Legacy) blocks Grok Bot; spend is visible, an action audit view is coming, and no Grok Bot-specific spend cap exists yet. | SRC-005, SRC-006, SRC-028 | Enterprise availability, account-team settings, cloud-agent behavior, egress ranges, durable-store contents, audit delivery, and enforcement require account or contractual verification; some controls are explicitly coming or rolling out. |
| GBF-030 | Deletion and retained shared state | VERIFIED FACT — DOCUMENTED | Deleting a Bot removes its active profile, conversation, and routines from Grok Bot, but files and sign-ins may remain on the shared computer; backend retention follows applicable Cursor terms. | SRC-002, SRC-005, SRC-008 | Deletion latency, backups, and contractual retention were not verified in this task. |
| GBF-031 | Model and provider policy | VERIFIED FACT — DOCUMENTED FOR TEAM/ENTERPRISE SURFACE | The teams page says there is no model picker for members or admins, no planned user/admin model choice, and no per-team model list. Each request routes to a product-managed fixed set for its surface with automatic failover. Usage analytics show the model that actually served each request, including failovers, and billing follows that serving model. | SRC-006, SRC-007 | The fixed set and surface mapping are not identified in this baseline. SRC-007 conditionally lists `Default Model, when model selection is available`; whether an individual-account surface exposes that control is an explicit ambiguity, not a generic unknown about the documented team policy. |

## Documented inconsistencies and ambiguities in official sources

These are conflicts or ambiguities inside current first-party material, not black-box observations. The baseline preserves both statements and uses the narrower operational reading without inventing an implementation.

### DOC-A-001 — Per-Bot VM wording versus one user/member computer

- `DOCUMENTED CONTRADICTION`: SRC-001 says `Each Bot runs on a persistent cloud VM`, then says all Bots use the same persistent cloud computer. SRC-005, SRC-006, SRC-008, and SRC-013 repeatedly assign one computer to a user/member, and SRC-025 says Bots share a cloud computer.
- `RESOLVING READING`: for functional and security comparison, the computer is user/member-scoped; each Bot has a separate screen, not a separate security boundary. Whether the underlying infrastructure uses processes, sessions, nested VMs, or another mechanism remains unknown.

### DOC-A-002 — Demonstration becomes a routine versus a draft skill

- `DOCUMENTED CONTRADICTION`: SRC-001 describes a demonstrated path as persisted into a routine without a rollout qualifier. SRC-004 and SRC-008 say the feature is available only when enabled, records up to ten minutes, and produces a draft skill for review and testing.
- `RESOLVING READING`: classify teach-by-demonstration as rollout-dependent and draft-skill-generating. Do not infer trusted routine creation until a current account shows the exact flow.

### DOC-A-003 — Reset “keeps its data” versus unsynced-work loss

- `DOCUMENTED AMBIGUITY`: SRC-006 summarizes Reset as recreating the computer while keeping its data. SRC-013 and SRC-016 say Reset returns to durable state and can discard recent unsaved work; SRC-030 says conversation history is separate, synced box data is durable, and unsynced data does not return.
- `RESOLVING READING`: Reset preserves the documented durable/synced layers, not every byte of recent state. Sync timing and the exact loss window remain unknown.

### DOC-A-004 — Local-execution policy labels

- `DOCUMENTED TERMINOLOGY AMBIGUITY`: SRC-005 lists policies equivalent to always require approval, always allow, and never allow, then calls the default `Ask every time`. SRC-006 uses `Never`, `Ask every time`, and `Always` for a forthcoming team ceiling.
- `RESOLVING READING`: treat the individual default as approval on every local action. UI labels and the future team ceiling require build-specific confirmation.

### DOC-A-005 — No model picker versus conditional Default Model setting

- `DOCUMENTED SURFACE AMBIGUITY`: SRC-006 explicitly denies member/admin model choice for Grok Bot team surfaces. SRC-007 lists `Default Model, when model selection is available` in agent settings.
- `RESOLVING READING`: the no-choice/fixed-set/failover policy is verified for the documented team and enterprise surface. Whether an individual or other surface currently exposes the conditional setting is unknown and requires an identified account/build.

## Feature-parity evidence map

`Reference documented` means the official documentation supports the public capability claim. It does not mean our product has selected or implemented it.

| Capability family | Reference status | Evidence IDs | Clean-room status |
|---|---|---|---|
| Persistent agent identity and role | Reference documented | GBF-001–GBF-004 | No design selected; no implementation. |
| Persistent/background execution | Reference documented; storage layers partly documented; runtime/sync limits unknown | GBF-005, GBF-010, GBF-011; DOC-A-003 | No design selected; no implementation. |
| Browser, terminal, files, connectors, GUI | Reference documented; reliability unknown | GBF-008, GBF-012, GBF-013 | No design selected; no implementation. |
| User-scoped computer and isolation | Reference documented; contractual tenant boundary incomplete | GBF-006, GBF-007, GBF-009 | Comparison input only; do not copy the security boundary by default. |
| Steering, cancellation, and recovery | Reference partial | GBF-011, GBF-015 | Semantics require black-box evidence before parity can be claimed. |
| Approvals and human takeover | Reference documented; enforcement untested | GBF-022–GBF-024 | No policy architecture selected. |
| Activity, artifacts, and evidence | Reference documented; automatic verification unknown | GBF-013, GBF-014 | Verified-completion differentiation remains a founder hypothesis. |
| Multi-Bot groups and handoffs | Reference documented; ownership internals unknown | GBF-016, GBF-017 | Later-stage capability, outside first MVP by current decisions. |
| Skills and routines | Reference documented; several rollouts unknown | GBF-018–GBF-021 | Later-stage capability, outside first MVP by current decisions. |
| Search, notifications, and mobile supervision | Reference documented; rollout-dependent | GBF-025–GBF-027 | Surface selection remains provisional. |
| Team administration | Reference documented in material part; enterprise access and several controls rollout-dependent | GBF-029 | Later-stage capability; no enterprise architecture selected. |
| Model selection and transparency | Reference documented as product-managed for team/enterprise: no member/admin picker, fixed set per surface, automatic failover, actual serving model visible in usage analytics; individual conditional control ambiguous | GBF-031; DOC-A-005 | D-007 remains a provisional project differentiator; no project routing design or provider choice selected. |
| Metering and billing | Reference documented for eligible plan paths, weekly usage, optional on-demand continuation, serving-model billing, dashboard spend, and absence of a Grok Bot-specific spend cap; project-account values unknown | GBF-028, GBF-029, GBF-031; SRC-006, SRC-008, SRC-028, SRC-034 | Exact project entitlement, allowance, price, metering units, negotiated terms, taxes, and account behavior require account readback. |
| Audit and retention | Reference partial | GBF-014, GBF-030 | Audit export, immutability, and contractual retention remain unknown. |

## Strong inferences

1. `STRONG INFERENCE`: the documented user/member-scoped shared computer likely reduces handoff friction because Bots can reuse files and sessions. The underlying facts that Bots share credentials/files and must not be used as separate security boundaries are directly documented in SRC-005, SRC-006, SRC-008, and SRC-013; only the product-tradeoff interpretation is inferential.
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
- Which models/providers are in the published fixed set, how surfaces map to that set, what triggers failover, how reliably analytics identify the serving model, and whether an individual-account build exposes SRC-007's conditional `Default Model` control. Team/member/admin non-choice and automatic failover are documented facts, not open questions.
- Complete approval interception coverage and resistance to prompt injection or malicious tools.
- Secure-secret storage, supported connections, revocation, retention, and audit behavior.
- Exact project-account entitlement, included allowance, price or negotiated terms, on-demand rates, metering units, trial credit, and region rollout; public plan paths and weekly/on-demand mechanics are documented but not account-verified.
- Whether known authentication and phone-verification failure modes in SRC-031 affect the project account.
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

As revalidated at `2026-08-22T03:07:34Z`, current official sources support a broad capability baseline for a vendor-labelled early-beta product: persistent named Bots, one shared user/member cloud computer, browser/terminal/files/connectors, background work, collaboration, skills, routines, approvals, takeover, mobile supervision, team controls, expanded plan eligibility, and product-managed model routing with automatic failover on the documented team/enterprise surface. Official-source contradictions and surface ambiguities are retained rather than normalized into false certainty.

The sources do not establish runtime reliability, complete account rollout, internal architecture, the identity of the managed model set, contractual controls beyond the cited text, or this project's entitlement/build. Zero black-box runs were performed. Those gaps remain explicit and block a runtime parity or account-availability claim.

No final architecture, MVP workflow, or customer wedge is selected by this record.
