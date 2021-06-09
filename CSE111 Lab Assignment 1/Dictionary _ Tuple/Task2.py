primaryDict =dict()
while True:
    String = input()
    if String == "STOP":
        break
    else:
        number = int(String)
        if number not in primaryDict.keys():
            primaryDict[number] = 1
        else:
            primaryDict[number] += 1

for key,value in primaryDict.items():
    print(str(key)+"-"+str(value)+" times")
