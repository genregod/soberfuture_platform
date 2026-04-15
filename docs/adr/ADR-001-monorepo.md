# ADR-001: Monorepo Strategy

**Date:** 2026-04-15
**Status:** Accepted
**Deciders:** Anthony Navarro, Arnie (Build Bot)

## Context

SoberFuture.me requires coordinated development across web app, mobile app, clinician workspace, backend services, MCP servers, shared packages, infra, and ML. We need a repo strategy that supports shared types, consistent tooling, and clear boundaries.

## Options Considered

| Option | Pros | Cons |
|--------|------|------|
| Monorepo | Shared types/schemas, atomic commits, single CI, easier refactoring | Larger clone, requires workspace tooling discipline |
| Polyrepo | Independent deploys, smaller repos | Cross-repo type drift, harder to refactor, more CI overhead |
| Hybrid | Some sharing | Complexity without full benefit of either |

## Decision

**Monorepo** with clear app/service/package boundaries.

## Rationale

- Shared schemas and types are critical for a health-adjacent product (data contracts must be consistent)
- Single CI pipeline simplifies security scanning and compliance checks
- Atomic commits across app + service + package changes reduce integration bugs
- Team is small — monorepo overhead is manageable

## Layout

```
apps/web, mobile, clinician
services/api, agent-orchestrator, worker, notifications, audit, mcp-*/
packages/ui, design-tokens, config, schemas, sdk, prompts, evals
infra/terraform, environments
ml/datasets, evaluations, prompts, policies
docs/adr, runbooks, diagrams, compliance
.github/workflows
```

## Consequences

- Requires workspace tooling (pnpm workspaces or Turborepo for JS, uv workspaces for Python)
- CODEOWNERS required to enforce ownership boundaries
- CI must support selective builds (only rebuild what changed)
