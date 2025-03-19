# Day 18: Encapsulation and Abstraction  

'''
In this day, we will learn about encapsulation and abstraction in Python.

Encapsulation is the process of bundling data and methods together within a class, making them private to the class and accessible only through the class methods.
Abstraction is the process of hiding the internal details of a class from the outside world, and exposing only the necessary information to the outside world.
'''

# Encapsulation

''''
Encapsulation is the process of bundling data and methods together within a class, making them private to the class and accessible only through the class methods.
'''

# Example
print("Encapsulation")
class Car: # Class
    def __init__(self, make, model, year): # Constructor
        self.make = make # Instance Variable
        self.model = model
        self.year = year

    def drive(self): # Method
        print(f"The {self.make} {self.model} is driving.")

    def stop(self): # Method
        print(f"The {self.make} {self.model} has stopped.")

    def info(self): # Method
        print(f"Make: {self.make}") # Instance Variable
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car = Car("Dodge", "SRT", 2025) # Object Creation
car.drive() # Method Call
car.stop()
car.info()

# Abstraction

''''
Abstraction is the process of hiding the internal details of a class from the outside world, and exposing only the necessary information to the outside world.
'''

# Example
print("Abstraction")
class Car: # Class
    def __init__(self, make, model, year): # Constructor
        self.make = make # Instance Variable
        self.model = model
        self.year = year

    def drive(self): # Method
        print(f"The {self.make} {self.model} is driving.")

    def stop(self): # Method
        print(f"The {self.make} {self.model} has stopped.")

    def info(self): # Method
        print(f"Make: {self.make}") # Instance Variable
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car = Car("Dodge", "SRT", 2025) # Object Creation
car.drive() # Method Call
car.stop()
car.info()