"""Rough token estimate (~4 chars per token for English prose). Replace with HF tokenizer in Phase 0."""


def estimate_tokens(text: str, chars_per_token: float = 4.0) -> int:
    if not text.strip():
        return 0
    return max(1, int(len(text) / chars_per_token))


def main(text: str = "Sample prompt for token estimate.") -> None:
    n = estimate_tokens(text)
    print(f"Text length: {len(text)} chars")
    print(f"Estimated tokens: {n} (~{len(text) / n:.1f} chars/token)")


if __name__ == "__main__":
    import sys

    arg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Sample prompt for token estimate."
    main(arg)
