from unittest import TestCase
import SomeThing


class Test(TestCase):
    def test_strings_ly(self):
        self.assertEqual(SomeThing.strings("Dulling"), "Dullingly")

    def test_strings_ing(self):
        self.assertEqual(SomeThing.strings("Dull"), "Dulling")

    def test_strings_lesser_than_3(self):
        self.assertEqual(SomeThing.strings("it"), "it")

    def test_strings_equal_to_3(self):
        self.assertEqual(SomeThing.strings("zip"), "ziping")
