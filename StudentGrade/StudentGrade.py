student = int(input("Student Size: "))
subject = int(input("Subject Size: "))
print()


def method_score(students, subjects):
    multi_dimensional = []
    for i in range(students):
        score_list = []
        for j in range(subjects):
            print(f"Entering scores for student {(i + 1)}: ")
            score = int(input(f"Enter score for student {(j + 1)}: "))
            print("Saving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaving Successful\n")
            score_list.append(score)
        multi_dimensional.append(score_list)
    return multi_dimensional


list_student_score = method_score(student, subject)


def method_total(list_student_scores):
    list_total = []
    for i in range(len(list_student_scores)):
        total = 0
        for j in range(len(list_student_scores[i])):
            total += list_student_scores[i][j]
        list_total.append(total)

    return list_total


list_total = method_total(list_student_score)


def method_ave(subjects, list_totals):
    average = []
    for i in range(subjects):
        ave = list_totals[i] / subjects
        average.append(ave)
    return average


list_ave = method_ave(subject, list_total)


def method_pos(subjects, list_totals):
    list_pos = []

    for i in range(len(list_totals)):
        pos = 0
        for j in range(len(list_totals)):
            if list_totals[j] > list_ave[i]:
                pos += 1
            list_pos.append(pos)
    return list_pos


list_pos = method_pos(subject, list_total)


def display_student_statics(student, subject, list_student_score, list_total, list_ave, list_pos):
    print("==========================================================")
    print("STUDENT\t\t", end='')
    for i in range(subject):
        print(f"SUB {(i + 1)}\t\t", end='')
    print("TOT\t\tAVE\t\tPOS\t\n", end='')
    print("===========================================================")
    for i in range(student):
        print(f"Student {i + 1}\t\t", end='')
        for j in range(subject):
            print(f"{list_student_score[i][j]}\t\t", end=' ')
        print(f"\t{list_total[i]}\t", end='')
        print(f'\t{list_ave[i]}\t\t', end='')
        print(f'{list_pos[i]}\t\t\n', end='')
    print("===========================================================")
    print("===========================================================")


display_student_statics(student, subject, list_student_score, list_total, list_ave, list_pos)


def method_swapped_score(list_student_score):
    num_rows = len(list_student_score)
    num_columns = len(list_student_score[0])

    transposed_list = [[0 for _ in range(num_rows)] for _ in range(num_columns)]

    for i in range(num_rows):
        for j in range(num_columns):
            transposed_list[j][i] = list_student_score[i][j]

    return transposed_list


swapped_score = method_swapped_score(list_student_score)

swapped_totals = method_total(swapped_score)
swapped_average = method_ave(subject, swapped_totals)
swapped_pos = method_pos(subject, swapped_totals)


def display_subject_statics(student, subject, swapped_totals, swapped_score, swapped_average, swapped_pos):

    print("\nSUBJECT SUMMARY")
    thread = 50
    for i in range(student):
        list_passes = [i]
        list_faille = [i]
        too_many_storyooo = []

        largest = 0
        largest_pos = 0
        lowestScore = swapped_score[0][i]
        lowest_pos = swapped_pos[i]
        passes = 0
        fails = 0
        for j in range(subject):
            score = swapped_score[i][j]
            if score > largest:
                largest = score
                largest_pos = swapped_pos[j]

            if score < lowestScore:
                lowestScore = score
                lowest_pos = swapped_pos[j]

            if score >= thread:
                passes += 1

            else:
                fails += 1

        print(f"""Subject {(i + 1)}
Highest scoring Student is: Student {largest_pos} scoring {largest}
Lowest scoring Student is: Student {lowest_pos} scoring {lowestScore}
Total Score is: {swapped_totals[i]}
Average score is: {swapped_average[i]:.2f}
Numbers of passes: {passes}
Numbers of fails: {fails}""")
        list_faille.append(fails)
        list_passes.append(passes)
        print()
    if student >= i:

        print(f"""
The hardest subject is swapped_score.index with 
              """)


display_subject_statics(student, subject, swapped_totals, swapped_score, swapped_average, swapped_pos)

# display_class_summary()























