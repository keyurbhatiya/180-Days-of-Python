# Day 13: Comprehensions (List, Dict, Set)


# List Comprehension

'''

List Comprehension is a way to create a new list by applying a function to each element of an existing list.


'''

# Example

numbers = [1, 2, 3, 4, 5] 

squares = [num ** 2 for num in numbers] # List Comprehension to create a new list

print(squares)


# Dictionary Comprehension

'''

Dictionary Comprehension is a way to create a new dictionary by applying a function to each key-value pair of an existing dictionary.

'''

# Example

numbers = [1, 2, 3, 4, 5] 

squares = {num: num ** 2 for num in numbers} # Dictionary Comprehension to create a new dictionary

print(squares)


# Set Comprehension

'''

Set Comprehension is a way to create a new set by applying a function to each element of an existing set.

'''

# Example

numbers = [1, 2, 3, 4, 5]

squares = {num ** 2 for num in numbers} # Set Comprehension to create a new set

print(squares)