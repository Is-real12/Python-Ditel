import unittest
from FilesFolder import HappyBirthdayDIV


class MyTestCase(unittest.TestCase):
    def test_something(self):
        tuple1 = (10, 20, 30, 40, 50)
        self.assertEqual(HappyBirthdayDIV.reverseTurple(tuple1), (50, 40, 30, 20, 10))

    def test_index_value_turple(self):
        tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
        tuple2 = ("Apple", [15, 30], (5, 10, 25, 40))
        tuple3 = ([20, 30], (10, 25, 30), "Banana")

        self.assertEqual(HappyBirthdayDIV.get_index_and_values(tuple1), ((1, 20), (2, 25)))
        self.assertEqual(HappyBirthdayDIV.get_index_and_values(tuple2), ((2, 25),))
        self.assertEqual(HappyBirthdayDIV.get_index_and_values(tuple3), ((0, 20), (1, 25)))


if __name__ == '__main__':
    unittest.main()
