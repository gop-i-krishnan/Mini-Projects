import math
from abc import ABC, abstractmethod

class SHAPE(ABC):
    @abstractmethod
    def area(self):
        pass


class CIRCLE(SHAPE):
    def __init__(self,radius):
        self.radius=radius


    def area(self):
        return math.pi*self.radius**2

class SQUARE(SHAPE):

    def __init__(self,side):
        self.side=side

    def area(self):

        return self.side**2

class TRIANGLE(SHAPE):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):

        return 0.5*self.height*self.base

print('\n#WELCOME TO AREA FIND PROGRAM \n')
print('Select the shape to find the area:\n1.Circle\n2.Square\n3.Triangle\n')
choice=int(input('Enter your choice: '))

if choice==1:
    radius=float(input('Enter the radius of circle(in cm): '))
    circle=CIRCLE(radius)
    print(f'\nArea of your circle is {circle.area():0.2f}cm²')

elif choice==2:
    side=float(input('Enter the side length of circle(in cm): '))
    square=SQUARE(side)
    print(f'\nArea of your Square is {square.area():0.2f}cm²')

elif choice==3:
     base,height=(float(input('Enter the base length of triangle(in cm): ')),
                 float(input('Enter the height length of triangle(in cm): ')))
     triangle=TRIANGLE(base,height)
     print(f'\nArea of your Triangle is {triangle.area():0.2f}cm²')

