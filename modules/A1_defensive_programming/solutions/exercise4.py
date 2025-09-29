"""Solution for exercise4: safe_divide with logging."""

class DivisionByZeroError(Exception):
    pass


def safe_divide(a, b, logger=None):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    if b == 0:
        if logger:
            logger.error("Division by zero attempt: a=%r, b=%r", a, b)
        raise DivisionByZeroError("Division by zero is not allowed.")
    return a / b
