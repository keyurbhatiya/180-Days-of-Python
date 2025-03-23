# Day 32: Map, Filter, and Reduce 


# Map

'''
The map function is a higher-order function that applies a function to each element of an iterable and returns a new iterable.'
'''

# Example

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers)) # Map function to create a new list

print(squares)


# Filter

'''
The filter function is a higher-order function that filters elements from an iterable based on a predicate function.
'''

# Example

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Filter function to create a new list

print(even_numbers)


# Reduce

'''
The reduce function is a higher-order function that applies a function to a sequence of elements and returns a single value.'
'''

# Example

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers) # Reduce function to create a single value

print(product)
