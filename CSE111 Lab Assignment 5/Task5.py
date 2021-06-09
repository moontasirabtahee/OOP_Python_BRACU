# Created by Moontasir Abtahee at 6/5/2021
class Circle():
    pi = 3.1416
    def __init__(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * (self.radius**2)
    def __add__(self, other):
        result = self.area() + other.area()
        return Circle(result)

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())