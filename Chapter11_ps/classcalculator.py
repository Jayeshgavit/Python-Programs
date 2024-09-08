import math
class Calculator:
    

    def __init__(self, n):
        self.n = n

    @staticmethod
    def welcome():
        print("Welcome to the Calculator Program!\n")
    def calculate(self):
        print(f"Square of {self.n} is : {self.n ** 2}") #{self.n * self.n}
        print(f"Cube of {self.n} id : {self.n **3}") #self.n * self.n * self.n
        print(f"Square root of {self.n} is : {round(math.sqrt(self.n))}")



n = int(input(" Enter the number to find square/cube and square root of Number : "))
obj1 = Calculator(n)
obj1.welcome()
obj1.calculate()