#
# times = 0
# largest = 0
# smallest = 0
# for i in range(4):
#     times+=1
#     input1 = int(input(f'Enter integer {times}: '))
#
#     smallest = input1
#     if input1 > smallest:
#         smallest = input1
#
#
#     if input1 > smallest:
#         smallest += input1
#
#     if input1 > smallest:
#         smallest += input1
#
#     if input1 > smallest:
#         smallest += input1
#
#
#     largest = input1
#     if input1 < largest:
#         largest = input1
# print(largest)
# print(smallest)
result = 0

# user = int(input('enter four integer'))
# each1 = user//1000
# each2 = user//100%10
# each3 = user//10%10
# each4 = user  % 10
#
# print(f'{each1} {each2} {each3} {each4}')
temp = 0
for i in range(5):
    user = int(input('enter four integer'))

    each1 = user // 1000
    each2 = user // 100%10
    each3 = user // 10%10
    each4 = user  %10
    print(f'{each1} {each2} {each3} {each4}')























