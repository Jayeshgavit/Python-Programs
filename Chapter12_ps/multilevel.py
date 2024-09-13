class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):  # First level of inheritance
    def bark(self):
        print("Dog barks")

class Puppy(Dog):  # Second level of inheritance (Dog inherits from Animal)
    def cute(self):
        print("Puppy is cute")

puppy = Puppy()
puppy.sound()  # Inherited from Animal
puppy.bark()   # Inherited from Dog
puppy.cute()   # Defined in Puppy
