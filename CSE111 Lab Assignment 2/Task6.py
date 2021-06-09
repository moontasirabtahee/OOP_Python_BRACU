String = input()
def numberOfVowel(String):
    vowel ="AEIOUaeiou"
    counter = 0
    vowelPlace = list()

    for i in String:
        if i in vowel:
            counter+=1
            vowelPlace.append(i)

    if counter == 0:
        return "No vowels in the name!"
    else:
        return "Vowels : " + str(vowelPlace) + ". Total number of vowels: " + str(counter)

print(numberOfVowel(String))