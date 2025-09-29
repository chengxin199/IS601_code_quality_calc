"""Hardened arithmetic operations for the calculator exercise.

This module uses guard clauses, explicit type checks, custom exceptions, and logging
so tests can assert both behavior and logs.
"""

from typing import Union
import logging

from app.exceptions import DivisionByZeroError, InvalidOperandError

Number = Union[int, float]

logger = logging.getLogger("app.operations")


def _check_number(x: object, name: str) -> None:
    """Guard clause: ensure x is int or float, otherwise raise InvalidOperandError."""
    if not isinstance(x, (int, float)):
        logger.debug("Invalid operand type detected: %s=%r", name, x)
        raise InvalidOperandError(f"Operand '{name}' must be int or float, got {type(x).__name__}")


class Operations:
    """Basic math operations with defensive checks."""

    @staticmethod
    def addition(a: Number, b: Number) -> Number:
        _check_number(a, "a")
        _check_number(b, "b")
        return a + b

    def subtraction(self, a: Number, b: Number) -> Number:
        _check_number(a, "a")
        _check_number(b, "b")
        return a - b

    @staticmethod
    def multiplication(a: Number, b: Number) -> Number:
        _check_number(a, "a")
        _check_number(b, "b")
        return a * b

    @staticmethod
    def division(a: Number, b: Number) -> float:
        _check_number(a, "a")
        _check_number(b, "b")
        if b == 0:
            logger.error("Division by zero attempt: a=%r, b=%r", a, b)
            raise DivisionByZeroError("Division by zero is not allowed.")
        result = a / b
        # Post-condition: division should return float
        if not isinstance(result, float):
            result = float(result)
        return result
