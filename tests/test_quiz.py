import pytest

from quiz_service import calculate_score


def test_all_correct():
    user_answers = [1, 2, 0, 3, 1]
    correct_answers = [1, 2, 0, 3, 1]

    assert calculate_score(user_answers, correct_answers) == 5


def test_some_correct():
    user_answers = [1, 0, 0, 3, 2]
    correct_answers = [1, 2, 0, 3, 1]

    assert calculate_score(user_answers, correct_answers) == 3


def test_none_correct():
    user_answers = [0, 0, 1, 1, 0]
    correct_answers = [1, 2, 0, 3, 1]

    assert calculate_score(user_answers, correct_answers) == 0


def test_different_number_of_answers():
    with pytest.raises(ValueError):
        calculate_score([1, 2], [1, 2, 3])