counter = int(input())
flag = 0
maximum = int()
newList = list()
for count in range(counter):
    Numbers = list(map(int,input().split()))

    if flag == 0:
        maximum = sum(Numbers)
        newList = Numbers.copy()
        flag += 1
    else:
        if sum(Numbers) > maximum:
            maximum = sum(Numbers)
            newList = Numbers.copy()

print(maximum)
print(newList)



