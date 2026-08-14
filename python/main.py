"""Demo runner — runs min_moves_to_escape on one example case and prints the result."""

import os

from escape_vault import min_moves_to_escape
from test_data import TEST_DATA_DIR, load_case


def main() -> None:
    path = os.path.join(TEST_DATA_DIR, "simple", "04_worked_example_k2.txt")
    case = load_case(path)

    print(f"Case: {case.name}")
    print("Grid:")
    for row in case.grid:
        print(" ", row)
    print(f"K = {case.k}")

    result = min_moves_to_escape(case.grid, case.k)
    print(f"Minimum moves to escape: {result}")


if __name__ == "__main__":
    main()
