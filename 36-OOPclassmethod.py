
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    @classmethod
    def birth_year(cls, name, birth_year):
        current_year = 2026
        calculated_age = current_year - birth_year
        return cls(name, calculated_age)
    #* cls , Person'u temsil eder

    def display_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person.birth_year("Veysel KUŞ",2007)
print(p1.display_info()) 

print()
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_company(cls, new_company_name):
        cls.company = new_company_name

    @classmethod
    def get_value(cls, name , salary):
        return cls(name, int(salary))

    def display_info(self):
        return f"Employee: {self.name}\nSalary: {self.salary}\nCompany: {self.company}"


emp1 = Employee.get_value("Veysel KUŞ",10000)
Employee.set_company("VeYdasel")
print(emp1.display_info())