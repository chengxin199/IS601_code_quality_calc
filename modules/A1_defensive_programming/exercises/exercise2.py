"""Exercise 2 (starter): replace ambiguous return codes with custom exceptions.

Students: implement `DivisionByZeroError` and `divide(a, b)` below.

Hints:
- Create a custom exception class for division by zero.
- Validate operand types and raise `TypeError` for non-numeric inputs.
"""


class DivisionByZeroError(Exception):
    """Raised when division by zero is attempted."""
    pass


def divide(a: float, b: float) -> float:
    """Divide a by b. Replace this stub with a proper implementation.

    Raise DivisionByZeroError when b == 0.
    """
    raise NotImplementedError("Implement divide(a,b) and raise DivisionByZeroError on zero divisor")

