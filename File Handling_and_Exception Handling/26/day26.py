#  Day 26: Logging in Python  

''''
In this day, we will learn about logging in Python.'
'''

# Logging in Python

''''
Logging in Python is a way to record events and errors in a program. It allows developers to track and analyze the behavior of the program over time.
'''


# Logging Levels

''''
There are four logging levels in Python:'
'''

# DEBUG
# INFO
# WARNING
# ERROR


# Example

import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

logging.info('This is an info message')

logging.warning('This is a warning message')

logging.error('This is an error message')

