# Day 16: Constructors and Instance Variables  


# Constructor

'''
A constructor is a special method that is called when an object of a class is created. It is used to initialize the attributes of the object.
'''

# Example

class Car:
    def __init__(self, make, model, year): # Constructor
        self.make = make
        self.model = model
        self.year = year

    def drive(self): # Method
        print(f"The {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")
    
    def info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car = Car("Dodge", "SRT", 2024) # Object Creation
car.drive() # Method Call
car.stop() 
car.info()

# Instance Variables

'''
Instance variables are variables that are specific to each instance of a class. They are created when an object of the class is created and are destroyed when the object is destroyed.
'''

# Example

class Car:
    def __init__(self, make, model, year): # Constructor
        self.make = make # Instance Variable
        self.model = model # Instance Variable
        self.year = year # Instance Variable

    def drive(self): # Method
        print(f"The {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")
    
    def info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car = Car("Mercedes", "maybach", 2024) # Object Creation 
car.drive() # Method Call
car.stop() 
car.info()

