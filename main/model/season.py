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
            return [scenario for scenario in self.scenarios if couple_in_scenario(couple, scenario)]
        else:
            return [scenario for scenario in self.scenarios if couple_not_in_scenario(couple, scenario)]

    def is_bisexual_season(self):
        return type(self).__name__ == "BisexualSeason"

    @abstractmethod
    def add_name(self,name):
        pass

    @abstractmethod
    def add_updated_scenarios(self, new_scenarios):
        pass

    @abstractmethod
    def update_solved(self, solved):
        pass

    @abstractmethod
    def update_confirmed_info(self, confirmed_matches, confirmed_no_matches):
        pass

class StraightSeason(Season):
    def __init__(self, women, men, season_name=None, scenarios=None, solved=False, confirmed_matches=set(), confirmed_no_matches=set()):
        if confirmed_matches is None:
            confirmed_matches = set()
        print("in init")
        print(confirmed_no_matches)
        print(solved)
        self.women = women
        self.men = men
        self.scenarios = scenarios or self.create_scenarios()
        self.season_name = season_name
        self.solved = solved
        self.confirmed_matches = confirmed_matches
        self.confirmed_no_matches = confirmed_no_matches


    def create_possible_pairings(self):
        return itertools.product(self.women, self.men)

    def create_scenarios(self):
        return [set(zip(woman, self.men)) for woman in itertools.permutations(self.women, len(self.men))]

    def add_name(self,name):
        return StraightSeason(self.women, self.men, name, self.scenarios, self.solved, self.confirmed_matches, self.confirmed_no_matches)

    def add_updated_scenarios(self, new_scenarios):
        return StraightSeason(self.women, self.men, self.season_name, new_scenarios, self.solved, self.confirmed_matches, self.confirmed_no_matches)

    def update_solved(self, solved):
        return StraightSeason(self.women, self.men, self.season_name, self.scenarios, solved, self.confirmed_matches, self.confirmed_no_matches)

    def update_confirmed_info(self, confirmed_matches, confirmed_no_matches):
        return StraightSeason(self.women, self.men, self.season_name, self.scenarios, self.solved, confirmed_matches, confirmed_no_matches)


def count_shared(scenario_1, scenario_2):
    return sum(map(lambda couple: 1 if couple_in_scenario(couple, scenario_2) else 0, list(scenario_1)))


def couple_in_scenario(couple, scenario):
    a, b = couple
    return (a, b) in scenario or (b, a) in scenario or frozenset({a, b}) in scenario


def couple_not_in_scenario(couple, scenario):
    a, b = couple
    return (a, b) not in scenario and (b, a) not in scenario and frozenset({a, b}) not in scenario


class BisexualSeason(Season):
    def __init__(self, contestants, season_name=None, scenarios = [], solved = False, confirmed_matches = set(), confirmed_no_matches = set()):
        self.contestants = contestants
        self.scenarios = scenarios or self.create_scenarios()
        self.season_name = season_name
        self.solved = solved
        self.confirmed_matches = confirmed_matches
        self.confirmed_no_matches = confirmed_no_matches

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
        print("no scenarios so creating new ones")
        return list(set(l) for l in self.all_pairs(self.contestants))

    def create_possible_pairings(self):
        return list(itertools.combinations(self.contestants, 2))

    def add_name(self, name):
        return BisexualSeason(self.contestants, name, self.scenarios)

    def add_updated_scenarios(self, new_scenarios):
        return BisexualSeason(self.contestants, self.season_name, new_scenarios, self.solved)

    def update_solved(self, solved):
        return BisexualSeason(self.contestants, self.season_name, self.scenarios, solved)

    def update_confirmed_info(self, confirmed_matches, confirmed_no_matches):
        return BisexualSeason(self.contestants, self.season_name, self.scenarios, self.solved, confirmed_matches, confirmed_no_matches)

