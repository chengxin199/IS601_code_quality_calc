import pytest

from modules.A1_defensive_programming.exercises.exercise5 import safe_lookup


def test_safe_lookup_success():
    d = {"a": 1}
    assert safe_lookup(d, "a") == 1


def test_safe_lookup_missing():
    d = {"a": 1}
    with pytest.raises(KeyError):
        safe_lookup(d, "b")
