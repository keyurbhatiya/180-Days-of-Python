# Day 24: Exception Handling (try, except, finally) 

# try 

'''
The try block is used to define a block of code that may raise an exception.
'''

# Example

try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero")

# except

'''
The except block is used to define a block of code that should be executed if an exception occurs in the try block.
'''

# Example

try:
    x = open("file.txt", "r")
    print(x)
except FileNotFoundError:
    print("File not found")



# finally

'''
The finally block is used to define a block of code that should be executed regardless of whether an exception occurs or not in the try block.
'''

# Example

try:
    x = open("file.txt", "r")
    print(x)
except FileNotFoundError:
    print("File not found")
finally:
    print("finally block")
   