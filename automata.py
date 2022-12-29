import copy

""" 
Automata: clase encargada de modelar un autómata celular
"""
class Automata():

    def __init__(self, lhn, rhn, init_state):
        self.lhn = lhn # left-hand neighbor
        self.rhn = rhn # right-hand neighbor
        self.state = init_state
    
    def getState(self):
        return self.state

    def setState(self, rules):
        current_state = int(f'{self.lhn}{self.state}{self.rhn}', 2) # regla en númeración decimal
        self.state = rules[current_state]

    def setInitState(self, state):
        self.state = state
    
    def set_lhn(self, lhn):
        self.lhn = lhn
    
    def set_rhn(self, rhn):
        self.rhn = rhn