# Created by Moontasir Abtahee at 6/4/2021
class Cat():
    def __init__(self,color = "White",do = "sitting"):
        self.color = color
        self.do = do

    def printCat(self):
        print(f"{self.color} cat is {self.do}")
    def changeColor(self,color):
        self.color = color

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()