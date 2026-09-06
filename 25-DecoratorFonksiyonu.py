
#? 1.Örnek
print("\n--------1.Örnek--------\n")

def decorator_function(func):
    def wrapper_function(*args,**kwargs):
        print(f"{func.__name__} is start")
        result = func(*args,**kwargs)
        print(f"{func.__name__} is end")
        return result
    return wrapper_function

@decorator_function
def myMessage():
    print("This is an example function")

myMessage()

#* __name__ : fonksiyonun ismini verir


#? 2.Örnek
print("\n--------2.Örnek--------\n")

def authentication(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("auth",False):
            print(f"Authorization failed for {user['name']} !")
            return
        return func(user,*args,**kwargs)
    return wrapper

@authentication
def view_account(user):
    print(f"Welcome, {user['name']}")

user1 = {
    "name":"Veysel KUŞ",
    "auth":True
}
user2 = {
    "name":"Abuzer ÇAYCI",
    "auth":False
}

view_account(user1)
view_account(user2)

#? 3.Örnek
print("\n --------3.Örnek--------\n")
import time

def timer_decoration(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} completed in {end_time-start_time:.4f} second\n")
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

#? 4.Örnek
print("\n --------4.Örnek--------\n")

def flexible_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Function name is {func.__name__}")
        if(args):
            print(f"args for {func.__name__}: {args}")
        else:
            print(f"args for {func.__name__}: none")
        if(kwargs):
            print(f"kwargs for {func.__name__}: {kwargs}")
        else:
            print(f"kwargs for {func.__name__}: none")
        result = func(*args,**kwargs)
        print(f"{func.__name__} function's result: {result}",end="\n\n")
        return result
    return wrapper

@flexible_decorator
def add(x,y):
    return x+y

@flexible_decorator
def greet(name,age,country):
    return f"Hello {name}, your age is {age} and your country is {country}"

@flexible_decorator
def multiply_and_sum(*numbers,factor):
    return sum(numbers)*factor

add(3,4)
greet("Veysel KUŞ", age=19, country="Türkiye")
multiply_and_sum(2,5,7,1,factor=3)

