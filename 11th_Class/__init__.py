""""===================================
wow this actually works
====================================
"""
import os
import webbrowser

# file = open("demo.cs", mode='a')
# file.write("ope is a short girl\r")
# file.write("Uye is a man beater\r")
# file.write("Tobi is a sweet husband to ope\r")
# file.close()
# right now when you are done you have to close it
# but if you do with you don't need to close

# with open("dem.txt", mode='w') as fi

# #     files.write("eat any you want ")
# with open("demo.txt", mode='r') as files:
#     for record in files:
#         first, second, *third = record.split()
#         print(f'{first:<10} {second:<10} {third}')
#
# try:
#     with open("datas.txt", mode='r') as datas:
#         for data in datas:
#             a, *b = data.split()
#             print(a, *b)
# except FileNotFoundError:
#     print("It be like say you no get sense abi of tee ba kwo ")
#
#     webbrowser.open('www.google')
#
# try:
#     user = int(input("Enter better thing: "))
#     result =  10/user
#     print(result)
# except ZeroDivisionError:
#     print("Oga i will close this my eye and open it")
#
# user = int(input("Enter better thing: "))
#
# if user <= 2:
#     raise ValueError("i Finally did it")

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def draw(self):
#         print(f"From point {self.a} to {self.b}")
#
# point1 = Point(3, 7)
# point1.draw()





sum = 0
product = 1
promt_size = 4
largest = 0
for i in range(promt_size):
    print('Input Value',(i+1),': ',end =' ')
    promt_user = int(input())
    minimum = promt_user

    sum+=promt_user
    product*=promt_user
    if  promt_user > largest:
        largest = promt_user
    if minimum < promt_user:
        minimum = promt_user

average = sum / promt_size
print('this here is the sum: ',sum)
print('this here is the product: ',product)
print('this here is the average: ',average)
print('this here is the largest: ',largest)
print('this here is the smallest: ',minimum)












