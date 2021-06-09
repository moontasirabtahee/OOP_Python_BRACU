# Created by Moontasir Abtahee at 6/4/2021
#Write your class code here
class Joker():
    def __init__(self,name ,power,is_he):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')