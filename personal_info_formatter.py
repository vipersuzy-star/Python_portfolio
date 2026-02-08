# personal_info_formatter.py
# Portfolio Task 1 – Basics: variables, input, f-strings, type conversion, simple math + colors

# ANSI escape codes
BLACK_BG = "\033[40m"
RESET    = "\033[0m"
CYAN     = "\033[36m"
MAGENTA  = "\033[35m"
YELLOW   = "\033[33m"
GREEN    = "\033[32m"
RED      = "\033[31m"
WHITE    = "\033[37m"

# -------------------------------
# YOUR DATA – EDIT THESE!
# -------------------------------
name           = "VIPERSUZY-STAR"
age            = 40
height_cm      = 168.0
favorite_color = "red"
average_sleep  = 7.5
weight_kg      = 62.0
occupation     = "Aspiring Python Developer"
favorite_quote = "The best way to predict the future is to create it. – Peter Drucker"

# -------------------------------
print("\n" + BLACK_BG)

print(CYAN + "=" * 70 + RESET)
print(CYAN + f" {name.upper()}'S PROFILE ".center(70) + RESET)
print(CYAN + "=" * 70 + RESET)
print()

def print_field(label, value, value_color=WHITE, emoji=""):
    print(f"{CYAN}{label:<18}{RESET} {value_color}{value}{RESET} {emoji}")

print_field("Name", name, WHITE, "✨")
print_field("Age", f"{age} years", YELLOW, "🎂")
print_field("Height", f"{height_cm:.1f} cm", WHITE, "📏")

color_emoji = "❤️" if "red" in favorite_color.lower() else "💜" if "purple" in favorite_color.lower() else "🌈"
print_field("Favorite color", favorite_color.capitalize(), MAGENTA, color_emoji)

# Sleep comment
if average_sleep >= 8:
    sleep_text = f"{GREEN}You rest very well! 😴✨{RESET}"
elif average_sleep >= 7:
    sleep_text = f"{YELLOW}Nice average, healthy range! 👍{RESET}"
else:
    sleep_text = f"{RED}Try to sleep more! 💤{RESET}"

print_field("Average sleep", f"{average_sleep:.1f} h/day → {sleep_text}", WHITE)

# BMI
if weight_kg > 0:
    bmi = round(weight_kg / ((height_cm / 100) ** 2), 1)
    if bmi < 18.5:
        cat = f"{YELLOW}underweight{RESET}"
    elif bmi < 25:
        cat = f"{GREEN}normal{RESET}"
    elif bmi < 30:
        cat = f"{YELLOW}overweight{RESET}"
    else:
        cat = f"{RED}obese{RESET}"
    print_field("BMI", f"{bmi} → {cat}", WHITE, "⚖️")
else:
    print_field("BMI", "Not calculated (no weight)", RED)

print_field("Occupation", occupation, GREEN, "💻")

# Quote
print()
try:
    quote_text, author = favorite_quote.rsplit(" – ", 1)
    author = author.strip()
except ValueError:
    quote_text = favorite_quote
    author = "Unknown author"

print(MAGENTA + f"“{quote_text.strip()}”{RESET}")
print(f"   – {author}".center(70))
print()

print(CYAN + "=" * 70 + RESET)
print(RESET)
print("   Created by Suzana / VIPERSUZY-STAR – Python practice 🚀🐍\n")