# TASK3 - Guess The Number (Advanced)

A fun console-based number guessing game built in Python.  
You have 10 attempts to guess a secret number between 1 and 1000. Includes name input, hints, input validation, and a simple persistent ranking system saved to a file.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## Features

- Enter your name (or play as "Anonymous")
- Secret number randomly chosen from 1 to 1000
- Maximum 10 guesses
- Helpful hints: "Too low ↑" or "Too high ↓"
- Input validation – only numbers count as attempts
- Results saved to `ranking.txt` (name | attempts | result | secret number)
- Shows the last 5 rankings after each game
- Friendly messages and emojis 🎉😔🚀

## How to Run

1. Make sure you have Python 3.8 or newer installed.
2. Go to the `TASK3_guess_the_number` folder in your terminal.
3. Run the game:

   ```bash
   python guess_the_number_advanced.py

 (On some systems use python3 instead of python)The file ranking.txt will be created automatically when you finish your first game.

## Folder Structure

Python_portfolio/
└── TASK3_guess_the_number/
    ├── guess_the_number_advanced.py     # the game script
    ├── ranking.txt                      # created automatically (example rankings)
    ├── README.md                        # this file
    └── output_example_guess.png         # screenshot of the game running

## Example Gameplay

Gameplay Screenshot
(Your screenshot showing up to 5 attempts – you can replace it later with a full game if you want)

## What This Project Practices

Random number generation (random module)
While loops and counters
Input validation with try / except
File reading and writing (open, with, append mode "a")
List slicing to show recent lines (lines[-5:])
Clean output formatting with f-strings

## Author

Suzana Babarci
Python learning portfolio – 2026
GitHub: vipersuzy-star
X: @AnaBabarci
  Feel free to play it, fork it, or suggest new features! 




