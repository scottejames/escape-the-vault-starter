<p align="center">
  <img src="logo.svg" alt="Escape the Vault" width="760">
</p>

# Escape the Vault — starter project

Somewhere below street level, a small robot has just woken up in a vault
it was never meant to see the inside of. The door's sealed, the corridors
twist back on themselves, and scattered through the place are locked
doors that won't budge for anything less than the exact number of keys
they're asking for. Nobody's coming to let it out.

That's where you come in. This repo is the robot's brain, waiting to be
written — in Python or Java, whichever you're happier in. Both are graded
the same way, so pick on comfort, not on which one you think looks better.

## The problem

The robot starts at `S` and has to reach the exit `E`, moving one cell at
a time — up, down, left, right, no cutting corners diagonally. The floor
it's standing on is made of:

- `.` — open floor, safe to cross
- `#` — a wall, solid, going nowhere
- `S` — the start (there's exactly one)
- `E` — the exit (also exactly one — that's the whole plan)
- a digit `1`–`9` — a locked door, and the number is exactly how many
  keys it costs to force it open

The robot arrives with a fixed budget of `K` keys already in its pocket.
Step onto a locked door — even one it's already forced open once before —
and that many keys are spent on the spot. Keys don't grow back, and the
robot is far too sensible to run a negative balance: it will never take a
door it can't afford.

**Your job:**

```
min_moves_to_escape(grid, K) -> int
```

Work out the fewest moves it takes to get the robot from `S` to `E`
without the key balance ever dipping below zero. If there's genuinely no
way out on that budget, say so honestly — return `-1`.

### Worked example

```
S.#.
.##.
.2..
##1E
```

- `K = 2` → `6`. The only way out runs through the cost-2 door — the
  cost-1 door looks interesting but it's a dead-end detour, not a
  shortcut.
- `K = 1` → `-1`. That cost-2 door isn't optional, and one key won't
  cover it.

Want a slower, more thorough walk through a case like this, at three
different key budgets? See [EXAMPLE.md](EXAMPLE.md).

### Constraints

Nothing sneaky here — just the numbers to design around:

- `1 ≤ rows, cols ≤ 200`
- `0 ≤ K ≤ 50`
- door costs are `1`–`9`
- exactly one `S` and one `E`, and neither is buried inside a wall

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
    run_tests.py           the test harness — every case, PASS/FAIL, timing, an efficiency band
    scripts/
      compile.sh           syntax-checks the Python files
      run.sh                runs main.py
      test.sh               runs run_tests.py
  java/
    src/
      EscapeVault.java    <- implement your solution here
      TestData.java         loads cases from ../test_data
      Main.java              a small demo runner (prints one example)
      TestRunner.java         the test harness — every case, PASS/FAIL, timing, an efficiency band
    scripts/
      compile.sh           javac's everything into java/build
      run.sh                compiles, then runs Main
      test.sh               compiles, then runs TestRunner
```

You only need to touch `escape_vault.py` / `EscapeVault.java` — everything
else is scaffolding that's already wired up and ready to go: the test
data, the demo runner, the test harness, the shell scripts.

Each solution file has a handful of empty helper methods already sketched
in (finding `S`/`E`, checking you're still on the grid, reading a door's
cost). Use them, rename them, rip them out entirely — whatever gets you
to a solution you're happy with. They're there to save you some typing,
not to tell you how to think about the problem.

## Test data tiers

- **Simple** (`test_data/simple/`) — a handful of cells across, small
  enough to check your movement and budget logic just by looking at it.
- **Medium** (`test_data/medium/`) — bigger, hand-designed grids (up to
  9×9). You can still trace a route on paper if you want to sanity-check
  an answer, but it takes real attention — one case has you adding up
  several door costs along a single corridor, another has you weighing a
  short expensive route against a long free one.
- **Hard** (`test_data/hard/`) — proper mazes, 61×61 and 101×101, with
  loops (more than one way through) and locked doors scattered around.
  Nobody's tracing these by hand — they exist to check that your solution
  is not just *correct* but *efficient*, at a size where the difference
  actually shows up. If a run hangs or drags on the `hard` tier, that's
  worth digging into — the maze isn't broken, your approach probably
  needs a rethink.

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
languages, ending with `Efficiency band: Efficient (< 2s total)`. Right
now every test fails with `NOT IMPLEMENTED` — that's your starting line,
not a bug.

That last line is reading the `hard` tier's total time: `Efficient` under
2 seconds, `Adequate` up to 10, `Slow` beyond that. A correct, reasonably
efficient solution should land comfortably in `Efficient`. If you're
seeing `Adequate` or `Slow`, or the hard tier just never finishes, take
that seriously — it's telling you something real about your approach, not
just filling space at the bottom of the output.

Good luck. The robot's counting on you.
