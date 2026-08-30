# ADR-E2-004 — Workspace, Filesystem/Process Execution, Isolation Tier, Git, and Local/Remote Execution Seam

ADR ID: `ADR-E2-004`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `MODERATELY_COSTLY_WITH_FOUNDATIONAL_SECURITY_CONTRACT`

## Context

Engineering work occurs against real repositories containing user-owned and untrusted material. Isolation must precede potentially mutating reproduction; filesystem, terminal, package, process and Git behavior must be bounded; stop/force/fence semantics must be truthful; the review package must contain only task-owned work. Future remote execution is compatibility scope. Concrete workspace, process and isolation technologies are unselected.

## Decision

Propose C01's core-owned workspace/filesystem/Git broker and separate owned execution supervisor port.

- Admission pins repository identity, base, topology, all applicable repository-condition rows, instructions and tracked/untracked/ignored/generated/nested/shared-ref state before task work.
- A task-identified isolated workspace or verified equivalent is bound before potentially mutating reproduction, dependency/build/test execution or edits.
- Filesystem access uses normalized admitted roots, effective object identity, link/topology checks, ownership and bounds at access, mutation and cleanup.
- The supervisor owns declared process/descendant identity, working directory, environment, time/output/resource/network/secret scopes, cancel/timeout/force-or-fence and result/effect readback.
- Git uses a sanitized typed adapter that applies all 30 frozen Git/effect classifications. Hooks, helpers, filters, signers, submodule/LFS handlers and transports are separate executable/effectful capabilities.
- The minimum support claim is the technology-neutral Tier 2 semantic isolation floor recorded by E2. No container, VM, worktree or process mechanism is selected or credited without E3 evidence.
- Local and future remote executors implement one versioned serializable execution contract while declaring capability/security/support differences. v0.1 implements only the authorized local path.

## E1/E2 constraints and trace

- Primary ARs: `AR-WSP-001..005`, `AR-EXE-002..004`, `AR-GIT-001/002`, `AR-TST-001`.
- Cross-cutting: `AR-EXE-001`, `AR-DUR-003/004/006`, `AR-SEC-002/004`, `AR-FUT-001`.
- Domains: `D07_FILESYSTEM_WORKSPACE_ABSTRACTION`, `D08_EXECUTION_PROCESS_CONTROL`, `D09_ISOLATION_SANDBOXING`, `D10_GIT_INTEGRATION`, `D22_FUTURE_REMOTE_EXECUTION`, shared `D25_E1_SUITE_TESTABILITY`.

## Options considered

1. C01 integrated broker plus owned child-process supervisor and remote-compatible port.
2. C02 replaceable leased/fenced workers behind a local service.
3. C03 command/event execution adapters driven from journal authority.

## Rationale

C01 isolates untrusted execution outside the trusted core while avoiding mandatory service/IPC/lease topology. The verified comparison gives no candidate a demonstrated isolation advantage; all share the same `AR-EXE-003` residual. C02's worker replacement and C03's serializable commands are preserved as future advantages, not imported.

## Rejected alternatives

C02 service/workers are not selected because remote/replaceable workers are not current scope. C03 command/event execution authority is not selected because journal/reducer authority is not part of C01. A specific isolation technology is rejected as premature until supported host/process classes are validated.

## Consequences and trade-offs

Positive: clear trust boundary around untrusted children; task/user-state separation; all Git effects classified; adapters remain replaceable; remote seam is explicit.

Negative: platform-specific path/process behavior remains a major E3/E4 burden; Tier 2 may exclude hosts/classes; force termination is not universal; broker/supervisor conformance and documentation are significant.

## Security implications

The broker/supervisor, not model memory, enforces paths, process identity, environment, egress, credentials, output and cleanup. Allowed-root does not imply ownership or secret permission. Untrusted content/scripts/hooks cannot grant capability. Missing effective-target, containment, authority or readback evidence denies or blocks.

## Recovery implications

Restart rereads repository/workspace topology, object identities, process survivors, Git state and canaries; stale bindings are invalid. Process termination and authority fencing remain distinct. Partial filesystem writes preserve actual bytes and yield partial/failed/blocked state; no core transaction rolls them back fictionally.

## Evidence and verification implications

Evidence must include initial/final inventories, workspace bind order, exact operations, process tree, limits, cancellation/fence endpoints, output references, Git refs/index/worktree, all applicable matrix dispositions and outside/unrelated canaries. Test seams must cover 16 repository conditions, 30 Git/effect rows and relevant compositions.

## Missing evidence and current evidence limit

No workspace adapter, process API, isolation mechanism, declared-host support matrix, process-tree containment result, Git conformance result, package trial, or remote seam implementation exists. `E3V-001/002/003/006` are unrun, including residual descendant containment under `AR-EXE-003`; therefore no host, isolation tier, cleanup path, Git mutation class, or remote execution path is qualified.

## Reversibility and migration

Conforming adapters are `MODERATELY_COSTLY`. The security/support-class contract is foundational. Local-to-remote migration preserves task/workspace/operation identity, capability declaration, owner epoch/fence, artifact/effect correlation and readback; it requires a conformance/security matrix and no downgrade of the isolation floor.

## Future compatibility

The execution port is serializable and replaces local placement without making cloud required. Future workers may use separate processes/hosts, but queues, leases, cloud credentials and production isolation are not implemented or selected.

## E3 validation obligations

- `E3V-001`: partial writes, operation/effect recovery at workspace boundaries.
- `E3V-002`: descendant accounting, pause/stop/force-or-fence on declared hosts.
- `E3V-003`: repository/workspace/Git/local package support matrix and contributor setup.
- `E3V-006`: path/process/network/secret/capability enforcement and protected-entry process/terminal surfaces.

## Handback and reopen conditions

Frozen handbacks: `E3V-001 -> ADR-E2-002/003/004/005`; `E3V-002 -> ADR-E2-003/004`; `E3V-003 -> ADR-E2-001/004/009`; `E3V-006 -> ADR-E2-001/004/005/008`. Reopen on structural root/user-state escape, unavoidable stale productive/effect authority, undeclared mandatory service, or inability to expose required deterministic seams for a required class. Narrow unsupported optional classes before architecture reopening.

## Unresolved implementation details

Workspace mechanism; process API; isolation technology; supported OS/filesystems/repository classes; descriptor/path primitives; network enforcement; resource controls; Git library/CLI strategy; hook/helper suppression; remote adapter; cleanup and package mechanisms.

## Source evidence and provenance

Frozen repository/Git/terminal/security contracts and evaluation matrices; E2 plan; requirements `AR-WSP`, `AR-EXE`, `AR-GIT` and E3V-002/003/006; C01 f04/f05/f09-f11/f18-f20/f23/f25/f28/f30; comparison §§6, 8, 11-14, 18; closure §§6, 9-10. External sandbox/provider patterns are Level-B comparison inputs only.
