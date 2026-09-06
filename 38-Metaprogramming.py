
#! Bu örnek çalışma zamanında sınıfa metot ekleme (monkey patching) gösterir.
#! metaprogramming kavramının yalnızca bir örneğidir.

def newMethod(self):
    print("New method added!")

class Person:
    pass

Person.newMethod = newMethod
p1 = Person()
p1.newMethod()


