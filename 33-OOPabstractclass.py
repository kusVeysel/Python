 #? Abstract Class (Soyut Sınıf)
#* Abstract class doğrudan nesne üretmek için değil, alt sınıflara bir şablon oluşturmak için kullanılır
#* @abstractmethod ile tanımlanan methodlar alt sınıflarda override edilmek zorundadır
#*  Abstract class'tan doğrudan nesne oluşturulamaz. shape = Shape()  # Hata verir, çünkü Shape abstract bir class'tır

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def primer(self):
        pass
#* area() ve perimeter() abstract methodlardır
#* Shape sınıfından türeyen sınıflar bu methodları kendilerine uygun şekilde tanımlamak zorundadır

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1415 * self.radius


rect = Rectangle(4,7)
print("Rectangle Area:",rect.area())
print("Rectangle Primeter:",rect.perimeter())

circle = Circle(3)
print("Circle Area:",circle.area())
print("Circle Primeter:",circle.perimeter())


#? Duck Typing
#* Bir nesnenin hangi sınıfa ait olduğundan çok, gerekli method veya davranışa sahip olup olmadığı önemlidir.
#* Kalıtım zorunlu değildir.
#* "Ördeğe benziyor ve ördek gibi davranıyorsa ördektir" yaklaşımıdır.
print("------------------------------------------")

class Dog:
    def make_sound(self):
        return "Woof! Woof!"
    
class Cat:
    def make_sound(self):
        return "Meow! Meow!"
    
class Car:
    def make_sound(self):
        return "Vroom! Vroom!"


def play_sound(obj):
    print(obj.make_sound())

dog = Dog()
cat = Cat()
car = Car()
play_sound(dog)
play_sound(cat)
play_sound(car)