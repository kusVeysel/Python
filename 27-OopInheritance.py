 #? Inheritance (Kalıtım/Miras Alma)
#* genel yapı → class class_adı(miras_alacağı_class_adı)
#* Kalıtım alan sınıf (child/subclass), kalıtım aldığı sınıftaki (parent/superclass) erişilebilir özellik ve metotları kullanabilir

class Kisi:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def myPrint(self):
        print(self.firstname, self.lastname)

class Ogrenci(Kisi): #* Kisi class'ını miras alır
    def __init__(self, fname, lname, year): #* kendi constructur'ı
        self.graduationyear = year
        super().__init__(fname, lname) #* super() kalıtım aldığı sınıfı gösterir
        # kalıtım aldığı sınıfa fname ve lname yolladık
        #! Child(miras alan) class kendi __init__() metodunu oluşturduğunda parent(miras alınan) class'ın __init__() metodu otomatik çağrılmaz. super().__init__() ile parent'ın __init__() metodunu çağırabiliriz
    
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")


print("------------------------------------------")
k1 = Ogrenci("Veysel","KUŞ",2021)
k1.myPrint()
print(k1.graduationyear)
k1.welcome()


#? Metot Ezme
print("------------------------------------------")

class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Hav!"

class Cat(Animal):
    def speak(self):
        return "Miyav!"

class Mouse(Animal):
    pass

#* Child class'ta parent class'taki aynı isimli method yeniden tanımlanırsa method overriding(metot ezme) yapılmış olur.
#* Child'da method yoksa parent class'taki method kullanılır.

dog = Dog()
cat = Cat()
mouse = Mouse()

print("dog.speak() →",dog.speak())
print("cat.speak() →",cat.speak())
print("mouse.speak() →",mouse.speak())


#? Birkaç hazır metot
#* isinstance(nesne, Class): nesne Class'tan mı

#* issubclass(Class1, Class2): Class1 Class2'den mi türemiş

print("------------------------------------------")

print(f"isinstance(dog, Dog) → {isinstance(dog, Dog)}") # dog nesnesi Dog sınıfından mı?
print(f"isinstance(dog, Animal) → {isinstance(dog, Animal)}") # dog nesnesi Animal sınıfından mı? 
print(f"isinstance(dog, Cat) → {isinstance(dog, Cat)}") # dog nesnesi Cat sınıfından mı?
print(f"issubclass(Dog, Animal) → {issubclass(Dog, Animal)}") # Dog sınıfı Animal sınıfından mı türemiş?
print(f"issubclass(Dog, Cat) → {issubclass(Dog, Cat)}") # Dog sınıfı Cat sınıfından mı türemiş?