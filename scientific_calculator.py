"""
Scientific Calculator with GUI

This Python script implements a full-featured scientific calculator with a
graphical user interface (GUI).
The calculator supports basic arithmetic operations (addition, subtraction,
multiplication, division), scientific functions (logarithms, square roots, powers),
and constants (π and e). It also includes a backspace button to delete single
digits or symbols and a clear button to reset the input.

The GUI is built using the `tkinter` library, and mathematical operations are
handled using Python's built-in `math` module.

Author: DeepSeek
Date: 2023-10-05
"""

import tkinter as tk
import math


class Calculator:
    """
    A class representing a scientific calculator with a graphical user interface.

    Attributes:
        root (tk.Tk): The main window of the calculator.
        expression (str): The current mathematical expression entered by the user.
        input_text (tk.StringVar): A variable to store and display the current
            input expression.
    """

    def __init__(self, root):
        """
        Initializes the Calculator class.

        Args:
            root (tk.Tk): The main window of the application.
        """
        self.root = root
        self.root.title("Scientific Calculator")  # Set the title of the window
        self.root.geometry("500x500")  # Set the size of the window
        self.root.resizable(False, False)  # Make the window non-resizable

        self.expression = ""  # Stores the current mathematical expression
        self.input_text = (
            tk.StringVar()
        )  # Variable to display the expression in the input field

        self.create_display()  # Create the display area
        self.create_buttons()  # Create the buttons for the calculator

    def create_display(self):
        """
        Creates the display area where the input expression and result are shown.
        """
        # Create a frame to hold the display
        display_frame = tk.Frame(
            self.root,
            width=400,
            height=50,
            bd=0,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )
        display_frame.pack(side=tk.TOP)  # Place the frame at the top of the window

        # Create an input field to display the expression
        input_field = tk.Entry(
            display_frame,
            font=("arial", 18, "bold"),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=tk.RIGHT,
        )
        input_field.pack(ipady=10)  # Add padding to the input field

    def create_buttons(self):
        """
        Creates and arranges all the buttons for the calculator.
        """
        # Create a frame to hold the buttons
        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        buttons_frame.pack()

        # Define button labels and their positions
        buttons = [
            ("C", 0, 0, 2, self.clear),  # Clear button (spans 2 columns)
            ("⌫", 0, 2, 1, self.backspace),  # Backspace button
            ("/", 0, 3, 1, lambda: self.click_button("/")),  # Division button
            ("7", 1, 0, 1, lambda: self.click_button(7)),  # Number 7
            ("8", 1, 1, 1, lambda: self.click_button(8)),  # Number 8
            ("9", 1, 2, 1, lambda: self.click_button(9)),  # Number 9
            ("*", 1, 3, 1, lambda: self.click_button("*")),  # Multiplication button
            ("4", 2, 0, 1, lambda: self.click_button(4)),  # Number 4
            ("5", 2, 1, 1, lambda: self.click_button(5)),  # Number 5
            ("6", 2, 2, 1, lambda: self.click_button(6)),  # Number 6
            ("-", 2, 3, 1, lambda: self.click_button("-")),  # Subtraction button
            ("1", 3, 0, 1, lambda: self.click_button(1)),  # Number 1
            ("2", 3, 1, 1, lambda: self.click_button(2)),  # Number 2
            ("3", 3, 2, 1, lambda: self.click_button(3)),  # Number 3
            ("+", 3, 3, 1, lambda: self.click_button("+")),  # Addition button
            ("0", 4, 0, 2, lambda: self.click_button(0)),  # Number 0 (spans 2 columns)
            (".", 4, 2, 1, lambda: self.click_button(".")),  # Decimal point
            ("=", 4, 3, 1, self.evaluate),  # Equals button
            ("log", 5, 0, 1, lambda: self.click_button("log(")),  # Logarithm button
            (
                "ln",
                5,
                1,
                1,
                lambda: self.click_button("ln("),
            ),  # Natural logarithm button
            ("x^y", 5, 2, 1, lambda: self.click_button("^")),  # Power button
            ("√", 5, 3, 1, lambda: self.click_button("sqrt(")),  # Square root button
            ("(", 6, 0, 1, lambda: self.click_button("(")),  # Left parenthesis
            (")", 6, 1, 1, lambda: self.click_button(")")),  # Right parenthesis
            ("π", 6, 2, 1, lambda: self.click_button("pi")),  # Pi constant
            ("e", 6, 3, 1, lambda: self.click_button("e")),  # Euler's number
        ]

        # Create and place buttons in the grid
        for text, row, col, colspan, command in buttons:
            button = tk.Button(
                buttons_frame,
                text=text,
                fg="black",
                width=10 if colspan == 1 else 21,
                height=3,
                bd=0,
                bg="#eee"
                if text
                in [
                    "C",
                    "⌫",
                    "/",
                    "*",
                    "-",
                    "+",
                    "=",
                    "log",
                    "ln",
                    "x^y",
                    "√",
                    "(",
                    ")",
                    "π",
                    "e",
                ]
                else "#fff",
                cursor="hand2",
                command=command,
            )
            button.grid(row=row, column=col, columnspan=colspan)

    def click_button(self, item):
        """
        Handles button clicks by appending the clicked item to the expression.

        Args:
            item (str or int): The button's value (e.g., a number, operator, or function).
        """
        self.expression += str(item)  # Append the clicked item to the expression
        self.input_text.set(self.expression)  # Update the display

    def clear(self):
        """
        Clears the entire expression and resets the display.
        """
        self.expression = ""  # Reset the expression
        self.input_text.set("")  # Clear the display

    def backspace(self):
        """
        Removes the last character from the expression.
        """
        self.expression = self.expression[:-1]  # Remove the last character
        self.input_text.set(self.expression)  # Update the display

    def evaluate(self):
        """
        Evaluates the current expression and displays the result.
        """
        try:
            # Replace custom symbols with Python-compatible ones
            self.expression = self.expression.replace("^", "**")  # Convert power symbol
            self.expression = self.expression.replace(
                "log", "math.log10"
            )  # Convert log to math.log10
            self.expression = self.expression.replace(
                "ln", "math.log"
            )  # Convert ln to math.log
            self.expression = self.expression.replace(
                "sqrt", "math.sqrt"
            )  # Convert sqrt to math.sqrt
            self.expression = self.expression.replace(
                "pi", str(math.pi)
            )  # Replace pi with its value
            self.expression = self.expression.replace(
                "e", str(math.e)
            )  # Replace e with its value

            result = str(eval(self.expression))  # Evaluate the expression
            self.input_text.set(result)  # Display the result
            self.expression = result  # Update the expression with the result
        except Exception as e:
            self.input_text.set("Error")  # Display "Error" if evaluation fails
            self.expression = ""  # Reset the expression


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    calc = Calculator(root)  # Initialize the calculator
    root.mainloop()  # Start the GUI event loop
