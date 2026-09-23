# Fulfillment Event Service

This service consumes at-least-once shipment events and maintains shipment state,
inventory reservations, notifications, and an audit trail.

A recent refactor introduced a production regression. Operators report duplicate
side effects during retries and inconsistent behavior around out-of-order events.

## Task
Find and fix the regression(s).

Requirements:
- Preserve the public API and at-least-once delivery semantics.
- Duplicate delivery of the same event must be safe.
- Distinct lifecycle events must not be suppressed.
- Older events must not roll shipment state backward.
- A retry after a partial failure must converge to the same externally visible result as a successful first attempt.
- Do not weaken/delete/hardcode around tests.
- Avoid unrelated refactoring.
- Run `python -m pytest -q`.
