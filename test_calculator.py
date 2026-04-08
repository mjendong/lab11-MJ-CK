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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()