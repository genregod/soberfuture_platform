# SoberFuture — Assumptions Log

**Date:** 2026-04-15

| ID | Assumption | Confidence | Notes |
|----|-----------|-----------|-------|
| A-001 | Target deployment region is us-east-1 | High | Confirmed from AWS identity check |
| A-002 | Monorepo is the right structure | High | Confirmed by MasterOrchestrator.md |
| A-003 | GitHub Actions is the CI/CD platform | High | Confirmed by MasterOrchestrator.md |
| A-004 | Slack workspace is arnieai.slack.com | High | Confirmed from LongTermMemory + SlackAppStartingConfig |
| A-005 | Python (uv) for MCP servers and backend services | High | Confirmed by existing scaffolding |
| A-006 | Next.js for web app | Medium | Candidate — needs ADR lock |
| A-007 | Expo React Native for mobile | Medium | Candidate — needs ADR lock |
| A-008 | PostgreSQL as primary database | Medium | Candidate — needs ADR lock |
| A-009 | Terraform for IaC | Medium | Preferred — needs ADR lock |
| A-010 | ECS/Fargate for container runtime | Medium | Candidate — needs ADR lock |
| A-011 | No existing GitHub repo for SoberFuture | High | Not confirmed — needs verification |
| A-012 | GITHUB_TOKEN not yet configured | High | Confirmed from LongTermMemory |
