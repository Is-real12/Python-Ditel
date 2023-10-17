import unittest
import LargestString


class MyTestCase(unittest.TestCase):
    def test_something(self):

        string = "23569"
        self.assertEqual(LargestString.largestString(string), 9)
