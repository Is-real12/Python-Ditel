#
# my_list = [3, 7, 2, 6, 5]
# mul = 1
# new_list = []
#
# for i in range(len(my_list)):
#     mul = my_list[i] * my_list[i]
#     mul *= my_list[i]
#     new_list.append(mul)
#
# print(new_list)









def Cube(my_list=[]):
    # my_list = [3, 7, 2, 6, 5]
    mul = 1
    new_list = []

    for i in range(len(my_list)):
        mul = my_list[i] * my_list[i]
        mul *= my_list[i]
        new_list.append(mul)
    return new_list
