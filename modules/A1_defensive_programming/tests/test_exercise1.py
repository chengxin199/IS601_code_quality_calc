import pytest

from modules.A1_defensive_programming.exercises.exercise1 import safe_parse_and_add


def test_safe_parse_and_add_success():
    assert safe_parse_and_add("add 2 3") == 5.0


def test_safe_parse_and_add_invalid_format():
    with pytest.raises(ValueError):
        safe_parse_and_add("add 2")


def test_safe_parse_and_add_unsupported_op():
    with pytest.raises(ValueError):
        safe_parse_and_add("subtract 2 1")
