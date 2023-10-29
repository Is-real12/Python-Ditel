my_list = [[2, 4, 5, 6], [2, 3, 5, 6]]

def sum_list(my_list1):
    sums = 0
    for i in range(len(my_list1)):
        for j in range(len(my_list[i])):
            sums += my_list1[i][j]
    return sums

fun = sum_list(my_list)
print(fun)
def oneFor(my_list1):
    sums = 0
    for i in range(len(my_list)):
        sums += sum(my_list[i])
    return sums

