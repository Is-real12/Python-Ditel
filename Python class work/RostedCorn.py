lst1 = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

for i in lst1:
    for w in i:
        if w == 0:
            print(" ", end=' ')

        else:
            print("*", end=' ')



        # for
        # if w == 0:
        #     print(" ", end=' ')
        #
        # if i == 1:
        #     print('*', end=' ')

    print()
    # for j in range(i+1, len(lst1)):
        # if lst1[i] < 1:
        #     result = lst1[i]
        #     print(result)
#     if i == 0:
#         print('\" " ')
#
#     if i == 1:
#         print('*')
