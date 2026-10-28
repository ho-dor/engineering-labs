---
name: pre-pr-quality-gate
description: Runs pre-push checks for Sabbatical repos — pytest, ruff, diff sanity, eval CI if agent code changed.
---

# Pre-PR quality gate

1. `uv run pytest` (or repo equivalent)
2. `uv run ruff check .` if configured
3. Scan diff for secrets and debug prints
4. If `agent/` or `evals/` changed, run eval job or `make eval`
5. Conventional commit message ready
