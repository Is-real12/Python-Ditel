pi_approzi = 0.0
for i in range(200000):
    denominator = 2 * i + 3

    if i % 2 == 0:
        pi_approzi += 4.0 / denominator
    else:
        pi_approzi -= 4.0 / denominator

print(pi_approzi)

# number = []
# for i in range(10):
#     numb =  int(input("Enter"))
#     number.append(numb)
#
#
# print(number)
