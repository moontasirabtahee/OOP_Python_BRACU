# Created by Moontasir Abtahee at 6/5/2021
class Team():
    def __init__(self,Tname=""):
        self.__Tname  = ""
        self.__player = []

    def setName(self,name):
        self.__Tname = name
    def addPlayer(self,play):
        self.__player.append(play.name)

    def printDetail(self):
        print("=====================")

        print(f"Team: {self.__Tname}\nList of Players:\n{self.__player}")
        print("=====================")

class Player():
    def __init__(self,name ):
        self.name = name


b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()