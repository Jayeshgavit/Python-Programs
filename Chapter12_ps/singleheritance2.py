class Employee:
    company = 'Wipro'

    def show(self):
        print(f'Name: {self.name}, Age: {self.age}, Company: {self.company}')
    
class Programmer(Employee):
    def show(self):
        print(f"Name: {self.name}, Company: {self.company}")


jayesh = Programmer()
Rohan = Employee()

jayesh.name = 'Jayesh'
Rohan.name = 'Rohan'
print(Rohan.company, Rohan.name)
print(jayesh.company, jayesh.name)