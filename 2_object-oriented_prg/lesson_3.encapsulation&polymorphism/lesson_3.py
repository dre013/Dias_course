# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print('Impossible years old')

#     def get_age(self):
#         return self.__age
    
#     def get_name(self):
#         return self.__name
    
#     def display_info(self):
#         print(f'Name: {self.__name} and sge: {self.__age}')

# tom = Person('Tom')
# tom.__name = 'Dias'
# tom.__age = 13
# tom.display_info()

class Person:
    MAX_SPEED = 100

    def __init__(self, name, age = 40):
        self.__name = name
        self.age = age
        self.__health = 100
        self.current_speed = 20

    def damage(self):
        self.__health -= 10

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @property
    def current_speed(self):
        return self.__current_speed
    
    @current_speed.setter
    def current_speed(self, value):
        if value < 0:
            self.__current_speed = 0
        elif value > 100:
            self.current_speed = 100
        else:
            self.__current_speed = value

p = Person('Nae')
print(p)

print(Person.MAX_SPEED)
p.__Person__name = 'Gabby'
print(p.__Person__name)