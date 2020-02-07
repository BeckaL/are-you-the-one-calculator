class ProbabilityCalculator():
    def __init__(self, possible_pairings, current_scenarios):
        self.possible_pairings = possible_pairings
        self.current_scenarios = current_scenarios
        self.total_scenarios = len(current_scenarios)

    def calculate(self):
        return {pair: self.pair_percentage(pair) for pair in self.possible_pairings}

    def pair_percentage(self, pair):
        return round(self.number_of_scenarios_for_pair(pair) / float(self.total_scenarios), 2)

    def number_of_scenarios_for_pair(self, pair):
        return len(list(filter(lambda scenario: pair in scenario, self.current_scenarios)))



