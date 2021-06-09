# Created by Moontasir Abtahee at 6/8/2021
class Student:
    t_stu=0
    brac_stu=0
    other_stu=0

    def __init__(self, name, dept, ins='BRAC University'):
        self.name = name
        self.dept = dept
        self.ins = ins
        Student.t_stu += 1
        if self.ins == 'BRAC University':
            Student.brac_stu += 1
        else:
            Student.other_stu += 1

    @classmethod
    def printDetails(cls):
        print('Total Student(s):', Student.t_stu)
        print('BRAC University Student(s):', Student.brac_stu)
        print('Other Institution Student(s):', Student.other_stu)

    @classmethod
    def createStudent(cls, name, dept, ins='BRAC University'):
        x = cls(name, dept, ins)
        return x

    def individualDetail(self):
        print('Name:', self.name)
        print('Department:', self.dept)
        print('Institution:', self.ins)


Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()