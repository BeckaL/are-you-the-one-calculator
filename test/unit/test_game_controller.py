from main.game_controller.controller import *


def test_generates_a_bisexual_game():
    generator = BisexualController()
    assert solution_contains_all_contestants_only_once(generator.solution, bisexual_contestants)
    assert len(generator.solution) == 8


def test_generates_a_bisexual_game():
    generator = StraightController()
    assert solution_contains_all_contestants_only_once(generator.solution, straight_contestants)
    assert len(generator.solution) == 10


def test_marks_a_correct_truth_booth():
    assert generator_with_fixed_solution.is_couple({'B', 'A'})


def test_marks_an_incorrect_truth_booth():
    assert not generator_with_fixed_solution.is_couple({'C', 'A'})


def test_marks_a_match_up_ceremony():
    guess = {frozenset(('A', 'B')),
             frozenset(('C', 'D')),
             frozenset(('E', 'F')),
             frozenset(('G', 'H')),
             frozenset(('I', 'K')),
             frozenset(('M', 'O')),
             frozenset(('J', 'L')),
             frozenset(('N', 'P'))}
    assert (generator_with_fixed_solution.number_correct_in_guess(guess) == 4)


def test_marks_a_correct_match_up_ceremony():
    assert (generator_with_fixed_solution.number_correct_in_guess(mocked_solution) == 8)


mocked_solution = {frozenset(('A', 'B')),
                   frozenset(('C', 'D')),
                   frozenset(('E', 'F')),
                   frozenset(('G', 'H')),
                   frozenset(('I', 'J')),
                   frozenset(('K', 'L')),
                   frozenset(('M', 'N')),
                   frozenset(('O', 'P'))}
generator_with_fixed_solution = BisexualController(mocked_solution)


def solution_contains_all_contestants_only_once(solution, expected_contestants):
    return sorted([contestant for pair in solution for contestant in pair]) == expected_contestants
