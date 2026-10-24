import pytest

from app import validate_text, MIN_TEXT_LENGTH, MAX_TEXT_LENGTH


def test_text_too_short():
    with pytest.raises(ValueError):
        validate_text("a" * (MIN_TEXT_LENGTH - 1))


def test_text_minimum_length():
    text = "a" * MIN_TEXT_LENGTH
    assert validate_text(text) == text


def test_text_maximum_length():
    text = "a" * MAX_TEXT_LENGTH
    assert validate_text(text) == text


def test_text_too_long():
    with pytest.raises(ValueError):
        validate_text("a" * (MAX_TEXT_LENGTH + 1))


def test_text_is_trimmed():
    text = "   " + ("a" * MIN_TEXT_LENGTH) + "   "
    assert validate_text(text) == "a" * MIN_TEXT_LENGTH
