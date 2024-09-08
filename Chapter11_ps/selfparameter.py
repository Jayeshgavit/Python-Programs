

class Details:
    name = "Jayesh"
    age = 23

    def desc(self):
        print("My Name is ", self.name ," and My age is " , self.age)

    @staticmethod               #used when it does not require self parameter or not anithing pass variable
    def greet():
        print("Hello, Good Morning!")


obj1 = Details()
obj1.desc();

obj2 = Details()
obj2.name='Rohan'
obj2.age = 21

print("\n")
obj2.greet()
obj2.desc();
