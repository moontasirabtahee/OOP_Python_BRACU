# Created by Moontasir Abtahee at 6/5/2021

class ParcelKoro():
    def __init__(self,name = "No Name Set",weight = 0):
        self.name = name
        self.product_weight = weight



    def calculateFee(self,place = ""):
        if place == "" and self.product_weight != 0:
            self.fee =  (self.product_weight*20)+50
        elif place != "" and self.product_weight != 0:
            self.fee = (self.product_weight*20)+100
        elif self.product_weight == 0:
            self.fee = 0

    def printDetails(self):
        print(f"Customer Name: {self.name}\nProduct Weight: {self.product_weight}\nTotal fee:{self.fee}")
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()