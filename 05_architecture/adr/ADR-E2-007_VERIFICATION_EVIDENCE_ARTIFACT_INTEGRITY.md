# ADR-E2-007 — Verification, Evidence, Artifact, Provenance, and Integrity Architecture

ADR ID: `ADR-E2-007`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `FOUNDATIONAL_HIGH_COST`

Decision status and reversibility class are separate governance axes.

## Context

Engineering Preview is correct only when a reviewable candidate and evidence bundle let an independent verifier check an adequate predicate set against the exact state. Executor narrative, transcript, activity, telemetry, a digest or a passing but irrelevant check is insufficient. Evidence must survive restart, expose gaps/tamper/staleness, remain secret-safe and bind author/challenger/verifier roles.

## Decision

Propose C01's integrated evidence builder over ADR-E2-002 `AUTHORITATIVE STATE`/material history plus stable artifact references, followed by a separate least-privilege verifier process/context/workspace. A validated evidence bundle and immutable verification run are `AUTHORITATIVE STATE` evidence subtypes. Manifests and review views rebuilt from them are `DERIVED PROJECTION`; transient verifier buffers are `EPHEMERAL WORKING CONTEXT`; compacted result summaries are `LOSSY SUMMARY` and never substitute for the underlying evidence.

The evidence builder creates a versioned outcome-profile bundle binding task/attempt/actor, governing inputs, plan/predicate coverage, repository/base/workspace/candidate identity, changed-file inventory and diff/package, operations, exact commands/results/repetitions, approvals/effects/readbacks, routes/models/tools/configs, artifacts/provenance/retention, errors/recovery, limitations and disposition. Large outputs use bounded stable references. Raw protected values and forbidden/private material are excluded.

The verifier receives a bounded immutable input manifest for the exact candidate. It has no shared mutable author state, uses durable evidence and fresh readback, checks predicate adequacy before pass credit, runs deterministic oracles first and records an immutable verification run. Verifier infrastructure error is distinct from `CHANGES_REQUIRED`, `BLOCKED`, `INCONCLUSIVE` or pass. Any material candidate/evidence mutation invalidates the current result.

Evidence integrity has version, provenance, completeness, gap/tamper and stale state. A digest is an identity/integrity input, not authorization, confidentiality, correctness or proof that missing work occurred. Telemetry is never the evidence authority.

## E1/E2 constraints and trace

- Primary ARs: `AR-COR-004/005/006`, `AR-EVD-001/002/003`, `AR-VER-001/002/003`, `AR-TST-002`, `AR-PRF-005`.
- Cross-cutting: `AR-DAT-001/002`, `AR-CTX-001/002`, `AR-SEC-005`, `AR-OBS-001`.
- Domains: `D16_VERIFICATION_ARCHITECTURE`, `D17_EVIDENCE_ARTIFACT_SYSTEM`, shared `D05_CANONICAL_TASK_CONVERSATION_EVIDENCE_MODEL` and `D25_E1_SUITE_TESTABILITY`.

## Options considered

1. C01 integrated evidence manifests plus separate verifier process/context/workspace.
2. C02 service-owned evidence manifests and independent worker/verifier paths.
3. C03 journal-position-bound evidence projections and verifier replay.

## Rationale

C01 provides short access to current authority and material history while still requiring a physically/logically separate verifier path. C03's replay advantage and C02's component substitution are preserved, but neither justifies importing its topology. The hard independence and evidence contracts are identical across candidates.

## Rejected alternatives

Executor self-verification, same running session, transcript-only review, telemetry authority, self-hash-only proof, mutable verdicts and weak author predicate lists are rejected. C02/C03 evidence placement is not adopted because their authority shape is not proposed.

## Consequences and trade-offs

Positive: exact-state completion; strong false-completion barrier; reconstructable bundles; independent read access; explicit stale/tamper/error states.

Negative: evidence retention and large-output handling add overhead; separate verifier setup is nontrivial; integrated builder bugs can affect bundle construction; artifact/evidence schemas become foundational.

## Security implications

Verifier capability is least privilege and does not inherit author approvals/credentials. Evidence is bounded, source-labeled, redacted and validated before consumption. Untrusted output cannot forge approval, readback or a pass. Secret/private/clean-room and forbidden-artifact scans are mandatory and inconclusive results block.

## Recovery implications

Candidate and verification runs are immutable identities. Recovery rebuilds derived bundle views from retained authority while preserving any gap/tamper fact. A stale or partially written bundle cannot pass; verifier error may be rerun only under the prospectively frozen finite policy.

## Evidence and verification implications

This ADR defines the implication: every final completion claim needs adequate predicate coverage and a passed independent run bound to the current candidate. Historical passes remain historical when state changes. Deterministic authoritative readback outranks conflicting model judgment for the same predicate.

## Missing evidence and current evidence limit

No evidence-bundle schema, artifact carrier, integrity mechanism, predicate registry, stale-pass invalidator, independent-verifier implementation, tamper/gap trial, replay result, or large-output measurement exists. `E3V-005/007` are unrun; consequently no implementation completion claim can yet satisfy this proposed verification path.

## Reversibility and migration

Artifact carriers and individual validators are `MODERATELY_COSTLY`; evidence identity/profile, exact-candidate binding and independence semantics are `FOUNDATIONAL_HIGH_COST`. Migration requires manifest translation, old-bundle readability, source/provenance/integrity preservation, independently checked equivalence and fresh verification of migrated candidates.

## Future compatibility

Actor, verifier, artifact, policy and candidate scopes are explicit, enabling later remote verifiers or multiple agents without granting cross-task/tenant access. No remote verification service or multi-tenant evidence store is implemented now.

## E3 validation obligations

- `E3V-001`: recovery retains authoritative evidence inputs and certainty.
- `E3V-002`: process containment claims have independent readback/evidence.
- `E3V-004`: provider semantic preservation has raw-linked, exact-route evidence.
- `E3V-005`: stale/gap/tamper/adequacy/verifier-error and exact-revision behavior.
- `E3V-006`: security/capture exclusions and denials are independently evidenced without raw secrets.
- `E3V-007`: evidence/large-output measurement inputs and limit enforcement.

## Handback and reopen conditions

Canonical handbacks: `E3V-001 -> ADR-E2-002/003/004/005/007/008/009`; `E3V-002 -> ADR-E2-003/004/007`; `E3V-004 -> ADR-E2-001/004/005/006/007/008/009`; `E3V-005 -> ADR-E2-002/003/004/005/006/007/008`; `E3V-006 -> ADR-E2-001/004/005/007/008/009`; `E3V-007 -> ADR-E2-001/002/007/008/009`. Reopen on unavoidable executor-self-report dependence, stale-pass acceptance, telemetry authority, nondeterministic canonical evidence, unavoidable required-evidence loss or structurally unrepresentable protocol inputs. Validator/manifest/tool defects remain correction if the boundary is feasible.

## Unresolved implementation details

Bundle serialization/schema tooling; artifact carrier/content identity; retention/GC; integrity/gap mechanism; verifier process/tooling; sandbox/workspace; deterministic rerun harness; large-output storage; signing/attestation; redaction and provenance scanners.

## Source evidence and provenance

Frozen correctness/evidence/verification contracts, contribution workflow, suite and release checkpoint; E2 plan and requirements `AR-EVD`, `AR-VER`, E3V-005/007; C01 f06/f08/f14-f17/f23/f25/f28/f30; comparison §§7, 9-10, 14, 18; closure §9. Audit evidence-manifest patterns are test/design inputs only.
