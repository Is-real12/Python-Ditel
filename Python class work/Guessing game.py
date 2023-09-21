# a guessing game

# guessesd_number = random.randint(1, 10) # this here is to for the computer to guess a number between one and 10
# print(guessesd_number) # this  is a cheat deal with it
guess = int(input("Enter your guessed number: ")) # this is an input by the user
while guessesd_number != guess: # so here is the loop if it guessed num is not = guess it will repeat
    guess = int(input("Enter your guessed number: "))
    print(" ")

    ohgod = input("if you want to give up input y: ")
    if ohgod == 'y':
        print("you quiter the answer is ", guessesd_number , 'getat of my front')
        break
    else:
       continue


if guess <= 5:           #             this will not work because if you dont know the time the user will inut you use while if you want a tries limit you use for
    print("you exusted you tries")
    if guess == guessesd_number:
        print("you win mallam ")

    if guess != guessesd_number:
        print("you loose sule ")