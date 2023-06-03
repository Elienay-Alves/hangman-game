from unittest.mock import patch
import pytest
from src.user_interaction import guess_input


def test_if_input_raises_a_ValueError_if_is_not_a_letter():
    simulated_input = "#"

    with patch("builtins.input", return_value=simulated_input):
        with pytest.raises(ValueError, match="You can type only letter"):
            guess_input()


def test_if_input_raises_ValueError_when_empty():
    simulated_input = ""

    with patch("builtins.input", return_value=simulated_input):
        with pytest.raises(ValueError, match="You must type a letter"):
            guess_input()


def test_if_input_raises_a_ValueError_when_lenght_is_greater_than_one():
    simulated_input = "lq"

    with patch("builtins.input", return_value=simulated_input):
        with pytest.raises(
            ValueError, match="It is allowed only one letter per play"
        ):
            guess_input()
