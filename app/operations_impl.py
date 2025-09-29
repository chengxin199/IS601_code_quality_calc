"""Hardened arithmetic operations implementation.

This file contains the real implementation; the `app.operations` package __init__ will
re-export `Operations` so imports remain stable.
"""

from typing import Union
import logging

from app.exceptions import DivisionByZeroError, InvalidOperandError

Number = Union[int, float]

logger = logging.getLogger("app.operations")


def _check_number(x: object, name: str) -> None:
    if not isinstance(x, (int, float)):
        logger.debug("Invalid operand type detected: %s=%r", name, x)
        raise InvalidOperandError(f"Operand '{name}' must be int or float, got {type(x).__name__}")


class Operations:
    @staticmethod
    def addition(a: Number, b: Number) -> Number:
        _check_number(a, "a")
        _check_number(b, "b")
        return a + b

    @staticmethod
    def subtraction(a: Number, b: Number) -> Number:
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
        # Ensure a float result consistently (remove conditional branch)
        return float(a / b)
