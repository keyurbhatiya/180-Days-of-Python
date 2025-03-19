# Day 25: Raising and Custom Exceptions

''''
In this day, we will learn about raising and custom exceptions in Python.   
'''

# Raising Exceptions

''''
Raising an exception allows you to explicitly signal a condition that indicates an error has occurred.
'''

# Example

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero") # This will raise a ValueError
    return a / b

try:
    result = divide(10, 0) # This will raise a ValueError
    print(result)
except ValueError as e: # This will catch the ValueError
    print(e) # This will print the error message


# Custom Exceptions

''''
You can create your own custom exceptions by subclassing the built-in Exception class.
'''

# Example

class CustomException(Exception):
    pass

try:
    
    raise CustomException("This is a custom exception") # This will raise a CustomException
except CustomException as e: # This will catch the CustomException
    print(e) # This will print the error message


# Summary