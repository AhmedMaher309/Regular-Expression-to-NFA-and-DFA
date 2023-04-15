from typing import Dict, List
import copy

class State:
    counter = 0

    def __init__(self):
        self.name = ""
        self.is_terminate = False
        self.is_start = False

    def set_terminate(self, value):
        self.is_terminate = value

    def set_start(self, value):
        self.is_start = True

    def set_name(self, name):
        self.name = name


class NFA:
    def __init__(self, states: List[State], visual_dict=None):
        if visual_dict is None:
            visual_dict = {}
        self.states = states
        self.start_state: State = None
        self.end_state: State = None
        self.NFA_visual_dict: Dict[tuple, list] = visual_dict

    def get_states(self):
        return self.states

    def link_states(self, input_char, start_state, end_state):
        if not self.NFA_visual_dict.get((start_state, input_char)):
            self.NFA_visual_dict[(start_state, input_char)] = []
        self.NFA_visual_dict[(start_state, input_char)].append(end_state)

    def set_start_state(self, name):
        for state in self.states:
            if state.name == name:
                self.start_state = state
                state.set_start(True)
            else:
                state.set_start(False)

    def get_start_state(self):
        return self.start_state

    def set_end_state(self, name):
        for state in self.states:
            if state.name == name:
                self.end_state = state
                state.set_terminate(True)
            else:
                state.set_terminate(False)

    def get_end_state(self):
        return self.end_state

    def get_NFA_visual_dict(self):
        return self.NFA_visual_dict

    def print_NFA(self):
        NFA_for_printing = {}
        for state, input_char in self.NFA_visual_dict.keys():
            values_names = []
            for value in self.NFA_visual_dict[(state, input_char)]:
                values_names.append(value.name)
            NFA_for_printing[(state.name, input_char)] = values_names
        return NFA_for_printing,  self.get_start_state(), self.get_end_state()





