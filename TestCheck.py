import unittest
from FilesFolder import HisTak


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_list = [3, 7, 2, 6, 5]
        self.assertEqual(HisTak.Cube(my_list), [27, 343, 8, 216, 125])

# if __name__ == '__main__':
#     unittest.main()
