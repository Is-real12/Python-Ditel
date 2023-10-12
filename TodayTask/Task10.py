time_numer = int(input("Enter the times "))
if time_numer < 0:
    print("Common would you put a better value")

given_String = input("Enter a String: ")

if time_numer < 2:
    for i in range(time_numer):
        print(given_String)
n_times = " "

if time_numer >= 2:
    for i in range(time_numer):

        first_two = given_String[: 2 :]
        n_times += first_two+" "



print(n_times)
