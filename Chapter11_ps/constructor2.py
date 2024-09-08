

class Details:
    name = 'jayesh'
    age = 23
    language = 'python'


    def __init__(self, name, salary, laguage):
        self.name = name
        self.salary = salary
        self.language = laguage
        print("Welcome to my program! \n")
        

    @staticmethod               #used when it does not require self parameter or not anithing pass variable
    def greet():
        print("Hello, Good Morning!")


obj1 = Details(" Jayesh", 1300000, 'Python')

obj1.greet()
print(obj1.name, obj1.salary, obj1.language)

print("\n")

