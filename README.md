# Fulfillment Event Service — V4.1
This service consumes shipment lifecycle events from an at-least-once delivery system.
A recent refactor introduced a production regression involving retries after partial failures.

## Task
Find and fix the regression(s).

Requirements:
- Preserve the public API and at-least-once delivery semantics.
- Exact duplicate delivery must be safe.
- Distinct lifecycle events must not be suppressed.
- Older events must not roll state backward.
- A retry after a partial failure must converge to the same externally visible result as a successful first attempt.
- Do not modify/delete/weaken tests or hardcode around them.
- Avoid unrelated refactoring.

Run: `python -m pytest -q`
