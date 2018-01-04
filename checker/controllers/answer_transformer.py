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
    listexp = p.split(expression)
    print(listexp)
    groups = p.search(expression)
    top = groups.group(1)
    bottom = groups.group(2)
    if top.isnumeric() and bottom.isnumeric():
        return expression
    if not bottom.isnumeric():
        expression = re.sub(r'(\d+)'+re.escape(bottom)+r'(\d+)',r'\1*1*\2',expression)
        expression = re.sub(r'(\d+)'+re.escape(bottom),r'\1*1',expression)
        expression = re.sub(re.escape(bottom)+r'(\d+)',r'1*\1', expression)
        #expression = re.sub(bottom,'1', expression)
        expression = re.sub(r'([^A-Za-z])'+re.escape(bottom)+r'([^A-Za-z])',r'\g<1>1\2',expression)
    if not top.isnumeric():
        bottomInt = int(bottom)
        topInt = bottomInt+1
        expression = re.sub(top,str(topInt),expression)
    print('top'+top)
    #print(groups.pos)
    print('bottom'+bottom)
    print('expression'+expression)
    return expression
