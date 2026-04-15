# ADR-004: Agent Architecture

**Date:** 2026-04-15
**Status:** Accepted
**Deciders:** Anthony Navarro, Arnie (Build Bot)

## Context

SoberFuture.me requires AI agents for journaling support, pattern extraction, clinician summaries, and risk signal detection. Need to define the agent architecture.

## Decision

**Layered agent architecture with strict policy enforcement:**

```
User Input
    ↓
Policy/Safety Layer (rules, prohibited behaviors, escalation triggers)
    ↓
Foundation Model Layer (grounded generation, retrieval-augmented)
    ↓
Evaluation Layer (hallucination check, tone, faithfulness, safety)
    ↓
Human Review Layer (clinician review for high-risk outputs)
    ↓
Output
```

## Agent Services

| Service | Role |
|---------|------|
| agent-orchestrator | Coordinates agent tasks, manages context, enforces policy |
| worker | Async processing of journal analysis, pattern extraction |
| MCP servers | Tool access for agents (GitHub, Slack, browser, docs, repo) |

## Prohibited Agent Behaviors

- Diagnosis
- Claims of being a therapist or sponsor
- Unsupported medical advice
- Autonomous crisis intervention without approved escalation
- Opaque risk scoring without explanation and audit trail

## Retrieval Strategy

- Approved materials only (curated recovery resources)
- No retrieval from open web without explicit approval
- All retrieved context logged for audit

## Consequences

- Every agent action must produce an audit event
- High-risk outputs must be flagged for human review before delivery
- Prompt versions must be tracked in prompt registry
