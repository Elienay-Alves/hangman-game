import pytest
from unittest.mock import patch

from src.user_interaction import guess


def test_input_is_string():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess()
        assert isinstance(guessed_letter, str), "The input is not a string"
