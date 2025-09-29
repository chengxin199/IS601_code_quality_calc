import logging
import pytest

from app.operations import Operations
from app.exceptions import DivisionByZeroError, InvalidOperandError


def test_non_numeric_operands_raise_type_error():
    with pytest.raises(InvalidOperandError):
        Operations.addition("a", 1)
    with pytest.raises(InvalidOperandError):
        Operations().subtraction(1, object())


def test_division_by_zero_logs_and_raises(caplog):
    caplog.clear()
    caplog.set_level(logging.ERROR, logger="app.operations")
    with pytest.raises(DivisionByZeroError, match="Division by zero is not allowed."):
        Operations.division(1, 0)
    assert any("Division by zero attempt" in rec.message for rec in caplog.records)
