import random
from copy import deepcopy

bisexual_contestants = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
straight_contestants = bisexual_contestants + ['Q', 'R', 'S', 'T']


class BaseController:
    def is_couple(self, couple):
        return couple in self.solution

    def number_correct_in_guess(self, guess):
        return len([couple for couple in guess if couple in self.solution])


class BisexualController(BaseController):
    def __init__(self, solution=None):
        self.contestants = deepcopy(bisexual_contestants)
        self.solution = solution or generate_solution(self.contestants)


class StraightController:
    def __init__(self, solution=None):
        self.contestants = deepcopy(straight_contestants)
        self.solution = solution or generate_solution(self.contestants)


def generate_solution(contestants):
    contestants_to_shuffle = deepcopy(contestants)
    random.shuffle(contestants_to_shuffle)
    return {pair_at(i, contestants_to_shuffle) for i in range(0, len(contestants_to_shuffle) // 2)}


def pair_at(i, contestants):
    return frozenset((contestants[2 * i], contestants[2 * i + 1]))
