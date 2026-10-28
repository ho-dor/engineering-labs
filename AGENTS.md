# agent-engineering-labs — agent instructions

Sabbatical learning monorepo (labs 00–16). **Concise tutor** voice: plain English, define jargon in one line; expand only when the user asks.

## Purpose

Hands-on labs for LLM fundamentals through production agent patterns. Each lab is a small Python package under `labs/`.

## Commands

From a lab directory (e.g. `labs/00-llm-inference-basics`):

| Command | Purpose |
|---------|---------|
| `uv sync` | Install dependencies |
| `uv run pytest` | Run tests |
| `uv run python -m lab.main` | Run the lab entrypoint |

Repo-wide: see [README.md](README.md) and [docs/COMMITS.md](docs/COMMITS.md).

## Cursor skills

Repo-specific skills live under `.cursor/skills/` when present (eval-first, production-agent patterns, etc.).

Optional **local-only** Matt Pocock skills (not in git): see [docs/LOCAL-DEV.md](docs/LOCAL-DEV.md).
