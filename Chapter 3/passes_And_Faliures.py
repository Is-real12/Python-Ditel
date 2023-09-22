passes = 0
failure = 0
i = 0
while i < 10:
    userInput = int(input("Enter a number: "))

    if userInput == 1:
        passes += 1
        i+=1
    elif userInput == 2:
        failure += 1
        i+=1

print(f'The number of passes are {passes}')
print(f'The number of fails are {failure}')
# a =b  = 7
# print( b)
#
# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()

# for i in range(2):
#     for j in range(7):
#         print('@', end=" ")
#     print()