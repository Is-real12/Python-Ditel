def list_to_dictionary(input_list):
    result = {}
    for item in input_list:
        key = item[0].lower()
        if key in result:
            key = key.upper()
        result[key] = item
    return result


def two_lists_to_dictionary(list1, list2):
    result = {}
    for i in range(len(list1)):
        result[list1[i]] = list2[i]
    return result


def find_difference(lst):
    if not lst:
        return None
    min_value = min(lst)
    max_value = max(lst)
    return max_value - min_value


sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
sample_output = find_difference(sample_list)


# print(sample_output)

def elements_with_frequency_greater_than_k(lst, k):
    frequency_dict = {}
    result = []

    for element in lst:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    for element, frequency in frequency_dict.items():
        if frequency > k:
            result.append(element)

    return result


def remove_WhiteSpace(some_List: list):
    new_List = []

    for i in range(len(some_List)):
        if "" != some_List[i]:
            new_List.append(some_List[i])

    return new_List


in_a_testing_with_Halfs = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]


def split_In_Half(in_a_testing_with_Half):
    test = []
    second_test = []
    for i in range(len(in_a_testing_with_Half)):
        if len(in_a_testing_with_Half) // 2 < i + 1:
            test.append(in_a_testing_with_Half[i])
        name = "\r"

        if len(in_a_testing_with_Half) // 2 > i:
            second_test.append(in_a_testing_with_Half[i])

    final_List = [test, second_test]
    return final_List


# print(second_test)

# print(test)
# in_a_testing_with_Half.append(test)
# print(in_a_testing_with_Half)

# print(new_List)

multi_check = []
student = 3
subject = 2
for i in range(student):
    do = []
    for j in range(subject):
        do.append(-1)
    multi_check.append(do)

for l in range(len(multi_check)):
    for p in range(len(multi_check[l])):
        multi_check[l][p] = 119
print(multi_check)
# sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
# k = 2
# sample_output = elements_with_frequency_greater_than_k(sample_input, k)
