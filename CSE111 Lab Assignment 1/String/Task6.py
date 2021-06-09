String = input()
flagLow = 0
flagUpper = 0
flagDigit = 0
flagSpecial = 0

for char in String:
    if char.islower():
        flagLow += 1
    elif char.isupper():
        flagUpper += 1
    elif char.isdigit():
        flagDigit += 1
    elif char in ["_" , "$" , "#"," @"]:
        flagSpecial += 1
flag = 0
Output = ""
if flagLow>=1 and flagDigit >=1 and flagUpper >= 1 and flagSpecial>=1:
    Output = "OK"
    flag +=1
if flagLow == 0:
    Output += "Lowercase Charecter Missing ,"
if flagUpper == 0:
    Output += "Uppercase character missing ,"
if flagSpecial == 0:
    Output += "Special character missing ,"
if flagDigit == 0:
    Output += " Digit missing ,"

if flag == 1:
    print(Output)
else:
    print(Output[:-1])