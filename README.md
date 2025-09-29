# 📦 Project Setup

---

````markdown
# 📦 Calculator — Defensive Programming (A1) Workshop

This repository contains a small calculator exercise used for the A1 lesson: Defensive Programming, Errors, and Contracts. The goal is to harden arithmetic operations, add clear error handling and logs, and add tests that cover error paths.

---

## Repository layout (important files)
- `app/`
  - `operations.py`        — hardened calculator operations
  - `exceptions.py`        — custom exceptions
  - `__init__.py`
- `tests/`
  - `test_operations.py`   — original functional tests
  - `test_error_paths.py`  — (optional) added tests for errors/logging
- `venv/`                  — virtualenv (project-local)
- `.github/workflows/tests.yml` — CI that runs pytest

---

## Prerequisites
- Python 3.10+ (Linux/macOS/Windows)
- Git
- Virtualenv recommended

## Quick local setup
1. Create & activate a venv (if not present):

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows (PowerShell/CMD)
```

2. Install test deps (if requirements are provided):

```bash
pip install -r requirements.txt || pip install pytest
```

3. Run full test suite:

```bash
venv/bin/py.test -q
```

---

## Useful test commands
- Run all tests (quiet):

```bash
venv/bin/py.test -q
```
- Run a single test function:

```bash
venv/bin/py.test -q tests/test_operations.py::test_division_by_zero
```
- Run a single test file:

```bash
venv/bin/py.test -q tests/test_error_paths.py
```
- Run with verbose output and stop at first failure:

```bash
venv/bin/py.test -vv --maxfail=1
```

---

## Adding instructor references locally
Create a `references/` folder and clone any auxiliary repo there so the content is available to students and the AI for local reading:

```bash
mkdir -p references
git clone <REPO_URL> references/<repo-name>
```

Replace `<REPO_URL>` and `<repo-name>` with the appropriate values.

---

## GitHub Classroom / CI notes
- This repo contains a GitHub Actions workflow at `.github/workflows/tests.yml` that runs `pytest` on pushes/PRs. Classroom will run tests automatically for student submissions when configured.
- Keep tests deterministic and avoid printing secrets. Logs may include non-sensitive inputs or IDs for context.

---

## A1 Lesson: Defensive Programming — Overview (3–4h)
Goal: write resilient code that fails fast, communicates intent, and recovers gracefully.

Topics covered:
- EAFP vs LBYL and when to use each
- Invariants, assertions, guard clauses
- Python exceptions hierarchy, custom exceptions, error boundaries
- Design by contract (pre-/post-conditions)
- Sentinel values vs exceptions; logging basics

Before you start (preflight):
- Repo cloned; tests run locally (`venv/bin/py.test -q`)
- Python >= 3.10; venv active
- CI configured with pytest + coverage (see `.github/workflows/tests.yml`)

Outcomes:
- Choose EAFP or LBYL appropriately and justify the choice
- Implement clear error handling with actionable messages
- Add targeted tests for error paths and contracts

---

## Hands-on tasks (step-by-step)
1. Preflight (15 min)
   - Activate venv and run tests: `venv/bin/py.test -q`.
   - Read `tests/test_operations.py` to understand expected behaviour.

2. Quick discussion (30 min)
   - Small examples showing EAFP vs LBYL.

3. Harden the code (90–120 min)
   - Add custom exceptions in `app/exceptions.py` (subclass built-ins for compatibility).
   - Introduce guard clauses to validate input types and pre-conditions.
   - Replace ambiguous return codes with exceptions.
   - Add logging at error boundaries that includes non-sensitive context (inputs/IDs).
   - Add post-condition checks where helpful (e.g., division returns `float`).

4. Tests (30 min)
   - Add at least two tests covering error paths (e.g., non-number operand, division-by-zero).
   - Use `caplog` to assert log messages include context without secrets.

5. CI verification (15–30 min)
   - Push changes and confirm GitHub Actions run tests successfully.

6. Reflection (15–30 min)
   - Which guard clause or assertion prevented a bug?
   - EAFP vs LBYL tradeoffs in your decisions.

---

## Quick coding examples (safe, small)
- Custom exceptions (in `app/exceptions.py`):

```python
class CalculatorError(Exception):
   """Base exception for calculator errors."""
   pass

class DivisionByZeroError(ValueError, CalculatorError):
   """Raised when division by zero is attempted."""
   pass

class InvalidOperandError(TypeError, CalculatorError):
   """Raised when operands are of invalid type."""
   pass
```

- Guard clause and logging (in `app/operations.py`):

```python
import logging
from typing import Union

from .exceptions import DivisionByZeroError, InvalidOperandError

Number = Union[int, float]
logger = logging.getLogger("app.operations")

def _check_number(x: object, name: str) -> None:
   if not isinstance(x, (int, float)):
      logger.debug("Invalid operand type: %s=%r", name, x)
      raise InvalidOperandError(f"Operand '{name}' must be int or float, got {type(x).__name__}")

class Operations:
   @staticmethod
   def addition(a: Number, b: Number) -> Number:
      _check_number(a, "a")
      _check_number(b, "b")
      return a + b

   @staticmethod
   def division(a: Number, b: Number) -> float:
      _check_number(a, "a")
      _check_number(b, "b")
      if b == 0:
         logger.error("Division by zero attempt: a=%r, b=%r", a, b)
         raise DivisionByZeroError("Division by zero is not allowed.")
      result = a / b
      if not isinstance(result, float):
         result = float(result)
      return result
```

---

## Acceptance criteria (CI-verifiable)
- Tests pass locally and on CI (`venv/bin/py.test -q`).
- At least two new tests cover error paths (use `caplog` for logging assertions).
- No bare `except:` blocks in the codebase.
- Custom exceptions used where appropriate (e.g., `DivisionByZeroError`, `InvalidOperandError`).

---

## Quick debugging tips
- Use `caplog` in pytest to assert logged messages.
- Run one failing test at a time to iterate quickly.
- When changing exception types, keep backward compatibility in mind (subclassing built-ins).

---

## Want help?
I can:
- create or update the example files (`app/exceptions.py`, `app/operations.py`) for you,
- run the tests and report the output,
- generate an instructor rubric and slides for the A1 lesson.

Tell me which you want next and I will proceed.

````
git push origin main
