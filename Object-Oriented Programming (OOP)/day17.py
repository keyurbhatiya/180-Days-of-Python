# Day 17: Inheritance and Polymorphism


# Inheritance

''''
Inheritance is a way to create a new class based on an existing class. The new class inherits all the attributes and methods of the parent class, and can add new attributes and methods to the class.
'''

# Example

class Animal:
    def __init__(self, name): # Constructor
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} is barking.")

dog = Dog("jorge")
dog.eat() # Output: Fido is eating.
dog.bark() # Output: Fido is barking


# Polymorphism

''''
Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common base class.
'''

# Example

class Shape:
    def draw(self): # Method
        pass

class Circle(Shape):
    def draw(self): # Method
        print("Drawing a circle.")

class Rectangle(Shape):
    def draw(self): # Method
        print("Drawing a rectangle.")

shapes = [Circle(), Rectangle()] # List
for shape in shapes:
    shape.draw() # Method Call