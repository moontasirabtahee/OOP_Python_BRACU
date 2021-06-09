#Task3

String = input()
flagStart = 0
flagEnd = 0
flag = 0
for pos in range(len(String)):
    if String[pos].isupper() and flag == 0:
        flag+=1
        flagStart = pos
    elif String[pos].isupper() and flag == 1:
        flagEnd = pos


if flagEnd - flagStart == 1:
    print("BLANK")
else:
    print(String[flagStart+1:flagEnd])