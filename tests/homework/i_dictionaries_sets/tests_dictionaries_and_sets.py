import unittest

from src.homework.i_dictionaries_and_sets.dictionary import get_p_distance

class Test_Config(unittest.TestCase):

    def test_get_p_distance1(self):
        #Test that get_p_distance with parameter value ['T','T','T','C','C','A','T','T','T','A'] and
        #['G','A','T','T','C','A','T','T','T','C'] returns the value 4
        self.assertEqual(4, get_p_distance(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C']))