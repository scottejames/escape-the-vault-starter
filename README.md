# Escape the Vault — starter project

A starting point for the "Escape the Vault" coding assessment, provided in
both Python and Java. Pick whichever language you're more comfortable in —
they're graded the same way.

## The problem

A robot starts at `S` in a grid and must reach the exit `E`, moving one cell
at a time (up/down/left/right, no diagonals). Cells are:

- `.` — open floor
- `#` — a wall (impassable)
- `S` — the start (exactly one)
- `E` — the exit (exactly one)
- a digit `1`–`9` — a locked door costing that many keys to enter

You start with a fixed budget of `K` keys. Every time you step onto a
locked-door cell — even one you've already been through — it costs that many
keys from your remaining balance. Keys never regenerate, and your balance may
never go negative.

**Implement:**

```
min_moves_to_escape(grid, K) -> int
```

Return the minimum number of moves needed to reach `E` without the key
balance ever dropping below zero, or `-1` if it can't be done within budget.

### Worked example

```
S.#.
.##.
.2..
##1E
```

- `K = 2` → `6` (the only way out is through the cost-2 door; the cost-1
  door doesn't help since it's a detour)
- `K = 1` → `-1` (the cost-2 door is mandatory and unaffordable)

### Constraints

- `1 ≤ rows, cols ≤ 200`
- `0 ≤ K ≤ 50`
- door costs are `1`–`9`
- exactly one `S` and one `E`, both on non-wall cells

## Layout

```
escape-the-vault-starter/
  test_data/
    simple/    <- 8 tiny, hand-traceable grids
    medium/    <- 5 bigger hand-designed grids, still traceable on paper
    hard/      <- 6 generated mazes — too large to solve by hand
  python/
    escape_vault.py    <- implement your solution here
    test_data.py         loads cases from ../test_data
    main.py               a small demo runner (prints one example)
    run_tests.py           the test harness — loops over every case, prints PASS/FAIL per tier
    scripts/
      compile.sh           syntax-checks the Python files
      run.sh                runs main.py
      test.sh               runs run_tests.py
  java/
    src/
      EscapeVault.java    <- implement your solution here
      TestData.java         loads cases from ../test_data
      Main.java              a small demo runner (prints one example)
      TestRunner.java         the test harness — loops over every case, prints PASS/FAIL per tier
    scripts/
      compile.sh           javac's everything into java/build
      run.sh                compiles, then runs Main
      test.sh               compiles, then runs TestRunner
```

You only need to edit `escape_vault.py` / `EscapeVault.java`. Everything else
is scaffolding: the test data, the demo runner, the test harness, and the
shell scripts are already wired up and shouldn't need changes.

Each solution file has a few empty helper methods already sketched out
(finding `S`/`E`, bounds checking, reading a door's cost) — feel free to use
them, change their signatures, or ignore them entirely and structure your
solution however you like. They're there to save you typing, not to dictate
your approach.

## Test data tiers

- **Simple** (`test_data/simple/`) — tiny grids (a handful of cells across).
  Good for checking your basic movement and budget logic by inspection.
- **Medium** (`test_data/medium/`) — bigger, hand-designed grids (up to 9×9).
  You can still trace a route on paper if you want to double-check an
  answer, but it takes real attention — one case forces you to add up
  several door costs along a single corridor, another makes you compare a
  short expensive route against a long free one.
- **Hard** (`test_data/hard/`) — generated mazes, 61×61 and 101×101, with
  loops (so more than one route exists) and scattered locked doors. These
  are big enough that solving them by hand isn't realistic — they're there
  to check that your solution is both *correct* and *efficient* at a size
  where that distinction actually shows up. If your test run hangs or takes
  a very long time on the `hard` tier, that's worth investigating — it's
  not a sign the test data is wrong.

## Quick start

Python (needs Python 3.8+, no other dependencies):

```bash
cd python
./scripts/test.sh     # run the test suite
./scripts/run.sh       # run the demo on one example grid
```

Java (needs a JDK on your PATH, no build tool required):

```bash
cd java
./scripts/test.sh     # compiles, then runs the test suite
./scripts/run.sh       # compiles, then runs the demo on one example grid
```

## Definition of done

`./scripts/test.sh` should print `TOTAL: 19 passed, 0 failed` in both
languages, with the `hard` tier finishing in well under a second. Every
test currently fails with `NOT IMPLEMENTED` until you fill in the solution.
