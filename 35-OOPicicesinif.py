 #? Nested Class (İç İçe Sınıf)
#* Bir class'ın başka bir class içerisinde tanımlanmasıdır
#* İç class'a dış class üzerinden erişilebilir
#* Car.Engine şeklinde Engine sınıfına erişilebilir

class Car:
    def __init__(self, brand, model, engine_hp, engine_fuel):
        self.brand = brand
        self.model = model
        self.engine = Car.Engine(engine_hp, engine_fuel) #* iç sınıfın nesnesi oluşturuluyor, Car sınıfı içerisindeki Engine sınıfından bir nesne oluşturuluyor

    def show_details(self): #* instance method
        print(f"Car Brand: {self.brand}, Model: {self.model}")
        self.engine.show_engine() #* iç class'ın methodu çağırılıyor

    class Engine:
        def __init__(self, hp, fuel_type):
            self.engine_type = "V8"
            self.horse_power = hp
            self.fuel_type = fuel_type

        def show_engine(self):
            print(f"Engine Type: {self.engine_type}, Horse Power: {self.horse_power}, Fuel Type: {self.fuel_type}")

c1 = Car("BMW", "M3", 500, "Gasoline")
c1.show_details()

print("------------------------------------------")
#? Static method
#* @staticmethod decorator'ı ile tanımlanır. self veya cls parametresi almaz
#* Class veya instance'a ait verilere ihtiyaç duymadan bağımsız işlem yapmak için kullanılır
#* Class üzerinden doğrudan çağrılabilir

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

#! mathop = MathOperations(): Gerek yok
#* Static methodlar instance oluşturmadan class üzerinden doğrudan çağrılabilir
#* Bu nedenle MathOperations sınıfından nesne oluşturmaya gerek yoktur

print("MathOperations.add(10, 5) → ",MathOperations.add(10, 5))
print("MathOperations.sub(10, 5) → ",MathOperations.sub(10, 5))
print("MathOperations.mul(10, 5) → ",MathOperations.mul(10, 5))
print("MathOperations.div(10, 5) → ",MathOperations.div(10, 5))
print("MathOperations.div_floor(10, 5) → ",MathOperations.div_floor(10, 5))