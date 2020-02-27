import unittest

from RandomNumGen.ItemReturnType import ItemReturnType
from RandomNumGen.RandomList import RandomList
from RandomNumGen.RandomNumber import RandomNumber

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_random_number(self):
        result = RandomNumber.random_number(0, 10)
        self.assertEqual(int, type(result))

    def test_random_number_seed(self):
        result1 = RandomNumber.random_number_seed(0, 10, 5)
        result2 = RandomNumber.random_number_seed(0, 10, 5)
        self.assertEqual(True, result1 == result2)

    def test_random_list(self):
        result1 = RandomList.random_list(0, 10, 5, 5)
        result2 = RandomList.random_list(0, 10, 5,5,)
        self.assertEqual(True, result1 == result2)