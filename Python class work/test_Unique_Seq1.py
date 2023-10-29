from unittest import TestCase
import Unique_Seq1


class Test(TestCase):
    def test_unique(self):
        samplle_List = [2, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
        self.assertEqual(Unique_Seq1.unique(samplle_List), [2, 4, 6, 8, 10, 12, 14])
        print(samplle_List.Unique_Seq1)
