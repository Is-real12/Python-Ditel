import re


# arr = [2, 1, 4, 3];

# for i in range(len(arr)):
#    for j in range(len(arr)):
#         if arr[j] > arr[i]:
#             arr[i], arr[j] = arr[j], arr[i];
# print(arr)
# print("True" if re.fullmatch(r'\d{11}', '08023458684895'))
# --> this will will asign true or fales tru if the given string
# contains srt and only str and false if the given str contain string
# and other character or characters

# print("True" if re.fullmatch(r"\d+[A-Z][a-z]*[A-Z][a-z]*", "2FaceTo")else "False")


def strings(inputs):
    if len(inputs) < 3:
        return inputs
    else:
        var = inputs[-3::]
    if var == "ing":
        inputs += "ly"
    else:
        inputs += "ing"
    return inputs


news = open('name.txt', mode='w')
news.write("this is where i created my file ")
news.close()
