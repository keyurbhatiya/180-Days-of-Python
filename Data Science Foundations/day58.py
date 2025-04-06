# Day 58: Data Science Mini-Project (Sales Analysis) 

'''
In this day, we will create a sales analysis mini-project using Python and Pandas.
'''

# Sales Analysis

''''
Sales analysis is the process of analyzing sales data to gain insights into how a business is performing, what products are selling well, and how customers are behaving.
'''

# Example

import pandas as pd

data = pd.read_csv('sales_data.csv')

print(data)

print(data.describe())

# print(data.corr())

# print(data.plot(kind='scatter', x='Quantity', y='Sales'))


