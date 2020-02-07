class ProbabilityCalculator():
    def __init__(self, possible_pairings, current_scenarios):
        self.possible_pairings = possible_pairings
        self.current_scenarios = current_scenarios
        self.current_no_of_scenarios = len(current_scenarios)

    def calculate(self):
        return {pair: self.pair_percentage(pair) for pair in self.possible_pairings}

    def pair_percentage(self, pair):
        return round(len(list(filter(lambda scenario: pair in scenario, self.current_scenarios))) / float(
            self.current_no_of_scenarios), 2)
