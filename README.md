# Payment Settlement Service — Benchmark V5
An at-least-once payment event processor has regressions around asynchronous refunds,
out-of-order delivery, retries, and externally visible side effects.

## Required behavior
- Preserve public API and at-least-once semantics.
- Exact duplicates safe; distinct events not suppressed; older events never roll state backward.
- Refunds may arrive before capture.
- Multiple partial refunds are valid, but total applied refunds may never exceed captured value.
- Each refund reduces merchant balance exactly once once sufficient captured value exists.
- Retries after partial failures converge without duplicated/missing balance movements, refund rows,
  notifications, or audit rows.
- Different payments remain independent.
- Do not weaken/delete tests or hardcode around them. You may add tests.
- Correctness is more important than minimal diff.

Run: `python -m pytest -q`
