from lab.main import estimate_tokens


def test_empty() -> None:
    assert estimate_tokens("") == 0
    assert estimate_tokens("   ") == 0


def test_short_text() -> None:
    assert estimate_tokens("abcd") == 1


def test_longer_text() -> None:
    text = "a" * 40
    assert estimate_tokens(text) == 10
