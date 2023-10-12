coma_Seperated = input("Enter a comma separated numbers ")

in_List = list(coma_Seperated)
new_List = []

for i in in_List:
   if ',' in in_List:
      in_List.remove(',')



print(in_List)


















