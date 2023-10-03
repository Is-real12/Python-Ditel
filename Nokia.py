def print_menu():
    print("""
           1. PhoneBook     2. Message      3. Chat         4. Call Register
           5. Tone          6. Settings     7. Call Divert  8. Game
           9. Calculator    10. Reminders   11. Clock       12. Profile
           13. SIM service
           """)
    print("Select your choice:")


def phonebook_menu():
    print("""
           PhoneBook Menu
           1. Search       
           2. Service Nos      
           3. Add Name        
           4. Erase
           5. Edit         
           6. Assign Tone 
           7. Send 'B' Card
           8. Options
           9. Speed Dials
           10. Voice Tags
           """)
    print("Select a menu: ")
    search_menu = input()
    if search_menu == "1":
        print("Search....")
    elif search_menu == "2":
        print("Service Nos")
    elif search_menu == "3":
        print("Add Name")
    elif search_menu == "4":
        print("Erase")
    elif search_menu == "5":
        print("Edit")
    elif search_menu == "6":
        print("Assign Tone....")
    elif search_menu == "7":
        print("Send 'B' Card")
    elif search_menu == "8":
        print("Type of View\nMemory Status")
    elif search_menu == "9":
        print("Erase")
    elif search_menu == "10":
        print("Edit")
    else:
        print("Invalid")


def message_menu():
    print("""
           Message Menu
           1. Write Message
           2. Inbox
           3. Outbox
           4. Picture Message
           5. Template
           6. Smileys
           7. Message Settings
           8. Info Service
           9. Voice Mailbox Number
           10. Service Command editor
           """)
    print("Select a menu: ")
    message_menu = input()
    if message_menu == "1":
        print("Message Center Number\nMessage sent as\nMessage Validity")
    elif message_menu == "2":
        print("Deliver report\nReply via same Center\nCharacter support")


def chat_menu():
    print("""
           Chat Menu
           Nothing to see here;            
           """)


def call_register_menu():
    print("""
           Call Register Menu
           1. Missed call
           2. Received calls
           3. Dialed number
           4. Erase recent call lists
           5. Show call duration
           6. Show call cost
           7. Call cost Settings
           8. Prepaid Credit  
           """)
    print("Enter your Choice: ")
    call_reg = input()
    if call_reg == "5":
        print("Last call duration\nAll call's Duration\nReceive call duration\nDialled call's Duration\nClear Timers")
    elif call_reg == "6":
        print("Last call cost\nAll call's cost\nClear Counters")
    elif call_reg == "7":
        print("Call cost limit\nShow cost in")


def tone_menu():
    print("""
           Tone Menu
           1. Ringing tone
           2. Ringing volume
           3. Incoming call alert
           4. Composer
           5. Message alert tone
           6. Keypad tones
           7. Warning and game tones
           8. Vibrating alert
           9. Screen saver
           """)


def settings_menu():
    print("""
           Settings Menu
           1. Call settings
           2. Phone Settings
           3. Security Settings
           4. Restore Factory settings
           """)
    print("Enter your Choice: ")
    settings_menu = input()
    if settings_menu == "1":
        print \
            ("Call Settings Menu\n1. Automatic redial\n2. Speed dialing\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")
    elif settings_menu == "2":
        print \
            ("Phone Settings Menu\n1. Language\n2. Cell info display\n3. Welcome note\n4. Network selection\n5. Lights2\n6. Confirm SIM service actions")
    elif settings_menu == "3":
        print \
            ("Security Settings Menu\n1. PIN code request\n2. Call barring service\n3. Fixed dialing\n4. Closed user group\n5. Phone Security\n6. Change access code")
    elif settings_menu == "4":
        print("Nothing")


def call_divert_menu():
    print("""
           Call Divert menu
           """)


def games_menu():
    print("""
           Games menu
           """)


def calculator_menu():
    print("""
           Calculator menu
           """)


def reminders_menu():
    print("""
           Reminders menu
           """)


def clock_menu():
    print("""
           Clock Menu
           1. Alarm clock
           2. Date Settings
           3. Stop Watch
           5. Countdown time
           6. Auto update of date and time
           """)


def profile_menu():
    print("""
           Profile menu
           """)


def sim_service_menu():
    print("""
           Sim service
           """)


print_menu()
print_Choice = int(input())
match print_Choice:
    case 1:
        phonebook_menu()
        # phoneBook_Choice = int(input())

    case 2:
        message_menu()

    case 3:
        chat_menu()
    case 4:
        call_register_menu()
    case 5:
        tone_menu()
    case 6:
        settings_menu()
    case 7:
        call_divert_menu()
    case 8:
        games_menu()
    case 9:
        calculator_menu()
    case 10:
        reminders_menu()
    case 11:
        clock_menu()
    case 12:
        profile_menu()
    case 13:
        sim_service_menu()




