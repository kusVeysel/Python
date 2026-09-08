class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name_function(self): #* getter method
        return self.name

    @name_function.setter #* setter method
    def name_function(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty!")
        self.name = new_name

    @name_function.deleter
    def name_function(self): #* deleter method
        print("Deleting name varible...")
        self.name = None


p1 = Person("Veysel KUŞ")
print(p1.name_function)

p1.name_function = "Abuzer ÇAYCI"
print(p1.name_function)

del p1.name_function
print(p1.name_function)