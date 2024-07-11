import unittest

from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distancematrix

class Test_Config(unittest.TestCase):

    def test_get_p_distance1(self):
        #Test that get_p_distance with parameter value ['T','T','T','C','C','A','T','T','T','A'] and
        #['G','A','T','T','C','A','T','T','T','C'] returns the value 4
        self.assertEqual(0.4, get_p_distance(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C']))

    def test_get_p_distance_matrix1(self):
        #Test that get_p_distance with parameter value ['T','T','T','C','C','A','T','T','T','A'],
        #['G','A','T','T','C','A','T','T','T','C'], ['T','T','T','C','C','A','T','T','T','T'], and
        #['G','T','T','C','C','A','T','T','T','A'] returns the value 4
        self.assertEqual([[0.0, 0.4, 0.1, 0.1], [0.4, 0.0, 0.4, 0.3], [0.1, 0.4, 0.0, 0.2], [0.1, 0.3, 0.2, 0.0]], get_p_distance_matrix(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C'], ['T','T','T','C','C','A','T','T','T','T'], ['G','T','T','C','C','A','T','T','T','A']))