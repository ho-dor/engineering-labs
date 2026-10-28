# Lab 00: LLM inference basics

**Plan phase:** 0  
**Skill demonstrated:** Text → tokens with `AutoTokenizer` (compare to rough len/4 estimate)

## Run

```bash
uv sync          # installs transformers + pytest into .venv
uv run pytest    # must use uv run (not bare pytest) so imports use .venv
uv run python -m lab.main "Hello, bowling coach project"
```

## What I learned

- Tokenization approaches 
- Word, Char and sub-word tokenizations. 
- HF article - https://huggingface.co/learn/llm-course/chapter2/4
- Wordpiece tokenizer used by BERT
