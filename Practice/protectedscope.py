
class computer:

    def __init__(self):
        self.__maxPrice = 900
        self.__discount = 10
    
    def sell(self):
        print("Selling Price : {}".format(self.__maxPrice))
    
    def discount(self):
        print("Discount Price : {}".format(self.__discount))

    def setMaxPrice(self,price):
        self._maxPrice = price    

     



class computer:

    def __init__(self):
        self.__maxPrice = 900
        self.__discount = 10
    
    def sell(self):
        print("Selling Price : {}".format(self.__maxPrice))
    
    def discount(self):
        print("Discount Price : {}".format(self.__discount))

    def setMaxPrice(self,price):
        self.__maxPrice = price    

     



c = computer();
c.sell(); #900

#change the price
c.__maxPrice = 4000;
c.sell(); 


c.setMaxPrice(6000);
c.sell();
c.discount(); 