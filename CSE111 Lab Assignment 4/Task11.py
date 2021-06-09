# Created by Moontasir Abtahee at 6/5/2021
class Shinobi():
    def __init__(self,name ,rank):
        self.name = name
        self.rank = rank
        self.mission = 0
    def calSalary(self,mission):
        self.mission = mission
    def salary(self):
        if self.rank == 'Genin':
            return self.mission*50
        elif self.rank == "Chunin":
            return self.mission*100
        else:
            return self.mission*500
    def printInfo(self):
        print(f"Name: {self.name}\nRank: {self.rank}\nNumber of mission: {self.mission}\nSalary: {self.salary()}")
    def changeRank(self,rank):
        self.rank = rank


# Write your code here.
naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()
