# Test data

Every case for Escape the Vault lives here as a plain text file, grouped
into three difficulty tiers. Both `python/run_tests.py` and
`java/src/TestRunner.java` load directly from this directory — nothing is
duplicated in code.

## File format

```
name=<case name>
k=<int>
expected=<int>
grid=
<grid row 0>
<grid row 1>
...
```

Everything from the line after `grid=` to the end of the file is the grid,
one row per line, no trailing blank line. Filenames are numbered
(`01_...`, `02_...`) purely so both loaders sort them into a stable,
predictable order when they list a directory — the number carries no other
meaning.

`expected` was never computed by hand — it comes from a working reference
implementation kept outside this repository, checked once and then treated
as ground truth. Take it as correct.

## Simple — `simple/`

Tiny, hand-verifiable grids. Each one isolates a single mechanic rather
than combining several, so a failure here points at a specific piece of
missing logic rather than "something is wrong somewhere."

| Case | Grid | K | Expected | What it checks |
|---|---|---|---|---|
| `01_adjacent` | 1×2 | 0 | 1 | Basic movement between two open cells, with nothing else in play. If this fails, the core move-by-move traversal is broken. |
| `02_sealed_off` | 3×3 | 5 | -1 | `S` has no open neighbours at all. Checks that your solution terminates cleanly when there's nowhere left to go and reports `-1`, instead of crashing, looping forever, or returning some other default. |
| `03_door_too_dear` | 1×3 | 3 | -1 | A single door on the only route, costing more than the budget. Checks that the budget rule is actually enforced — a route through a door you can't afford isn't a valid route. |
| `04_worked_example_k2` | 4×4 | 2 | 6 | One mandatory door (cost 2) and one further, optional door (cost 1) that only adds a detour. Checks that you find the *shortest* affordable route, not merely *an* affordable one. |
| `05_worked_example_k1` | 4×4 | 1 | -1 | Same grid, budget cut below the mandatory door's cost. Checks that reachability is re-evaluated for the actual budget given, not assumed from a keys-agnostic route. |
| `06_trap_k0` | 3×5 | 0 | -1 | See below — neither of the two routes is affordable at `K=0`. |
| `07_trap_k2` | 3×5 | 2 | 8 | **The trap.** Two disjoint routes exist between `S` and `E`: a short one (4 moves) through a cost-5 door, and a long one (8 moves) through a cost-1 door. At `K=2`, only the long route is affordable. A solution that treats "find the shortest route" and "check whether it's affordable" as two separate steps will land on the 4-move route, see it's unaffordable, and wrongly report `-1` — even though the 8-move route is perfectly reachable. This is the single highest-signal case in the whole suite. |
| `08_trap_k5` | 3×5 | 5 | 4 | Same grid, budget now covers both routes. Checks that once both are affordable, you correctly prefer the shorter one — ruling out a fix for case `07` that just always prefers the cheaper route regardless of length. |

## Medium — `medium/`

Bigger hand-designed grids. Still traceable with pencil and paper, but big
enough that the interesting behaviour is a genuine decision, not a
one-glance inspection.

| Case | Grid | K | Expected | What it checks |
|---|---|---|---|---|
| `01_loop_choice_k6` | 9×9 | 6 | 8 | A square ring with two ways from `S` to `E`: straight across the top through a cost-6 door (8 moves), or all the way around a free outer loop (24 moves). A dead-end pocket containing a cost-3 door sits in the middle, reachable but leading nowhere. At `K=6` the short route is affordable, so it should win. Checks that a dead end doesn't throw off the result, and that you're comparing route *lengths* between the viable options, not just checking that *some* route exists. |
| `02_loop_choice_k3` | 9×9 | 3 | 24 | Same grid, budget below the short route's door cost. Only the free outer loop is affordable, so the answer jumps to 24. Same map as `01`, opposite conclusion — a solution hardcoded around one answer will fail here. |
| `03_forced_snake_k9` | 7×7 | 9 | 30 | A single corridor with no branching, folded into a snake shape and crossing three doors in sequence (costs 2, 4, 3 — total 9). Checks correct *accumulation* of cost across multiple doors on one route, and correct move-counting over a longer, folded path (it's easy to undercount the cells spent on each fold — worth double-checking your own trace against the expected value if you're not sure). |
| `04_forced_snake_k8` | 7×7 | 8 | -1 | Same corridor, budget one short of the total door cost (9). No alternate route exists, so this is a clean check of the budget arithmetic: 8 must be treated as insufficient, not rounded up or fudged. |
| `05_sealed_off` | 7×7 | 50 | -1 | A larger unreachable grid. Confirms that unreachability is still detected correctly at a size where it's no longer obvious at a glance. |

## Hard — `hard/`

Procedurally generated mazes with loops (more than one route between `S`
and `E`) and a scattering of locked doors, built with a fixed random seed
so they're reproducible. At this size, tracing a route by eye isn't
realistic — this tier exists to test your solution itself, not just its
correctness on a case a person already worked out by hand.

Correctness still matters as much as it does in the other two tiers, but
this tier also exercises how your solution behaves as the grid and key
budget grow. A solution that works fine on `simple` and `medium` can still
struggle here if it doesn't scale well — if a test run hangs or takes an
unreasonably long time on one of these cases, that's worth investigating
in its own right, separately from whether the final answer is correct.

| Case | Grid | K | Expected | What it checks |
|---|---|---|---|---|
| `maze_61x61_k12` | 61×61 | 12 | -1 | Just below the budget needed to reach `E` at all in this maze. Checks exact budget-threshold behaviour at a size where you can't just eyeball the answer. |
| `maze_61x61_k13` | 61×61 | 13 | 212 | One key more than `k12` — the maze becomes just barely solvable. A single extra unit of budget flipping the answer from `-1` to a real route is a good check that the budget is being evaluated precisely, not approximately. |
| `maze_61x61_k50` | 61×61 | 50 | 176 | Same maze, generous budget. The shortest route shrinks from 212 to 176 moves, because more keys make previously-unaffordable shortcuts usable. Checks that you keep looking for a genuinely shorter route as the budget grows, rather than stopping at the first one found. |
| `maze_101x101_k38` | 101×101 | 38 | -1 | The unreachable case at roughly 4x the grid size of the 61×61 maze. Mostly a scale check — this grid is large enough that some approaches which work on the smaller mazes will start to struggle here. |
| `maze_101x101_k39` | 101×101 | 39 | 384 | One key above the threshold, same dynamic as `maze_61x61_k13` but at the largest scale in the suite. |
| `maze_101x101_k50` | 101×101 | 50 | 328 | Generous budget on the largest maze — the same "more keys → shorter route" effect as `maze_61x61_k50`, and the heaviest scale check in the suite. |
