# GitHub Classroom — Assignment setup notes

1. Create an assignment in GitHub Classroom.
2. Use this repository as the starter repo (or create a copy with exercise stubs).
3. In the assignment settings, enable autograding and point to the tests under:

```
modules/A1_defensive_programming/tests
```

4. Map tests to points according to `RUBRIC.md`.
5. Ensure CI workflow (`.github/workflows/tests.yml`) runs `pytest` and returns non-zero on failures.
