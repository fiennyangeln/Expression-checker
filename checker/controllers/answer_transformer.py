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
    if "\\binom" in expression:
        expr = replace_binom(expr)
    for pattern, repl in pattern_dictionary_standardize_mathquill.rules:
        expr = replace_recursive(pattern, repl, expr)
    if mode.lower() == "mathquill only":
        return expr
    for pattern, repl in pattern_dictionary_all.rules:
        expr = replace_recursive(pattern, repl, expr)
    return expr

def replace_binom(expression):
    rules = pattern_dictionary_all.binomrules['topbottom']
    pattern = rules[0]
    p = re.compile(pattern)
    groups = p.findall(expression)
    for i in range(len(groups)):
        group = groups[i]
        top = group[0]
        bottom = group[1]
        if top.isnumeric() and bottom.isnumeric():
            continue
        if not bottom.isnumeric():
            expression = re.sub(r'(\d+)'+re.escape(bottom)+r'(\d+)',r'\1*1*\2',expression)
            expression = re.sub(r'(\d+)'+re.escape(bottom),r'\1*1',expression)
            expression = re.sub(re.escape(bottom)+r'(\d+)',r'1*\1', expression)
            expression = re.sub(r'([^A-Za-z])'+re.escape(bottom)+r'([^A-Za-z])',r'\g<1>1\2',expression)
        if not top.isnumeric():
            bottomInt = int(eval(bottom))
            topInt = bottomInt+1
            topStr = str(topInt)
            expression = re.sub(r'(\d+)'+re.escape(top)+r'(\d+)',r'\1*'+re.escape(topStr)+r'*\2',expression)
            expression = re.sub(r'(\d+)'+re.escape(top),r'\1*'+re.escape(topStr),expression)
            expression = re.sub(re.escape(top)+r'(\d+)',re.escape(topStr)+r'*\1', expression)
            expression = re.sub(r'([^A-Za-z])'+re.escape(top)+r'([^A-Za-z])',r'\g<1>'+re.escape(topStr)+r'\2',expression)
        # update the groups value
        groups = p.findall(expression)

    return expression
