class Employee:

    def __init__(self):
        print("This is a employee")

    a = 1

class programmer(Employee):
    def __init__(self):
        print("This is a programmer")
    b=2
class coder(programmer): 
    def __init__(self):
        super().__init__()
        print("This is a coder")
    c=3

coderobj = coder()

print(coderobj.a, coderobj.b, coderobj.c)