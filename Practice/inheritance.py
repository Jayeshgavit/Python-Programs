class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisthis(self):
        print("bird")
    
    def swim(self):
        print("swim Faster")

class peguine (Bird):
    def __init__(self):
        super().__init__()  #set super for get input first
        print("peguine is ready")
        
    def whoisthis(self):
        print("peguine")
    def run(self):
        print("run faster")



peg = peguine()
peg.whoisthis()
peg.swim()
peg.run()