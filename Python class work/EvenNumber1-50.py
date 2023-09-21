sumOf =0
for i in range(2,51):
    result = i %2
    if result == 0:
        sumOf += i+i
        average = sumOf / i
        print(i,end=" ")
print("\nthe sum is ",sumOf," the average is ",average)
#DONE!!!!!!!!!!!!!!!!


#or u can do range (1, 51, 2) she u get so
# even_number = []
# for c in range(2, 51, 2):
#     even_number.append(c)
#     average = sum(even_number) / len(even_number)
#     print(c,end=" ")
# print("\n",average)

# append is a method, sum is java puilt in method the square bracket mean a list append is adding somthing that list
# this is a functionwhen a function exist in a class is a method but when it outside a class it is a function