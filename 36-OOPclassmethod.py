    #? Class Method
#* @classmethod decorator'ı ile oluşturulur
#* İlk parametresi otomatik olarak cls'dir
#* cls, class'ın kendisini temsil eder
#* Class method hem class üzerinden hem de instance üzerinden çağrılabilir
#* Class attribute'larını değiştirmek veya class üzerinden işlem yapmak için kullanılabilir
#* Alternative constructor (alternatif kurucu) oluşturmak için de kullanılabilir

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birth_year(cls, name, birth_year):
        current_year = 2026
        calculated_age = current_year - birth_year
        return cls(name, calculated_age)
    #* cls, class'ın kendisini temsil eder.
    #* Person.birth_year() çağrıldığında cls → Person olur.

    def display_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person.birth_year("Veysel KUŞ",2007)
print(p1.display_info()) 

print("------------------------------------------")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_company(cls, new_company_name):
        cls.company = new_company_name

    @classmethod
    def create_employee(cls, name , salary):
        return cls(name, int(salary))

    def display_info(self):
        return f"Employee: {self.name}\nSalary: {self.salary}\nCompany: {self.company}"


emp1 = Employee.create_employee("Veysel KUŞ",10000)
Employee.set_company("VeYdasel")
print(emp1.display_info())