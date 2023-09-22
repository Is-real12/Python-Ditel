user = input("What is your problem: ")

userNextInput = input("have you had this problem before: ")

match userNextInput:
    case 'yes':
        print("Well you have it again!")

    case 'no':
        print('well you have it now')
