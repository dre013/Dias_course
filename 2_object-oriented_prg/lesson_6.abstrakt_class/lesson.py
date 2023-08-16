from abc import ABC
from abc import abstractclassmethod

class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractclassmethod
    def draw(self):
        pass

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetr(self):
        print('Calc peri')

    def drag(self):
        print("basic dragging")

        

# x = Shape()
# print(x)

import math

class Triangle(Shape):

    def __init__(self,a,b,c):

        self.a = a
        self.b = b 
        self.c = c 
        
        print("Triangle created")


    def draw (self):
        print("Triangle created")
    
    def area (self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s - self.c))
        
    
    def perimetr(self):
        super().perimetr()
        return (self.a + self.b + self.c)

    def drag(self):
        super().drag()
        print("Addition")

t = Triangle(10, 10, 10)

print(t.area())

