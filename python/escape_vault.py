"""
Escape the Vault.

Implement min_moves_to_escape below. See ../README.md for the full problem
statement, constraints, and worked examples.

The helper functions are optional scaffolding — use them, change their
signatures, or delete them and structure your solution however you like.
"""

from typing import List, Optional, Tuple


def find_start_and_end(grid: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Return ((start_row, start_col), (end_row, end_col))."""
    # TODO: implement
    raise NotImplementedError


def in_bounds(row: int, col: int, rows: int, cols: int) -> bool:
    """Return True if (row, col) is within a grid of size rows x cols."""
    # TODO: implement
    raise NotImplementedError


def door_cost(cell: str) -> int:
    """Return the number of keys needed to enter this cell (0 if it's not a locked door)."""
    # TODO: implement
    raise NotImplementedError


def min_moves_to_escape(grid: List[str], k: int) -> int:
    """
    Return the minimum number of moves from S to E without the key balance
    ever going negative, or -1 if it can't be done within the budget.
    """
    # TODO: implement
    raise NotImplementedError
