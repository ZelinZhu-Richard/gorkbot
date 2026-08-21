# Risk Register

| ID | Risk | Likelihood | Impact | Early mitigation | Owner |
|---|---|---:|---:|---|---|
| R-001 | Building a broad platform before validating a workflow | High | Critical | Stage 1 gate and strict MVP non-goals | Founder |
| R-002 | False completion damages trust | High | Critical | Completion predicates, external checks, verifier path | Runtime lead |
| R-003 | Prompt injection causes unauthorized action | High | Critical | least privilege, content trust labels, hard approvals, sandboxing | Security lead |
| R-004 | Cross-tenant or cross-agent data leakage | Medium | Critical | explicit scopes, isolation tests, audit | Security lead |
| R-005 | Model cost makes unit economics unworkable | High | High | metering, routing benchmark, per-task budgets | Product and infra |
| R-006 | Browser and GUI automation is too brittle | High | High | structured tools first, hybrid control, recovery benchmarks | Runtime lead |
| R-007 | Multi-model coordination adds latency and errors | High | High | compare against single-model baseline | Evaluation lead |
| R-008 | Consumer subscriptions are mistaken for production API access | Medium | High | account-level provider verification | Founder |
| R-009 | Credential handling exposes secrets to models or logs | Medium | Critical | secret vault, scoped injection, human takeover | Security lead |
| R-010 | Public repository receives sensitive data | Medium | High | security policy, redaction, private storage plan | Founder |
| R-011 | Product positioning depends on another company's brand | Medium | High | distinct name, independent wedge, clean-room policy | Founder |
| R-012 | Investor demo is theatrical but unreproducible | High | High | stable task, repeated runs, visible verification | Product lead |
| R-013 | Architecture becomes too complex for a small team | High | High | managed services, vertical slices, ADRs, no premature scale | Architect |
| R-014 | Provider changes break core behavior | High | Medium | adapters, version pinning, regression suite, fallbacks | Runtime lead |
| R-015 | Memory stores stale or poisoned facts | Medium | High | provenance, source reopening, correction and expiration | Runtime lead |
