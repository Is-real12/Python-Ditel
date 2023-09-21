yourMoni = float(input("ENTER YOUR MONEY: "))
for i in range(1, 31):
    roi = yourMoni * 0.10
    new_am = roi + yourMoni
    yourMoni = new_am
    print(f"your ROI is ${roi}  your investment is now ${new_am} for Year  {i}")






# the your moni is goin to be changing the yourmoni a it is beign calculated
