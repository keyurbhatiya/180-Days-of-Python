# Day 55: Data Cleaning and Preprocessing

'''
In this day, we will learn about data cleaning and preprocessing, which involves removing duplicates, handling missing values, and normalizing data.
'''

# Data Cleaning and Preprocessing

''''
Data cleaning and preprocessing is the process of preparing data for analysis by removing duplicates, handling missing values, and normalizing data.
'''

# Example

import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(data)

print(data.duplicated())

print(data.drop_duplicates())

print(data.fillna(0))

print(data['A'].mean())

print(data['A'].std())
