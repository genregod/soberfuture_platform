# Tech steering — SoberFuture

## Confirmed stack (per ADRs)

| Layer | Choice | Notes |
|-------|--------|-------|
| Mobile | Expo React Native (SDK 54) | Expo Router, file-based routing |
| Web | Next.js 15, App Router | TypeScript, Tailwind v4 |
| Backend API | FastAPI (Python 3.12) | uv, pydantic v2, async |
| MCP servers | FastAPI + mcp Python SDK | Hosted on AWS EC2 |
| Database | PostgreSQL 16 | RDS in prod, Docker locally |
| ORM | SQLAlchemy 2 + Alembic | Async sessions |
| Cache/Queue | Redis 7 | BullMQ for jobs |
| Auth | AWS Cognito | JWT, MFA, PKCE for mobile |
| Secrets | AWS Secrets Manager | Never in git |
| IaC | Terraform | State in S3, DynamoDB lock |
| CI/CD | GitHub Actions | Branch protection on main |
| Container runtime | ECS/Fargate | Dev: EC2 t3.small |
| Edge/Static | S3 + CloudFront | |
| Observability | CloudWatch + structured JSON logs | |

## Code standards
- TypeScript strict mode everywhere in JS/TS
- Python: ruff lint, pyright typecheck, pydantic models for all I/O
- No `any` in TypeScript without explicit justification comment
- All API endpoints documented in OpenAPI spec before implementation
- All DB changes via Alembic migrations with rollback notes
- Mobile: 44px minimum tap targets, safe-area insets, portrait-primary
