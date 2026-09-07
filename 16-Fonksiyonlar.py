# def fonksiyon_adı(props):
#     pass
#
# fonksiyon_adı(props)


def my_function_name(name):
    print(f"Merhaba {name}!")

name = input("İsminizi giriniz: ")
my_function_name(name)


#! Dinamik bir şey yapıyorsan ve kaç parametre geleceğini bilmiyorsan ya da gönderdiğin parametre adeti hep değişiyorsa "*" (accumulator) kullanılır 
def dinamik_fonksion(*args):
    for arg in args:
        print(f"{arg}", end=" ") 
    # döngü kullanmazsak arsg[index] ile de değerlere erişilebilir

dinamik_fonksion("Veysel","Kuş",19) 


def isim(name2, name3, name1):
    pass
isim(name1 = "veysel", name2 = "ahmet", name3 = "mahmut")
#* Bu sayede fonksiyonun parametresinde sıralama önemsiz şekilde değerleri atabiliyoruz


def my_name(**kwargs):
    print(kwargs["firstname"], kwargs["lastname"])

my_name(firstname = "abuzer", lastname = "çaycı")
#* Bu sayede fonksiyona giden her parametre için, karşılık yazmaya gerek yok ve anahtarlarla değelerine erişebiliyoruz

#! key-value için = **
#! normal kullanım için = *  


#? Default Parametre Kullanım

def my_counrty(counrty = "Türkiye"):
    print(f"Benim ülkem: {counrty}")

my_counrty("İsviçre")


#? return
#* Geriye değer döndürür

def mat(x):
    return x * x

sayi = mat(5)
print(sayi)

def carp(number):
    return number * 7

def x(a, value): #* a = carp fonksiyonu 
    return a(value)

result = x(carp, 10)
print(result)


#? Fonksiyon İçinde Fonksiyon Kullanımı

def outer_function(name):
    def greeting():
        return f"Hello {name}"
    return greeting()

print(outer_function("Veysel"))


def square(number):
    return number ** 2

def sum_and_square(x, y):
    sum_result= x + y
    return square(sum_result)

result = sum_and_square(3, 4)
print(result)

#! return birden fazla veri döndürebilir ,tek adet veri döndermek zorunda değil


#? Recursion(Rekürsif) fonksiyon

def fac(n):
    if n < 0:
        raise ValueError("Faktöriyel negatif sayılar için tanımlı değildir.")
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fac(n - 1)
    
print(fac(5))


def fib(n):
    if n < 0:
        raise ValueError("Fibonacci indisi negatif olamaz.")
    if(n <= 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
for item in range(10):
    print(fib(item), end=" ")

print()
def topla(n):
    if(n <= 0):
        raise ValueError("Pozitif bir sayı girilmelidir.")
    if(n == 1):
        return 1
    else:
        return n + topla(n-1)

print(topla(int(input("Toplanacak sayıyı gir"))))

#* raise hata yazdırmak için kullanılır