

class Automata():

    def __init__(self, lhn, rhn, init_state):
        self.lhn = lhn # left-hand neighbor
        self.rhn = rhn # right-hand neighbor
        self.state = init_state
    
    def getState(self):
        return self.state

    def setState(self, rules):
        #self.lhn = 1 if not self.lhn else self.lhn
        #self.rhn = 1 if not self.rhn else self.rhn
        current_state = int(f'{self.lhn}{self.state}{self.rhn}', 2)
        self.state = rules[current_state]

    def setInitState(self, state):
        self.state = state
    
    def set_lhn(self, lhn):
        self.lhn = lhn
    
    def set_rhn(self, rhn):
        self.rhn = rhn