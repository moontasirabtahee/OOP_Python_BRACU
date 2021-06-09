#task5
StringOne ,StringTwo = input().split(',')
Output = ""
Array = list(StringTwo)
for char in StringOne:
    if char in Array:
        Output += char
Array = list(StringOne)
for char in StringTwo:
    if char in Array:
        Output += char
print(Output)