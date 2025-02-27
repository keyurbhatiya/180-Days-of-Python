# Day 2: Variables, Data Types, and Basic I/O


# python Variables

'''
Creating Python Variables
Python variables do not need explicit declaration to reserve memory space or you can say to create a variable. A Python variable is created automatically when you assign a value to it. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable
'''

# Example

counter = 100               # Creates an integer variable
miles   = 1000.0            # Creates a floating point variable
name    = "Keyur Bhatiya"   # Creates a string variable

print (counter)
print (miles)
print (name)



# Python Data Types

'''
Python data types are actually classes, and the defined variables are their instances or objects. Since Python is dynamically typed, the data type of a variable is determined at runtime based on the assigned value.
'''

# Numeric Data Types
'''
    int
    flot
    complex
'''

# String Data Types

# Sequence Data Types
'''
    list
    tuple
    range
'''

# Binary Data Types
'''
    bytes
    bytearray
    memoryview
'''

# Dictionary Data Type

# Set Data Type

'''
    set
    frozenset
'''
# Boolean Data Type

# None Type


# Python Basic I/O

# Basic I/O in Python involves taking input from the user or a file and displaying or storing output


# Input
'''
input(): This function prompts the user for input from the console. It always returns a string, which might need to be converted to another data type using functions like int() or float().
'''

name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
print(f"Hello, {name}! You are {age} years old.")

# Output
'''
print(): This function displays output to the console. It can take multiple arguments, including variables, strings, and expressions.
'''

x = 10
y = 20
print("The sum of", x, "and", y, "is", x + y)
print(f"The sum of {x} and {y} is {x + y}") # using f-strings
