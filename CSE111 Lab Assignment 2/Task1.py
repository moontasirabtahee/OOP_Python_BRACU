def Fraction(num1,num2):
    if num2 == 0:
        return 0
    else:
        return num1/num2 - num1//num2

print(Fraction(5,2))