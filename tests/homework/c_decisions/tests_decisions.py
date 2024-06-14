import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio1(self):
        #test that the function get_options_ratio with values 5 and 20 returns .25
        self.assertEqual(.25, get_options_ratio(5, 20))

    def test_get_options_ratio2(self):
        #test that the function get_options_ratio with values 10 and 20 returns .5
        self.assertEqual(.5, get_options_ratio(10, 20))

    def test_get_faculty_rating1(self):
        #test that the function get_faculty_rating returns 'Excellent' with a value of .91
        self.assertEqual(get_faculty_rating(.91), 'Excellent')
    
    def test_get_faculty_rating2(self):
        #test that the function get_faculty_rating returns 'Very Good' with a value of .85
        self.assertEqual(get_faculty_rating(.85), 'Very Good')
    
    def test_get_faculty_rating3(self):
        #test that the function get_faculty_rating returns 'Good' with a value of .71
        self.assertEqual(get_faculty_rating(.71), 'Good')
    
    def test_get_faculty_rating4(self):
        #test that the function get_faculty_rating returns 'Needs Improvement' with a value of .66
        self.assertEqual(get_faculty_rating(.66), 'Needs Improvement')

    def test_get_faculty_rating5(self):
        #test that the function get_faculty_rating returns 'Unacceptable' with a value of .45
        self.assertEqual(get_faculty_rating(.45), 'Unacceptable')
    