import pytest
from unittest.mock import patch

from src.user_interaction import guess


def test_if_guess_uses_input_correctly():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        guessed_letter = guess
        assert guessed_letter == simulated_input, "Guess dont have a input"
