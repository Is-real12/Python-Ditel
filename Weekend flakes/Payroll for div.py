emplyee_name = input("Enter the Employee name: ")
noh = float(input("Enter the working hour spent in a week: "))
h_pay_rate = float(input("Enter hourly paid rate: "))
month = input("Enter Month: ")
fedral_tax = float(input("Enter the fedral tax withholding rate: "))
state = float(input("Enter the state tax withholding rate: "))
print("")
print("\t\t\t Payroll for ",month)
print("Employee name: ", emplyee_name)
print("Hourly Worked: ", noh)
print("Paid rate: ", h_pay_rate)
gross_pay = h_pay_rate * noh
print("Gross Pay: " , gross_pay ,"\n")




percent = gross_pay *fedral_tax / 100
per = gross_pay * state / 100
print("Deductions: \n")
print("Fedral Withholding tax: " ,percent)
print("State Withholding tax: " , per)
total_deduc = percent + per
next_pay = gross_pay - total_deduc
print("Total duction" , total_deduc)
print("Next Pay:" , next_pay)