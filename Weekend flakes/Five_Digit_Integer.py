user_input = input("Enter a five-digit integer: ")


if len(user_input) == 5 and user_input.isdigit():
    # Convert the input to a list of individual digits
    digits_list = list(user_input)

    # Print the digits separated by three spaces using str.join()
    result = "   ".join(digits_list)
    print(result)
else:
    print("Invalid input. Please enter a five-digit integer.")


