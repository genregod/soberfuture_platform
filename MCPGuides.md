Design MCP servers as first-class internal products.

Each MCP server must include:
- purpose
- scope
- allowed actions
- forbidden actions
- auth model
- least-privilege permissions
- input/output schema
- manifest
- health endpoint
- test suite
- runbook
- example prompts
- failure modes
- audit event schema

Maintain a central registry file that records:
- server name
- version
- owner
- capabilities
- auth requirements
- environment bindings
- status
- last validation date

A new MCP server cannot self-register until:
- schema validates
- tests pass
- security checks pass
- docs exist
- approval is recorded
