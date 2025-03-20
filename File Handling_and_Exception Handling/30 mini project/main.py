# Day 30: Revision and Mini Project (Basic CLI Tool)

# In this day, we will create a basic command-line interface (CLI) tool using Python.
# The CLI tool will allow users to perform basic operations such as adding, subtracting, multiplying, and dividing two numbers.

# Example

import sys

def calculator():
    print("Basic CLI Calculator")
    print("Enter your operation (add, subtract, multiply, divide):")
    operation = input("Operation: ").strip().lower()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation.")

        print(f"The result is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
