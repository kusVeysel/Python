
#* Abstract Class (Soyut Sınıf)

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def primer(self):
        pass
#* Abstract methodların içeriği olmaz , kullanılmak zorundadırlar ve @abstractmethod olarak da tanımlanması gerekmektedir


class Rectangle(Shape):
    def __init__(self,witdh,height):
        self.witdh = witdh
        self.height = height

    def area(self):
        return self.witdh * self.height

    def primer(self):
        return 2 * (self.witdh + self.height)
        

class Circle(Shape):
    def __init__(self,raidus):
        self.radius = raidus

    def area(self):
        return 3.1415 * self.radius ** 2

    def primer(self):
        return 2 * 3.1415 * self.radius


rect = Rectangle(4,7)
print("Rectangle Area:",rect.area())
print("Rectangle Primeter:",rect.primer())

circle = Circle(3)
print("Circle Area:",circle.area())
print("Circle Primeter:",circle.primer())


print()
#? Duck Typing
#* Kalıtımsız polymorphism

class Dog:
    def make_sound(self):
        return "Woof! Woof!"
    
class Cat:
    def make_sound(self):
        return "Meow! Meow!"
    
class Car:
    def make_sound(self):
        return "Vroom! Vroom!"


def play_sound(obg):
    print(obg.make_sound())

dog = Dog()
cat = Cat()
car = Car()
play_sound(dog)
play_sound(cat)
play_sound(car)