"""
Test harness for Escape the Vault.

Loops over every test case in ../test_data/{simple,medium,hard}/, calls
min_moves_to_escape on each, and reports PASS/FAIL per tier. Exits with
status 1 if any test fails.

Simple and medium cases are small enough to trace by hand; hard cases are
larger generated mazes intended to test how your solution scales, not just
whether it's correct. See ../test_data/README.md for details on every case.
"""

import time

from escape_vault import min_moves_to_escape
from test_data import load_tier

TIERS = ["simple", "medium", "hard"]


def run_tier(tier: str):
    cases = load_tier(tier)
    passed = 0
    failed = 0

    for case in cases:
        start = time.perf_counter()
        try:
            actual = min_moves_to_escape(case.grid, case.k)
        except NotImplementedError:
            actual = "NOT IMPLEMENTED"
        elapsed_ms = (time.perf_counter() - start) * 1000

        ok = actual == case.expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {tier}/{case.name}: expected={case.expected} actual={actual} ({elapsed_ms:.1f}ms)")

        if ok:
            passed += 1
        else:
            failed += 1

    return passed, failed


def main() -> None:
    total_passed = 0
    total_failed = 0

    for tier in TIERS:
        print(f"\n--- {tier} ---")
        passed, failed = run_tier(tier)
        total_passed += passed
        total_failed += failed
        print(f"{tier}: {passed} passed, {failed} failed")

    print(f"\nTOTAL: {total_passed} passed, {total_failed} failed out of {total_passed + total_failed}")
    raise SystemExit(1 if total_failed else 0)


if __name__ == "__main__":
    main()
