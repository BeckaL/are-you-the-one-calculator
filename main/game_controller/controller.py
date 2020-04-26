import random
from copy import deepcopy
from abc import ABC, abstractmethod

bisexual_contestants = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
straight_women = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
straight_men = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
straight_contestants = straight_women + straight_men


class BaseController(ABC):
    def is_couple(self, couple):
        return couple in self.solution

    def number_correct_in_guess(self, guess):
        return len([couple for couple in guess if couple in self.solution])

    @abstractmethod
    def generate_solution(self):
        pass


class BisexualController(BaseController):
    def __init__(self, fixed_solution=None):
        self.contestants = deepcopy(bisexual_contestants)
        self.solution = fixed_solution or self.generate_solution(self.contestants)

    def generate_solution(self):
        random.shuffle(self.contestants)
        return {_pair_at(i, contestants_to_shuffle) for i in range(0, len(contestants_to_shuffle) // 2)}


class StraightController(BaseController):
    def __init__(self, solution=None):
        self.contestants = deepcopy(straight_contestants)
        self.solution = solution or self.generate_solution(self.contestants)

    def generate_solution(self, contestants):
        shuffled_men = random.shuffle(deepcopy(straight_men))
        return {frozenset(couple) for couple in zip(straight_women, shuffled_men)}


def _pair_at(self, i, shuffled_contestants):
    return frozenset((shuffled_contestants[2 * i], shuffled_contestants[2 * i + 1]))
