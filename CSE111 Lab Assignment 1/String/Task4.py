#task4
String = input()
flagToo = String.find('too')
flagGood = String.find('good')

if flagToo<flagGood:
    String = String.replace(String[flagToo:(flagGood+4)],"Exellent")
    print(String)
else:
    print(String)

