numbers = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]

# Manual sorting
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
# multiple is number that 5 can div without re
print(numbers)
#             # mean += numbers / len(numbers)
# n = len(numbers)
# median = 0
#
# if n % 2 == 0:
#     median = (numbers[n / 2] + numbers[n / 2]) / 2
# else:
#     pass
# print("Sorted list:", numbers)
# print(median)
# #
# print(mean / len(numbers))
# print(mean)
#
#
# total = 0
# for a in numbers:
#     total += a
#     total = total / a
# print(total)
# median = numbers[n//2]
# print("Median:", median)
