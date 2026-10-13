# Security Policy

This repository is public. Treat every committed file as permanently public, even if it is later deleted.

## Never commit

- API keys or access tokens
- Passwords, passkeys, cookies, session exports, or one-time codes
- Private customer data
- Personally identifiable information without explicit authorization
- Unredacted screenshots containing credentials or sensitive records
- Private model transcripts that contain confidential material
- Cloud service account files
- Production database dumps

Use `.env.example` for variable names only. Store actual secrets in a proper secret manager or an untracked local environment file.

## Agent rules

AI agents may not weaken authentication, authorization, tenant isolation, approval gates, logging, or secret handling merely to make a demo work.

Any change involving the following requires independent review:

- authentication
- authorization
- organization or tenant boundaries
- credentials
- billing
- destructive actions
- production deployment
- computer execution
- browser session handling
- prompt injection defenses

## Reporting a vulnerability

Until a private disclosure channel exists, do not publish exploit details in a public issue. Contact the repository owner privately and include:

- affected component
- reproduction conditions
- expected and observed behavior
- likely impact
- suggested mitigation, if known

A formal security contact and disclosure policy must be created before public alpha.
