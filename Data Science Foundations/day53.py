# Day 53: Working with Pandas 

'''
In this day, we will learn about working with Pandas, a popular library for working with data in Python.
'''

# Working with Pandas

''''
Pandas is a library for working with data in Python. It provides a high-level data manipulation and analysis API on top of Numpy.
'''

# Example

import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(data)

print(type(data))

# Output    
'''
    A  B
0  1  4
1  2  5
2  3  6
<class 'pandas.core.frame.DataFrame'>
'''