# Created by Moontasir Abtahee at 6/4/2021
class Student():
    def __init__(self,name = "default"):
        self.name = name
        self.numb = 0
    def quizcalc(self,*number):
        self.numb = sum(number)/3

    def printdetail(self):
        print(f"Hello {self.name} student")
        print(f"Your average quiz score is {self.numb}")

s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()