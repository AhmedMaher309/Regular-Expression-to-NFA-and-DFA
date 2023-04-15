import json

def epsilon_closure(nfa, states):
    # Return the epsilon closure of a set of states
    closure = set()
    queue = list(states)
    while queue:
        state = queue.pop(0)
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
    dfas_list = []
    dfa = {}
    dfa_start = tuple(epsilon_closure(nfa, [start]))
    print("Epsilon closure of", dfa_start, "is", epsilon_closure(nfa, [start]))
    dfa_end = tuple(epsilon_closure(nfa, [end]))
    unmarked_states = [dfa_start]  # List of unmarked states
    marked_states = []  # List of marked states
    while unmarked_states:  # Loop until there are no unmarked states left
        dfa_state = unmarked_states.pop(0) # Take the first unmarked state
        marked_states.append(dfa_state)  # Mark the state as processed
        for input_char in set(c for (s, c) in nfa.keys() if c != ''):  # Loop over all input characters
            nfa_state = set()
            for state in dfa_state:
                if (state, input_char) in nfa:
                    nfa_state |= set(nfa[(state, input_char)])
            if nfa_state:
                print("Epsilon closure of", nfa_state)
                nfa_state = epsilon_closure(nfa, nfa_state)
                nfa_state = tuple(nfa_state)
                print("is", epsilon_closure(nfa, nfa_state))
                if nfa_state not in marked_states + unmarked_states:  # Check if the state is already marked or unmarked
                    unmarked_states.append(nfa_state)  # Add the unmarked state to the list of unmarked states
                dfa[dfa_state, input_char] = nfa_state  # Add a transition to the DFA

    return dfa, dfa_start, dfa_end







def nfa_to_dfa_json(nfa, start, end):
    # Convert the NFA to a DFA
    dfa, dfa_start, dfa_end = nfa_to_dfa(nfa, start, end)

    # Convert the DFA to a dictionary with string keys
    dfa_dict = {}
    for (state, symbol), next_state in dfa.items():
        state_str = ','.join(sorted(state))
        next_state_str = ','.join(sorted(next_state))
        dfa_dict[f'({state_str}, {symbol})'] = next_state_str

    # Create a dictionary representing the DFA
    dfa_json = {
        'start': ','.join(sorted(dfa_start)),
        'end': ','.join(sorted(dfa_end)),
        'transitions': dfa_dict,
    }

    # Serialize the dictionary to a JSON string
    return json.dumps(dfa_json, indent=4)

