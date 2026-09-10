 #? METAPROGRAMMING (Meta Programlama)

#* Metaprogramming, programların kendi yapılarını veya davranışlarını çalışma zamanında (runtime) incelemesini, oluşturmasını veya değiştirmesini sağlayan tekniklerdir

#* Kelime anlamı: "Programlama üzerine programlama"
#* → Kod, başka kodları oluşturabilir veya değiştirebilir.
#* → Sınıflar çalışma zamanında oluşturulabilir.
#* → Mevcut sınıflara veya nesnelere dinamik olarak özellik/metot eklenebilir.

#* Python'da metaprogramming ile ilişkili temel araçlar:
#*   1. type()                           → Sınıfları dinamik olarak oluşturabilir.
#*   2. getattr/hasattr/setattr/delattr  → Nitelikler üzerinde dinamik işlem yapabilir.
#*   3. __new__                          → Nesne oluşturma sürecini kontrol eder.
#*   4. Metaclass                        → Sınıfların nasıl oluşturulacağını kontrol eder.
#*   5. Monkey Patching                  → Çalışma zamanında mevcut yapıyı değiştirebilir.
#*   6. __init_subclass__                → Alt sınıfların oluşturulmasını takip/özelleştirebilir.
#*   7. __call__                         → Nesnelerin fonksiyon gibi çağrılmasını sağlar.


#? 1. Örnek - type() ile Dinamik Sınıf Oluşturma
#* type() sadece nesnenin tipini öğrenmek için kullanılmaz
#* type(name, bases, attrs) kullanımıyla çalışma zamanında yeni sınıflar oluşturulabilir.
#* name  → Oluşturulacak sınıfın adı
#* bases → Miras alınacak sınıfların bulunduğu tuple
#* attrs → Sınıfın attribute ve methodlarının bulunduğu dictionary

print("\n-------- 1. Örnek - type() ile Dinamik Sınıf --------\n")

#* Klasik sınıf tanımı
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

#* type() ile çalışma zamanında sınıf oluşturuluyor
PersonDynamic = type(
    "PersonDynamic",
    (),
    {
        "__init__": lambda self, name: setattr(self, "name", name),
        "greet": lambda self: f"Hello, I'm {self.name}"
    }
)

p1 = Person("Veysel")
p2 = PersonDynamic("Veysel (Dynamic)")

print(f"Klasik: {p1.greet()}")
print(f"Dynamic: {p2.greet()}")

print(f"p1'in sınıfı: {type(p1)}")
print(f"p2'nin sınıfı: {type(p2)}")


#? 2. Örnek - type() ile Miras Alan Dinamik Sınıf
print("\n-------- 2. Örnek - Dinamik Miras --------\n")

def extra_method(self):
    return f"Extra method from {self.__class__.__name__}"

#* Person sınıfından miras alan ve ekstra metodu bulunan
#* yeni bir sınıf çalışma zamanında oluşturuluyor.
DerivedPerson = type(
    "DerivedPerson",
    (Person,),
    {
        "extra": extra_method
    }
)


dp = DerivedPerson("Ayşe")

print(dp.greet())      #* Person sınıfından miras alınan metot
print(dp.extra())      #* Dinamik olarak eklenen metot


#? 3. Örnek - getattr(), hasattr(), setattr(), delattr()
#* Bu fonksiyonlar nesnelerin attribute'larıyla çalışma zamanında
#* dinamik olarak işlem yapmayı sağlar.

print("\n-------- 3. Örnek - Dinamik Nitelik Erişimi --------\n")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car("Toyota", "Corolla")

#* hasattr(nesne, "nitelik_adi")
#* Belirtilen attribute nesnede mevcut mu kontrol eder.
print(f"'brand' var mı? {hasattr(car, 'brand')}")  #* True
print(f"'color' var mı? {hasattr(car, 'color')}")  #* False

#* getattr(nesne, "nitelik_adi", varsayılan)
#* Attribute'un değerini dinamik olarak okur.
print(f"Marka: {getattr(car, 'brand')}")  #* Toyota
print(f"Renk: {getattr(car, 'color', 'Bilinmiyor')}")  #* Bilinmiyor

#* setattr(nesne, "nitelik_adi", deger)
#* Attribute ekler veya mevcut attribute'un değerini değiştirir.
setattr(car, "color", "Beyaz")
setattr(car, "year", 2024)

print(f"Renk: {car.color}, Yıl: {car.year}")

#* delattr(nesne, "nitelik_adi")
#* Belirtilen attribute'u siler.
delattr(car, "year")

print(f"'year' silindikten sonra var mı? {hasattr(car, 'year')}")  #* False


#? 4. Örnek - getattr() ile Dinamik Metot Çağırma
#* Bir metot adını string olarak alıp çalışma zamanında
#* ilgili metodu bulup çağırabiliriz.

print("\n-------- 4. Örnek - Dinamik Metot Çağırma --------\n")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

#* Kullanıcıdan bir metot adı geldiğini varsayalım.
method_name = "multiply"

#* String olarak verilen metot adına karşılık gelen metot alınır.
method = getattr(calc, method_name)

#* Alınan metot çağrılır.
result = method(5, 3)

print(f"calc.{method_name}(5, 3) = {result}")

#* Tüm public metotları dinamik olarak listele
print("\nTüm metotlar:")

for attr_name in dir(calc):
    if not attr_name.startswith("_"):
        attr = getattr(calc, attr_name)

        if callable(attr):
            print(f"  → {attr_name}(): {attr(10, 5)}")


