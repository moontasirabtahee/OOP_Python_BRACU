def Palindrome(String):
    word = ""
    for i in String:
        if i != " ":
            word += i


    oppositeWord = ""
    for i in range(len(String)-1,-1,-1):
        if String[i] != " ":
            oppositeWord += String[i]
    #
    # print(word)
    # print(oppositeWord)
    #

    if word == oppositeWord:
        print("Palindrome")
    else:
        print("Not a Palindrome")


Palindrome(input())