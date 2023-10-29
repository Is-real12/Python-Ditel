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
print(sample_output)

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

sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
k = 2
sample_output = elements_with_frequency_greater_than_k(sample_input, k)
