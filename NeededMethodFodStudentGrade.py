original_list = [[12, 33], [43, 15]]

num_rows = len(original_list)
num_columns = len(original_list[0])

transposed_list = [[0 for _ in range(num_rows)] for _ in range(num_columns)]

for i in range(num_rows):
    for j in range(num_columns):
        transposed_list[j][i] = original_list[i][j]

print(transposed_list)
