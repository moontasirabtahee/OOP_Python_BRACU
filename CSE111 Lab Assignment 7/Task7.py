# Created by Moontasir Abtahee at 6/9/2021


class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return 'Name: ' + self.__name + ', Team Name: ' + self.__team

class Player(Football):
    def __init__(self,name,team,role,goal,play):
        super().__init__(team,name,role)
        self.goal = goal
        self.play = play
        self.earning_per_match = (self.goal * 1000) + (self.play * 10)

    def calculate_ratio(self):
        self.ratio = self.goal/self.play

    def print_details(self):
        print(self.get_name_team())
        print(f"Team Role: {self.ratio}\nTotal Goal: {self.goal}, Total Played: {self.play}\nGoal Ratio: {self.ratio} \nMatch Earning: {self.earning_per_match}")
# write your code here

class Manager(Football):
    def __init__(self,name,team,role,win):
        super().__init__(team,name,role)
        self.win = win
        self.earning_per_match = win*1000

    def print_details(self):
        print(self.get_name_team())
        print(f"Team Role: {self.role}\nTotal Win: {self.win}\nMatch Earning: {self.earning_per_match}K")


player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
