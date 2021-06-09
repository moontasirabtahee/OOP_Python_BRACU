# Created by Moontasir Abtahee at 6/4/2021
class Customer():
    def __init__(self,name):
        self.name = name

    def greet(self,name= ""):
        print(f"Hello!{name}")
    def purchase(self,*item):
        length = len(item)
        items = ""
        for i in item:
            items += " "+i
        print(f"{self.name} , You have purchased {length} item(s): {items}")

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")