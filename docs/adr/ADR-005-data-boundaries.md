# ADR-005: Data Boundaries

**Date:** 2026-04-15
**Status:** Accepted
**Deciders:** Anthony Navarro, Arnie (Build Bot)

## Context

SoberFuture.me handles sensitive addiction recovery data. Need strict data boundary definitions.

## Decision

**Three-tier data separation:**

| Tier | Contents | Access | Retention |
|------|---------|--------|-----------|
| Operational | User journals, clinician notes, session data | RBAC, encrypted at rest + in transit | Per user consent + legal minimum |
| Analytics | Aggregated, de-identified usage metrics | Internal analytics team only | 2 years |
| Research/Evaluation | De-identified, consented research datasets | Explicit opt-in required | Per research protocol |

## Rules

1. Customer data is NOT training data by default
2. De-identification pipeline required before any secondary use
3. PII/PHI never enters analytics or research tier without de-identification
4. Deletion requests must cascade across all tiers
5. Access control logs required for all operational data access
6. No cross-tier data flow without explicit approval and audit record

## Encryption

- At rest: AES-256 (RDS encryption, S3 SSE)
- In transit: TLS 1.2+ everywhere
- Key management: AWS KMS

## Audit

- All agent actions logged to audit service
- All data access logged
- Logs retained minimum 1 year
- Logs immutable (append-only)

## Consequences

- Requires de-identification pipeline before ML work begins
- Analytics dashboards must use aggregated tier only
- Research use requires separate consent flow
