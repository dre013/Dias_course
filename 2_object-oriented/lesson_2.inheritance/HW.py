class Shape:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('Shape Created')

    def draw(self):
        print('Drawing a shape')
    
    def area(self):
        print('Calculated area')
    
    def perimetr(self):
        print('Calculated perimetr')

shape = Shape(0, 0)


class Rectangle(Shape):
    def __init__(self, a, b):
        Shape.__init__(self, a, b)
    
    def draw(self):
        Shape.draw(self)
        print(f'Drawing rectangle with width = {self.a} and height = {self.b}')

    def perimetr(self):
        Shape.perimetr(self)
        print('Perimetr is: ', (self.a + self.b) * 2)

    def area(self):
        Shape.area(self)
        print('Area is: ', self.a * self.b)

import math

class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self, a, b)
        self.c = c
    
    def draw(self):
        Shape.draw(self)
        print(f'Drawing rectangle with width = {self.a} and height = {self.b}')
    
    def perimetr(self):
        Shape.perimetr(self)
        print(f'Perimetr is: ', self.a + self.b + self.c)
    
    def area(self):
        Shape.area(self)
        s = (self.a + self.b + self.c) / 2
        print('Area is: ', math.sqrt(s * (s-self.a) * (s-self.b) * (s - self.c)))

r = Rectangle(5, 7)
t = Triangle(6, 6, 6)

print()

shapes_list = [r, t]

for shapes in shapes_list:
    shapes.draw()
    shapes.area()
    shapes.perimetr()