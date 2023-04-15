import json


def epsilon_closure(nfa, states):
    # Return the epsilon closure of a set of states
    closure = set()
    queue = list(states)
    while queue:
        state = queue.pop(0)
        closure.add(state)
        if (state, 'ε') in nfa:
            for next_state in nfa[state, 'ε']:
                if next_state not in closure:
                    closure.add(next_state)
                    queue.append(next_state)
    closure = list(closure)
    closure.sort()
    return closure


def nfa_to_dfa(nfa, start, end):
    # Convert an NFA to a DFA
    dfa = {}
    dfa_start = tuple(epsilon_closure(nfa, [start]))
    unmarked_states = [dfa_start]  # List of unmarked states
    marked_states = []  # List of marked states
    while unmarked_states:  # Loop until there are no unmarked states left
        dfa_state = unmarked_states.pop(0)  # Take the first unmarked state
        marked_states.append(dfa_state)  # Mark the state as processed
        for input_char in set(c for (s, c) in nfa.keys() if c != 'ε'):  # Loop over all input characters
            nfa_state = set()
            for state in dfa_state:
                if (state, input_char) in nfa:
                    nfa_state |= set(nfa[(state, input_char)])
            if nfa_state:
                nfa_state = epsilon_closure(nfa, nfa_state)
                nfa_state = tuple(nfa_state)
                if nfa_state not in marked_states + unmarked_states:  # Check if the state is already marked or unmarked
                    unmarked_states.append(nfa_state)  # Add the unmarked state to the list of unmarked states
                dfa[dfa_state, input_char] = nfa_state  # Add a transition to the DFA
    dfa_end = set()
    for key, value in dfa.items():
        if end in value:
            dfa_end.add(value)
    return dfa, dfa_start, dfa_end


def dfa_in_simple_form(dfa, dfa_start, dfa_end):
    i = 1
    grouped_dfa = {dfa_start: 'new_S0'}
    for key, value in dfa.items():
        if value not in grouped_dfa.keys():
            grouped_dfa[value] = 'new_S' + str(i)
            i += 1
    new_dfa = {}
    start_state = grouped_dfa[dfa_start]
    end_state = set()
    for key, value in grouped_dfa.items():
        if key in dfa_end:
            end_state.add(grouped_dfa[key])
    for key, value in dfa.items():
        new_key = (grouped_dfa[key[0]], key[1])
        new_value = grouped_dfa[value]
        new_dfa[new_key] = [new_value]
    return new_dfa, start_state, end_state







#
# def nfa_to_dfa_json(nfa, start, end):
#     # Convert the NFA to a DFA
#     dfa, dfa_start, dfa_end = nfa_to_dfa(nfa, start, end)
#
#     # Convert the DFA to a dictionary with string keys
#     dfa_dict = {}
#     for (state, symbol), next_state in dfa.items():
#         state_str = ','.join(sorted(state))
#         next_state_str = ','.join(sorted(next_state))
#         dfa_dict[f'({state_str}, {symbol})'] = next_state_str
#
#     # Create a dictionary representing the DFA
#     dfa_json = {
#         'start': ','.join(sorted(dfa_start)),
#         'end': ','.join(sorted(dfa_end)),
#         'transitions': dfa_dict,
#     }
#
#     # Serialize the dictionary to a JSON string
#     return json.dumps(dfa_json, indent=4)
