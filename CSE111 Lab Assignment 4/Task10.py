# Created by Moontasir Abtahee at 6/5/2021

class Avengers():
    def __init__(self,name ,partner):
        self.name = name
        self.partner = partner
    def super_powers(self,*symp):
        self.super_power = ""
        flag = 0
        for i in symp:
            if flag == 0:
                self.super_power += i
                flag += 1
            else:
                self.super_power += (", " + i)
    def printAvengersDetail(self):
        print(f"Name: {self.name}\nPartner: {self.partner}\nSuper powers: {self.super_power}")




a1 = Avengers('Captain America', 'Bucky Barnes')
a1.super_powers('Stamina', 'Slowed ageing')
a2 = Avengers('Doctor Strange', 'Ancient One')
a2.super_powers('Mastery of magic')
a3 = Avengers('Iron Man', 'War Machine')
a3.super_powers('Genius level intellect', 'Scientist ')
print("=========================")
a1.printAvengersDetail()
print("=========================")
a2.printAvengersDetail()
print("=========================")
a3.printAvengersDetail()
print("=========================")