# def largestString(Nonsense):
#     count = 1
#     empty = []
#     largest = 0
#     for i in range(5):
#         slicing = Nonsense[:count:]
#         inThe = int(slicing)
#         empty.append(inThe)
#         count += 1
#
#         while inThe > 0:
#
#             remainder = inThe % 10
#             if remainder > largest:
#                 largest = remainder
#
#             inThe //= 10
#
#     return largest
import random


# def largestString(Nonsense):
def largestString(numbers):
    num = int(numbers)
    empty = []
    largest = 0

    for i in range(num):
        palin = num % 10
        empty.append(palin)
        num //= 10
    for i in range(len(empty)):
        if empty[i] > largest:
            largest = empty[i]
    return largest



    # return largest


# or return max([number for number in numbers if int(numbers > 2)])




# print(largestString("23569"))
# for i in range
# innerInt = (int)(Nonsense)
# while Nonsense > 0:
#     remainder = innerInt % 10
#     remainder //= 10
#     print(remainder)
# for i in range(innerInt):

# do
# j _ i enumerate when the index is needed but the vailu is not fucking neede
# the underscore mostly

# list of nums
# user_In = 3
# list_t = [[i for i in range(user_In)],
#              [0, 0, 0,],
#              [0, 0, 0]
# ]
#
# for idx, i in enumerate(list_t):
#     for j, _ in enumerate(i):
#         list_t[idx][j] = 5
#         print(list_t[idx][j],end='   ')
#     print("\n")
def character_Checking(first, second):
    # first = "love"
    # second = "evlo"
    empty = []
    count = 0
    lenght1 = len(first)
    lenght2 = len(second)
    isTru = False
    for i in range(len(first)):
        slicing1 = first[:count:]
        slicing2 = second[:count:]
        if slicing1 in slicing2 and lenght1 == lenght2:
            isTru =True
        elif slicing1 not in slicing2  and lenght1 != lenght2:
            isTru = False
            count+=1
        else:
            isTru =False
    return isTru

