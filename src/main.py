from typing import Dict
from nfa_graphing import draw_automata
from input_handler import *
from shunt_yard import *
from dfa import nfa_to_dfa, dfa_in_simple_form
from nfa import NFA, State
from json_settings import write_dict_to_json
from NFA_construction import postfix_splitter, postfix_to_NFA_creator

def do_work():
    expression_written = read_input()
    if is_valid_expression(expression_written):
        modified_expression = modify_expression(expression_written)
        postfix = shunt_yard(modified_expression)
        postfix_list = postfix_splitter(postfix)
        final_nfa = postfix_to_NFA_creator(postfix_list)
        NFA_to_print, start, end = final_nfa.print_NFA()
        print(NFA_to_print)
        for key, value in NFA_to_print.items():
            print(f"state: {key[0]}, input: {key[1]} -> go to {value}")
        print(f"start state is: {start.name}")
        print(f"end state is: {end.name}\n")
        draw_automata(NFA_to_print, start.name, [end.name], "nfa")
        print("\n The nfa drawing is done, check the pngs in the folder")
        print(
            "=================================================================================================================================")
        dfa, dfa_start, dfa_end = nfa_to_dfa(NFA_to_print, start.name, end.name)
        print("This is the dfa: \n")
        for key, value in dfa.items():
            print(f"state: {key[0]}, input: {key[1]} -> go to {value}")
        print(f"start state is: {dfa_start}")
        print(f"end state is: {dfa_end}")
        print(
            "===============================================================================================================================")
        new_dfa, new_start, new_end = dfa_in_simple_form(dfa, dfa_start, dfa_end)
        draw_automata(new_dfa, new_start, list(new_end), "dfa")
        print("\n The dfa drawing is done, check the pngs in the folder")
        print(
            "=========================================================================================================================================")
        print("This is the dfa after simplification: \n")
        for key, value in new_dfa.items():
            print(f"state: {key[0]}, input: {key[1]} -> go to {value}")
        print(f"start state is: {new_start}")
        print(f"end state is: {new_end}")

        write_dict_to_json(NFA_to_print, start.name, [end.name], 'NFA')
        write_dict_to_json(new_dfa, new_start, new_end, 'DFA')
        print("Both DFA and NFA json files are now done, check the files")


def main():
    print("This is a program that takes a regular expression and prints its NFA and DFA, output them in Json, and draw them in two pngs")
    while True:
        print("Do you want to write regular expression [y/n]")
        user_input = input()
        if user_input == 'n':
            break
        elif user_input == 'y':
            do_work()
        else:
            print('Invalid answer (only y or n)')




if __name__ == "__main__":
    main()
