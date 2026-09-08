 #? Sihirli Metotlar (Dunder Methods)

#* __methodadı__ şeklinde yazılan özel metotlardır
#* Python'un belirli işlemler sırasında otomatik olarak çağırdığı metotlardır
#* Bu metotları genellikle kendimiz doğrudan çağırmayız
#* Yaptığımız işlemin arka planında ilgili sihirli metot çalışır

#* Örneğin:
#* len(obj) → obj.__len__()
#* obj[index] → obj.__getitem__(index)
#* obj[index] = value → obj.__setitem__(index, value)
#* del obj[index] → obj.__delitem__(index)
#* obj1 + obj2 → obj1.__add__(obj2)

#! Sihirli metotların işlevlerini değiştirebilir ve kendi sınıflarımızda farklı davranışlar tanımlayabiliriz.


class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self,):  #* uzunluk için kullanılır
        return len(self.items)

    def __getitem__(self, index):  #* öğeleri almak için kullanılır
        return self.items[index]

    def __setitem__(self, index, value):  #* öğeleri güncellemek için kullanılır
        self.items[index] = value

    def __delitem__(self, index):  #* öğeleri silmek için kullanılır
        del self.items[index]

my_list = CustomList([1, 7, 19, 12, 5, 2])

print("------------------------------------------")
print("len(my_list) →",len(my_list))
print("my_list[3] →",my_list[3])

my_list[3] = 100
print("my_list[3] = 100 →",my_list[3])

del my_list[3]
print("del my_list[3] (3.index'in yerini 4.indexteki(5) aldı)→",my_list[3]) #* 3.indexteki silindi ama hata vermez, artık 3.indexte 5 var

print("------------------------------------------")


class Greet:
    def __call__(self, name):  #* nesnenin fonksiyon gibi çağrılabilmesini sağlar
        return f"Hello {name}"

greet = Greet()
print('greet("Veysel KUŞ") →',greet("Veysel KUŞ"))

print("------------------------------------------")


class Person:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):  #* eşit mi diye karşılaştırmak için kullanılır
        return self.number == other.number

    def __lt__(self, other):  #* küçük mü diye karşılaştırmak için kullanılır
        return self.number < other.number

    def __le__(self, other):  #* küçük eşit mi diye karşılaştırmak için kullanılır
        return self.number <= other.number

    def __gt__(self, other):  #* büyük mü diye karşılaştırmak için kullanılır
        return self.number > other.number

    def __ge__(self, other):  #* büyük eşit mi diye karşılaştırmak için kullanılır
        return self.number >= other.number

    def __ne__(self, other):  #* eşit değil mi diye karşılaştırmak için kullanılır
        return self.number != other.number

p1 = Person(4)
p2 = Person(8)

print(f"p1 == p2 → {p1 == p2}") #* __eq__ çalışır
print(f"p1 < p2 → {p1 < p2}") #* __lt__ çalışır
print(f"p1 <= p2 → {p1 <= p2}") #* __le__ çalışır
print(f"p1 > p2 → {p1 > p2}") #* __gt__ çalışır
print(f"p1 >= p2 → {p1 >= p2}") #* __ge__ çalışır
print(f"p1 != p2 → {p1 != p2}") #* __ne__ çalışır

print("------------------------------------------")


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  #* toplama işleminin sihirli metodu
        return Number(self.value + other.value)

    def __sub__(self, other):  #* çıkarma işleminin sihirli metodu
        return Number(self.value - other.value)

    def __mul__(self, other):  #* çarpma işleminin sihirli metodu
        return Number(self.value * other.value)

    def __truediv__(self, other):  #* bölme işleminin sihirli metodu
        if other.value == 0:
            raise ValueError("Division by zero is not allowed!")
        return Number(self.value / other.value)

    def __floordiv__(self, other):  #* ondalıksız bölme işleminin sihirli metodu
        return Number(self.value // other.value)

    def __mod__(self, other):  #* mod alma işleminin sihirli metodu
        return Number(self.value % other.value)

    def __pow__(self, other):  #* üst alma işleminin sihirli metodu
        return Number(self.value ** other.value)

    def __neg__(self):  #* sayıyı negatif yapma işleminin sihirli metodu
        return Number(-self.value)

    def __pos__(self):  #* sayıyı pozitif yapma işleminin sihirli metodu
        return Number(+self.value)

    def __abs__(self):  #* sayının mutlak değerini alma işleminin sihirli metodu
        return Number(abs(self.value))

    def __str__(self):
        return str(self.value)


number1 = Number(10)
number2 = Number(-3)
print("number1 →",number1)
print("number2 →",number2)
print()

print("number1 + number2 →",number1 + number2) #* __add__ çalışır
print("number1 - number2 →",number1 - number2) #* __sub__ çalışır
print("number1 * number2 →",number1 * number2) #* __mul__ çalışır
print("number1 / number2 →",number1 / number2) #* __truediv__ çalışır
print("number1 // number2 →",number1 // number2) #* __floordiv__ çalışır
print("number1 ** number2 →",number1 ** number2) #* __pow__ çalışır
print("number1 % number2 →",number1 % number2) #* __mod__ çalışır
print("-number1 →",-number1) #* __neg__ çalışır
print("+number1 →",+number1) #* __pos__ çalışır
print("abs(number2) →",abs(number2)) #* __abs__ çalışır

print("------------------------------------------")


#! Sihirli metotların işlevini değiştirebiliriz
#* Yani normalde belirli bir işlem için kullanılan sihirli metoda, kendi sınıfımız içerisinde farklı bir işlev verebiliriz

class IslevDisi:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        #* __getitem__ normalde elemanı getirmek için kullanılır.
        #* Ancak burada elemanı döndürmek yerine siliyoruz.
        del self.items[index]


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
islevdisi = IslevDisi(liste)

print(islevdisi[2])
#* [2] ile eleman çağırıldığı için __getitem__ metodu çalışır. Ancak __getitem__ içerisinde elemanı döndürmek yerine siliyoruz. Methodda return olmadığı için sonuç None olur