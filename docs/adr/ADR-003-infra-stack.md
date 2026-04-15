# ADR-003: Infrastructure Stack

**Date:** 2026-04-15
**Status:** Accepted
**Deciders:** Anthony Navarro, Arnie (Build Bot)

## Context

Need to select IaC tooling and AWS runtime for SoberFuture.me.

## Options

| Option | Pros | Cons |
|--------|------|------|
| Terraform | Multi-cloud, large community, mature state management | HCL learning curve |
| AWS CDK | TypeScript-native, AWS-first | AWS lock-in, CDK version churn |
| CloudFormation | Native AWS, no extra tooling | Verbose, slow feedback loop |

## Decision

**Terraform** for IaC. **ECS/Fargate** for container runtime.

## Rationale

- Terraform has the broadest community support and most mature state management
- ECS/Fargate is simpler to operate than EKS for a small team at this stage
- Fargate eliminates node management overhead
- Can migrate to EKS later if scale demands it (ADR to be written at that point)

## Environments

| Env | Purpose |
|-----|---------|
| local | Docker Compose, no AWS |
| dev | AWS DEV account, minimal resources, cost-controlled |
| staging | Pre-prod, mirrors prod topology |
| prod | Production — requires explicit approval for every change |

## Consequences

- Terraform state must be stored in S3 with DynamoDB locking
- All resources tagged: Project=SoberFuture, Env=dev|staging|prod
- Billing alerts required at $50/month (dev) and $200/month (staging)
