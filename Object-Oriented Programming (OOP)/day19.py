# Day 19: Magic/Dunder Methods

'''  
Magic/Dunder Methods are special methods that are called automatically by Python when certain operations are performed on an object. They are used to implement custom behavior for objects. 
'''

# syntax

''''
class ClassName:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self): # Magic/Dunder Method
        return f"ClassName({self.arg1}, {self.arg2})"
'''

# Example

class Person:
    def __init__(self, name, age): # Constructor
        self.name = name # Instance Variable
        self.age = age

    def __str__(self): # Magic/Dunder Method
        return f"{self.name} is {self.age} years old." # Return a string representation of the object

person = Person("Keyur", 21) # Create an instance of the Person class
print(person)
