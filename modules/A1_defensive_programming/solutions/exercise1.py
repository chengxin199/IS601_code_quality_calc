"""Solution for exercise1 (guard clauses)."""

def safe_parse_and_add(s: str) -> float:
    parts = s.strip().split()
    if len(parts) != 3:
        raise ValueError("Invalid input format. Expected: <op> <num1> <num2>")
    op, a_str, b_str = parts
    if op != "add":
        raise ValueError(f"Unsupported operation: {op}")
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError as e:
        raise ValueError("Operands must be numbers") from e
    return a + b
