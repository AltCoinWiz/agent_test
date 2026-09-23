# Ledger Service

A small event-driven wallet ledger used by a marketplace.

A recent change introduced a production regression involving account balances after
payment events are retried. The service is designed for at-least-once event
delivery, so receiving the same external event more than once is normal.

## Task

Find and fix the regression.

Requirements:

- Preserve the public API.
- Preserve at-least-once delivery semantics.
- Do not disable retries or suppress legitimate distinct transactions.
- Do not change tests merely to make them pass.
- Avoid unrelated refactoring.
- Run the complete test suite before finishing.

Install/run:

```bash
python -m pytest -q
```
