# Created by Moontasir Abtahee at 6/8/2021
class Cylinder():
    radius = 5
    height = 18
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("Default radius =", Cylinder.radius, "and height=", Cylinder.height)
        Cylinder.radius = self.x
        Cylinder.height = self.y
        print("Updated: radius=", self.x, "and height=", self.y)

    @staticmethod
    def volume(value1, value2):
        print("Volume:", (3.1416* (float(Cylinder.radius) ** 2) * float(Cylinder.height)))

    @classmethod
    def swap(cls, x, y):
        obj = cls(y, x)
        return obj

    @classmethod
    def changeFormat(cls, info):
        r, h = info.split("-")
        obj1 = cls(float(r), float(h))
        return obj1

    @staticmethod
    def area(num1, num2):
        print("Area: ",
              (2 * (3.1416) * float(Cylinder.radius) * float((Cylinder.radius) + float(Cylinder.height))))
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
