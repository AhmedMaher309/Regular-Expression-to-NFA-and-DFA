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
    print(nfa.get_start_state().name)
    print(nfa.get_end_state().name)
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

