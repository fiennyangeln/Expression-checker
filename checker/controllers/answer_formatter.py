import re
'''
Splitting a sequence of character into a list of terms.
Used improve trigonometric proving assessment.
This is to support first additional feature: Find if the user writes the
important step.
Approach: Split the expression into a list of term, then compare each term.
'''


def split_term(expression):
    # End of expression
    if len(expression) == 0:
        return []
    # Find the number of bracket pairs needed
    # Counter should be number of bracket
    if re.match(r"^\\frac", expression):
        bracket_left = 2
    elif re.match(r"^\\(sin|cos|tan|cot|sec|csc|log)\^", expression):
        bracket_left = 2
    elif re.match(r"^\\(sin|cos|tan|cot|sec|csc|log)", expression):
        bracket_left = 1
    else:
        bracket_left = 0
    # Find the index of first bracket + 1, or 0 otherwise
    # Indicates the starting index to explore
    if bracket_left > 0:
        start_position = expression.index("{")
    else:
        start_position = 0
    end_position = start_position
    counter = 1
    # Find the location of closing bracket
    while counter > 0 and bracket_left > 0:
        end_position = end_position + 1
        # Increment or decrement according to the current character
        if expression[end_position] == '{':
            counter = counter + 1
        elif expression[end_position] == '}':
            counter = counter - 1
        # One pair of bracket has been found
        if counter == 0:
            bracket_left = bracket_left - 1
    # Include the following string before delimited (+ or -)
    while end_position < len(expression) - 1:
        if ((expression[end_position + 1] == '+') or
                (expression[end_position + 1] == '-')):
            break
        else:
            end_position = end_position + 1
    result = expression[0:end_position + 1]
    # Remove the unnecessarry positive sign (+) at the beginning
    if result.startswith('+'):
        result = result[1:]
    # Wrap into list
    result_list = [result]
    return (result_list + split_term(expression[end_position + 1:]))


'''
Splitting a sequence of character into a list of answer.
Delimiter = "|"
'''


def split_answer(expression):
    return expression.split("|")


"""
Split an expression into two parts, LHS and RHS
Can handle the plane geometry as well.
"""


def split_LHS_RHS(expression):
    # Remove space
    expression = expression.replace(" ", "")
    split_expr = re.split("=|\bot|\\\parallel", expression)
    if len(split_expr) != 2:
        # Error
        return None, None
    # Find delimiter
    if "\bot" in expression:
        delimiter = "\bot"
    elif "\parallel" in expression:
        delimiter = "\parallel"
    else:
        delimiter = "="
    LHS = split_expr[0]
    RHS = split_expr[1]
    return LHS, RHS, delimiter


def split_plane_geometry_term(expression):
    LHS, RHS, delimiter = split_LHS_RHS(expression)
    if LHS is None and RHS is None:
        # Error when splitting RHS and RHS
        return None
    result_dict = {}
    result_dict['LHS'] = LHS
    result_dict['RHS'] = RHS
    result_dict['delimiter'] = delimiter
    return result_dict
