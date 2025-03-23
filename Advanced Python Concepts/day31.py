# Advanced Python Concepts

# Day 31: Lambda Functions and Higher-Order Functions  


# Lambda Functions

'''
Lambda functions are anonymous functions that can be defined using the lambda keyword. They are used to create small, single-expression functions that can be passed as arguments to other functions.
'''

# Example

add = lambda x, y: x + y
print(add(2, 3))

# Higher-Order Functions

'''
Higher-order functions are functions that take other functions as arguments or return functions as results.'
'''

# Example

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def calculate(operation, x, y):
    return operation(x, y)

print(calculate(add, 2, 3))
print(calculate(subtract, 5, 2))

