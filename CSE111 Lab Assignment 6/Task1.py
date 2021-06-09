# Created by Moontasir Abtahee at 6/5/2021
class Student():
    ID = 0
    def __init__(self,name,department,age,cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
    def get_details(self):
        print(f"ID: 1\nName: {self.name}\nDepartment: {self.department}\nAge: {self.age}\nCGPA: {self.cgpa}")
    @classmethod
    def from_string(cls,string):
        a,b,c,d = string.split("-")
        obj = cls(a,b,c,d)
        return obj

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_string("Sumaiya-BBA-23-3.96")
s4.get_details()