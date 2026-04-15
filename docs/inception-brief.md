# SoberFuture — Inception Brief

**Date:** 2026-04-15
**Status:** Active

---

## Product Summary

SoberFuture.me is an AI-powered interactive recovery journal and clinician support platform. It helps people in addiction recovery track their journey through structured journaling, AI-assisted reflection, and longitudinal pattern detection — while giving clinicians a safe, auditable workspace to review client progress.

---

## Goals

1. Provide a private, safe journaling experience for people in recovery
2. Surface meaningful patterns and insights to support recovery (not replace clinical care)
3. Give clinicians a structured, auditable view of client progress
4. Operate with full transparency, human oversight, and privacy-first defaults
5. Build a scalable, maintainable platform ready for real users

---

## Constraints

- Health-adjacent product: all user content treated as sensitive
- No diagnosis, no medical advice, no claims of being a therapist
- No training on customer data without explicit opt-in
- Human review required for high-risk AI outputs
- HIPAA-adjacent data handling practices required from day one
- Least-privilege access everywhere
- Audit trail for all agent actions

---

## Risks (summary — see risk-register.md)

- Privacy breach of recovery journal content
- AI output causing harm (unsupported clinical guidance)
- Credential exposure (Slack tokens already exposed — rotation required)
- AWS cost overrun from untagged/unmonitored resources
- Scope creep delaying core journaling MVP

---

## Assumptions

- See assumptions.md

---

## Milestone Map

- See milestones.md

---

## Platform Surfaces

| Surface | Description |
|---------|-------------|
| apps/web | Public marketing site + authenticated client journal |
| apps/mobile | iOS + Android journaling app (Expo React Native) |
| apps/clinician | Clinician/admin workspace |
| services/api | Core backend API |
| services/agent-orchestrator | AI agent coordination |
| services/worker | Async job processing |
| services/notifications | Push/email/Slack notifications |
| services/audit | Audit event logging |
| services/mcp-* | MCP server suite (7 servers) |
