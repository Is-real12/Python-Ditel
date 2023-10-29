samplle_List = [2, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]


def unique(samplle_List1):
    newli = []
    myList = list(set(samplle_List1))
    for i in range(len(myList)):
        if myList[i] % 2 == 0:
            newli.append(myList[i])

    return newli


print(unique(samplle_List))
