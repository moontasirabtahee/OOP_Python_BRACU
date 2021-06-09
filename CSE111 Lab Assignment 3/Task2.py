# Created by Moontasir Abtahee at 6/4/2021
class Flower():
    def __init__(self,name="",color="",petal=0):
        self.name = name
        self.color = color
        self.num_of_petal = petal

    def compare(self,other):
        if self == other:
            print("They are same")
        else:
            print("They are not same")

flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print('=====================')
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)

flower1.compare(flower2)