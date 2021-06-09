# Created by Moontasir Abtahee at 6/4/2021
#Write your class code here
class DataType():
    def __init__(self,type,data):
        self.name = type
        self.value = data


data_type1 = DataType("Integer", 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType("String", "Hello")
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType("Float", 4.0)
print(data_type3.name)
print(data_type3.value)