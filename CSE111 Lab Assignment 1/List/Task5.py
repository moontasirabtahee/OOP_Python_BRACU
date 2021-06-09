#task 5
String = input()
low = list()
upp = list()
odd = list()
even=  list()

for char in String:
    if char.isupper():
        upp.append(char)
    elif char.islower():
        low.append(char)
    elif char.isdigit():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)

low.sort()
upp.sort()
odd.sort()
even.sort()

Output = low+upp+odd+even
Output = "".join(Output)
print(Output)