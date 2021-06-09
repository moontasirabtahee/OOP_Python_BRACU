# Created by Moontasir Abtahee at 6/4/2021
class Calculator():
    def __init__(self):
        print("Lets Calculate!")
    def add(self,x,y):
        print(f"Value 1: {x}\nOperator: +\nValue 2: {y}\nResult: {x+y}")
    def substract(self,x,y):
        print(f"Value 1: {x}\nOperator: +\nValue 2: {y}\nResult: {x-y}")
    def multiplay(self,x,y):
        print(f"Value 1: {x}\nOperator: +\nValue 2: {y}\nResult: {x*y}")
    def divide(self,x,y):
        print(f"Value 1: {x}\nOperator: +\nValue 2: {y}\nResult: {x/y}")

calculator = Calculator()
x = int(input())
symb = input()
y = int(input())
if symb == '+':
    calculator.add(x,y)
elif symb == "-":
    calculator.substract(x,y)
elif symb == "*":
    calculator.multiplay(x,y)
elif symb == "/":
    calculator.divide(x,y)




