def teacherPeriod(name, period):
    name += ""
    name += f"\n{period}"
    the_Sum = 1
    monthly = 0
    if period <= 100:

        monthly = 20
    else:
        the_sum = period - 100
        the_sum *= the_Sum
        monthly = 25

    for i in range(1, period + 1):
        the_Sum = i * monthly
    name += f"\n{the_Sum}"
    return name


# print(teacherPeriod("John Kelly", 100))


# if period <= 100:
#     monthly = 20
#     for i in range(period):
#         the_sum *= monthly
#     the_Sum = period * 20
#
# else:
#     monthly = 25
#     the_sum = period - 100
#     for i in range(the_sum):
#         the_sum *= monthly
#     for i in range(period):


monthly = 1

period = int(input("Enter period: "))
mul = 1
the_minus = 0
multiplication = 1
if period <= 100:
    monthly = 20
    mul = monthly * period
    print(mul)
else:
    result = (100 * 20) + (period - 100) * 25
    print(result)



