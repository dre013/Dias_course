#1 задание
class soda:
    def __init__(self, ingredient = None):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

ingredient = str(input('Введите название добавки: '))
soda1 = soda(ingredient)
soda1.show_my_drink()

#2 задание
import re

class calculator:
    try:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def add(self):
            print(int(self.x) + int(self.y))

        def sub(self):
            print(int(self.x) - int(self.y))

        def mult(self):
            print(int(self.x) * int(self.y))

        def div(self):
            print(int(self.x) / int(self.y))

    except ZeroDivisionError:
        print('На 0 делить нельзя')

calculator1 = calculator(15, 3)
calculator1.div()

#3 задание

class Rectangle:
    def __init__(self, width, heigth):
        self.heigth = heigth
        self.weidth = width

    def get_width(self):
        return self.weidth
    
    def set_width(self, w):
        self.width = w

    def get_hegth(self):
        return self.heigth
    
    def set_height(self, h):
        self.heigth = h
        
    def area(self):
        return self.width * self.heigth

    
