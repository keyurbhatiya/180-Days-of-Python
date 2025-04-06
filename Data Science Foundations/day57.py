# Day 57: Handling Missing Data

'''
In this day, we will learn about handling missing data, which involves dealing with data that is missing or incomplete.
'''

# Handling Missing Data

''''
Handling missing data is the process of dealing with data that is missing or incomplete. It is important to handle missing data to ensure that the data is accurate and useful for analysis.
'''

# Example

import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, None]})

print(data)

print(data.isnull())

print(data.fillna(0))

print(data['B'].mean())

print(data['B'].std())

# Output
