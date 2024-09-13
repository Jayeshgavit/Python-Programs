class TwoDvector:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f" The vector is {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):

    def __init__(self,i,j,k):
        super().__init__(i,j)  #set super for get input first 
        self.k = k

    def show(self):
        print(f" The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(1,3)
a.show()
b = ThreeDvector(1,2,3)
b.show()








'''
Purpose: Reuses the __init__ method of TwoDvector to initialize i and j in ThreeDvector.
Why: Avoids duplicating code for the 2D vector components (i, j) while adding the 3D vector component (k).
Benefit: Simplifies initialization and makes code easier to maintain

In this example, TwoDvector is a parent class and ThreeDvector is a child class. The child class inherits the __init__ method of the parent class and adds a new component (k) to the 2D vector. The show() method is also inherited from the parent class, so it prints the 3D vector in the same format as the 2D vector.

'''
