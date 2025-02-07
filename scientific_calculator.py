import tkinter as tk

# from tkinter import ttk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        # Display frame
        display_frame = tk.Frame(
            self.root,
            width=400,
            height=50,
            bd=0,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=1,
        )
        display_frame.pack(side=tk.TOP)

        # Input field
        input_field = tk.Entry(
            display_frame,
            font=("arial", 18, "bold"),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=tk.RIGHT,
        )
        input_field.pack(ipady=10)

    def create_buttons(self):
        # Button frame
        buttons_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        buttons_frame.pack()

        # First row
        clear = tk.Button(
            buttons_frame,
            text="C",
            fg="black",
            width=21,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self.clear,
        )
        clear.grid(row=0, column=0, columnspan=2)
        backspace = tk.Button(
            buttons_frame,
            text="⌫",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self.backspace,
        )
        backspace.grid(row=0, column=2)
        divide = tk.Button(
            buttons_frame,
            text="/",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("/"),
        )
        divide.grid(row=0, column=3)

        # Second row
        seven = tk.Button(
            buttons_frame,
            text="7",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(7),
        )
        seven.grid(row=1, column=0)
        eight = tk.Button(
            buttons_frame,
            text="8",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(8),
        )
        eight.grid(row=1, column=1)
        nine = tk.Button(
            buttons_frame,
            text="9",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(9),
        )
        nine.grid(row=1, column=2)
        multiply = tk.Button(
            buttons_frame,
            text="*",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("*"),
        )
        multiply.grid(row=1, column=3)

        # Third row
        four = tk.Button(
            buttons_frame,
            text="4",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(4),
        )
        four.grid(row=2, column=0)
        five = tk.Button(
            buttons_frame,
            text="5",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(5),
        )
        five.grid(row=2, column=1)
        six = tk.Button(
            buttons_frame,
            text="6",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(6),
        )
        six.grid(row=2, column=2)
        subtract = tk.Button(
            buttons_frame,
            text="-",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("-"),
        )
        subtract.grid(row=2, column=3)

        # Fourth row
        one = tk.Button(
            buttons_frame,
            text="1",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(1),
        )
        one.grid(row=3, column=0)
        two = tk.Button(
            buttons_frame,
            text="2",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(2),
        )
        two.grid(row=3, column=1)
        three = tk.Button(
            buttons_frame,
            text="3",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(3),
        )
        three.grid(row=3, column=2)
        add = tk.Button(
            buttons_frame,
            text="+",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("+"),
        )
        add.grid(row=3, column=3)

        # Fifth row
        zero = tk.Button(
            buttons_frame,
            text="0",
            fg="black",
            width=21,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self.click_button(0),
        )
        zero.grid(row=4, column=0, columnspan=2)
        point = tk.Button(
            buttons_frame,
            text=".",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("."),
        )
        point.grid(row=4, column=2)
        equals = tk.Button(
            buttons_frame,
            text="=",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self.evaluate,
        )
        equals.grid(row=4, column=3)

        # Sixth row (Scientific functions)
        log = tk.Button(
            buttons_frame,
            text="log",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("log("),
        )
        log.grid(row=5, column=0)
        ln = tk.Button(
            buttons_frame,
            text="ln",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("ln("),
        )
        ln.grid(row=5, column=1)
        power = tk.Button(
            buttons_frame,
            text="x^y",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("^"),
        )
        power.grid(row=5, column=2)
        sqrt = tk.Button(
            buttons_frame,
            text="√",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("sqrt("),
        )
        sqrt.grid(row=5, column=3)

        # Seventh row
        left_paren = tk.Button(
            buttons_frame,
            text="(",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("("),
        )
        left_paren.grid(row=6, column=0)
        right_paren = tk.Button(
            buttons_frame,
            text=")",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button(")"),
        )
        right_paren.grid(row=6, column=1)
        pi = tk.Button(
            buttons_frame,
            text="π",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("pi"),
        )
        pi.grid(row=6, column=2)
        e = tk.Button(
            buttons_frame,
            text="e",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.click_button("e"),
        )
        e.grid(row=6, column=3)

    def click_button(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def backspace(self):
        self.expression = self.expression[:-1]  # Remove the last character
        self.input_text.set(self.expression)

    def evaluate(self):
        try:
            # Replace custom symbols with Python-compatible ones
            self.expression = self.expression.replace("^", "**")
            self.expression = self.expression.replace("log", "math.log10")
            self.expression = self.expression.replace("ln", "math.log")
            self.expression = self.expression.replace("sqrt", "math.sqrt")
            self.expression = self.expression.replace("pi", str(math.pi))
            self.expression = self.expression.replace("e", str(math.e))

            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
