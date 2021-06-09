# Created by Moontasir Abtahee at 6/8/2021
class Assassin():
    assassin = 0
    def __init__(self,name ,rate ):
        self.name = name
        self.rate = rate
        Assassin.assassin += 1

    @classmethod
    def failureRate(cls,name,rate):
        obj = cls(name,(100-rate))
        return obj

    @classmethod
    def failurePercentage(cls,name,rate):
        obj = cls(name,(100-rate))
        return obj
    def printDetails(self):
        print(f"Name: {self.name}\nSuccess rate: {self.rate}%\nTotal number of Assassin: {Assassin.assassin}")


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage('Akabane', 10)
akabane.printDetails()