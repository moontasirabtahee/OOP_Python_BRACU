# Created by Moontasir Abtahee at 6/9/2021


class Tournament:
    def __init__(self, name='Default'):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# write your code here
class Cricket_Tournament(Tournament):
    def __init__(self,name = "Default",team= "0",type="No type"):
        super().set_name(name)
        self.team = team
        self.type = type

    def detail(self):
        print(f"Cricket Tournament Name: {self.get_name()} \nNumber of Teams:{self.team} \nType: {self.type}")
class Tennis_Tournament(Tournament):
    def __init__(self, name="Default", team="0"):
        super().__init__(name)
        self.team = team

    def detail(self):
        print(f"Cricket Tournament Name: {self.get_name()} \nNumber of Teams:{self.team} ")

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL", 10, "t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros", 128)
print(tt.detail())
