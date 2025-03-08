# Day 9: Tuples and Tuple Operations


# Tuples

'''
Tuples are used to store a collection of items in a single variable. They are ordered and can contain elements of different data types.

''' 

# Example

fruits = ("apple", "banana", "cherry")

print(fruits) 

# Tuple Operations

'''
len(): Returns the number of items in the tuple.
index(): Returns the index of the first occurrence of an element in the tuple.
count(): Returns the number of times an element appears in the tuple.
'''

# Example

fruits = ("apple", "banana", "cherry") # Create a tuple
length = len(fruits) # Get the length of the tuple

print(length)

index = fruits.index("banana") # Returns the index of the first occurrence of "banana"

print(index)

count = fruits.count("apple") # Count the number of times "apple" appears in the tuple

print(count)


