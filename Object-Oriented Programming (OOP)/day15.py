# Day 15: Introduction to OOP and Classes


# Introduction to OOP and Classes 

'''
In this day, we will learn about Object-Oriented Programming (OOP) and classes.


'''

# Classes in Python

'''
A class is a blueprint for creating objects, which are instances of the class. It defines the attributes and methods that objects of the class will have.

'''

# Example

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

car = Car("Toyota", "Camry", 2022)
car.drive()
car.stop()

