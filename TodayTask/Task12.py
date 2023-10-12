user_letter = input("Enter a letter: ")

vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vowel)):
    if user_letter in vowel[i]:
        print("true")
        break
    else:
        print("False")
        break