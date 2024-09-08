import random 

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"The ticket is Booked from {fro} to {to} ")
    
    def status(self):
        print(f"Train is running {self.trainNo}")
    
    def getfare(self,fro,to):
        print(f" the ticket fare is TrainNo {self.trainNo} from {fro} to {to} is {random.randint(222, 5555)}")


obj1 = train(23124)
obj1.book('Nashik','Pune')
obj1.status()
obj1.getfare('Nashik', 'Pune')