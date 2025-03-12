# Day 14: Practice Problems (Sorting, Searching, Dictionary Manipulation)



# Sort a List of Tuples

'''

Sort a list of tuples based on the second element of each tuple.
'''

# Example

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print(students)

sorted_students = sorted(students, key=lambda x: x[1]) # Sort the list based on the second element of each tuple

print(sorted_students)


# Custom Sort using a Key Function

'''
Sort a list of words by their length. If two words have the same length, maintain their original order.
'''
word = ["apple", "banana", "cherry", "date", "elderberry"]

print(word)
sorted_words = sorted(word, key=len)

print(sorted_words)



# Sort a Dictionary by Values

'''
Given a dictionary of items and their prices, sort it by price in ascending order.'
'''

price = {
    "apple": 1.99,
    "banana": 0.99,
    "cherry": 1.49,
    "date": 2.99,
    "elderberry": 2.49
}
print(price)
sorted_price = sorted(price.items(), key=lambda x: x[1])

print(sorted_price)


# Searching Problems

# Binary Search

'''
Implement binary search to find the index of a given number in a sorted list. If not found, return -1'
'''

nums = [2, 4, 4, 4, 6, 7, 8]
target = 4
# Expected Output: (1, 3)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

print(binary_search(nums, target))


# Dictionary Manipulation Problems

# Merge Two Dictionaries

'''
Merge two dictionaries, adding values for common keys.
'''
dict1 = {"a": 5, "b": 10, "c": 15}
dict2 = {"b": 3, "c": 5, "d": 8}
# Expected Output: {'a': 5, 'b': 13, 'c': 20, 'd': 8}

merged_dict = {**dict1, **dict2}

print(merged_dict)


# Group Elements by Frequency

'''
Given a list of elements, create a dictionary with elements as keys and their counts as values.'
'''

items = ["apple", "banana", "apple", "orange", "banana", "banana"]
# Expected Output: {'apple': 2, 'banana': 3, 'orange': 1}

freq_dict = {}

for item in items:
    freq_dict[item] = freq_dict.get(item, 0) + 1

print(freq_dict)


# Invert a Dictionary

'''
Swap the keys and values of a dictionary, assuming values are unique.
'''

mapping = {"a": 1, "b": 2, "c": 3}
# Expected Output: {1: 'a', 2: 'b', 3: 'c'}

inv_mapping = {value: key for key, value in mapping.items()}

print(inv_mapping)