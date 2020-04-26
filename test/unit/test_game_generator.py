from main.game_controller.generator import *


def test_generates_a_game():
    generator = BisexualGenerator()
    assert (solution_contains_all_contestants_only_once(generator.solution, bisexual_contestants))
    assert (len(generator.solution) == 8)


def solution_contains_all_contestants_only_once(solution, expected_contestants):
    contestants = [contestant for pair in solution for contestant in pair]
    print()
    print(sorted(contestants))
    print(expected_contestants)
    return sorted(contestants) == expected_contestants

