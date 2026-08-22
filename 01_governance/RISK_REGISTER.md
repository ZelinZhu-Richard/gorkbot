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
| R-008 | Consumer subscriptions or public API catalogs are mistaken for funded production API access | High | High | separate product and API records; account model listing or minimal authorized call; record quotas and billing | Founder |
| R-009 | Credential handling exposes secrets to models or logs | Medium | Critical | secret vault, scoped injection, human takeover | Security lead |
| R-010 | Public repository receives sensitive data | Medium | High | security policy, redaction, private storage plan | Founder |
| R-011 | Product positioning depends on another company's brand | Medium | High | distinct name, independent wedge, clean-room policy | Founder |
| R-012 | Investor demo is theatrical but unreproducible | High | High | stable task, repeated runs, visible verification | Product lead |
| R-013 | Architecture becomes too complex for a small team | High | High | managed services, vertical slices, ADRs, no premature scale | Architect |
| R-014 | Provider changes break core behavior | High | Medium | adapters, version pinning, regression suite, fallbacks | Runtime lead |
| R-015 | Memory stores stale or poisoned facts | Medium | High | provenance, source reopening, correction and expiration | Runtime lead |
| R-016 | Official Grok Bot documentation is mistaken for reproduced account behavior or reliability | High | High | record build plan region and rollout; run repeated black-box tests; keep documentation and observation labels separate | Research lead |
| R-017 | Moving model aliases, served versions, and prices invalidate benchmark comparisons | High | High | record exact ID returned version configuration price and run date; pin snapshots where available; rerun drifted blocks | Evaluation lead |
| R-018 | Claude Fable 5 classifier false positives, documented 30-day retention requirement, or regulatory/service suspension disrupt benchmark consistency or conflict with data policy | Medium | High | use scrubbed fixtures; test refusal and opt-in fallback handling; distinguish policy refusal from provider suspension; confirm workspace retention before any sensitive use; keep another provider/family candidate available during evaluation | Security and evaluation leads |
| R-019 | Treating the reference product's shared user computer as a default design leaks credentials or files across agents | Medium | Critical | preserve it as a documented comparison point only; threat-model agent and credential scopes before architecture selection | Security lead |
| R-020 | DeepSeek's documented PRC processing/storage, possible training use with opt-out, no fixed API-specific retention commitment, and PRC governing law may be incompatible with customer data or production policy | High | Critical | prohibit sensitive and customer fixtures; obtain written API-specific data-processing, retention, training, and jurisdiction terms; require founder/legal/security approval before production suitability can advance from UNKNOWN | Founder and security lead |
