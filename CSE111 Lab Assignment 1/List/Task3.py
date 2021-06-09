firstList = list(map(int, input().split()))
SecondList = list(map(int, input().split()))
output = list()

for i in firstList:
    for j in SecondList:
        output.append(i*j)

print(output)