import pytest

from cli_demo import (
    AUDIENCE_LABELS,
    LANGUAGE_LABELS,
    MAX_INPUT_CHARS,
    STYLE_LABELS,
    RewriteError,
    validate_input,
)


def test_option_sets_match_product_contract():
    assert set(STYLE_LABELS) == {
        "angry",
        "sarcastic",
        "passive_aggressive",
        "polite",
        "warm",
        "direct",
        "formal",
        "academic_presentation",
        "resume",
        "job_interview",
    }
    assert set(AUDIENCE_LABELS) == {
        "general",
        "friend",
        "colleague",
        "manager",
        "professor",
        "recruiter_interviewer",
    }
    assert set(LANGUAGE_LABELS) == {"zh", "en"}


def test_validate_input_strips_surrounding_whitespace():
    result = validate_input(
        "  Please move the deadline.  ", "polite", "manager", "en"
    )
    assert result == "Please move the deadline."


@pytest.mark.parametrize("text", ["", "   "])
def test_validate_input_rejects_empty_text(text):
    with pytest.raises(RewriteError, match="Enter the meaning"):
        validate_input(text, "polite", "general", "en")


def test_validate_input_accepts_exact_character_limit():
    text = "a" * MAX_INPUT_CHARS
    assert validate_input(text, "formal", "general", "en") == text


def test_validate_input_rejects_text_over_character_limit():
    with pytest.raises(RewriteError, match="2,000 characters"):
        validate_input("a" * (MAX_INPUT_CHARS + 1), "formal", "general", "en")


@pytest.mark.parametrize(
    ("style", "audience", "language", "message"),
    [
        ("unknown", "general", "en", "style"),
        ("polite", "unknown", "en", "audience"),
        ("polite", "general", "fr", "language"),
    ],
)
def test_validate_input_rejects_unknown_options(style, audience, language, message):
    with pytest.raises(RewriteError, match=message):
        validate_input("Hello", style, audience, language)
