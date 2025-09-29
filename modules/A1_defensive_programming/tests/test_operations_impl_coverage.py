def test_division_postcondition_converts_non_float(monkeypatch):
    """Force a non-float result from __truediv__ and ensure the post-condition converts it to float."""
    from app import operations_impl

    class Weird:
        def __truediv__(self, other):
            return 2  # intentionally return int, not float

    # Disable the type checks so we can pass Weird instances
    monkeypatch.setattr(operations_impl, "_check_number", lambda x, name: None)

    res = operations_impl.Operations.division(Weird(), Weird())
    assert isinstance(res, float)
    assert res == 2.0
