 #? @property
#* Getter: Property'nin değerini okumak için kullanılır
#* Setter: Property'ye yeni bir değer atanırken çalışır
#* Deleter: Property silinirken çalışır
#* @property sayesinde method, parantez kullanılmadan attribute gibi kullanılabilir

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name_function(self): #* Getter method: Değeri okumak için kullanılır
        return self.name

    @name_function.setter #* Setter method: Yeni değer atanırken çalışır
    def name_function(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty!")
        self.name = new_name

    @name_function.deleter
    def name_function(self): #* Deleter method: Property silinirken çalışır
        print("Deleting name variable...")
        self.name = None


p1 = Person("Veysel KUŞ")
print(p1.name_function)

p1.name_function = "Abuzer ÇAYCI"
print(p1.name_function)

del p1.name_function
print(p1.name_function)