from sympy import *

def expression_checker(x,y):
    z=simplify(int (x) - int (y))
    return z==0
