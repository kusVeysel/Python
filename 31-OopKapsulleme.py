
#* Public: Her yerden erişilebilir
#* Protected(_): Python'da gerçek bir erişim engeli oluşturmaz ama dışarıdan erişmek yanlış bir kullanımdır. Class içinden veya bu class'ı miras alan class'lardan erişilmelidir
# → "_" kullanımı, bunun class dışından doğrudan kullanılmaması gerektiğini belirten bir isimlendirme kuralıdır
#* Private(__): Python name mangling uygular
#* Class dışından doğrudan erişim zorlaşır, ancak tamamen imkânsız değildir
#! Python'da C++/Java'daki gibi gerçek private ve protected erişim engeli yoktur


class Car:
    def __init__(self, brand, model):
        self.brand = brand #* public attribute(property)
        self.model = model #* public attribute(property)

    def display_info(self): #* public method
        return f"Car: {self.brand} {self.model}"

c1 = Car("Skoda","Superb")

print(c1.display_info()) #* Dışarıdan erişildi

print("------------------------------------------")


class Animal:
    def __init__(self, name, species):
        self.name = name #* public attribute(property)
        self._species = species #* protected attribute(property)

    def _makeSound(self): #* protected method
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def display_info(self):
        return f"Dog name: {self.name}, Breed: {self.breed}, Species: {self._species}" #* protected attribute(propert) kullanıldı 

    def make_sound(self):
        return self._makeSound() #* protected method kullanıldı

dog = Dog("Kurt","Golden Retriever")

print(dog.display_info())
print(dog.make_sound())
print(dog._makeSound()) #* Erişilir ama hatalı kullanım

print("------------------------------------------")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number #* public attribute(property)
        self.__balance = balance #* private attribute(property)

    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount
            return f"Deposit: ${amount} New Balance: ${self.__balance}"
        return "Invalid deposit amount!"

    def __display_balance(self): #* private metot
        return f"Balance: ${self.__balance}"

    def get_balance(self):
        return self.__display_balance()


account = BankAccount("12345678",2000)

print(account.deposit(700))
# print(account.__display_balance()) #* Class dışından doğrudan __display_balance() şeklinde erişilemez
print("------------------------------------------")

class Kapsulleme:
    def __display_balance(self):
        return f"Kapsullendi"

    def get_balance(self):
        return self.__display_balance()


kpsl = Kapsulleme()

print(kpsl.get_balance())

#* get_balance() public methodu üzerinden, private __display_balance() metoduna dolaylı olarak erişildi