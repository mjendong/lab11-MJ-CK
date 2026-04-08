# https://github.com/mjendong/lab11-MJ-CK.git
# Partner 1: Matthew Jendong
# Partner 2: Charlie Kuang

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
   return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    try:
        return math.log(a, b)
    except:
        raise ValueError

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:

        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)



