# Slot-machine-

A small terminal-based slot machine game written in Python.

## Overview

`Slot-machine-` is a simple text-based casino game where the player starts with a bankroll, chooses the number of wheels to play, places a bet, and tries to hit matching results. The game is entirely driven from the terminal using standard input and output.

## Requirements

- Python 3

## Run the game

```bash
python main.py
```

## How to play

1. Enter how much money you have.
2. Choose the number of wheels:
   - `3` wheels
   - `4` wheels
   - `5` wheels
3. Enter a bet amount or type `all in` to bet your entire bankroll.
4. Decide whether to wager on a specific number for a higher-risk, higher-reward outcome.
5. Watch the animation, then see whether your spin wins or loses.
6. Continue until you quit or your balance reaches zero.

## Game mechanics

- The game uses a small random wheel set of numbers from `1` to `3`.
- Matching results determine the win condition depending on the selected wheel count.
- `3`-wheel, `4`-wheel, and `5`-wheel sessions have different payout rules.
- A special “specific number” bet increases the risk and reward, depending on the selected mode.
- The script tracks total spins, wins, losses, and win percentage before ending the session.

## Notes

This project is intentionally lightweight and self-contained: the entire game logic and UI live in `main.py`, with no separate modules, frameworks, or automated test suite.
