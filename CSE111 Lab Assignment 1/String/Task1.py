#Task1
String = input()
flagCapital = 0
flagLower = 0
for char in String:
    if char.islower():
        flagLower += 1
    else:
        flagCapital += 1

if flagLower >= flagCapital:
    print(String.lower())
else:
    print(String.upper())

