
class employee:
    def __init__(self, name): 
        self.name = name 
        
    def greet(self):
        print(f"Hello, Good Morning, {self.name}!")

jayesh = employee("Jayesh")
jayesh.greet()


