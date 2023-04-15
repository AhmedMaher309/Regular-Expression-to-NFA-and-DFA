

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


def nfa_to_dfa(nfa, start_state, end_state):
    pass

