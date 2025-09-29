import pytest

from modules.A1_defensive_programming.exercises.exercise2 import divide, DivisionByZeroError


def test_divide_success():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(1, 0)


def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("a", 1)
