"""Solution for exercise5: safe_lookup."""

def safe_lookup(mapping, key):
    if key in mapping:
        return mapping[key]
    raise KeyError(f"Key {key!r} not found")
