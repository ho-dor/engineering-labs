---
name: production-agent-code
description: Implements LangGraph agents, tools, and workers with production patterns — Pydantic schemas, timeouts, correlation IDs, structured errors.
---

# Production agent code

- Tools: JSON schema + validation; idempotent where possible; timeouts.
- Graph: max steps; explicit state schema; log `run_id` on each node.
- Workers: failures visible in DB/job status; no silent swallow.
- Tests for tool happy path + one failure path.
