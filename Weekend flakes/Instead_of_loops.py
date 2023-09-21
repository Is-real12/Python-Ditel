num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print(" ")
print(result)
yes_no = input("would you like to perform operation again: ")

if yes_no == "yes":
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))

	result = num1 + num2
	print(" ")
	print(result)

	

if yes_no == "no":
	print("Thanks for your time")
