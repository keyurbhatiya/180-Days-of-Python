# Day 60: Practice & Review

'''
In this day, we will practice and review concepts from previous days to solidify our understanding of Python programming.
'''

# Practice

'''
1. Write a function that takes a list of integers as input and returns the sum of all the even numbers in the list.
'''

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Review

'''
2. What is a generator function in Python?
A generator function is a function that returns an iterator. It uses the yield keyword to generate a sequence of values on the fly.
'''

'''
3. What is a decorator in Python?
A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
'''

'''
4. What is a context manager in Python?
A context manager is a class that defines a __enter__() and __exit__() method. It is used to manage the resources and state of a block of code.
'''

'''
5. What is a closure in Python?
A closure is a function that has access to variables defined in its enclosing scope, even after the function has returned.
'''

'''
6. What is a lambda function in Python?
A lambda function is a function that is defined using the lambda keyword. It is used to create small, single-expression functions that can be passed as arguments to other functions.
'''

'''
7. What is a list comprehension in Python?
A list comprehension is a way to create a new list by iterating over an existing list and applying a condition to each element.
'''