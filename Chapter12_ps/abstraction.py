class employee:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter    
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



e = employee()

e.name = "Jayesh Gavit"
print(e.name)

#this an example of decorator / abstraction and encapsulation