# Rock, Paper, Scissors Game

A simple command-line implementation of the classic Rock, Paper, Scissors game.

## How to Play

Run the game using Python 3:

```bash
python3 rock_paper_scissors.py
```

Or run it directly (if executable):

```bash
./rock_paper_scissors.py
```

## Game Rules

- **Rock beats Scissors** ✊ > ✌️
- **Scissors beats Paper** ✌️ > ✋
- **Paper beats Rock** ✋ > ✊
- Same choices result in a tie

## Features

- ✅ Interactive command-line interface
- ✅ Computer randomly selects its choice
- ✅ Clear display of both choices and results
- ✅ Score tracking across multiple rounds
- ✅ Win rate statistics
- ✅ Input validation with helpful error messages
- ✅ Support for both full names (rock/paper/scissors) and shortcuts (r/p/s)
- ✅ Case-insensitive input
- ✅ Graceful exit handling

## Input Options

You can enter your choice in multiple ways:

- Full name: `rock`, `paper`, `scissors` (case-insensitive)
- Shortcuts: `r`, `p`, `s`

## Examples

```
Enter your choice (rock/paper/scissors): rock
You chose: ROCK
Computer chose: SCISSORS
----------------------------------------
🎉 YOU WIN! 🎉
```

```
Enter your choice (rock/paper/scissors): p
You chose: PAPER
Computer chose: PAPER
----------------------------------------
🤝 IT'S A TIE! 🤝
```

## Exit the Game

Type `no` or `n` when asked "Do you want to play again?" to exit the game and see your final statistics.

You can also press `Ctrl+C` at any time to exit gracefully.
