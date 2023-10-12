# def lol():
# turpile = [15, 25, 60, 50, 30, 40, 45, 55]
#
# toStart = 0
# toEnd = len(turpile) - 1
#
# while toEnd > toStart:
#     turpile[toStart] = turpile[toStart] + turpile[toEnd]
#     turpile[toEnd] = turpile[toStart] - turpile[toEnd]
#
#     turpile[toStart] = turpile[toStart] - turpile[toEnd]
#     toEnd -= 1
#     toStart += 1
# print(turpile)

# print(turpile)

# print(turpile[toEnd - 1])

def reverseTurple(tuple1=[]):
    emptyTuple = ()
    for i in range(4, -1, -1):
        emptyTuple += (tuple1[i],)
    return emptyTuple


# def get_index_and_values(t):
#     indices_values = []
#     for index, item in enumerate(t):
#         if 20 or 25 in item:
#             if 20 == item:
#                 indices_values.append((index, 20))
#             elif 25 == item:
#                 indices_values.append((index, 25))
#     sorted(t, reverse=True)
#     return tuple(indices_values)
#
#
# def Unpack_First_Last(tuple3, first, last):
#     tuple3 = ()
#
#     # (15, 25, 60, 50, 30, 40, 45, 55)
#     length = len(tuple3)
#     newT = ()
#     for i in range(length - 1):
#         if tuple3[first] and tuple3[last] not in newT:
#             newT += (tuple3[i])
#     return newT
#
#
# def Sort_By_Second(arr):
#     tuple4 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
#     for i in tuple4:
#         print(tuple4[i])
#
#     return
#
#
# print(Sort_By_Second((15, 25, 60, 50, 30, 40, 45, 55)))
