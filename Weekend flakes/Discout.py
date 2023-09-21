item_name = input("Enter the item name: ")
price = int(input("Enter the item price: "))
credict_score_status = int(input("Enter your credit score: "))

credits_score = 70

if credict_score_status >= credits_score:
    discount = price * 10/100
    discount_minus_price = price - discount

    print("1. With a 10% discount you can pay: ",discount_minus_price)
    print("2. you can also do a down payment of ", discount,"\n")
    yourChoice = int(input("select your choice: "))
    if  yourChoice == 1:
        print("""
    *************************
        invoice
    **************************""",
    "\n\tName of item: ", item_name,
    "\n\tDiscount: ", discount_minus_price,
    "\n\tDeposit: ", discount)
    elif yourChoice == 2:
        print("""
        *************************
            invoice
        **************************""",
        "\n\tName of item: ", item_name,
        "\n\tDiscount: ", discount_minus_price,
        "\n\tDeposit: ", discount)
        discout_pay2 = int(input("Enter the amount: "))
elif credict_score_status < 70:
    discount1 = price * 25 / 100
    print("you have a bad credit score so you dont get a discount: ")
    print("you can also do a down payment of $", discount1)

    print("""
    *************************
        invoice
    **************************""",
    "\n\tName of item: ", item_name,
    "\n\tDiscount: ", 0,
    "\n\tDeposit: ", discount1)
