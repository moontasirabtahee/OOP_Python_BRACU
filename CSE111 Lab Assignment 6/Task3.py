# Created by Moontasir Abtahee at 6/8/2021
class Passenger():
    count = 0
    def __init__(self,name):
        self.name = name
        self.money = 0
        Passenger.count +=1


    def set_bag_weight(self,weight):
        self.weight = weight
        self.fare()

    def get_bag_weight(self):
        return self.weight
    def fare(self):
        if self.weight <= 20:
            self.money = 450
        elif self.weight >21 and self.weight<50:
            self.money = 500
        elif self.weight>50:
            self.money = 550

    def printDetail(self):
        print('Name:', self.name)
        print('Bus Fare:', self.money)
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)