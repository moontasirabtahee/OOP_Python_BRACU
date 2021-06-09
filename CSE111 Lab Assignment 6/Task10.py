# Created by Moontasir Abtahee at 6/8/2021
class SultansDine:
    total_sell = 0
    total_branch = 0
    info = []

    def __init__(self, place):
        self.place = place
        self.quantity = 0
        SultansDine.total_branch += 1
        SultansDine.info.append([self.place])

    def sellQuantity(self, quantity):
        self.quantity = quantity

    def branchInformation(self):
        total = 0
        if self.quantity < 10:
            total = self.quantity * 300
        elif self.quantity < 20:
            total = self.quantity * 350
        else:
            total = self.quantity * 400
        SultansDine.total_sell += total
        SultansDine.info[SultansDine.total_branch - 1] += [total]
        print(f"Branch Name: {self.place}\nBranch Sell: {total} Taka")

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.total_branch}\nTotal Sell: {SultansDine.total_sell} Taka")
        for b, s in cls.info:
            print(f"Branch Name: {b}, Branch Sell: {s} Taka")
            print(f"Branch consists of total sell's: {round(s / SultansDine.total_sell * 100, 2)}%")

    # Driver class...


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()