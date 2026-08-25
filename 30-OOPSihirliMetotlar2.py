my_tuple = ("Grpahe","Strawberry","Fig","Cherry","Pineapple")
my_iterable = iter(my_tuple)

# my_string = "Veysel"
# my_iterable = iter(my_string)

print(next(my_iterable)) #* sonraki değeri verir
print(next(my_iterable)) #* sonraki değeri verir
print(next(my_iterable)) #* sonraki değeri verir

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

print()
for item in my_object:
    print(item)

print()


class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def __delattr__(self, attr):
        if attr == "name":
            raise AttributeError("Cannot delete name attribute!")
        super().__delattr__(attr)
    def __getattr__(self, attr): #* attribute(property) için kullanılan sihirli methodu
        return f"'{attr}' attribute (propert) is not found"
    def __setattr__(self, attr, value): #* attribute(property) güncellemek(eklemek) için kullanılan sihirli methodu
        super().__setattr__(attr,value)
        

p1 = Person("Veysel KUŞ",1)
print(p1.name)
print(p1.age)
p1.age = 19
print(p1.age)
del p1.number
print(hasattr(p1,"number"))

print()
class Number:
    def __init__(self,value):
        self.value = value
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)

number = Number(7.19)
number2 = Number(7)
print(int(number))
print(float(number2))
    