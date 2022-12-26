class automata():

    def __init__(self, lhn, rhn, init_state):
        self.lhn = lhn
        self.rhn = rhn
        self.state = init_state
    
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state