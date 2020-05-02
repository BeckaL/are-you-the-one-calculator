class ProbabilityCalculator():
    def __init__(self, possible_pairings, current_scenarios):
        self.possible_pairings = possible_pairings
        self.current_scenarios = current_scenarios
        self.total_scenarios = len(current_scenarios)

    def calculate(self):
        return {pair: self.pair_percentage(pair) for pair in self.possible_pairings}

    def pair_percentage(self, pair):
        return round(self.number_of_scenarios_for_pair(pair[0], pair[1]) / float(self.total_scenarios), 2)

    def number_of_scenarios_for_pair(self, a, b):
        return len([scenario for scenario in self.current_scenarios if (a, b) in scenario or (b, a) in scenario])

    def calculate_initial_probabilities_bi_season(self, no_of_contestants):
        initial_universal_probability = round(1 / (no_of_contestants - 1), 2)
        return {pair:  initial_universal_probability for pair in self.possible_pairings}




