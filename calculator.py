"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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

