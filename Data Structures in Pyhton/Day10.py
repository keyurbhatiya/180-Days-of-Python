# Day 10: Sets and Set Operations


# Sets

'''
Sets are used to store a collection of unique elements. They are unordered and can contain elements of different data types.

'''

# Example

fruits = {"apple", "banana", "cherry"}

print(fruits)

# Set Operations

'''
add(): Adds an element to the set.
remove(): Removes an element from the set.
union(): Returns a new set containing the union of two sets.
intersection(): Returns a new set containing the intersection of two sets.
difference(): Returns a new set containing the elements in the first set but not in the second set.
symmetric_difference(): Returns a new set containing the elements in either the first set or the second set but not in both.

'''

# Example

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

fruits.remove("banana")

print(fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
symmetric_difference = set1.symmetric_difference(set2)

print(union)
print(intersection)
print(difference)
print(symmetric_difference)

