# Commerce Order Service — Regression Benchmark v2

A small commerce/order service. A recent internal change introduced a regression affecting order totals under certain combinations of promotions, shipping, and tax.

## Your task

Find and fix the regression using the existing code and tests.

Requirements:
- Reproduce failures with the test suite.
- Find the root cause; don't hardcode outputs for individual tests.
- Preserve public APIs.
- Don't delete, skip, weaken, or modify tests merely to make them pass.
- Avoid unrelated refactors.
- Run the complete suite before finishing.

Run:

```bash
python -m pytest -q
```
