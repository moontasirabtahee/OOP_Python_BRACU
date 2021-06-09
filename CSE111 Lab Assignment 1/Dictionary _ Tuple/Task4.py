firstList = list(input())
secondList = list(input())

if len(firstList) != len(secondList):
    print("Those strings are not anagrams.")
else:
    counter = 0
    for i in firstList:
        for j in secondList:
            if i == j:
                counter+=1

    if counter == len(firstList) == len(secondList):
        print("Those strings are anagrams.")