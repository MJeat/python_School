
from abc import ABC, abstractmethod
class Animal(ABC): # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass # Must be implemented by subclasses
    @abstractmethod
    def move(self):
        pass
    # You cannot instantiate Animal directly
    # animal = Animal() # This would raise TypeError
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    def move(self):
        return "Running on four legs"
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"
    def move(self):
        return "Flying with wings"
husky = Dog()
print(husky.make_sound())
print(husky.move())
