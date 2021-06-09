# Created by Moontasir Abtahee at 6/8/2021
class Employee():
    def __init__(self,name ,time):
        self.name = name
        self.workingPeriod = time

    @classmethod
    def employeeByJoiningYear(cls,name ,year):
        newYear = 2021-year
        obj = cls(name,newYear)
        return obj

    @staticmethod
    def experienceCheck(duration, s):
        if duration < 3 and s == 'female':
            return ('She is not experienced')
        elif duration < 3 and s == 'male':
            return ('He is not experienced')
        elif duration >= 3 and s == 'female':
            return ('She is experienced')
        elif duration >= 3 and s == 'male':
            return ('He is experienced')

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))