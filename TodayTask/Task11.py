def targetExist(the_list, target):
    the_list = []
    the_boolean = True | False
    for i in range(len(the_list)):
        if target in the_list[i]:
            the_boolean = True

        else:
            the_boolean = False

    return the_boolean


result = [2, 3, 5, 3, 6, 1]

print(targetExist(result, 2))

