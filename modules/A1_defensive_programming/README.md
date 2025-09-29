# A1 — Defensive Programming (Design & Exercises)

This module contains teaching material, exercises, solutions, and pytest tests for the A1 unit on Defensive Programming, Errors, and Contracts.

Structure

```
modules/
  A1_defensive_programming/
    README.md          # this file (lesson + instructions)
    exercises/         # student-facing code (starter or completed)
    solutions/         # reference implementations
    tests/             # pytest tests used for auto-grading
```

Lesson contents

- EAFP vs LBYL (with examples)
- Guard clauses, pre/post conditions, assertions
- Custom exceptions and replacing ambiguous return codes
- Logging at error boundaries
- Small exercises to practice

How to use

- Instructors: you can replace `exercises/` implementations with stubs before giving to students so tests will fail until students implement them.
- Students: implement the functions in `modules/A1_defensive_programming/exercises/` and run tests:

```bash
source venv/bin/activate
venv/bin/py.test -q modules/A1_defensive_programming/tests -q
```

Design notes

- Tests import `modules.A1_defensive_programming.exercises` so they grade the student code directly.
- Solutions are provided in `solutions/` for instructors and reviewers.
