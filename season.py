import itertools

class Season():
    def __init__(self, women, men, scenarios = None):
        self.women = women
        self.men = men
        self.scenarios = scenarios or self.create_scenarios()

    def createPossiblePairings(self):
        return itertools.product(self.women, self.men)

    def create_scenarios(self):
        return [set(zip(woman, self.men)) for woman in itertools.permutations(self.women, len(self.men))]

    def register_guess(self, guess, noCorrect):
        return [scenario for scenario in self.scenarios if count_shared(scenario, guess) == noCorrect]

    def register_truth_booth(self, couple, correct):
        if correct:
            return [scenario for scenario in self.scenarios if  couple in scenario]
        else:
            return [scenario for scenario in self.scenarios if couple not in scenario]


def count_shared(scenario_1, scenario_2):
    return sum(map(lambda couple: 1 if couple in scenario_2 else 0, list(scenario_1)))