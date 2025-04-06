# Day 56: Exploratory Data Analysis (EDA)

'''
In this day, we will learn about exploratory data analysis (EDA), which involves analyzing data to gain insights into its structure, patterns, and relationships.
'''

# Exploratory Data Analysis (EDA)

''''
EDA is a process of analyzing data to gain insights into its structure, patterns, and relationships.
'''

# Example

import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(data.describe())

print(data.corr())

print(data.plot(kind='scatter', x='A', y='B'))
