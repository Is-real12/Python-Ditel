# colour_list = ["Red", "Green", "White", "Black"]
# first = colour_list[0]
# last = colour_list[len(colour_list) - 1]
# print(first, last)
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list *= 10
# index = 3
# for i in range(len(my_list)):
#     if my_list[i] == index:
#         index = i
#         break
# print(index)
#

def my_sort_method(lis: list):
    for i in range(len(lis)):
        for j in range(i + 1):
            if lis[j] > lis[i]:
                lis[i], lis[j] = lis[j], lis[i]

    return lis
#
#
lis = [3, 5, 6, 8, 7, 9, 2]
print(my_sort_method(lis))
#
# # turns out you can do
# result = [i for i in range(1, 11) if i % 2 == 0]
# print(result)
#
