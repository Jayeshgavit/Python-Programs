class Animal:
    pass

class pets(Animal):
    pass

class Dog(pets):
    @staticmethod
    def bark():                 #We are using static method so we have to use self keyword
        print("Woof!")





Dog1 = Dog()

Dog1.bark()




'''
@staticmethod (Short Note):
Purpose: Defines a method that doesn't depend on instance or class variables.
Usage: It can be called on the class or an instance but can't access self (instance) or cls (class).
Benefit: Used for utility functions related to the class but not needing access to class or instance data.

In this example, bark() is a static method because it doesn't use self or cls. It's a utility function that doesn't require a Dog object to operate. This is a good practice when you have utility functions that don't depend on the state of an object.
'''