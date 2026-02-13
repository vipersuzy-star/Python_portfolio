# Simple Grade Calculator – match-case version (Python 3.10+)
# Suzana Babarci – Python Portfolio 2026

# ANSI color codes
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

def calculate_grade_match(score):
    if not isinstance(score, (int, float)):
        return f"{RED}ERROR: Input must be a number!{RESET}"
    
    if score < 0 or score > 100:
        return f"{RED}ERROR: Score must be between 0 and 100!{RESET}"
    
    # match-case with guards
    match score:
        case p if p >= 90:
            return f"{GREEN}5 (Excellent! Very proud of you! 🌟){RESET}"
        case p if p >= 80:
            return f"{GREEN}4 (Good job! Keep it up! 👍){RESET}"
        case p if p >= 70:
            return f"{YELLOW}3 (Satisfactory. Room for improvement.){RESET}"
        case p if p >= 60:
            return f"{YELLOW}2 (Passable. Study more next time!){RESET}"
        case _:
            return f"{RED}1 (Fail. Don't give up, keep practicing! 💪){RESET}"

# Main program
print(f"{BLUE}{BOLD}=== Simple Grade Calculator (match-case version) ==={RESET}\n")

try:
    user_input = input("Enter your score (0-100): ").strip()
    score_value = float(user_input)
    
    result = calculate_grade_match(score_value)
    print(f"\n{BLUE}Result: {result}{RESET}")
    
except ValueError:
    print(f"\n{RED}ERROR: Please enter a valid number!{RESET}")