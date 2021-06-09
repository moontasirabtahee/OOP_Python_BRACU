# Created by Moontasir Abtahee at 6/5/2021

# Write your code here
class Batsman():
    def __init__(self, *args):
        if type(args[0]) is str:
            self.name  = args[0]
            self.run = args[1]
            self.ball =args[2]
        else:
            self.name = "New Batsman"
            self.run = args[0]
            self.ball = args[1]

    def printCareerStatistics(self):
        print(f"Name: {self.name}\nRuns Scored: {self.run} , Balls Faced: {self.ball}")
    def battingStrikeRate(self):
        x = self.run/self.ball*100
        return (x)
    def setName(self,name):
        self.name = name
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
