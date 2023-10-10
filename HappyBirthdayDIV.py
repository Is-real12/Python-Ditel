def reverseTurple(tuple1=[]):
    emptyTuple = ()
    for i in range(4, -1, -1):
        emptyTuple += (tuple1[i],)
    return emptyTuple


# def print_indices_and_values(t):
#     for index, item in enumerate(t):
#         if 20 in item:
#             print(f'({index}, 20)')
#         if 25 in item:
#             print(f'({index}, 25)')
#     return

def get_index_and_values(t):
    indices_values = []
    for index, item in enumerate(t):
        if 20 in item or 25 in item:
            if 20 in item:
                indices_values.append((index, 20))
            else:
                indices_values.append((index, 25))

    return tuple(indices_values)

    # for j in range(len(tuple2[2])):

# tuple2 = ("orange", [10, 20, 30,], (5, 15, 25))
# newT = ()
# for i in tuple2:
#     if tuple2[i] not in newT:
#      newT +=(tuple2,)
#
# print(newT)
#
#
#
# # count = 0
# # reverse = 0
# # intputt = (7, 8, 7, 5, 5,)
# # while intputt > 0:
# #     reverse = intputt % 10
# #
# #     intputt /= 10
# #     print(reverse)
