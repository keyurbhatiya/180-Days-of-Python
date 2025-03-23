# Day 37: Practice Problems 

'''
In this day, we will practice problems using decorators in Python. Decorators are functions that can be used to modify the behavior of other functions.
'''

# Example

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def greet():
    return "hello world"

print(greet())

# Output
# HELLO WORLD