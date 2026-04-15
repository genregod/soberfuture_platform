# ADR-002: Application Stack

**Date:** 2026-04-15
**Status:** Accepted (candidates confirmed, lock pending final validation)
**Deciders:** Anthony Navarro, Arnie (Build Bot)

## Context

Need to select the technology stack for web, mobile, and backend surfaces.

## Decisions

### Web App
**Next.js (React)** — SSR/SSG support, strong ecosystem, Vercel/Amplify deploy compatibility, accessibility tooling, TypeScript-first.

### Mobile App
**Expo React Native** — Cross-platform iOS + Android from single codebase, shared component logic with web possible, strong community, OTA updates.

### Backend API
**FastAPI (Python)** — Async, type-annotated, OpenAPI auto-generation, strong ML/AI library ecosystem. TypeScript service layer for BFF/gateway where justified.

### Database
**PostgreSQL** — Battle-tested, JSONB for flexible schema, strong audit/compliance tooling, RDS-compatible.

### Cache / Queue
**Redis** — Session cache, job queue (BullMQ or Celery), pub/sub for real-time features.

### Auth
**AWS Cognito** — Managed, HIPAA-eligible, integrates with IAM, supports MFA. Evaluate Auth0 as alternative if Cognito UX proves limiting.

## Consequences

- Python and TypeScript both present — requires clear service boundary discipline
- Expo adds React Native complexity but avoids maintaining two native codebases
- FastAPI + PostgreSQL is a well-understood stack for health-adjacent products
