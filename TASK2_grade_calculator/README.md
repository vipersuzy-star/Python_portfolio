# Grade Calculator

A simple Python program that converts a numerical score (0–100) into a Hungarian-style grade (1–5) with encouraging feedback messages.  
Implemented in two versions to compare classic conditional logic with modern structural pattern matching.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Last Commit](https://img.shields.io/github/last-commit/vipersuzy-star/Python_portfolio?style=flat)

## Features

- Accepts scores as integers or decimals (e.g. 88.5)
- Validates input: must be number between 0 and 100
- Two implementation approaches:
  - Classic `if/elif/else`
  - Modern `match-case` (Python 3.10+)
- Colorful terminal output using ANSI escape codes
- Friendly error messages for invalid input

## Grade Mapping

| Score     | Grade | Message (example)                          |
|-----------|-------|--------------------------------------------|
| ≥ 90      | 5     | Excellent! Very proud of you! 🌟          |
| ≥ 80      | 4     | Good job! Keep it up! 👍                  |
| ≥ 70      | 3     | Satisfactory. Room for improvement.       |
| ≥ 60      | 2     | Passable. Study more next time!           |
| < 60      | 1     | Fail. Don't give up, keep practicing! 💪  |

## How to Run

1. Make sure you have **Python 3.10 or higher** installed.
2. Clone or download this repository.
3. Navigate to the `grade_calculator` folder (or wherever you placed the scripts).
4. Run either version:

   ```bash
   # If/elif/else version
   python solution_if_version.py

   # match-case version (recommended if using Python 3.10+)
   python solution_match_version.py


## Project Structure

Python_portfolio/
└── grade_calculator/
    ├── README.md                       # Project documentation (this file)
    ├── solution_if_version.py          # if/elif/else implementation
    ├── solution_match_version.py       # match-case implementation
    ├── output_example_if.png           # screenshot of colorful output from if-version
    └── output_example_match.png        # screenshot of colorful output from match-case version



## Example Output

### If / Elif / Else Version

![If Version Output](output_example_if.png)

---

### Match-Case Version (Python 3.10+)

![Match Version Output](output_example_match.png)

## Author

Created by Babarci Szuzana  
Python learning portfolio project
