# Created by Moontasir Abtahee at 6/4/2021
class Programmer():
    def __init__(self,name , lang , experience):
        self.name=name
        self.lang = lang
        self.experience = experience
        print("Horray! A new programmer is born")


    def printDetails(self):
        print(f"\nName: {self.name}\nLanguage: {self.lang}\nExperience:{self.experience} years.")
    def addExp(self,year):
        print("Updating experience of Jon Snow",end="")
        self.experience += year



p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()