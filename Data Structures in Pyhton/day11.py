# Day 11: Dictionaries and Dictionary Methods 


# Dictionaries

'''
Dictionaries are used to store a collection of key-value pairs. They are similar to lists, but they use keys instead of indices to access elements.

'''

# Example

person = {
    "name": "keyur",
    "age": 21,
    "city": "Los Angelis"
}

print(person)

# Dictionary Methods

'''

clear(): Removes all elements from the dictionary.
copy(): Returns a shallow copy of the dictionary.
fromkeys(): Returns a dictionary with the specified keys and a default value.
get(): Returns the value associated with the specified key.
items(): Returns a list of key-value tuples in the dictionary.
keys(): Returns a list of all keys in the dictionary.
pop(): Removes the element with the specified key and returns its value.
popitem(): Removes the last inserted key-value pair and returns it as a tuple.
setdefault(): Returns the value associated with the specified key, or a default value if the key is not found.  
update(): Updates the dictionary with the key-value pairs from another dictionary.'

'''

# Example

person = {
    "name": "keyur",
    "age": 21,
    "city": "Los Angelis"
}

print(person.keys())

# Output
'''
dict_keys(['name', 'age', 'city'])
'''