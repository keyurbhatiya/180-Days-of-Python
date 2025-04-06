# Day 59: Working with Seaborn 

'''
In this day, we will learn about working with Seaborn, a popular library for data visualization in Python.
'''

# Working with Seaborn

''''
Seaborn is a library for data visualization in Python. It provides a high-level API for creating charts and graphs.
'''

# Example

import seaborn as sns

data = sns.load_dataset("tips")

print(data)

print(type(data))
