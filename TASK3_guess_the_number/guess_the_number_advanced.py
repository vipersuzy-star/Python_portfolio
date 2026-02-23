# guess_the_number_advanced.py
# Portfolio Task 3 – Loops, file handling, input validation
# Vipersuzy-star – Python learning 2026

import random

# Ranking file name
RANKING_FILE = "ranking.txt"

print("\n" + "=" * 60)
print(" GUESS THE NUMBER GAME – Advanced Version ".center(60))
print("=" * 60 + "\n")

# Get player's name
player_name = input("Enter your name: ").strip()
if not player_name:
    player_name = "Anonymous"

print(f"\nWelcome, {player_name}! I've thought of a number between 1 and 1000.")
print("You have a maximum of 10 attempts!\n")

# Generate secret number
secret_number = random.randint(1, 1000)
max_attempts = 10
attempts = 0
guessed = False

while attempts < max_attempts:
    attempts += 1
    
    # Get and validate input
    try:
        guess = int(input(f"{attempts}. attempt / {max_attempts} – Your guess: "))
    except ValueError:
        print("Please enter a whole number only!")
        continue  # Doesn't count as an attempt
    
    # Correct guess
    if guess == secret_number:
        print(f"\nCongratulations, {player_name}! You guessed it in {attempts} attempts! 🎉")
        guessed = True
        break
    
    # Hints
    elif guess < secret_number:
        print("Too low! Try a bigger number ↑")
    else:
        print("Too high! Try a smaller number ↓")
    
    print(f"You have {max_attempts - attempts} attempts left.\n")

# If not guessed
if not guessed:
    print(f"\nSorry, {player_name}, you've run out of attempts.")
    print(f"The secret number was {secret_number}. 😔")

# Save result to ranking (append mode)
result = "Success" if guessed else "Failed"
line = f"{player_name} | {attempts} attempts | {result} | Secret number: {secret_number}\n"

with open(RANKING_FILE, "a", encoding="utf-8") as f:
    f.write(line)

# Display ranking (last 5 entries)
print("\n" + "-" * 60)
print("Ranking (last 5 results):")
print("-" * 60)

try:
    with open(RANKING_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # Last 5 lines (or fewer if not enough)
        recent = lines[-5:]
        for line in recent:
            print(line.strip())
except FileNotFoundError:
    print("No ranking yet – this will be the first entry!")

print("-" * 60)
print("\nThanks for playing! Try again anytime 🚀🐍\n")