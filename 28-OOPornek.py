class Animal:
    def __init__(self, name, alive):
        self.name = name
        self.is_alive = alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping in a cozy bed")

    def sound(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    pass

class Rabbit(Animal):
    def __init__(self,name,alive):
        super().__init__(name,alive)
        self.is_hopping = True


dog = Dog("Scooby Doo",True)
cat = Cat("Tom",True)
mouse = Mouse("Jerry",False)
rabbit = Rabbit("Bugs Bunny",True)


animals = [dog,cat,mouse,rabbit]

for animal in animals:
    print(f"Animal name: {animal.name}, is alive: {animal.is_alive}")

    if hasattr(animal,'is_hopping'):
        print(f"{animal.name} is hopping!")

    animal.eat()
    animal.sleep()

    if hasattr(animal, 'sound'):
        animal.sound()

    print()

#* hasattr(nesne, "attribute"): Bir nesnede belirtilen özelliğin(attribute) bulunup bulunmadığını kontrol eder