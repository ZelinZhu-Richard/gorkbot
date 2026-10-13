# Existing Code Intake

No reusable application code has been identified in this repository yet.

When adding prior code, preserve it under a dated subdirectory and include an inventory:

```yaml
snapshot_name:
source_repository:
source_commit:
license:
created_by:
last_updated:
languages:
frameworks:
known_secrets_removed:
tests_present:
known_issues:
reason_it_may_be_reusable:
```

Before reuse, review:

- license and ownership
- secret history
- dependency age
- architecture compatibility
- test quality
- security posture
- whether it solves a current requirement

Do not force existing code into the architecture merely because it already exists.
