class Car:
    def __init__(self, brand, model, engine_hp, engine_fuel):
        self.brand = brand
        self.model = model
        self.engine = Car.Engine(engine_hp, engine_fuel) #* iç class'ın nesnesi oluşturuluyor

    def show_details(self): #* instance method
        print(f"Car Brand: {self.brand}, Model: {self.model}")
        self.engine.show_engine() #* iç class'ın methodu çağırılıyor

    class Engine:
        def __init__(self, hp, fuel_type):
            self.type = "V8"
            self.hourse_power = hp
            self.fuel_type = fuel_type

        def show_engine(self):
            print(f"Enigne Type: {self.type}, Horse Power: {self.hourse_power}, Fuel Type: {self.fuel_type}")

c1 = Car("BMW", "M3", 500, "Gasoline")
c1.show_details()

print()
#? Static method

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def sub(a, b):
        return a - b
    @staticmethod
    def mul(a, b):
        return a * b
    @staticmethod
    def div(a, b):
        if b == 0:
            return "Division by zero is not allowed."
        return a / b
    @staticmethod
    def div_floor(a, b):
        if b == 0:
            return "Division by zero is not allowed."
        return a // b

# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     if b == 0:
#         return "Division by zero is not allowed."
#     return a / b
# def div_floor(a, b):
#     if b == 0:
#         return "Division by zero is not allowed."
#     return a // b

print(MathOperations.add(10, 5))
print(MathOperations.sub(10, 5))
print(MathOperations.mul(10, 5))
print(MathOperations.div(10, 5))
print(MathOperations.div_floor(10, 5))