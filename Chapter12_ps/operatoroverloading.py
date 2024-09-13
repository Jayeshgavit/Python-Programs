class Number:

    def __init__(self, n):
        self.n = n  


    def __add__(self, num):
        return self.n + num.n 

    def __sub__(self, num):
        return self.n - num.n

    def __mul__(self, num):
        return self.n * num.n


    def __truediv__(self, num):
        return self.n / num.n

    def __floatdiv__(self, num):
        return self.n // num.n   
    



n = Number(1)
m = Number(4)

print(" This is a programe which represents operator overloading concepts...".center(80, '-'))

print("\n\t__add__ : ", n + m)
print("\n\t__sub__ :",n - m)
print("\n\t__mul__ :",n * m)
print("\n\t__truediv__ :",n / m)
print("\n\t___floatdiv__ : ",float(n / m))  # converts the result to float before printing




'''
Your program defines a `Number` class that allows adding two `Number` objects by overloading the `+` operator using the `__add__` method. It initializes each object with a number (`n`), and when you add two objects (`n + m`), it returns the sum of their `n` values.

**Output:** The sum of `1 + 4` is printed as `5`.'''




'''
Operator Overloading :
Definition: Operator overloading allows custom behavior for operators (e.g., +, -, *) when applied to user-defined objects.

Purpose: Enables objects to interact with operators in a meaningful way, similar to built-in types (e.g., adding two custom objects).

Key Method:

__add__(self, other): Overloads the + operator to define how two objects are added.
'''
