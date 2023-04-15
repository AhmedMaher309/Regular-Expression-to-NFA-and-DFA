
operators_precedence = {
                        '*': 2, '+': 2, '?': 2,
                        '^': 1,
                        '|': 0
                        }

def shunt_yard(expression):
    output_postfix = ""
    operators_stack = []
    flag = 0
    for char in expression:
        if char in operators_precedence.keys() and flag == 0:
            while len(operators_stack) != 0 and operators_stack[-1] != '(' and\
                    operators_precedence[operators_stack[-1]] >= operators_precedence[char]:
                output_postfix += operators_stack[-1]
                operators_stack.remove(operators_stack[-1])
            operators_stack.append(char)
        elif char == '(' and flag == 0:
            operators_stack.append(char)
        elif char == ')' and flag == 0:
            while len(operators_stack) != 0 and operators_stack[-1] != '(':
                output_postfix += operators_stack[-1]
                operators_stack.remove(operators_stack[-1])
            if operators_stack[-1] == '(':
                operators_stack.remove(operators_stack[-1])
        elif char == '[':
            output_postfix += char
            flag += 1
        elif char == ']':
            output_postfix += char
            flag -= 1
        else:
            output_postfix += char

    while len(operators_stack) != 0:
        output_postfix += operators_stack[-1]
        operators_stack.remove(operators_stack[-1])

    print(output_postfix)
    return output_postfix



