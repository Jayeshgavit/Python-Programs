class Employee:
    company = 'Microsoft Corporation'
    name = "Default Name"

    def show(self):
        print(f"Name is: {self.name} and Company: {self.company}")
    
class Coder: 
    language = 'Python'
    
    def printlanguage(self):  # Fixed the method name spelling
        print(f"Language is: {self.language}")

class Programmer(Employee, Coder):  # Corrected the class name to 'Programmer'
    def showlaguages(self):
        print(f"Company: {self.company} and Laguage: {self.language}")  # Optionally, you can add 'name' here

# Creating instances
jayesh = Employee()
rohan = Programmer()

# Calling methods
rohan.show()           # Output: Company: Microsoft Corporation
rohan.printlanguage()   # Output: Language is: Python
rohan.showlaguages()


