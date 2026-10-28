"""Count tokens with a Hugging Face tokenizer (Lab 00 / HF tokenizers lesson)."""

from functools import lru_cache

from transformers import AutoTokenizer

MODEL_ID = "bert-base-cased"


@lru_cache(maxsize=1)
def _tokenizer() -> AutoTokenizer:
    return AutoTokenizer.from_pretrained(MODEL_ID)


def estimate_tokens_rough(text: str, chars_per_token: float = 4.0) -> int:
    """Legacy char/4 guess for comparison with real tokenization."""
    if not text.strip():
        return 0
    return max(1, int(len(text) / chars_per_token))


def estimate_tokens(text: str) -> int:
    if not text.strip():
        return 0
    return len(_tokenizer().tokenize(text))


def main(text: str = "Sample prompt for token estimate.") -> None:
    n = estimate_tokens(text)
    rough = estimate_tokens_rough(text)
    print(f"Text length: {len(text)} chars")
    print(f"Token count ({MODEL_ID}): {n}")
    if n:
        print(f"Chars per token: {len(text) / n:.1f}")
    print(f"Rough estimate (len/4): {rough}")


if __name__ == "__main__":
    import sys

    arg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Sample prompt for token estimate."
    main(arg)
