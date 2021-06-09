# Created by Moontasir Abtahee at 6/5/2021
class Account():
    def __init__(self,name = "Default Account",balance = 0.0):
        self.name = name
        self.balance = balance

    def details(self):
        print(self.name)
        return float(self.balance)
    def withdraw(self,money):
        if self.balance - money <= 3070:
            print(
                "Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")

        else:
            self.balance -= money
            print(f"Withdraw successful! New balance is : {float(self.balance)}")


a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930);
print("------------------------")
a2.withdraw(600);
print("------------------------")
a1.withdraw(6929)