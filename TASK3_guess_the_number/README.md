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

## Projects Structure

```

TASK3_guess_the_number/
├── README.md                        # This documentation
├── guess_the_number_advanced.py     # The main game script
├── ranking.txt                      # Generated automatically on first play (rankings)
└── output_example_guess.png         # Screenshot example of gameplay
```

## Example Gameplay

Here's a short example of how the game looks when running (medium difficulty, successful guess):

```text
Welcome to Guess The Number! 🎉
What's your name? Suzana

I've thought of a number between 1 and 1000. You have up to 10 attempts!

Guess a number: 500
Too high! ↓   Attempts left: 9

Guess a number: 250
Too low! ↑    Attempts left: 8

Guess a number: 375
Too high! ↓   Attempts left: 7

Guess a number: 300
Too low! ↑    Attempts left: 6

Guess a number: 340
Congratulations, Suzana! 🎯 You guessed the number (340) in 5 attempts!

Current top 5 rankings:
1. Suzana    | 5 attempts | Win  | Number: 340
2. PlayerX   | 7 attempts | Win  | Number: 712
3. Anonymous | 8 attempts | Win  | Number: 199
4. TestUser  | 10 attempts| Win  | Number: 555
5. Suzana    | 4 attempts | Win  | Number: 88   (from previous game)

Play again? (y/n): 
```

## What This Project Practices

- Random number generation (random module)
- While loops and counters
- Input validation with try / except
- File reading and writing (open, with, append mode "a")
-  slicing to show recent lines (lines[-5:])
- output formatting with f-strings

## Author

Suzana Babarci
Python learning portfolio – 2026
GitHub: vipersuzy-star
X: @AnaBabarci
 Feel free to play it, fork it, or suggest new features! 






