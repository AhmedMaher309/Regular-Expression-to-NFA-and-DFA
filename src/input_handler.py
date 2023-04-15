import re

operators = ['+', '*', '?', '|', ']', ')']


def read_input():
    print("Enter the regular expression")
    regex = input()
    while regex == "":
        print("Enter a valid regular expression")
        regex = input()
    return regex


def is_valid_expression(expression_read):
    try:
        re.compile(expression_read, flags=0)
        print("The expression is valid")
        return True
    except:
        print("The expression is not valid")
        return False


def modify_expression(expression_read):
    flag = 0
    modified_expression = ""
    for index, char in enumerate(expression_read):
        if char == ']':
            flag -= 1
        if char not in operators and flag == 0 and index != 0:
            if expression_read[index - 1] != '(' and expression_read[index-1] != '|':
                modified_expression += '^'
        modified_expression += char
        if char == '[':
            flag += 1
    print(modified_expression)
    return modified_expression

