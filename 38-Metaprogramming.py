 #? METAPROGRAMMING (Meta Programlama)

#* Metaprogramming, programların kendilerini çalışma zamanında (runtime)
#* manipulate etmesini sağlayan tekniklerdir.

#* Kelime anlamı: "programlama üzerine programlama"
#*   - Kod, diğer kodu üretir veya değiştirir
#*   - Sınıflar çalışma zamanında oluşturulabilir
#*   - Mevcut sınıflara/davranışlara dinamik olarak ekleme yapılabilir

#* Python'da metaprogramming'in temel araçları:
#*   1. type()         → Sınıflar dinamik olarak oluşturulabilir
#*   2. getattr/hasattr/setattr/delattr → Nitelikler üzerinde dinamik işlem
#*   3. __new__        → Nesne oluşumunu kontrol eden sihirli metot
#*   4. Metaclass      → Sınıfların nasıl oluşturulduğunu denetler
#*   5. Monkey Patching → Çalışma zamanında sınıfa/davranışa müdahale


#? 1.Örnek - type() ile Dinamik Sınıf Oluşturma
#* type() sadece tiplere bakmakla kalmaz, yeni sınıflar da üretir
#* type(name, bases, attrs) → name: sınıf adı, bases: miras alınan sınıflar, attrs: sözlük

print("\n--------1.Örnek - type() ile Dinamik Sınıf--------\n")

#* Klasik sınıf tanımı
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

#* type() ile aynısını oluşturabiliriz
PersonDynamic = type("PersonDynamic", (), {
    "name": None,
    "greet": lambda self: f"Hello, I'm {self.name}"
})

p1 = Person("Veysel")
p2 = PersonDynamic()
p2.name = "Veysel (Dynamic)"

print(f"Klasik: {p1.greet()}")
print(f"Dynamic: {p2.greet()}")
print(f"p1'in sınıfı: {type(p1)}")
print(f"p2'nin sınıfı: {type(p2)}")


#? 2.Örnek - type() ile Miras Alan Dinamik Sınıf
print("\n--------2.Örnek - Dinamik Miras--------\n")

def extra_method(self):
    return f"Extra method from {self.__class__.__name__}"

#* Person'dan türeyen ve ekstra metodu olan bir sınıf oluştur
DerivedPerson = type(
    "DerivedPerson",          #* Sınıf adı
    (Person,),                #* Miras alınan sınıflar (tuple)
    {"extra": extra_method}   #* Ek özellikler (sözlük)
)

dp = DerivedPerson("Ayşe")
print(dp.greet())      #* Person'dan gelen metot
print(dp.extra())      #* Dinamik olarak eklenen metot


#? 3.Örnek - getattr, hasattr, setattr, delattr
#* Bu fonksiyonlar bir nesnenin nitelikleriyle çalışma zamanında etkileşim kurar
#* Metaprogramming'in en temel araçlarındandır

print("\n--------3.Örnek - Dinamik Nitelik Erişimi--------\n")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Corolla")

#* hasattr(nesne, "nitelik_adi") → Nitelik var mı kontrol et
print(f"'brand' var mı? {hasattr(car, 'brand')}") #* True
print(f"'color' var mı? {hasattr(car, 'color')}") #* False

#* getattr(nesne, "nitelik_adi", varsayilan) → Niteliği oku
print(f"Marka: {getattr(car, 'brand')}") #* Toyota
print(f"Renk: {getattr(car, 'color', 'Bilinmiyor')}") #* Bilinmiyor (varsayılan)

#* setattr(nesne, "nitelik_adi", deger) → Niteliği ekle veya değiştir
setattr(car, "color", "Beyaz")
setattr(car, "year", 2024)
print(f"Renk: {car.color}, Yıl: {car.year}")

#* delattr(nesne, "nitelik_adi") → Niteliği sil
delattr(car, "year")
print(f"'year' silindikten sonra var mı? {hasattr(car, 'year')}")  #* False


#? 4.Örnek - getattr ile Dinamik Metot Çağırma
#* Bir metot adını string olarak alıp çalışma zamanında çağırabiliriz
print("\n--------4.Örnek - Dinamik Metot Çağırma--------\n")

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b

calc = Calculator()

#* Kullanıcıdan bir metot adı geldiğini varsayalım
method_name = "multiply"
method = getattr(calc, method_name)  #* Metodu string olarak al
result = method(5, 3)               #* Çağır
print(f"calc.{method_name}(5, 3) = {result}")

#* Tüm metotları dinamik olarak listele
print("\nTüm metotlar:")
for attr_name in dir(calc):
    if not attr_name.startswith("_"):  #* Özel nitelikleri atla
        attr = getattr(calc, attr_name)
        if callable(attr):  #* Çağrılabilir mi kontrol et
            print(f"  → {attr_name}(): {attr(10, 5)}")


