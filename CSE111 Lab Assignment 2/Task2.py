def BMI(height,weight):
    BMI = weight / (height / 100) ** 2
    
    if BMI<18.5:
        print("Score is "+str(BMI)+". You are Underweight")
    elif BMI>=18.5 and BMI<=24.9:
        print("Score is "+str(BMI)+". You are Normal")
    elif BMI>=25 and BMI <=30:
        print("Score is "+str(BMI)+". You are Overweight")
    elif BMI>30:
        print("Score is "+str(BMI)+". You are Obese")


BMI(175,96)