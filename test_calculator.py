# https://github.com/mjendong/lab11-MJ-CK.git
# Partner 1: Matthew Jendong
# Partner 2: Charlie Kuang

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 10), 9)
        self.assertEqual(add(5, 0), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(10, 5), 5)

    ######## Partner 1
    def test_multiply(self):
        # 3 assertions for multiplication
        self.assertEqual(mul(3, 7), 21)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        # 3 assertions for division
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-6, 3), -2)
        # Testing float division
        self.assertEqual(div(5, 2), 2.5)
    # ############################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # Tests that a ZeroDivisionError is raised when b is 0
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(8, 2), 3)
        
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1) # 1 is an invalid base for logarithms
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        # 1 assertion: log of 0 or negative numbers is undefined
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        # 3 assertions: common Pythagorean triples
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        # 1. Test for invalid argument (negative number)
        with self.assertRaises(ValueError):
            square_root(-4)

        # 2 & 3. Test basic function
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(100), 10)
    ##############################


# Do not touch this
if __name__ == "__main__":
    unittest.main()