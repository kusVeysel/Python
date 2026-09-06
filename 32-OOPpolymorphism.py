
#* Polymorphism(Çok Biçimlilik): Aynı isimdeki methodların farklı classlarda farklı davranması

class Vehicle:
    def move(self):
        return f"This vehicle moves"

class Car(Vehicle):
    def move(self):
        return f"This car drives on the road"

class Boat(Vehicle):
    def move(self):
        return f"The boat sails on water"

class Airplane(Vehicle):
    def move(self):
        return f"The airplane flies in the sky"

class Bicycle(Vehicle):
    pass


vehicles = [Car(),Boat(),Airplane(),Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())