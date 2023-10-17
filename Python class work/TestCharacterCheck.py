import unittest
import LargestString


class MyTestCase(unittest.TestCase):
    def test_something(self):
        first = "love"
        second = "olve"
        self.assertTrue(LargestString.character_Checking(first, second))

    def test_false(self):
        first = "love"
        second = "oliejk"
        self.assertFalse(LargestString.character_Checking(first, second))
