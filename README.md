# Scientific Calculator with GUI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A full-featured scientific calculator with graphical user interface (GUI) built using Python and Tkinter. Supports basic arithmetic operations, scientific functions, and constants.

<p align="center">
  <img src="https://github.com/user-attachments/assets/656385d0-4b8e-45fd-bc00-231129cdea21" width="400">
</p>

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Scientific Functions**:
  - Logarithms (log<sub>10</sub> and ln)
  - Powers (x<sup>y</sup>)
  - Square roots (√)
- **Parentheses Support**: Complex expressions with nested parentheses
- **Constants**: π (Pi) and e (Euler's number)
- **GUI Features**:
  - Backspace button (⌫) to delete single characters
  - Clear button (C) to reset input
  - Real-time expression display
  - Error handling for invalid expressions

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually comes pre-installed with Python)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/scientific-calculator.git
cd scientific-calculator
```

2. Run the calculator
```bash
python scientific_calculator.py
```

## Usage
1. Basic Operations:
 - Click number buttons (0-9) to input digits
 - Use operator buttons (+, -, *, /) for arithmetic operations
 - Press "=" to evaluate the expression

2. Scientific Functions:
.`log` for base-10 logarithm
.`ln` for natural logarithm
.`x^y` for power operations (e.g., 2^3 = 8)
.`√` for square root

3. Special Features:
.`⌫` removes the last entered character
.`C` clears the entire input
.Use `(` and `)` for parentheses
.Access constants `π` and `e` with dedicated buttons

## Code Structure
```
scientific_calculator.py
├── Calculator Class
│   ├── __init__() - Initializes GUI and variables
│   ├── create_display() - Creates input display
│   ├── create_buttons() - Creates button layout
│   ├── click_button() - Handles button presses
│   ├── clear() - Resets calculator
│   ├── backspace() - Deletes last character
│   └── evaluate() - Calculates results
```

## Implementation Details
.GUI Framework: Built with Tkinter for cross-platform compatibility
.Math Engine: Uses Python's eval() with safety checks
.Error Handling: Catches invalid expressions and displays errors
.Constants: Implements math.pi (π) and math.e (e) from Python's math module

## Possible extensions
.Add trigonometric functions (sin, cos, tan)
.Implement memory functions (M+, M-, MR)
.Add keyboard input support
.Create history tracking of calculations
.Add theme customization options

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
lucalevi - [GitHub](https://github.com/lucalevi)
