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

## Agent skills

### Issue tracker

Work is tracked as markdown under `.scratch/` until GitHub is wired up. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout: root `GLOSSARY.md` (when created) and `docs/adr/`. See `docs/agents/domain.md`.

## Matt Pocock workflow

Skills live in [`.agents/skills/`](.agents/skills/). Typical feature flow: `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`.

Repo-specific skills (eval-first, etc.) may live under `.cursor/skills/` when added.
