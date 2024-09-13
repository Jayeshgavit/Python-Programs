
class Employee:
    company = 'Microsoft Corporation'

    def show(self, name, slary):
        print(name, slary, self.company)
    

class Program(Employee):
    def show(self, name, salary):
        print(name, salary, self.company)

jayesh = Employee()
Rohan = Program()

Rohan.show('Rohan', '120000')
jayesh.show('Jayesh', 30000)

