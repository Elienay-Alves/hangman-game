import re
from unittest.mock import patch
import pytest
from src.user_interaction import guess


def test_if_input_is_a_letter():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess()
        assert not re.search(
            r"[\d+\-*/%&$#@!~^]", guessed_letter
        ), "The input should not contain a number, symbol or signal"


def test_if_input_is_not_empty():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess()
        assert len(guessed_letter) > 0, "The input should contain a letter"


def test_if_length_of_input_is_one():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess()
        assert (
            len(guessed_letter) == 1
        ), "The input should contain only one letter"


def test_if_input_raises_ValueError_when_empty():
    simulated_input = ""

    with patch("builtins.input", return_value=simulated_input):
        with pytest.raises(ValueError, match="You must type a letter"):
            guess()
