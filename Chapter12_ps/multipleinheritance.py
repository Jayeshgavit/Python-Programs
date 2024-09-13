class Animal:
    def sound(self):
        print("Animal sound")

class Vehicle:
    def start(self):
        print("Vehicle starts")

class RobotDog(Animal, Vehicle):  # Multiple inheritance
    pass

robodog = RobotDog()
robodog.sound()  # Inherited from Animal
robodog.start()  # Inherited from Vehicle
