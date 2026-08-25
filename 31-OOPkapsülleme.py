
#* Public: Veriye her yerden erişilebilir
#* Protected(_): Sadece class içinden veya bu class'ı miras alan class'lardan erişilebilir
#* Private(__): Sadece tanımlandığı class içinden erişilebilir



class Car:
    def __init__(self,b,m):
        self.brand = b #* public attribute(property)
        self.model = m #* public attribute(property)
    def display_info(self): #* public method
        return f"Car: {self.brand} {self.model}"

c1 = Car("Skoda","Superb")

print()

class Animal:
    def __init__(self,n,s):
        self.name = n #* public attribute(property)
        self._species = s #* protected attribute(property)

    def _makeSound(self): #* protected method
        return "Animal sound"


class Dog(Animal):
    def __init__(self, n, b):
        super().__init__(n, "Dog")
        self.breed = b
    def display_info(self):
        return f"Dog name: {self.name}, Breed: {self.breed}, Species: {self._species}" #* protected attribute(propert) kullanıldı 
    def make_sound(self):
        return self._makeSound() #* protected method kullanıldı

dog = Dog("Kurt","Golden retiriever")

print()

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number #* public attribute(property)
        self.__balance = balance #* private attribute(property)

    def deposit(self,amount):
        if(amount > 0):
            self.__balance += amount
            return f"Deposit: ${amount} New Balance: ${self.__balance}"
        return "Invalid deposit amount!"

    def __display_balance(self): #* private method
        return f"Balance: ${self.__balance}"

    def get_balance(self):
        return self.__display_balance()


account = BankAccount("12345678",2000)
print(account.deposit(700))
print(account.__display_balance()) #* hata verir dışarıdan ulaşılamaz


