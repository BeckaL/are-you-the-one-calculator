import itertools
from abc import ABC, abstractmethod

class Season(ABC):

    @abstractmethod
    def create_scenarios(self):
        pass

    @abstractmethod
    def create_possible_pairings(self):
        pass

    def register_guess(self, guess, noCorrect):
        return [scenario for scenario in self.scenarios if count_shared(scenario, guess) == noCorrect]

    def register_truth_booth(self, couple, correct):
        if correct:
            return [scenario for scenario in self.scenarios if couple in scenario]
        else:
            return [scenario for scenario in self.scenarios if couple not in scenario]

    def is_bisexual_season(self):
        return type(self).__name__ == "BisexualSeason"

    def add_name(self,name):
        pass

    def add_updated_scenarios(self, new_scenarios):
        pass

class StraightSeason(Season):
    def __init__(self, women, men, season_name=None, scenarios=None):
        self.women = women
        self.men = men
        self.scenarios = scenarios or self.create_scenarios()
        self.season_name = season_name

    def create_possible_pairings(self):
        return itertools.product(self.women, self.men)

    def create_scenarios(self):
        return [set(zip(woman, self.men)) for woman in itertools.permutations(self.women, len(self.men))]

    def add_name(self,name):
        return StraightSeason(self.women, self.men, name, self.scenarios)

    def add_updated_scenarios(self, new_scenarios):
        return StraightSeason(self.women, self.men, self.season_name, new_scenarios)


def count_shared(scenario_1, scenario_2):
    return sum(map(lambda couple: 1 if couple in scenario_2 else 0, list(scenario_1)))


class BisexualSeason(Season):
    def __init__(self, contestants, season_name=None, scenarios = []):
        self.contestants = contestants
        self.scenarios = scenarios or self.create_scenarios()
        self.season_name = season_name

    def all_pairs(self, lst):
        if len(lst) < 2:
            yield []
            return
        a = lst[0]
        for i in range(1, len(lst)):
            pair = (a, lst[i])
            for rest in self.all_pairs(lst[1:i] + lst[i + 1:]):
                yield [pair] + rest

    def create_scenarios(self):
        return list(set(l) for l in self.all_pairs(self.contestants))

    def create_possible_pairings(self):
        return itertools.combinations(self.contestants, 2)

    def add_name(self, name):
        return BisexualSeason(self.contestants, name, self.scenarios)

    def add_updated_scenarios(self, new_scenarios):
        return BisexualSeason(self.contestants, self.season_name, new_scenarios)
