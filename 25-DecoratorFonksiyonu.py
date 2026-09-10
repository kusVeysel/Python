 #? DECORATOR (Süsleyici / Dekoratör) Fonksiyonu

#* Decorator, bir fonksiyonun çalışma zamanında davranışını değiştirmeden ona yeni özellikler eklememizi sağlayan bir tasarım kalıbıdır

#* Temel prensip: Fonksiyonları birer nesne olarak kabul eden Python, onları başka bir fonksiyona argüman olarak gönderebilir ve geri döndürebilir

#* @decorator sözdizimi aslında şuna eşdeğerdir:
#*   my_func = decorator(my_func)

#* Yani @ işareti, fonksiyonu decorator'a sarar(wrap) ve orijinal fonksiyonun yerine wrapper fonksiyonu koyar.

#* *args ve **kwargs:
#* *args   → Sıralı (positional) argümanları tuple olarak toplar
#* **kwargs → Anahtar kelime (keyword) argümanlarını dict olarak toplar. Bu sayede decorator her tür fonksiyona uygulanabilir.


#? 1.Örnek - Temel Decorator Yapısı
print("\n--------1.Örnek--------\n")

from functools import wraps  #* wraps: decorator'ın orijinal fonksiyonun __name__, __doc__ gibi metadata'sını korur

def decorator_function(func):
    @wraps(func)  #* Orijinal fonksiyonun ismini ve docstring'ini korur
    def wrapper_function(*args, **kwargs):
        print(f"{func.__name__} is start")  #* Fonksiyon çalışmadan önce yapılacak işlem
        result = func(*args, **kwargs)       #* Orijinal fonksiyonu çalıştırır
        print(f"{func.__name__} is end")    #* Fonksiyon çalıştıktan sonra yapılacak işlem
        return result                        #* Orijinal fonksiyonun dönüş değerini iletir
    return wrapper_function  #* Wrapper fonksiyonu döndürür (fonksiyonun kendisi değil!)

@decorator_function  #* myMessage = decorator_function(myMessage) anlamına gelir
def myMessage():
    print("This is an example function")

myMessage()

#* __name__ : fonksiyonun ismini verir
#* @wraps kullanılmazsa myMessage.__name__ "wrapper_function" olurdu, "myMessage" değil
print(f"Fonksiyon ismi: {myMessage.__name__}\n")  #* myMessage (dekoratör sayesinde)


#? 2.Örnek - Yetkilendirme (Authentication) Decorator'ı
#* Gerçek hayatta API endpoint'lerinde, sayfa erişimlerinde kullanılır
print("\n--------2.Örnek--------\n")

def authentication(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        #* user parametresi wrapper içinde doğrudan alınır, böylece orijinal fonksiyona extra parametre eklenmez
        if not user.get("auth", False):
            print(f"Authorization failed for {user['name']} !")
            return  #* Yetkisi yoksa fonksiyonu hiç çalıştırmaz
        return func(user, *args, **kwargs)  #* Yetkisi varsa orijinal fonksiyonu çalıştırır
    return wrapper

@authentication
def view_account(user):
    print(f"Welcome, {user['name']}")

user1 = {
    "name": "Veysel KUŞ",
    "auth": True
}
user2 = {
    "name": "Abuzer ÇAYCI",
    "auth": False
}

view_account(user1) 
view_account(user2)


#? 3.Örnek - Zaman Ölçücü (Timer) Decorator'ı
#* Performans testlerinde, API çağrılarında, veritabanı sorgularında kullanılır
print("\n --------3.Örnek--------\n")
import time

def timer_decoration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()           #* Başlangıç zamanını kaydet
        result = func(*args, **kwargs)     #* Orijinal fonksiyonu çalıştır
        end_time = time.time()             #* Bitiş zamanını kaydet
        elapsed = end_time - start_time    #* Geçen süreyi hesapla
        print(f"Function {func.__name__} completed in {elapsed:.4f} seconds\n")
        return result
    return wrapper

@timer_decoration
def slow_function(n):
    total = sum(range(n))
    print(f"Total: {total}")

@timer_decoration
def fast_function(n):
    total = sum(range(n))
    print(f"Total: {total}")

@timer_decoration
def faster_function(n):
    total = sum(range(n))
    print(f"Total: {total}")

slow_function(1000000)
fast_function(100000)
faster_function(10000)


#? 4.Örnek - Esnek (Flexible) Decorator
#* Farklı imzalara sahip fonksiyonlarda kullanılabilir
print("\n --------4.Örnek--------\n")

def flexible_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")

        #* Positional argümanları göster
        if args:
            print(f"  args: {args}")
        else:
            print(f"  args: none")

        #* Keyword argümanları göster
        if kwargs:
            print(f"  kwargs: {kwargs}")
        else:
            print(f"  kwargs: none")

        result = func(*args, **kwargs)  #* Orijinal fonksiyonu çalıştır
        print(f"  Result: {result}\n")
        return result
    return wrapper

@flexible_decorator
def add(x, y):
    return x + y

@flexible_decorator
def greet(name, age, country):
    return f"Hello {name}, your age is {age} and your country is {country}"

@flexible_decorator
def multiply_and_sum(*numbers, factor):
    """Sayıları toplar ve factor ile çarpar."""
    return sum(numbers) * factor

add(3, 4)
greet("Veysel KUŞ", age=19, country="Türkiye")
multiply_and_sum(2, 5, 7, 1, factor=3)


#? 5.Örnek - Decorator Zincirleme (Decorator Chaining)
#* Birden fazla decorator'ı üst üste uygulayabilirsiniz
#* @A @B my_func → A(B(my_func)) şeklinde çalışır
print("\n --------5.Örnek--------\n")

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold       #* Dış: bold(say_hello)
@italic     #* İç: italic(say_hello)
def say_hello(name):
    return f"Hello {name}"

print(say_hello("Veysel"))  #* <b><i>Hello Veysel</i></b>
print(f"Fonksiyon adı: {say_hello.__name__}\n")  #* say_hello (metadata korunur)


#? 6.Örnek - Parametre Alan Decorator
#* Decorator'ın kendisi de parametre alabilir
#* Bunun için 3 katmanlı yapı kullanılır
print("\n --------6.Örnek--------\n")

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times = 3)  #* repeat(3) → decorator döndürür → @decorator uygulanır
def greet(name):
    print(f"Hello {name}!")

greet("Veysel")