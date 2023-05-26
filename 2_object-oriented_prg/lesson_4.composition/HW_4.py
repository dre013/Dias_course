class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст
 
    @property
    def name(self):
        return self.__name
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
 
 
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company
 
    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print("Компания:", self.company)
 
 
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university
 
    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)

class Boss(Person):                                                          # Добавление в композицию
    def __init__(self, name, age, company, cup):
        Employee.__init__(self, name, age, company)
        self.cup = cup

    def display_info(self):
        # Person.display_info(self)
        Employee.display_info(self)
        print(f'Босс из компании {self.company} пьет из {self.cup} кружки.')

tom = Person("Tom", 23)
bob = Student("Bob", 19, "Harvard")
sam = Employee("Sam", 35, "Google")
vitya = Boss('Vitaliy', 45, 'Yandex', 'красной')

employees = [tom, bob, sam, vitya]
for employee in employees:
    employee.display_info()
    print()





# def my_decorator(f):                                          # Тест декораторов 1
#     @wraps(f)
#     def wrapper(*args, **kwds):
#         print('Calling decorated function')
#         return f(*args, **kwds)
#     return wrapper

# @my_decorator
# def example():
#     """Docstring"""
#     print('Called example function')

# example()




import math
from functools import wraps

def salary(func):                                               # Тест декораторов 2
    @wraps(func)
    def total(*args, **kwargs):
        print(f'Function {func.__name__} is ended')
        return func(*args, **kwargs)
    return total

@salary
def factorial(num):
    print(math.factorial(num))

factorial(8)