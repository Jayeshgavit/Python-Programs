class company:
    company = 'Microsoft'

    def __init__(self,name, Salary, pincode):
        self.name = name
        self.salary = Salary
        self.pincode = pincode



Jayesh = company('Jayesh', 23, 422215)
print(f" Name is {Jayesh.name} , Salary is {Jayesh.salary} , pincode is {Jayesh.pincode} and Comapany is {Jayesh.company} ")