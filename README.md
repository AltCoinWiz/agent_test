# Thor Agent Benchmark

A small order-processing service used to benchmark autonomous coding agents.

## Run tests

```bash
python -m pytest -q
```

## Benchmark task

The repository contains a regression in the checkout/order-pricing path.

Your task is to:

1. Inspect the repository without being told which file is wrong.
2. Reproduce the failing behavior with the test suite.
3. Identify the root cause.
4. Implement the smallest correct fix.
5. Run the complete test suite until all tests pass.
6. Do not modify or delete tests merely to make them pass.
7. Preserve the public API unless a change is required for correctness.

The expected behavior is encoded in the tests and domain objects.
