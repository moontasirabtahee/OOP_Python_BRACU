# Created by Moontasir Abtahee at 6/5/2021
class Color():
    def __init__(self ,color):
        self.clr = color
    def __add__(self, other):
        x = self.clr
        y = other.clr

        if (x == "red" or x == "blue") and (y == "red" or y == "blue"):
            return Color("Violet")
        elif (x == "red" or x == "yellow") and (y == "red" or y == "yellow"):
            return Color("Orange")
        elif (x == "blue" or x == "yellow") and (y == "blue" or y == "yellow"):
            return Color("Green")

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)