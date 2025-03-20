#  Day 29: Debugging Techniques 

''''
In this day, we will learn about debugging techniques in Python. Debugging is the process of finding and fixing errors in a program.
'''

# Debugging Techniques

''''
Debugging is the process of finding and fixing errors in a program. There are several debugging techniques that can be used in Python, including:
'''

# Using print statements
# Using breakpoint() function
# Using pdb module
# Using logging module

# Example

# Using print statements

print("Hello, world!")

# Using breakpoint() function

x = 10
y = 20
print(x + y)

# Using pdb module

import pdb

x = 10
y = 20
# pdb.set_trace() # Set a breakpoint and start debugging
print(x + y) # This line will be paused and the debugger will be activated

# Using logging module

import logging

logging.basicConfig(filename='app.log', level=logging.INFO) # Set up logging

logging.info('This is an info message') # Log an info message
logging.warning('This is a warning message') # Log a warning message
logging.error('This is an error message') # Log an error message

logging.shutdown() # Close the logging session