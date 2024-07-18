import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    #Write a test to make sure that get_rolled_value returns a value from 1 to 6
    def test_get_rolled_value1(self):
        die = Die()
        for i in range(10):
            die.roll()
            die_val = die.get_rolled_value()
            self.assertTrue(1 <= die_val <= 6, f"Invalid Roll: {die_val}")