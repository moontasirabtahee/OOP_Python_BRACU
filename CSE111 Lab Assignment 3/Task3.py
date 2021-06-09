# Created by Moontasir Abtahee at 6/4/2021
class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True
    def detail(self):
        print(f"Name of President: {self.name}\nDesignation: {self.designation}\nNumber of wife: {(self.num_of_wife)}\nIs he/she a dictator: {self.dictator}")


wadia1 = Wadiya()
print("Part 1")
wadia1.detail()
wadia2 = Wadiya()
wadia2.num_of_wife = 1
wadia2.dictator = False
wadia2.designation = "President"
wadia2.name = "Donald Trump"
print("Part 2")
wadia2.detail()


