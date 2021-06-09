checkList = []
while True:
    number = input()
    if number == "STOP":
        break
    else:
        checkList.append(number)
testcase = sorted(list(set(checkList)))
for num in testcase:
    flag = 0
    for x in checkList:
         if num == x:
             flag += 1
    print(str(num) +" - "+str(flag) +" times")

