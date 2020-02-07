import itertools

class Season():
    def __init__(self, women, men):
        self.women = women
        self.men = men

    def createPossiblePairings(self):
        return itertools.product(self.women, self.men)

