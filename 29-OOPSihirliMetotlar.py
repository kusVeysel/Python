
#! Sihirli metorlar(__methodadı__) otomatik çalışır hepsinin görevi vardır, mesela bir elemanı silmek için del yaptığınızda siz methody çağırmasanız bile otomatik olarak __del__ sihirli methoduna gider ve siler, ya da bir listenin bir elemenını getirmek istediğinizde listeadı[index] yaptığınızda __getitem__ sihirli methodunu çağırmazsanız bile otomatik olarak __getitem__ sihirli methoduna gider ve size ilgili elemanı getirir

class CustomList:
    def __init__(self,items):
        self.items = items
    def __len__(self): #* uzunluk için kullanılır
        return len(self.items)
    def __getitem__(self, index): #* öğeleri almak için kullanılır
        return self.items[index]
    def __setitem__(self, index, value): #* öğeleri güncellemek için kullanılır
        self.items[index] = value
    def __delitem__(self, index): #* öğeleri silmek için kullanılır
        del self.items[index]

class Greet:
    def __call__(self, name): #* self.name demeden direk name diyerek değişkeni yazmamızı sağlar
        return f"Hello {name}"

class Person:
    def __init__(self,  number):
        self.number = number
    def __eq__(self,other): #* eşit mi diye karşılaştırmak için kullanılır
        return self.number == other.number
    def __lt__(self, other): #* küçük mü diye karşılaştırmak için kullanılır
        return self.number < other.number
    def __le__(self, other): #* küçük eşit mi diye karşılaştırmak için kullanılır
        return self.number <= other.number
    def __gt__(self, other): #* büyük mü diye karşılaştırmak için kullanılır
        return self.number > other.number
    def __ge__(self, other): #* büyük eşit mi diye karşılaştırmak için kullanılır
        return self.number >= other.number
    def __ne__(self, other): #* eşit değil mi diye karşılaştırmak için kullanılır
        return self.number != other.number

class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self, other): #* toplama işleminin sihirli methodu
        return Number(self.value + other.value)
    def __sub__(self, other): #* çıkarma işleminin sihirli methodu
        return Number(self.value - other.value)
    def __mul__(self, other): #* çarpma işleminin sihirli methodu
        return Number(self.value * other.value)
    def __truediv__(self, other): #* bölme işleminin sihirli methodu
        if(other.value == 0):
            raise ValueError("Division by zero is not allowed!")
        return Number(self.value / other.value)
    def __floordiv__(self, other): #* ondalıksız bölme işleminin sihirli methodu
        return Number(self.value // other.value)
    def __mod__(self, other): #* mod alma işleminin sihirli methodu
        return Number(self.value % other.value)
    def __pow__(self, other): #* üst alma işleminin sihirli methodu
        return Number(self.value ** other.value)
    def __neg__(self): #* sayıyı negatif yapma işleminin sihirli methodu
        return Number(-self.value)
    def __pos__(self):  #* sayıyı pozitif işleminin sihirli methodu
        return Number(+self.value)
    def __abs__(self): #* sayının mutlak değerini(pozitif yapmanın) almanın işleminin sihirli methodu
        return Number(abs(self.value))
    def __str__(self):
        return str(self.value)


number1 = Number(10)
number2 = Number(3)
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(number1 // number2)
print(number1 ** number2)
print(number1 % number2)
print(-number1)
print(+number1)
print(abs(number1))


print()
p1 = Person(4)
p2 = Person(8)
print(p1 == p2)
print(p1 < p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 >= p2)
print(p1 != p2)

print()
my_list = CustomList([1,7,19,12,5,2])
print(len(my_list))


print()
greet = Greet()
print(greet("Veysel KUŞ"))



#! Sihirli methodların işlevini değiştirebiliriz yani işlevinin dışında bir yeni işlev verebiliriz

class IslevDisi:
    def __init__(self,items):
        self.items = items
    def __getitem__(self, index):
        del self.items[index] #* getitem normalde elemanı getirmek için kullanılan sihirli bir methottur ama biz del kullanarak çağrılan elemanın silinmesini sağladık 

liste = [1,2,3,4,5,6,7,8,9]
islevdisi = IslevDisi(liste)
print(islevdisi[2]) #* elemanı çağırdığımız için __getitem__ methoduna gider ama orda çağrılan elemanın silinmesini sağladığımız için elemanı bulamaz Null(None) döner