import unittest


from Assignment import list_to_dictionary, two_lists_to_dictionary, find_difference, elements_with_frequency_greater_than_k

class TestMyFunctions(unittest.TestCase):

    def test_list_to_dictionary(self):
        input_list = ['apple', 'banana', 'cherry']
        expected_output = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
        self.assertEqual(list_to_dictionary(input_list), expected_output)

    def test_two_lists_to_dictionary(self):
        input1 = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(two_lists_to_dictionary(input1, input2), expected_output)

    def test_find_difference(self):
        sample_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected_output = 70
        self.assertEqual(find_difference(sample_list), expected_output)

    def test_elements_with_frequency_greater_than_k(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        k = 2
        expected_output = [1, 2, 5]
        self.assertEqual(elements_with_frequency_greater_than_k(sample_input, k), expected_output)

# if _name_ == '_main_':
#     unittest.main()