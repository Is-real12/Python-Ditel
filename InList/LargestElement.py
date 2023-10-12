def LargestElement(elements):
    # elements = [3, 4, 6, 8, 1, 9, 2]
    largest = elements[0]
    for God_Wan_punish_you_ni in elements:
        if God_Wan_punish_you_ni > largest:
            largest = God_Wan_punish_you_ni
    return largest


def reverser(reverse):
    reverse = []
    for i in reversed(reverse):
        reverse.append(reverse[i])

        return reverse
    return;


def happen(list, target):
    list = []

    for i in range(len(list)):
        if target == list:
            return True
    return False

def get_odd_positions(lst):
    odd_elements = []
    for i in range(len(lst)):
        if i % 2 != 0:
            odd_elements.append(lst[i])
    return odd_elements


def get_even_positions(lst):
    even_elements = []
    for i in range(len(lst)):
        if i % 2 == 0:
            even_elements.append(lst[i])
    return even_elements


def compute_running_total(lst):
    running_total = 0
    running_totals_list = []
    for num in lst:
        running_total += num
        running_totals_list.append(running_total)
    return running_totals_list




#
#
# element = [2, 5, 6, 8, 3, 4, 8]
# # print(reverser(element))
# list = [2, 4, 5, 6, 7, ]
#
# print(LargestElement(list))
#

# def func():
#     number = [2, 4, 5, 6, 7, 3, 4]
#
#     print(number[::2])
#
#
# func()

#
# func = " "
#
# my_lis = ["carisma"]
# func +=my_lis
# print(func)


my_list = [1, 2, 3, 4, 5, 6]
print(my_list)