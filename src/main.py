from typing import Dict
from nfa_graphing import draw_nfa
from input_handler import *
from shunt_yard import *
from dfa import nfa_to_dfa
from nfa import NFA, State
from json_settings import write_dict_to_json
from NFA_construction import concatenate_NFAs, \
    oring_NFAs, \
    zero_or_more_NFA, \
    one_or_more_NFA, \
    zero_or_one_NFA


def create_nfa(input_string):
    states = []
    visual_dict = {}
    s1 = State()
    State.counter += 1
    s1.set_name('S' + str(State.counter))
    s2 = State()
    State.counter += 1
    s2.set_name('S' + str(State.counter))
    states.append(s1)
    states.append(s2)
    nfa = NFA(states, visual_dict)
    nfa.link_states(input_string, s1, s2)
    nfa.set_start_state(s1.name)
    nfa.set_end_state(s2.name)
    return nfa

def postfix_splitter(postfix):
    postfix_list = []
    i = 0
    while i < len(postfix):
        if postfix[i] == '[':
            end_index = postfix.index(']', i)
            postfix_list.append(postfix[i:end_index + 1])
            i = end_index + 1
        else:
            postfix_list.append(postfix[i])
            i += 1
    return postfix_list

def postfix_to_NFA_creator(postfix_list):
    NFAs_stack = []
    for string in postfix_list:
        if string == '+':
            nfa = NFAs_stack.pop()
            new_nfa = one_or_more_NFA(nfa)
            NFAs_stack.append(new_nfa)
        elif string == '*':
            nfa = NFAs_stack.pop()
            new_nfa = zero_or_more_NFA(nfa)
            NFAs_stack.append(new_nfa)
        elif string == '?':
            nfa = NFAs_stack.pop()
            new_nfa = zero_or_one_NFA(nfa)
            NFAs_stack.append(new_nfa)
        elif string == '^':
            second_nfa = NFAs_stack.pop()
            first_nfa = NFAs_stack.pop()
            new_nfa = concatenate_NFAs(first_nfa, second_nfa)
            NFAs_stack.append(new_nfa)
        elif string == '|':
            second_nfa = NFAs_stack.pop()
            first_nfa = NFAs_stack.pop()
            new_nfa = oring_NFAs(first_nfa, second_nfa)
            NFAs_stack.append(new_nfa)
        else:
            nfa = create_nfa(string)
            NFAs_stack.append(nfa)
    last_nfa = NFAs_stack.pop()
    return last_nfa


def main():
    while True:
        expression_written = read_input()
        if is_valid_expression(expression_written):
            modified_expression = modify_expression(expression_written)
            postfix = shunt_yard(modified_expression)
            postfix_list = postfix_splitter(postfix)
            final_nfa = postfix_to_NFA_creator(postfix_list)
            NFA_to_print, start, end = final_nfa.print_NFA()
            print(start.name)
            print(end.name)
            print(NFA_to_print)
            for key, value in NFA_to_print.items():
                print(f"state: {key[0]}, input: {key[1]} -> go to {value}")
            write_dict_to_json(NFA_to_print,start.name, end.name, 'NFA')
            draw_nfa(NFA_to_print, start.name, end.name)
            nfa_to_dfa(NFA_to_print, start.name, end.name)
        break




if __name__ == "__main__":
    main()
