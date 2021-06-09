firstList = input().split(",")
secondList = input().split(",")

fisrtDict = dict()
secondDict = dict()

for i in firstList:
    temp = i.split(":")
    print(temp)
    fisrtDict[temp[0]] = int(temp[1])

for i in secondList:
    temp = i.split(":")
    secondDict[temp[0]]= int(temp[1])

Output = fisrtDict.copy()

for elem in secondDict:
    if elem in Output.keys():
        Output[elem] = Output[elem]+secondDict[elem]
    else:
        Output[elem] = secondDict[elem]

print(Output)
print("Values:"+str(Output.values()))