#? 5. Örnek - __new__ ile Nesne Oluşturma Kontrolü
#* __new__ metodu, __init__ metodundan önce çalışır.
#* Nesnenin oluşturulma sürecini kontrol eder.
#* Singleton gibi tasarım kalıplarında kullanılabilir.

print("\n-------- 5. Örnek - __new__ ve Singleton --------\n")

class Singleton:
    _instance = None  #* Sınıfa ait tek instance referansı

    def __new__(cls, *args, **kwargs):
        #* Eğer daha önce instance oluşturulmadıysa oluştur.
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        #* Her zaman aynı instance döndürülür.
        return cls._instance

    def __init__(self, value):
        #* __init__ her çağrıda çalışır.
        #* Ancak __new__ aynı instance'ı döndürür.
        self.value = value

s1 = Singleton("İlk")
s2 = Singleton("İkinci")

print(f"s1.value: {s1.value}")  #* İkinci
print(f"s2.value: {s2.value}")  #* İkinci
print(f"s1 is s2: {s1 is s2}")  #* True
print(f"id(s1): {id(s1)}, id(s2): {id(s2)}")  #* Aynı id


#? 6. Örnek - Monkey Patching
#* Mevcut bir sınıfın veya nesnenin davranışını çalışma zamanında değiştirmeye
#* veya ona yeni özellik/metot eklemeye Monkey Patching denir.
#* Özellikle mevcut kodu doğrudan değiştirmeden davranışını değiştirmek için kullanılabilir.

print("\n-------- 6. Örnek - Monkey Patching --------\n")

class Person:
    pass

#* Sınıfa çalışma zamanında yeni metot ekleniyor.
def new_method(self):
    print("New method added!")

Person.new_method = new_method

p1 = Person()
p1.new_method()

#* Sınıfa çalışma zamanında __init__ metodu ekleniyor/değiştiriliyor.
def enhanced_init(self, name, age):
    self.name = name
    self.age = age

Person.__init__ = enhanced_init

p2 = Person("Veysel", 25)

print(f"İsim: {p2.name}, Yaş: {p2.age}")

#* Sınıfa çalışma zamanında class attribute ekleniyor.
Person.species = "Homo Sapiens"

print(f"Tür: {p2.species}")


#? 7. Örnek - Sınıf Dekoratörü ile Dinamik Sınıf Modifikasyonu
#* Sınıf dekoratörü, sınıf tanımı tamamlandıktan sonra sınıfı alır
#* ve sınıf üzerinde değişiklik yapabilir.
#* Bu örnekte tüm instance'lara otomatik olarak creation_time ekleniyor.

print("\n-------- 7. Örnek - Sınıf Dekoratörü --------\n")

def add_timestamp(cls):
    #* Orijinal __init__ metodu saklanıyor.
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        import time

        #* Instance oluşturulurken yeni özellik ekleniyor.
        self.creation_time = time.time()

        #* Orijinal __init__ metodu çalıştırılıyor.
        original_init(self, *args, **kwargs)

    #* __init__ metodu yeni davranışla değiştiriliyor.
    cls.__init__ = new_init

    return cls

@add_timestamp
class User:
    def __init__(self, name):
        self.name = name

user = User("Veysel")

print(f"Kullanıcı: {user.name}")
print(f"Oluşturulma zamanı: {user.creation_time:.4f}")


#? 8. Örnek - type() ile Sınıf Üretimi
#* Sınıfın attribute ve metotları bir dictionary içerisinde tanımlanabilir.
#* Daha sonra type() kullanılarak bu bilgilerden yeni bir sınıf oluşturulabilir.
#* Burada eval() kullanılmamaktadır.

print("\n-------- 8. Örnek - Sınıf Üretimi --------\n")

class_dict = {
    "__init__": lambda self, x: setattr(self, "value", x),
    "__repr__": lambda self: f"DynamicClass(value={self.value})"
}

#* Dictionary içerisindeki bilgiler kullanılarak
#* çalışma zamanında yeni sınıf oluşturuluyor.
DynClass = type(
    "DynClass",
    (),
    class_dict
)

obj = DynClass(42)

print(f"DynamicClass: {obj}")


#? 9. Örnek - __call__ ile Sınıfı Fonksiyon Gibi Kullanma
#* __call__ metodu tanımlanan instance'lar fonksiyon gibi çağrılabilir.
#* Örneğin: object() şeklinde kullanılabilir.
#* Decorator ve callable object yapılarında kullanılabilir.

print("\n-------- 9. Örnek - __call__ ile Sınıf Kullanımı --------\n")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")  #* 10
print(f"triple(5) = {triple(5)}")  #* 15
print(f"double callable mı? {callable(double)}")  #* True


#? 10. Örnek - __init_subclass__ ile Sınıf Mirası Kontrolü
#* __init_subclass__, bir sınıftan yeni bir alt sınıf oluşturulduğunda
#* otomatik olarak çalışır.
#* Alt sınıfları takip etmek, kayıt altına almak veya kontrol etmek için kullanılabilir.

print("\n-------- 10. Örnek - __init_subclass__ --------\n")

class Plugin:
    _plugins = []  #* Tüm alt sınıfları takip eder.

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        #* Yeni oluşturulan alt sınıfı listeye ekle.
        Plugin._plugins.append(cls.__name__)

        print(f"  → Yeni eklenti kaydedildi: {cls.__name__}")

class AudioPlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

print(f"\nTüm eklentiler: {Plugin._plugins}")