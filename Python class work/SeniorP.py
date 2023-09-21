
number = input("Enter a five-digit integer: ")


number = int(number)


digit_5 = number % 10
number //= 10
digit_4 = number % 10
number //= 10
digit_3 = number % 10
number //= 10
digit_2 = number % 10
digit_1 = number // 10

print(digit_1, digit_2, digit_3, digit_4, digit_5)





product = 5

while product <= 10:
    product = product +1
    print("python loop")

for counter in 'PROGRAMMING':
    print(counter, end=' ')



fist_num = int(input("Enter first number: "))
scnd_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

print("your mumu sum is ",fist_num+scnd_num+third_num)
print("your mumu product  is ",fist_num-scnd_num-third_num)
print("your mumu average is ",(fist_num+scnd_num+third_num)/3)

smallest = fist_num

if scnd_num < smallest:
    smallest = scnd_num

if third_num < smallest:
    smallest = third_num

#
largest = fist_num
if scnd_num > smallest:
    largest = scnd_num

if third_num > smallest:
    largest = third_num


#
#
print("your smallest number is : ",smallest)
print("your largest number is : ",largest)

invested_amount = int(input("Enter your invested amount: "))

percent = int (input("Enter the percentage expected: "))

year_cal_for = int(input("Enter the year u are planning to invest for: "))

percent = invested_amount * percent / 100
year_cal = (percent + 1 * invested_amount) * year_cal_for

print("\nyour return in percentage will be: ",percent)

print("\nin a year you will have: ",year_cal)

















