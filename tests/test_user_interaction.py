import re
from unittest.mock import patch
import pytest
from src.user_interaction import guess


def test_if_raises_TypeError_when_input_is_not_a_letter():
    simulated_input = "#"
    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess()
        assert not re.search(
            r"[\d+\-*/%&$#@!~^]", guessed_letter
        ), "The input should not contain a number, symbol or signal"
