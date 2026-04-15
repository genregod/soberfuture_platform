# SoberFuture

AI-powered interactive recovery journal and clinician support platform.

## Project Structure

```
apps/
  web/          Next.js web app (marketing + client journal)
  mobile/       Expo React Native (iOS + Android)
  clinician/    Clinician/admin workspace
services/
  api/          Core backend API (FastAPI)
  agent-orchestrator/  AI agent coordination
  worker/       Async job processing
  notifications/ Push/email/Slack notifications
  audit/        Audit event logging
  mcp-*/        MCP server suite
packages/
  ui/           Shared component library
  design-tokens/ Design system tokens
  config/       Shared configuration
  schemas/      Shared data schemas
  sdk/          Client SDK
  prompts/      Prompt registry
  evals/        Evaluation suite
infra/
  terraform/    Infrastructure as code
  environments/ Environment configs
ml/
  datasets/     Evaluation datasets
  evaluations/  Eval results
  prompts/      Prompt versions
  policies/     Safety policies
docs/
  adr/          Architecture Decision Records
  runbooks/     Operational runbooks
  compliance/   Compliance docs
SoberFuture/    Active MCP server implementations (session 1 work)
```

## Local Development

### Prerequisites
- Python 3.11+ with `uv`
- Node.js 20+ with `pnpm`
- Docker

### MCP Servers (Python)

```bash
cd SoberFuture/services/mcp-slack
uv run app.py
```

### Environment Setup

```bash
cp SoberFuture/.env.example SoberFuture/.env.local
# Fill in values — never commit .env.local
```

## Key Docs

- [Inception Brief](docs/inception-brief.md)
- [Architecture ADRs](docs/adr/)
- [Task Ledger](docs/task-ledger.md)
- [Progress Log](docs/progress.md)
- [Approval Queue](docs/approval-queue.md)
- [Risk Register](docs/risk-register.md)
- [Long Term Memory](SoberFuture/LongTermMemory.md)

## Security

- Never commit secrets or credentials
- See [docs/compliance/](docs/compliance/) for data handling policies
- Credential rotation required — see approval-queue.md APPROVAL-001

## Status

Active development. See [docs/milestones.md](docs/milestones.md) for roadmap.
