# Grok Bot Black-Box Examples

This folder is intentionally evidence-first. It currently contains templates and a test matrix, not fabricated observations.

When access to Grok Bot is available, create one folder per experiment:

```text
GB-001_research_task/
├── experiment.md
├── prompt.txt
├── observations.md
├── result/
├── screenshots/
└── recording_reference.md
```

## Collection rules

- Record the date and product surface.
- Capture the initial state.
- Preserve the exact prompt.
- Distinguish visible behavior from architectural inference.
- Note what the Bot claimed and what was independently verified.
- Redact credentials and personal information before committing.
- Do not upload session cookies, browser profiles, authentication exports, or private customer data.
- Repeat important tests at least twice when practical.
- Include failures. Failures are more informative than promotional successes.

Use `EXPERIMENT_TEMPLATE.md` for each experiment and `TEST_MATRIX.md` to select coverage.
