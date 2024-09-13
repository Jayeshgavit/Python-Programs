class Employee:
    salary = 12000
    increment = 20

    @property
    def salaryafterincrement(self):
        return " Salary after increment : ", self.salary + self.salary * (self.increment/100)

    @salaryafterincrement.setter
    def salaryafterincrement(self, new_salary):
        self.increment = ((new_salary/self.salary)-1) * 100

        
e = Employee()
e.salaryafterincrement = 14400
print(e.increment)




'''
### Program Summary:

- **Class `Employee`**:
  - **Attributes**: `salary` (234), `increment` (20).
  - **`salaryafterincrement` Property**:
    - **Getter**: Calculates and returns salary after applying the increment.
    - **Setter**: Updates the increment to achieve a target salary after increment.
- **Execution**: 
  - Sets the target salary to 280.
  - Calculates and prints the new increment value.
'''



