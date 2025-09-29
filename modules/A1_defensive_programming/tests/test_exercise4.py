import logging
import pytest

from modules.A1_defensive_programming.exercises.exercise4 import safe_divide


def test_safe_divide_success():
    assert pytest.approx(safe_divide(6, 3)) == 2


def test_safe_divide_logs_and_raises(caplog):
    caplog.set_level(logging.ERROR, logger="modules.A1_defensive_programming.exercises.exercise4")
    with pytest.raises(Exception):
        safe_divide(1, 0, logger=logging.getLogger("modules.A1_defensive_programming.exercises.exercise4"))
    assert any("Division by zero" in rec.message or "Division by zero attempt" in rec.message for rec in caplog.records)
