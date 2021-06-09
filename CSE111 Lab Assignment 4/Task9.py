# Created by Moontasir Abtahee at 6/5/2021
class Patient():
    def __init__(self,name ,age):
        self.name = name
        self.age = age

    def add_Symptom(self,*symp):
        self.symptoms = ""
        flag  = 0
        for i in symp:
            if flag == 0:
                self.symptoms += i
                flag+=1
            else:
                self.symptoms +=(", "+i)
    def printPatientDetail(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSymptoms: {self.symptoms}")


p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
print("=========================")