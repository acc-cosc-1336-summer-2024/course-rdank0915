import unittest

from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

    def test_get_factorial1(self):
        #Test that get_factorial with parameter value 4 returns the value 24
        self.assertEqual(24, get_factorial(4))

    def test_get_factorial2(self):
        #Test that get_factorial with parameter value 5 returns the value 120
        self.assertEqual(120, get_factorial(5))

    def test_get_factorial3(self):
        #Test that get_factorial with parameter value 6 returns the value 720
        self.assertEqual(720, get_factorial(6))

    def test_sum_odd_numbers1(self):
        #Test that sum_odd_numbers with parameter value 7 returns 16
        self.assertEqual(16, sum_odd_numbers(7))

    def test_sum_odd_numbers2(self):
        #Test that sum_odd_numbers with parameter value 9 returns 25
        self.assertEqual(25, sum_odd_numbers(9))

    def test_sum_odd_numbers3(self):
        #Test that sum_odd_numbers with parameter value 10 returns 25
        self.assertEqual(25, sum_odd_numbers(10))