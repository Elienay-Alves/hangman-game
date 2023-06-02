import pytest
from unittest.mock import patch

from src.user_interaction import guess


def test_input_is_string():
    simulated_input = "l"

    with patch("builtins.input", return_value=simulated_input):
        assert guess() == "l", "The input is not a string"


def test_if_raises_TypeError_when_input_is_not_string():
    simulated_input = 43
    with patch("builtins.input", return_value=simulated_input):
        with pytest.raises(TypeError):
            guess()
