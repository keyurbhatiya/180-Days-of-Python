# Day 33: Iterators and Generators  

''''
In this day, we will learn about iterators and generators in Python. Iterators are objects that can be iterated over, and generators are functions that can be used to create iterators.
'''

# Iterators

''''
An iterator is an object that can be iterated over, and it allows you to access the elements of a sequence one at a time.
'''

# Example

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

print(next(iterator)) # Output: 1
print(next(iterator)) # Output: 2

# Generators

'''''
A generator is a function that returns an iterator, and it allows you to generate a sequence of values on the fly.
'''

# Example

def generate_squares(n):
    for i in range(n):
        yield i ** 2

squares = generate_squares(5) # Generator function

print(list(squares))

