def student(name):
    student_age = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}

    if name in student_age:
        sting = f"hi  {name}  you are  {student_age.get(name)}"
    else:
        print("your name is not in the dictionary ")
        otherkey = int(input("Enter your age "))
        student_age.setdefault(name, otherkey)

        sting = f"Hi  {name} you are  {student_age.get(name, otherkey)}"
        print(student_age)
    return sting


user = input("Enter your name ")
user1 = user.lower()
func = student(user1)
print(func)
