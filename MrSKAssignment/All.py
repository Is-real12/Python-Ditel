my_list = [15, 20, 25, 20, 10, 5]
sum1 = 0
for i in range(len(my_list)):
    sum1 +=my_list[i]
print("The sum is ",sum1)


mul1 = 1
for i in range(len(my_list)):
    mul1 *=my_list[i]
print("the multiplication ",mul1)


minimum = 0
largest = 0
for i in range(len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
    if my_list[i] < largest:
        minimum = my_list[i]


print("The largest is ",largest)
print("the minim ",minimum)


same = []
for i in my_list:
    if i not in same:
       same.append(i)

print(same)
#     # print(my_list)
#     if my_list[i] != my_list[i]:
#         same.remove(my_list[i])
#
# print(same)


