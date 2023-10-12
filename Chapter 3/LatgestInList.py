my_list = [2, 4, 6, 5, 7, 8, 9, 10]
largest = my_list[0]
for i in my_list:
    if my_list[i] > largest:
        largest = my_list

print(my_list)