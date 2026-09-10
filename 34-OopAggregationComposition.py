    #? Aggregation
#* Birbirinden bağımsız bağımlı classlar
#* Classlar birbirinden bağımsız olarak var olabilir
#* Department, Employee nesnelerini kullanır ancak Employee'leri kendisi oluşturmaz

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Department:
    def __init__(self, name_dp):
        self.name_dp = name_dp
        self.employees = [] #* Aggregation

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_department(self):
        print(f"Department: {self.name_dp}")
        for item in self.employees:
            print(f"Employee: {item.name}, ID: {item.emp_id}")

e1 = Employee("Veysel KUŞ",19)
e2 = Employee("Abuzer ÇAYCI",21)

dept = Department("Software Development")

dept.add_employee(e1)
dept.add_employee(e2)

dept.show_department()
#* Aggregation: "Has-a" ilişkisi vardır
#* Department, Employee nesnelerine sahiptir
#* Ancak Employee nesneleri Department'tan bağımsız olarak var olabilir
#* Department silinse bile Employee nesneleri varlığını sürdürebilir


#? Birbirinden bağımsız bağımlı classlar , bağları daha güçlüdür
#* Composition: "Has-a" ilişkisi vardır ancak bağ daha güçlüdür
print("------------------------------------------")

class Employee2:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Department2:
    def __init__(self, name_dp, employees):
        self.name_dp = name_dp
        self.employees = [Employee2(e[0],e[1]) for e in employees] #* Composition

    def show_department(self):
        print(f"Department: {self.name_dp}")
        for item in self.employees:
            print(f"Employee: {item.name}, ID: {item.emp_id}")

dept = Department2("Software Development",[("Veysel KUŞ",19),("Abuzer ÇAYCI",21)])

dept.show_department()

#* Department2, Employee2 nesnelerinin oluşturulmasından sorumludur
#* Employee2 nesneleri Department2'nin yapısının bir parçasıdır