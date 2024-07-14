import unittest

from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance1(self):
        #Test that get_hamming_distance with parameter value GAGCCTACTAACGGGAT and
        #CATCGTAATGACGGCCT that returns 7
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

    def test_get_dna_complement1(self):
        #Test that get_dna_complement with parameter value AAAACCCGGT returns ACCGGGTTTT
        self.assertEqual("ACCGGGTTTT", get_dna_complement("AAAACCCGGT"))