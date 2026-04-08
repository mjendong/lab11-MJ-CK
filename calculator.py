import math
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        return ZeroDivisionError
    else:
        return b / a
def log(a, b):
    try:
        log(a, b)
    except:
        return ValueError
def exp(a, b):
    return a ** b

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
   return a * b

def logarithm(a, b):
    return log(a,b)

    # use math library/raise ValueError

def exponent(a, b):
    return a**b

