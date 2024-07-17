import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    #Write a test to make sure that get_rolled_value returns a value from 1 to 6
    def test_get_rolled_value1(self):
        roll = Die()
        self.assertEqual(Die.get_rolled_value())