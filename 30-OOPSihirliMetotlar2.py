 #? iter() - next() Kullanımı

my_tuple = ("Grpahe","Strawberry","Fig","Cherry","Pineapple")
my_iterable = iter(my_tuple)

# my_string = "Veysel"
# my_iterable = iter(my_string)

print(next(my_iterable)) #* Iterator'ın sıradaki değerini döndürür
print(next(my_iterable)) #* Iterator'ın sıradaki değerini döndürür
print(next(my_iterable)) #* Iterator'ın sıradaki değerini döndürür


for item in my_tuple:
    print(item)
#* next next next next... ile aynı işlevi görür


class Counter:
    def __init__(self,max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.current < self.max_value):
            self.current += 1
            return self.current
        else:
            raise StopIteration
    
my_object = Counter(19)
my_iterable = iter(my_object)

print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))

print("------------------------------------------")

for item in my_object:
    print(item)
#* aynı gösterim
print("------------------------------------------")


class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def __delattr__(self, attr):
        if attr == "name":
            raise AttributeError(f"Cannot delete {attr} attribute!")
        super().__delattr__(attr)

    def __getattr__(self, attr): #* İstenen attribute bulunamadığında otomatik çalışır.
        raise AttributeError(f"{attr} attribute (propert) is not found")
    
    def __setattr__(self, attr, value): #* Bir attribute oluşturulurken veya değeri değiştirilirken çalışır
        super().__setattr__(attr,value)
        
    def __str__(self):
        return str(self.value)
    
p1 = Person("Veysel KUŞ",1)

print(p1.name)
# print(p1.age) #* Bu attribute olmadığı için __getattr__ çalışır
p1.age = 19 #* __setattr__ çalışır
print(p1.age)

del p1.number
print(hasattr(p1, "number"))

print("------------------------------------------")


class Number:
    def __init__(self,value):
        self.value = value

    def __int__(self): #* sayıyı int yapma işleminin sihirli metodu
        return int(self.value)
    
    def __float__(self): #* sayıyı float yapma işleminin sihirli metodu
        return float(self.value)

    def __str__(self):
        return str(self.value)


number1 = Number(7.19)
number2 = Number(7)
print("number1 →",number1)
print("number2 →",number2)

print("int(number1) →",int(number1)) #* __int__ çalışır
print("float(number2) →",float(number2)) #* __float__ çalışır