inputDict=dict()
outputDict = dict()

stringList = input().split(",")
for i in stringList:
    temp = i.split(":")
    inputDict[temp[0]] = temp[1]

for key , value in inputDict.items():
    if value not in outputDict.keys():
        outputDict[value] = [key]

    else:
        outputDict[value] = outputDict[value] + [key]

print(outputDict)