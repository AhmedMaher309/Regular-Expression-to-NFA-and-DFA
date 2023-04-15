from nfa import NFA
from nfa import State


def concatenate_NFAs(first_nfa: NFA, second_nfa: NFA):
    new_visual_dict = {}
    new_nfa_states = first_nfa.get_states() + second_nfa.get_states()
    new_visual_dict.update(first_nfa.get_NFA_visual_dict())
    new_visual_dict.update(second_nfa.get_NFA_visual_dict())
    new_nfa = NFA(new_nfa_states, new_visual_dict)
    new_nfa.set_start_state(first_nfa.get_start_state().name)
    new_nfa.set_end_state(second_nfa.get_end_state().name)
    new_nfa.link_states('ε', first_nfa.get_end_state(), second_nfa.get_start_state())
    return new_nfa

def oring_NFAs(first_nfa: NFA, second_nfa: NFA):
    new_visual_dict = {}
    new_nfa_states = first_nfa.get_states() + second_nfa.get_states()
    new_visual_dict.update(first_nfa.get_NFA_visual_dict())
    new_visual_dict.update(second_nfa.get_NFA_visual_dict())
    new_nfa = NFA(new_nfa_states, new_visual_dict)
    new_start_state = State()
    State.counter += 1
    new_start_state.set_name('S' + str(State.counter))
    new_end_state = State()
    State.counter += 1
    new_end_state.set_name('S' + str(State.counter))
    new_nfa.states.append(new_start_state)
    new_nfa.states.append(new_end_state)
    new_nfa.link_states('ε', new_start_state, first_nfa.get_start_state())
    new_nfa.link_states('ε', new_start_state, second_nfa.get_start_state())
    new_nfa.link_states('ε', first_nfa.get_end_state(), new_end_state)
    new_nfa.link_states('ε', second_nfa.get_end_state(), new_end_state)
    new_nfa.set_start_state(new_start_state.name)
    new_nfa.set_end_state(new_end_state.name)
    return new_nfa

def zero_or_more_NFA(nfa: NFA):
    new_start_state = State()
    State.counter += 1
    new_start_state.set_name('S' + str(State.counter))
    new_end_state = State()
    State.counter += 1
    new_end_state.set_name('S' + str(State.counter))
    nfa.states.append(new_start_state)
    nfa.states.append(new_end_state)
    nfa.link_states('ε', new_start_state, nfa.get_start_state())
    nfa.link_states('ε', nfa.get_end_state(), new_end_state)
    nfa.link_states('ε', nfa.get_end_state(), nfa.get_start_state())
    nfa.set_start_state(new_start_state.name)
    nfa.set_end_state(new_end_state.name)
    nfa.link_states('ε', nfa.get_start_state(), nfa.get_end_state())
    return nfa

def one_or_more_NFA(nfa: NFA):
    new_start_state = State()
    State.counter += 1
    new_start_state.set_name('S' + str(State.counter))
    new_end_state = State()
    State.counter += 1
    new_end_state.set_name('S' + str(State.counter))
    nfa.states.append(new_start_state)
    nfa.states.append(new_end_state)
    nfa.link_states('ε', new_start_state, nfa.get_start_state())
    nfa.link_states('ε', nfa.get_end_state(), new_end_state)
    nfa.link_states('ε', nfa.get_end_state(), nfa.get_start_state())
    nfa.set_start_state(new_start_state.name)
    nfa.set_end_state(new_end_state.name)
    return nfa

def zero_or_one_NFA(nfa: NFA):
    new_start_state = State()
    State.counter += 1
    new_start_state.set_name('S' + str(State.counter))
    new_end_state = State()
    State.counter += 1
    new_end_state.set_name('S' + str(State.counter))
    nfa.states.append(new_start_state)
    nfa.states.append(new_end_state)
    nfa.link_states('ε', new_start_state, nfa.get_start_state())
    nfa.link_states('ε', nfa.get_end_state(), new_end_state)
    nfa.set_start_state(new_start_state.name)
    nfa.set_end_state(new_end_state.name)
    nfa.link_states('ε', nfa.get_start_state(), nfa.get_end_state())
    return nfa




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
    print(postfix_list)
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
