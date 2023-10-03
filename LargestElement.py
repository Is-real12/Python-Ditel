def LargestElement():
    elements = [3, 4, 6, 8, 1, 9, 2]
    largest = elements[0]
    for element in elements:
        if element > largest:
            largest = element
    return largest

def get_odd_positions(lst):
    odd_elements = []
    for i in range(len(lst)):
        if i % 2 != 0:
            odd_elements.append(lst[i])
    return odd_elements

def get_even_positions(lst):
    even_elements = []
    for i in range(len(lst)):
        if i % 2 == 0:
            even_elements.append(lst[i])
    return even_elements

def compute_running_total(lst):
    running_total = 0
    running_totals_list = []
    for num in lst:
        running_total += num
        running_totals_list.append(running_total)
    return running_totals_list
