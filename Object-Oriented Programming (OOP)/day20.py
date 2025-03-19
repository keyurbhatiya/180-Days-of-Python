# Day 20: Static & Class Methods

''''
Static and Class Methods are special methods that are called automatically by Python when certain operations are performed on an object. They are used to implement custom behavior for objects.
'''

# syntax

''''
class ClassName:
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2

    @classmethod
    def class_method(cls, arg1, arg2):
        return arg1 + arg2

'''

# Example

class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        return arg1 + arg2

    @classmethod
    def class_method(cls, arg1, arg2):
        return arg1 + arg2

    def instance_method(self, arg1, arg2):
        return arg1 + arg2

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return f"MyClass({self.arg1}, {self.arg2})"

    def __repr__(self):
        return f"MyClass({self.arg1}, {self.arg2})"

    def __add__(self, other):
        return MyClass(self.arg1 + other.arg1, self.arg2 + other.arg2)

    def __len__(self):
        return self.arg1

    def __getitem__(self, index):
        return self.arg1[index]

    def __setitem__(self, index, value):
        self.arg1[index] = value

    def __delitem__(self, index):
        del self.arg1[index]

    def __iter__(self):
        return iter(self.arg1)

    def __next__(self):
        return next(iter(self.arg1))

    def __contains__(self, item):
        return item in self.arg1

    def __call__(self, arg1, arg2):
        return arg1 + arg2

    def __bool__(self):
        return bool(self.arg1)

    def __int__(self):
        return int(self.arg1)

    def __float__(self):
        return float(self.arg1)

    def __complex__(self):
        return complex(self.arg1)

    def __index__(self):
        return self.arg1

    def __round__(self):
        return round(self.arg1)

    def __floor__(self):
        import math
        return math.floor(self.arg1)

    def __ceil__(self):
        import math
        return math.ceil(self.arg1)

    def __trunc__(self):
        import math
        return math.trunc(self.arg1)

# Example
obj = MyClass(1, 2)

print(MyClass.static_method(1, 2)) # 3
print(MyClass.class_method(1, 2)) # 3
print(obj.instance_method(1, 2)) # 3
print(obj(1, 2)) # 3
print(obj + MyClass(1, 2)) # MyClass(2, 4)
print(len(obj)) # 1

obj = MyClass([1], 2)
print(obj[0]) # 1
obj[0] = 2
del obj[0]

obj = MyClass([1, 2, 3], 2)
for x in obj:
    print(x) # 1, 2, 3

print(1 in obj) # True
print(bool(obj)) # True

# print(int(obj)) # 1
# print(float(obj)) # 1.0
# print(complex(obj)) # (1+0j)
# print(round(obj)) # 1

import math
# print(math.floor(obj)) # 1
# print(math.ceil(obj)) # 1
# print(math.trunc(obj)) # 1


