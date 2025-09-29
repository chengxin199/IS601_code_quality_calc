"""Custom exceptions for the calculator app."""

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class DivisionByZeroError(ValueError, CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class InvalidOperandError(TypeError, CalculatorError):
    """Raised when operands are of invalid type."""
    pass
