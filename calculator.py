
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    if a == 0:
        return ZeroDivisionError
    return b / a

def logarithm(a, b):
    raise ValueError

def exponent(a, b):
    return a**b
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a,b):
    math.hypot(a, b)



