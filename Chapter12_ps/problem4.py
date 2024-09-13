class Complex:
    def __init__(self,r, i):
        self.i = i
        self.r = r


    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    

    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1 = Complex(2, 5)
c2 = Complex(3,5)

print(c1 + c2)










'''

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __repr__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(2, 5)
c2 = Complex(3, 5)

print(c1 + c2)  # Output: 5 + 10i

'''



'''
Program Summary:
Class Complex: Represents complex numbers with real (r) and imaginary (i) parts.
__add__ Method: Adds two Complex objects by summing their real and imaginary parts.
Execution: Adds c1 (2 + 5i) and c2 (3 + 5i) to produce a new Complex object 5 + 10i.
'''


'''

Concepts Used in the Program:
Operator Overloading:

Concept: Customizing the behavior of operators (like +) for user-defined classes.
Usage: The __add__ method overloads the + operator to add two Complex objects.
Class Definition:

Concept: Creating a blueprint for objects with attributes and methods.
Usage: The Complex class defines complex numbers with r (real part) and i (imaginary part).
'''