

class Employee:
    company = 'Microsoft'

    def show(self, name, slary):
        print(f" Name is : {name},  Salary : {slary}, and Company : {self.company} \n");

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


# Create an instance of Employee
obj = Employee()

# Show employee details (Initial company is 'Microsoft')
obj.show('John', 50000)  

# Change the company using the class method
Employee.change_company('Amazon')

# Show employee details again (Company is now 'Amazon')
obj.show('John', 50000) 




'''
A class method in Python is a method that belongs to the class itself rather than an instance of the class. It means that when you call a class method, you can work with the class attributes (the values shared by all instances of the class), and it affects all objects created from that class.

Class methods are defined using the @classmethod decorator, and they take cls (short for class) as the first parameter instead of self. The cls parameter refers to the class itself, allowing you to modify class-level attributes.

'''