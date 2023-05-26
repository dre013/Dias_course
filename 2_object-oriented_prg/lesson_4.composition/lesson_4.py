# # def hello_world():
# #     print("Hello")

# # hello_world()
# # hello = hello_world

# # def hello_world2():
# #     def internal():
# #         print("Hello my little world")
# #     return internal

# # hello2 = hello_world2()
# # print(hello2)

# # def say_smt(func):
# #     func()

# # say_smt(hello_world )

# # def log_dec(func):
# #     def wrap():
# #         print(f'Callinf a func {func} ')
# #         func()
# #         print(f'Tnding  a func {func} ')
# #     return wrap

# # wrapped = log_dec(hello_world)
# # wrapped()

# # @log_dec
# # def hello():
# #     print("hello my little friend")

# # hello()

# from timeit import default_timer as ti
# import math
# import time 
# from functools import wraps

# def measure_time(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         start = ti()

#         func(*args,**kwargs)

#         end = ti()

#         print(f'Function {func.__name__} took {end-start} for execution')
    
#     return inner

# @measure_time
# def factorial(num):
#     time.sleep(3)
#     print(math.factorial(num))

# factorial(6) 

# help(factorial)


# def decorator(F): # F – функция или метод, не связанный с экземпляром
#     def wrapper(*args):
#         z = 1 
#         for i in args:
#             z*=i
#         print(z) 
#     return wrapper

# @decorator
# def func(*args): # func = decorator(func)
#     time.sleep(1    )
#     print(f"The number what you enter {args}")

# func(6, 7,8,5,2,5) # В действительности вызовет wrapper(6, 7)



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


class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def yeatly_salary(self):
        return (self.pay*12) + self.bonus
 
 
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company,pay,bonus):
        Person.__init__(self, name, age)
        self.test1  = Salary(pay, bonus)
        self.company = company


    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print("Компания:", self.company)
    
    def  total_salary(self):
        return self.test1.yeatly_salary()
 
 
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university
 
    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)
 
people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google",150000,100000)]
 
for person in people:
    person.display_info()
    print()

