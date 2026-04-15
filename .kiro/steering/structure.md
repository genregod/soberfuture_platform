# Structure steering — SoberFuture

## Monorepo layout

```
/
  apps/
    web/          Next.js — marketing + PWA journal
    mobile/       Expo React Native — iOS + Android
    clinician/    Next.js — clinician/admin portal
  services/
    api/          FastAPI core backend
    agent-orchestrator/  AI agent coordination
    worker/       Async job processing (Celery/Redis)
    notifications/ Push + email + Slack
    audit/        Audit event logging
    mcp-gateway/  MCP gateway — routes to all MCP servers
    mcp-slack/    Slack bot (Socket Mode)
    mcp-github/   GitHub context
    mcp-browser/  Playwright headless browser
    mcp-aws-docs/ AWS docs fetcher
    mcp-repo-context/  Codebase search
    mcp-package-docs/  PyPI + npm metadata
    mcp-adr/      ADR registry reader
    mcp-filesystem/  Repo-scoped filesystem MCP
    mcp-openapi/  OpenAPI contract grounding
    mcp-location/ Geo resources (AWS Location)
    mcp-meetings/ Meeting discovery (AA/NA/SMART)
    mcp-bedrock/  Multimodal extraction (Bedrock)
  packages/
    ui/           Shared React component library
    design-tokens/ Design system tokens
    config/       Shared configuration
    schemas/      Shared Pydantic + Zod schemas
    sdk/          Client SDK (TypeScript)
    prompts/      Prompt registry
    evals/        Evaluation suite
  infra/
    terraform/    IaC — all environments
    environments/ Per-env config
  ml/
    datasets/     Evaluation datasets
    evaluations/  Eval results
    prompts/      Prompt versions
    policies/     Safety policies
  docs/
    adr/          Architecture Decision Records
    api/          OpenAPI specs
    mcp/          MCP manifests + registry
    runbooks/     Operational runbooks
    compliance/   Compliance docs
  .kiro/
    settings/     mcp.json, lsp.json
    steering/     product.md, tech.md, structure.md
    agents/       Custom agent definitions
```

## Key rules
- `packages/` are shared — no app-specific code there
- `services/` are independently deployable
- `infra/` is the only place AWS resources are defined
- Secrets never in source — always env vars or AWS Secrets Manager
