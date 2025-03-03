# Day 6: Functions and Scope  


# Function

'''
Function is a block of code that performs a specific task. It can be called by other functions or by the program itself. A function can be defined using the def keyword.
'''

# Example

def my_function():
    print("Hello from a function")

my_function()


# Scope

'''
The scope of a variable is the region in a program where that variable is accessible. The scope of a variable can be either global or local.
'''

# Example

print("Scope")

x = 10 # Global variable

def my_function():
    x = 20 # Local variable
    print(x)

my_function()
print(x)