from lab.main import estimate_tokens, estimate_tokens_rough


def test_empty() -> None:
    assert estimate_tokens("") == 0
    assert estimate_tokens("   ") == 0


def test_bert_tokenize_short() -> None:
    # bert-base-cased: one token per char for this lowercase string
    assert estimate_tokens("abcd") == 4


def test_bert_tokenize_repeated_char() -> None:
    assert estimate_tokens("a" * 40) == 21


def test_rough_estimate_unchanged() -> None:
    assert estimate_tokens_rough("abcd") == 1
    assert estimate_tokens_rough("a" * 40) == 10
