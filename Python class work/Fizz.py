# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list)
#
# list1 = ['w', 'a', 'th', 'xplo']
# list2 = ['e', 're', 'e', 'rers']
# new_list = []
# for i in range(len(list1)):
#     new_list.append(list1[i] + list2[i])
# print(new_list)













#
# interList = [
#     [0, 0, 0], [0, 0, 0], [0, 0, 0]
#     ]
# for i in range(len(interList)):
#     for j in range(len(interList[i])):
#         interList[i][j] = 2
# for w in range(len(interList)):
#     print(interList[w])


averageList = [[25, 50, 75],
               [40, 50, 60],
               [75, 65, 80]
 ]
sum = 0
average = 0
for i in range(len(averageList)):
    for j in range(len(averageList[i])):

      sum += averageList[i][j]
      lenght_divisor =  len(averageList[i][j])
      average /=lenght_divisor
print(average)

























# lister = [[], [], []]
# for i in range(2):
#     print()
#     for j in range(3):
#         lister[i][j]= 2
#     print(lister)
#
# lister = []
# for i in range(3):
#     for j in range(2):
#
#         lister.append(i,j)
#
#
#
#
# print(lister)