import random
from copy import deepcopy

bisexual_contestants = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
straight_contestants = bisexual_contestants + ['Q', 'R', 'S', 'T']


class BisexualGenerator:
    def __init__(self):
        self.contestants = deepcopy(bisexual_contestants)
        self.solution = generate_solution(self.contestants)


def generate_solution(contestants):
    random.shuffle(contestants)
    return {pair_at(i, contestants) for i in range(0, len(contestants) // 2)}


def pair_at(i, contestants):
    return frozenset((contestants[2 * i], contestants[2 * i + 1]))
