# https://github.com/mjendong/lab11-MJ-CK.git
# Partner 1: Matthew Jendong
# Partner 2: Charlie Kuang

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 10), 9)
        self.assertEqual(add(5, 0), 5)

    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(sub(3, 5), 2)
        self.assertEqual(sub(0, 3), 3)
        self.assertEqual(sub(10, 5), -5)
    ######## Partner 1
    def test_multiply(self):
        # 3 assertions for multiplication
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        # 3 assertions for division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Testing float division
        self.assertEqual(self.calc.divide(5, 2), 2.5)
    # ############################


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        self.assertRaises(div(0, 5), ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(10, 10), 1)
        self.assertRaises(log(-5, 0), ValueError)
        self.assertRaises(log(0, -5), ValueError)
    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        self.assertRaises(div(0, 5), ZeroDivisionError)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        # 1 assertion: log of 0 or negative numbers is undefined
        with self.assertRaises(ValueError):
            self.calc.logarithm(0, 5)

    def test_hypotenuse(self):
        # 3 assertions: common Pythagorean triples
        self.assertEqual(self.calc.hypotenuse(3, 4), 5)
        self.assertEqual(self.calc.hypotenuse(5, 12), 13)
        self.assertEqual(self.calc.hypotenuse(8, 15), 17)

    def test_sqrt(self):
        # 1. Test for invalid argument (negative number)
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)

        # 2 & 3. Test basic function
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(100), 10)
    ##############################


# Do not touch this
if __name__ == "__main__":
    unittest.main()