#? 5.Örnek - __new__ ile Nesne Oluşturma Kontrolü
#* __new__, __init__'den önce çalışır
#* Nesnenin oluşumunu tamamen kontrol etmemizi sağlar
#* Genellikle Singleton tasarım kalıbı için kullanılır
print("\n--------5.Örnek - __new__ ve Singleton--------\n")

class Singleton:
    _instance = None  #* Sınıfa ait tek_instance referansı

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  #* Eğer henüz instance yoksa
            cls._instance = super().__new__(cls)  #* Yeni oluştur
        return cls._instance  #* Her zaman aynı instance'ı döndür

    def __init__(self, value):
        self.value = value  #* __init__ her çağrıda çalışır ama instance aynıdır

s1 = Singleton("İlk")
s2 = Singleton("İkinci")

print(f"s1.value: {s1.value}")          #* İkinci (son atama)
print(f"s2.value: {s2.value}")          #* İkinci
print(f"s1 == s2: {s1 is s2}")          #* True (aynı nesne)
print(f"id(s1): {id(s1)}, id(s2): {id(s2)}")  #* Aynı id


#? 6.Örnek - Monkey Patching (Çalışma Zamanında Sınıfa Müdahale)
#* Mevcut bir sınıfa çalışma zamanında yeni metot veya nitelik ekler
#* Üçüncü parti kütüphanelerde davranış değiştirmek için kullanılır
print("\n--------6.Örnek - Monkey Patching--------\n")

class Person:
    pass

#* Sınıfa yeni metot ekle
def newMethod(self):
    print("New method added!")

Person.newMethod = newMethod

p1 = Person()
p1.newMethod()  #* New method added!

#* Mevcut metodu değiştir (override)
def enhanced_init(self, name, age):
    self.name = name
    self.age = age

Person.__init__ = enhanced_init
p2 = Person("Veysel", 25)
print(f"İsim: {p2.name}, Yaş: {p2.age}")

#* Sınıfa类属性 ekle
Person.species = "Homo Sapiens"
print(f"Tür: {p2.species}")


#? 7.Örnek - Sınıf Dekoratörü ile Dinamik Sınıf Modifikasyonu
#* Sınıf dekoratörleri, sınıf tanımı biter bitmez çalışır
#* Tüm instance'lara otomatik olarak özellik ekler
print("\n--------7.Örnek - Sınıf Dekoratörü--------\n")

def add_timestamp(cls):
    """Her instance'a creation_time ekler."""
    import time
    original_init = cls.__init__  #* Orijinal __init__'i sakla

    def new_init(self, *args, **kwargs):
        self.creation_time = time.time()  #* Yeni özellik ekle
        original_init(self, *args, **kwargs)  #* Orijinal_init'i çağır

    cls.__init__ = new_init
    return cls

@add_timestamp
class User:
    def __init__(self, name):
        self.name = name

user = User("Veysel")
print(f"Kullanıcı: {user.name}")
print(f"Oluşturulma zamanı: {user.creation_time:.4f}")


#? 8.Örnek - Sınıfı String Olarak Oluşturma ve eval() ile Çalıştırma
#* __new__ gibi __prepare__ ve __init_subclass__ da metaprogramming araçlarıdır
print("\n--------8.Örnek - Sınıf Üretimi--------\n")

#* Bir sınıfı sözlükten oluştur
class_dict = {
    "__init__": lambda self, x: setattr(self, 'value', x),
    "__repr__": lambda self: f"DynamicClass(value={self.value})"
}

#* Sınıf oluştur ve kullan
DynClass = type("DynClass", (), class_dict)
obj = DynClass(42)
print(f"DynamicClass: {obj}")


#? 9.Örnek - __call__ ile Sınıfı Fonksiyon Gibi Kullanma
#* __call__ metodu tanımlanırsa, instance() ile çağrılabilir hale gelir
#* Bu, decorator'lar ve factory fonksiyonları için çok kullanışlıdır
print("\n--------9.Örnek - __call__ ile Sınıf Kullanımı--------\n")

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  #* Çarpma faktörünü sakla

    def __call__(self, x):
        return x * self.factor  #* Instance fonksiyon gibi çağrılabilir

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")    #* 10
print(f"triple(5) = {triple(5)}")    #* 15
print(f"double callable mı? {callable(double)}")  #* True


#? 10.Örnek - __init_subclass__ ile Sınıf Mirası Kontrolü
#* Ebeveyn sınıf, türeyen sınıfları otomatik olarak düzenleyebilir
print("\n--------10.Örnek - __init_subclass__--------\n")

class Plugin:
    _plugins = []  #* Tüm eklentileri takip et

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin._plugins.append(cls.__name__)  #* Yeni türeyen sınıfı kaydet
        print(f"  → Yeni eklenti kaydedildi: {cls.__name__}")

class AudioPlugin(Plugin):
    pass

class VideoPlugin(Plugin):
    pass

print(f"\nTüm eklentiler: {Plugin._plugins}")
