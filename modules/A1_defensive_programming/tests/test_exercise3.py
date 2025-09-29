import pytest

from modules.A1_defensive_programming.exercises.exercise3 import mean


def test_mean_success():
    assert mean([1, 2, 3]) == pytest.approx(2.0)


def test_mean_empty():
    with pytest.raises(AssertionError):
        mean([])


def test_mean_type_error():
    with pytest.raises(AssertionError):
        mean([1, "a"])
