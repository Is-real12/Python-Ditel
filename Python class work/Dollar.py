def givenStr(e_g):
    other = e_g[1:]

    first = e_g[:1]
    new_str = ""
    new_str += first

    for i in other:
        if i == first:
            i = '$'

        new_str += i
    return new_str


list_student_scores = [[34, 54, 67, 76],[12, 21, 13, 31]]
list_total = []
for i in range(len(list_student_scores)):
    total = 0
    for j in range(len(list_student_scores[i])):
        total += list_student_scores[i][j]
    list_total.append(total)
print(list_student_scores)