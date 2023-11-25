import unittest
import Dollar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e_g = "delighted"
        self.assertEqual(Dollar.givenStr(e_g),"delighte$")

    # def test_one_occurance(self):
    #     e_g = "delighte"
    #     self.assertEqual(Dollar.givenStr(e_g),"delighte")

