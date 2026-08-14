"""
Loads Escape the Vault test cases from ../test_data/{simple,medium,hard}/*.txt.

File format:

    name=<case name>
    k=<int>
    expected=<int>
    grid=
    <grid row 0>
    <grid row 1>
    ...
"""

import os
from dataclasses import dataclass
from typing import List

TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "test_data")


@dataclass
class TestCase:
    name: str
    grid: List[str]
    k: int
    expected: int


def load_case(path: str) -> TestCase:
    with open(path) as f:
        lines = f.read().splitlines()

    name = None
    k = None
    expected = None
    grid_start = None

    for i, line in enumerate(lines):
        if line == "grid=":
            grid_start = i + 1
            break
        key, _, value = line.partition("=")
        if key == "name":
            name = value
        elif key == "k":
            k = int(value)
        elif key == "expected":
            expected = int(value)

    grid = lines[grid_start:]
    return TestCase(name=name, grid=grid, k=k, expected=expected)


def load_tier(tier: str) -> List[TestCase]:
    tier_dir = os.path.join(TEST_DATA_DIR, tier)
    cases = []
    for filename in sorted(os.listdir(tier_dir)):
        if filename.endswith(".txt"):
            cases.append(load_case(os.path.join(tier_dir, filename)))
    return cases
