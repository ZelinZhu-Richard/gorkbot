# ADR-E2-008 — Observability, Audit, Logging, Metering, and Typed Failure Architecture

ADR ID: `ADR-E2-008`

Status: `PROPOSED_PENDING_INDEPENDENT_ARCHITECTURE_VERIFICATION`

Candidate: `EP-ARCH-C01`

Decision class: `MODERATELY_COSTLY_WITH_STABLE_SEMANTIC_CONTRACTS`

## Context

Users and verifiers need structured task/operation/control/approval/effect/recovery/verification visibility without exposing private reasoning or confusing telemetry with truth. Failures need stable accountable layers and retry/terminal/unknown semantics. E1 measurement protocols require raw attributed inputs and enforceable finite limits, but E2 may not invent results or missing numeric ceilings.

## Decision

Propose four semantically separate C01 observability classes over a correlated identity backbone:

1. authoritative domain/operation/effect state owned by ADRs 002/003/005;
2. append-only material audit facts required for recovery, denial, approval/revocation, effect and verification history;
3. evidence records/artifacts owned by ADR-E2-007; and
4. optional lossy logs, telemetry, metrics projections and exporters.

They may share physical infrastructure later only if authority, retention, confidentiality, integrity and failure consequences remain explicit. Telemetry/logs never authorize, recover or prove completion.

Every failure is a bounded versioned record with stable semantic code, accountable layer, safe public description, protected internal reference, retryability, terminal/unknown state, operation/correlation identity, cause/effect/readback facts and next permitted action. Provider/model/tool/fixture/verifier failures remain distinguishable.

Measurement ports expose raw timestamps, counters, usage/cost, outcomes, limits, missingness, environment/workload/config identities and layer attribution. The policy gate denies dispatch when a required finite ceiling is absent or exceeded. Numeric verification-rerun, deterministic-check-repetition and correction-attempt values are not selected here; `E3-QPA-001` owns their prospective freeze.

## E1/E2 constraints and trace

- Primary ARs: `AR-OBS-001/002`, `AR-FAIL-001/002`, `AR-TST-003`, `AR-PERF-001/002`.
- Cross-cutting: `AR-DAT-001/002`, `AR-EVD-003`, `AR-MOD-003`, `AR-SEC-003/006`, `AR-PRF-001/005`.
- Domains: `D18_OBSERVABILITY_LOGGING`, `D19_ERROR_FAILURE_MODEL`, shared `D20_SECURITY_BOUNDARIES`, `D25_E1_SUITE_TESTABILITY`.

## Options considered

1. C01 semantic separation inside the integrated core with replaceable sinks.
2. C02 service telemetry/audit around IPC and workers.
3. C03 material journal plus derived telemetry/projections.
4. One undifferentiated log/event stream (rejected).

## Rationale

C01 can correlate short in-process traces while preserving semantic class boundaries. A single physical log is not assumed. C03 has replayable audit strengths and C02 component-level telemetry strengths, but importing their topology would create a hybrid. Stable semantic failures and measurement ports are architecture needs; exporter/storage choices are not.

## Rejected alternatives

Telemetry-as-authority, assistant-text failures, silent retry, unbounded output, missing-cost-as-zero and post-result metric/ceiling definition are rejected. C02/C03 placement is not adopted.

## Consequences and trade-offs

Positive: consistent user explanations; attributable errors; protocol-ready raw inputs; replaceable exporters; audit/evidence remain trustworthy.

Negative: schema/version/redaction burden; correlation across semantic classes; instrumentation overhead; integrated-core loss may temporarily remove live visibility while durable facts persist.

## Security implications

Logs/telemetry are untrusted, bounded and secret-safe. Protected entry suspends/excludes ordinary logging/capture; no raw secret or unsafe path/internal payload appears. Correlation IDs do not grant access. Audit tamper/gaps block dependent verification. This ADR explicitly participates in `E3V-006` because ordinary logging/telemetry exclusion is part of protected-entry safety.

## Recovery implications

Durable semantic audit facts survive restart; lossy telemetry may not. Recovery reports missing samples rather than reconstructing them as facts. Typed failures and exhaustion records drive retry/block/fail/reserve behavior; old logs never overwrite current state.

## Evidence and verification implications

Evidence references authoritative audit/failure/metric inputs and their completeness, not a dashboard. Verifiers can reproduce calculations from raw records and inspect ceiling denials. Explanations expose state and evidence without private chain-of-thought.

## Missing evidence and current evidence limit

No audit/failure schema, instrumentation port, redaction/capture test, provider-usage fixture, raw timing sample, metric calculation, finite ceiling value, ceiling denial, gap/tamper trial, or telemetry-loss test exists. `E3V-004/005/006/007` are unrun, so this ADR establishes no SLO, performance, cost, reliability, completeness or secret-exclusion result.

## Reversibility and migration

Exporters/dashboards are `REVERSIBLE_EARLY`. Stable audit/failure/metric schemas are `MODERATELY_COSTLY`. Migration requires version adapters, gap/redaction/integrity checks, calculation equivalence and explicit missingness; it may not promote telemetry to authority.

## Future compatibility

Explicit actor/task/workspace/operation/provider/policy scopes permit later remote aggregation or tenant isolation. No cloud telemetry backend, analytics vendor, alerting system or production SLO service is selected.

## E3 validation obligations

- `E3V-004`: provider/failure/usage semantic preservation.
- `E3V-005`: audit/evidence/telemetry separation and gap/tamper behavior.
- `E3V-006`: secret/protected-entry capture and log/telemetry exclusion.
- `E3V-007`: raw protocol inputs, calculations, missingness and finite ceiling denial.

## Handback and reopen conditions

Frozen handbacks: `E3V-004 -> ADR-E2-001/005/006/008`; `E3V-005 -> ADR-E2-002/003/005/007/008`; `E3V-006 -> ADR-E2-001/004/005/008`; `E3V-007 -> ADR-E2-002/007/008/009`. Reopen on unavoidable telemetry authority, unrepresentable required failure/measurement semantics, unenforceable mandatory limits or inability to exclude protected input from ordinary capture. Ordinary exporter/instrumentation/performance defects remain correction/evidence.

## Unresolved implementation details

Audit/log/metric physical storage; schema registry; correlation/tracing representation; redaction; exporters; UI; retention; integrity mechanism; clock; cost/usage ingestion; error codes; ceiling-policy encoding and enforcement implementation.

## Source evidence and provenance

Frozen observability/failure/security/reliability protocol contracts and release checkpoint; E2 plan; requirements `AR-OBS`, `AR-FAIL`, `AR-PERF`, E3V-004/005/006/007; C01 f15/f17/f18/f23/f25/f28/f30; comparison §§9-10, 14, 18; closure §9 and E2-004 verifier N3. External telemetry/error patterns are non-authoritative Level-B inputs only.
