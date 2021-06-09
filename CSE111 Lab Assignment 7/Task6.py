# Created by Moontasir Abtahee at 6/9/2021
class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return "Height: " + str(self.height) + ",Base: " + str(self.base)

class triangle(Shape):
    def calcArea(self):
        self.area = (self.height * self.base)/2

    def printDetail(self):
        print(f"Shape name: {self.name}")
        print(self.get_height_base())
        return "Area: "+ str(self.area)

class trapezoid(Shape):
    def __init__(self,p,q,r,s):
        super().__init__(p,q,r)
        self.sideA = s
    def calcArea(self):
        self.area = ((self.sideA+self.base)*self.height)/2
    def printDetail(self):
        return (f"Shape name: {self.name} \nHeight: {self.height}, Base: {self.base}, Side_A: {self.sideA}\nArea: {self.area}")
# write your code here
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
