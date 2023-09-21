num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
num3 = int(input("Enter integer 3: "))

# Calculate the sum
sum_result = num1 + num2 + num3

average_result = sum_result / 3


product_result = num1 * num2 * num3


if num1 <= num2 and num1 <= num3:
    smallest_result = num1
elif num2 <= num1 and num2 <= num3:
    smallest_result = num2
else:
    smallest_result = num3


if num1 >= num2 and num1 >= num3:
    largest_result = num1
elif num2 >= num1 and num2 >= num3:
    largest_result = num2
else:
    largest_result = num3


print(f"Sum: {sum_result}")
print(f"Average: {average_result}")
print(f"Product: {product_result}")
print(f"Smallest: {smallest_result}")
print(f"Largest: {largest_result}")