# Created by Moontasir Abtahee at 6/8/2021
class Cat():
    Number_of_cats = 0
    def __init__(self,color = "White" ,do = "sitting" ):
        self.color = color
        self.do = do
        Cat.Number_of_cats+=1
    @classmethod
    def no_parameter(cls):
        return cls()
    @classmethod
    def first_parameter(cls,color):
        return cls(color)

    @classmethod
    def second_parameter(cls,do):
        color = "Gray"
        return cls(color,do)

    def printCat(self):
        print(self.color, ("cat is"), self.do)

    def changeColor(self,color):
        self.color=color
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
