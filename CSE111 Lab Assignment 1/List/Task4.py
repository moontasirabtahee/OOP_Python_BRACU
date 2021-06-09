PrimaryList = list()
while True:
    String = input()
    if String == "STOP":
        break
    else:
        PrimaryList.append(String)

for elemt in PrimaryList:
    SecondaryList = list(map(int,elemt.split(" ")))
    checker = []

    for i in range(len(SecondaryList)-1):
        checker.append(abs(SecondaryList[i]-SecondaryList[i+1]))
    Jumper = True

    for i in range(1,len(SecondaryList)):
        if i in checker:
            pass
        else:
            Jumper = False


    if Jumper == True:
        print("UB Jumper ")
    else:
        print("Not UB Jumper")