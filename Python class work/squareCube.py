
# print("number\t\tSquare\t\tCube")
# for i in range(1, 11):
#     number = i
#     square = number * number
#     cube = number * number * number
#     print(f"{number}\t\t\t {square}\t\t\t {cube}")

print()
n = 1
print("number\t\tSquare\t\tCube")
while n < 11:
    number1 = n
    square1 = number1 * number1
    cube1 = number1 * number1 * number1
    print(f"{number1} {square1:>14}{cube1:>11}")
    n+=1
    #the column and the greater than is the space needed after your numbers without it depending on each other

    #  median