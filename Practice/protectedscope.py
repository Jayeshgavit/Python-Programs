
class computer:

    def __init__(self):
        self._maxPrice = 900
    
    def sell(self):
        print("Selling Price : {}".format(self._maxPrice))

    def setMaxPrice(self,price):
        self._maxPrice = price    
        



c = computer();
c.sell(); #900

c.setMaxPrice(3000);
c.sell(); #3000

c.setMaxPrice(4000);
c.sell(); #4000