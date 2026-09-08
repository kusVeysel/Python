class Vehicle:
    # brand = "Skoda" #* property 
    # model = "Superb" #* property 
    # color = "White" #* property 
    def __init__(self, brand, model, color):
        self.brand = brand 
        self.model = model
        self.color = color
        #* self → oluşturulan mevcut nesneyi temsil eder.
        #* self.brand → oluşturulan nesnenin brand özelliğidir.
        #* brand → constructor'a gönderilen parametredir.

#* __init__ → Constructor metodudur
#* → Nesne oluşturulduğunda otomatik olarak çalışır
#* → Nesneye başlangıç değerleri vermek için kullanılır
#* → Yazılmazsa sınıf varsayılan davranışla çalışır

car_obj = Vehicle() # Vehicle class'ından yeni bir nesne oluşturur

print("Brand =", car_obj.brand)
print("Model =", car_obj.model)
print("Color =", car_obj.color)


class Vehicle2:
    def __init__(self, brand, model, color):
        self.brand = brand 
        self.model = model
        self.color = color
        #* atama için constructor methodunun ilk parametresi kullanılır

car1_obj = Vehicle2("Skoda", "Superb", "White")
#* Burada:
#* self.brand = "Skoda"
#* self.model = "Superb"
#* self.color = "White"

car2_obj = Vehicle2("Honda", "Civic", "Green")
car3_obj = Vehicle2("Nissan", "Juke", "Black")

print("------------------------------------------")
print(f"car1_obj.brand → {car1_obj.brand}, car1_obj.model → {car1_obj.model}, car1_obj.color → {car1_obj.color}")
print(f"car2_obj.brand → {car2_obj.brand}, car2_obj.model → {car2_obj.model}, car2_obj.color → {car2_obj.color}")
print(f"car3_obj.brand → {car3_obj.brand}, car3_obj.model → {car3_obj.model}, car3_obj.color → {car3_obj.color}")
print("------------------------------------------")

class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def __str__(self): #* __str__ → Nesnenin kullanıcıya gösterilecek okunabilir metinsel temsilini döndürür.
        return f"self.name → {self.name}\nself.age → {self.age}"
    def __repr__(self): #* __repr__ → Nesnenin geliştirici/developer odaklı daha açıklayıcı temsilini döndürmek için kullanılır. Özellikle debugging ve nesnenin yapısını anlamada kullanışlıdır.
        return f"self.name!r → {self.name!r}\nself.age!r → {self.age!r}"

p1 = Person("Veysel",19)
print(p1)
print(repr(p1)) #* str methodu return ediyor bu yüzden repr methoduna girmiyor girmesi için böyle çağırıyoruz

print("------------------------------------------")

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myInfo(self):
        print(f"Hello my name is {self.name}")
        print(f"I am {self.age} years old")


prsn1 = Person2("Veysel",18)
prsn1.myInfo()

#* Bir sınıfın içindeki Dunder(magic) methodları kendiliğinden çalışırken kendimiz oluşturduğumuz methodları oluşturduğumuz nesne üzerinden çağırmamız gerekir
