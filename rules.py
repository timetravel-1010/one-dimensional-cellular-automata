
""" 
Rules: clase utilizada para manipular las reglas de transición
"""
class Rules():
    def __init__(self):
        self.rules = {
            0: 0, #'000'
            1: 0, #'001'
            2: 0, #'010'
            3: 0, #'011'
            4: 0, #'100'
            5: 0, #'101'
            6: 0, #'110'
            7: 0, #'111'
        }

    def getRules(self):
        return self.rules
    
    def setRule(self, r, val):
        try:
            self.rules[r] = val
        except Exception as e:
            return 'Error ocurred: ' + str(e)

    def setRules(rules):
        self.rules = rules
            