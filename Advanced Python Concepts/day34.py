# Day 34: Decorators in Python  

''''
In this day, we will learn about decorators in Python. Decorators are functions that can be used to modify the behavior of other functions.
'''

# Decorators

''''
A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
'''

# Example

def decorator_function(func):
    def wrapper_function():
        print("This is before the function call.")
        func()
        print("This is after the function call.")
    return wrapper_function

@decorator_function
def my_function():
    print("This is the function being decorated.")

my_function()
