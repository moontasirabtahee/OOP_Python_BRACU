
def YearConverter(time):
    year= time//365
    month= (time % 365)//30
    day =  (time % 365)%12

    return str(year) + " year, " + str(month) + " month and " + str(day) + " day."



print(YearConverter(4000))