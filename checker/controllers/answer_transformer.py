import re
from . import pattern_dictionary_all
from . import pattern_dictionary_standardize_mathquill

"""
Helper method to make sure that the process is recursive.
"""

def replace_recursive(pattern, repl, expression):

    count = 1
    expr = expression[:]
    while count != 0:
        expr, count = re.subn(pattern, repl, expr)
        if (count!=0):
            print("pattern"+pattern)
            print("repl"+repl)
            print (expr)
    return expr


"""
Transform expression in Latex format into ASCII (Sympy) format.
Approach: Recursive transformation using regular expression.
"""


def transform_latex_to_sympy(expression, mode="Other"):
    # Remove all spaces
    expr = expression.replace(' ', '')
    # Replace all character '*' to 'X' to avoid confusion
    expr = expr.replace('*', '\\times')
    # Makes all character to lowercase (uppercase variable name in Sympy is
    # considered as function)
    # expr = expr.lower()

    for pattern, repl in pattern_dictionary_standardize_mathquill.rules:
        expr = replace_recursive(pattern, repl, expr)
    if mode.lower() == "mathquill only":
        return expr
    for pattern, repl in pattern_dictionary_all.rules:
        expr = replace_recursive(pattern, repl, expr)
    return expr
