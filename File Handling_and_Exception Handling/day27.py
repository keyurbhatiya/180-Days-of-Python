# Day 27: Regular Expressions (re module) 

''''
In this day, we will learn about regular expressions (re module) in Python. Regular expressions are used to match patterns in text and strings.
'''

# Regular Expressions (re module)

''''
Regular expressions (re module) are used to match patterns in text and strings. They are a powerful tool for working with text and strings in Python.'
'''

# Example

import re

text = "Hello, world!"

# match = re.search(r"world", text)
match = re.search(r"Hello", text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")