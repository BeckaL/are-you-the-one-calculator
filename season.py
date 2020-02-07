import itertools

class Season():
    def __init__(self, women, men):
        self.women = women
        self.men = men
        self.scenarios = self.create_scenarios()

    def createPossiblePairings(self):
        return itertools.product(self.women, self.men)

    def create_scenarios(self):
        return [set(zip(woman, self.men)) for woman in itertools.permutations(self.women, len(self.men))]

    def register_guess(self, guess, noCorrect):
        return list(filter(lambda x: count_shared(x, guess) == noCorrect, self.scenarios))

    def register_truth_booth(self, couple, correct):
        if correct:
            return list(filter(lambda scenario: couple in scenario, self.scenarios))
        else:
            return list(filter(lambda scenario: couple not in scenario, self.scenarios))


def count_shared(scenario_1, scenario_2):
    return sum(map(lambda couple: 1 if couple in scenario_2 else 0, list(scenario_1)))