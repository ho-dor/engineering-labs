# agent-engineering-labs

Learning monorepo: small labs (00–16) for the Sabbatical agent-engineering path.

| Lab | Topic | Status |
|-----|--------|--------|
| 00 | LLM inference basics | done |
| 01–16 | See plan | pending |

## Run a lab

```bash
cd labs/00-llm-inference-basics
cp .env.example .env
uv sync
uv run pytest
uv run python -m lab.main
```

## Docs

- [COMMITS.md](docs/COMMITS.md) — commit message conventions
- [LOCAL-DEV.md](docs/LOCAL-DEV.md) — optional local Cursor skills (not committed)
