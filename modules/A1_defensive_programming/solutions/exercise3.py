"""Solution for exercise3 (design by contract mean)."""

def mean(values):
    vals = list(values)
    if len(vals) == 0:
        raise ValueError("values must be non-empty")
    for v in vals:
        if not isinstance(v, (int, float)):
            raise TypeError("all elements must be numbers")
    result = sum(vals) / len(vals)
    return float(result)
