# Worked example, step by step

This walks through the problem by hand, using one small grid at three
different key budgets (the same grid as
`test_data/simple/06_trap_k0.txt`, `07_trap_k2.txt`, and
`08_trap_k5.txt`, so you can cross-check every answer below against
those files). The goal here is to make sure the *rules* of the problem
are completely clear before you write any code — it deliberately stops
short of showing you an efficient way to search a big grid. See
[README.md](README.md) for the full problem statement and constraints.

## The setup

```
S.5.E
.###.
..1..
```

Laid out with row/column coordinates (row, then column, both starting at
0):

```
        col0  col1  col2  col3  col4
row0:    S     .     5     .     E
row1:    .     #     #     #     .
row2:    .     .     1     .     .
```

`S` is at `(0,0)`, `E` is at `(0,4)`. The robot moves one cell at a time,
up/down/left/right only, never through a `#`. A digit is a locked door —
step onto it and that many keys get spent immediately, and the robot
never takes a door it can't afford.

## Stage 1 — find the routes

Looking at the grid, there are exactly two ways to get from `S` to `E`
that don't backtrack over themselves:

**Route A — straight across the top, through the cost-5 door:**

```
(0,0) → (0,1) → (0,2)[door, cost 5] → (0,3) → (0,4)
```

4 moves. 1 door, costing 5 keys.

**Route B — down and around the bottom, through the cost-1 door:**

```
(0,0) → (1,0) → (2,0) → (2,1) → (2,2)[door, cost 1] → (2,3) → (2,4) → (1,4) → (0,4)
```

8 moves. 1 door, costing 1 key. (Row 1 is walled off in the middle —
`.###.` — so this is the only way around; there's no shortcut through
the wall.)

Route A is shorter. Route B is cheaper. Which one is actually usable
depends entirely on the key budget `K`.

## Stage 2 — K = 0

Neither door is free. Route A needs 5 keys, Route B needs 1 key — both
more than the 0 available. With no way to afford either route, there is
no way to reach `E` at all.

**Answer: `min_moves_to_escape(grid, 0)` = `-1`.**

## Stage 3 — K = 2

Route A still needs 5 keys — unaffordable. Route B needs only 1 key,
which fits comfortably inside a budget of 2 (the robot doesn't need to
spend its whole budget, just not go below zero). Route B is the *only*
affordable way through, so it's also, by default, the shortest
*affordable* one.

**Answer: `min_moves_to_escape(grid, 2)` = `8`.**

This is the case worth paying attention to: the shortest route overall
(Route A, 4 moves) is *not* the answer, because it's outside the budget.
A solution that finds the shortest route first and only afterwards
checks whether it can be afforded would land on Route A, see that 5 > 2,
and incorrectly conclude the vault is inescapable — even though Route B
gets the robot out just fine. Affordability has to be part of the search
itself, not a check bolted on at the end.

## Stage 4 — K = 5

Now both doors are affordable: Route A costs exactly 5 (the whole
budget, but 0 is still not negative, so it's allowed), and Route B costs
1. With both routes usable, the shorter one wins.

**Answer: `min_moves_to_escape(grid, 5)` = `4`.**

Put the three stages side by side and the shape of the problem becomes
clear: the same grid gives three different answers depending on the
budget, because the budget changes which routes are even in play — not
just what they cost.

| K | Route A (4 moves, costs 5) | Route B (8 moves, costs 1) | Answer |
|---|---|---|---|
| 0 | unaffordable | unaffordable | `-1` |
| 2 | unaffordable | affordable | `8` |
| 5 | affordable | affordable | `4` (shorter of the two affordable routes) |
