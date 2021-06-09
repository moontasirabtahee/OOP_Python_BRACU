# Created by Moontasir Abtahee at 6/5/2021
class Triangle():
    def __init__(self,base,height):
        self.__base = base
        self.__height = height
    def getBase(self):
        return self.__base
    def getHeight(self):
        return self.__height
    def setBase(self,base):
        self.__base = base
    def setHeight(self,height):
        self.__height = height
    def area(self):
        return (self.__height*self.__base)/2
    def __sub__(self, other):
        h = self.__height-other.__height
        b = self.__base-other.__base
        return Triangle(b,h)


t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())