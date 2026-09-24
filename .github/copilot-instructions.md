# Copilot Instructions for Slot-machine-

## Build, test, and lint

- This repository is a single-file Python console game; there is no package manager, build system, or CI configuration in the repo.
- Run the game directly with:
  - `python main.py`
- There is no automated test suite or lint config in this project.
- There is no single-test command to run; validation currently consists of manual smoke tests by launching the script and checking the interactive prompts and payout flow.
- If you add automation later, keep it lightweight and compatible with the script's stdin-driven gameplay rather than introducing a full app framework.

## High-level architecture

- The entire game lives in `main.py`.
- The script starts at the top level, reads the starting bankroll from `input()`, asks how many wheels to play with, and then enters a continuous loop.
- Each loop iteration:
  - generates random results for 3–5 wheels via `random.choice(wheel1)`
  - prompts for the bet amount and optional “specific number” wager
  - animates the spin output with `time.sleep(...)`
  - evaluates win/loss logic based on the chosen wheel count and payout rules
  - updates the money balance and tracking counters
  - exits when the bankroll reaches zero or the player quits
- The win rules, display text, validation, and state updates are all embedded in the same script instead of being separated into a game engine, model layer, or UI layer.
- `README.md` is intentionally minimal, so the actual implementation in `main.py` is the primary source of truth for behavior.

## Key conventions

- Keep project changes focused on `main.py` unless a bigger refactor is explicitly requested; there is no package structure or module layout to extend.
- The script uses module-level mutable state (`money`, `bet`, `wheels`, `spins`, `succesful_spins`, `unsuccesful_spins`, etc.). Preserve this structure for small fixes rather than introducing classes or helpers unless the task clearly calls for a refactor.
- The game is intentionally input-driven and terminal-based: prompt text, validation loops, and balance updates are all interleaved in one flow.
- Balance and payout calculations are integer-based and must stay consistent with the game rules for the `all in`, `3-wheel`, `4-wheel`, and `5-wheel` cases.
- Avoid broad cleanup or reorganization while fixing a bug; this repo is a small demo project and surgical changes are the expected style.
