"""Solution for exercise2 (custom exception on division by zero)."""

class DivisionByZeroError(Exception):
    pass


def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be numbers")
    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")
    return a / b
