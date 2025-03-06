
# Week 2: Data Structures in Python


# Day 8: Lists and List Methods  


# Lists

'''
Lists are used to store a collection of items in a single variable. They are ordered and can contain elements of different data types.

'''

# Example

fruits = ["apple", "banana", "cherry"]

print(fruits)

# List Methods

'''

append(): Adds an element to the end of the list.
clear(): Removes all elements from the list.
copy(): Returns a shallow copy of the list.
count(): Returns the number of times an element appears in the list.
extend(): Adds all elements of another list to the end of the current list.
index(): Returns the index of the first occurrence of an element in the list.
insert(): Inserts an element at a specific position in the list.
pop(): Removes and returns the element at a specific position in the list.
remove(): Removes the first occurrence of an element from the list.
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the elements in the list in ascending order.

'''

# Example

# append

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

print(fruits)

# clear

fruits.clear()

print(fruits)

# copy

fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()

print(new_fruits)

# count

fruits = ["apple", "banana", "cherry"]
count = fruits.count("apple")

print(count)

# extend

fruits = ["apple", "banana", "cherry"]
fruits.extend(["orange", "grape"])

print(fruits)

# index

fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")

print(index)

# insert

fruits = ["apple", "banana", "cherry"]  
fruits.insert(1, "orange")

print(fruits)

# pop

fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)

print(removed_fruit)

# remove

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

print(fruits)

# reverse

fruits = ["apple", "banana", "cherry"]
fruits.reverse()

print(fruits)

# sort

fruits = ["apple", "banana", "cherry"]
fruits.sort()

print(fruits)





