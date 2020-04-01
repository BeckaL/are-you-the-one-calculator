from main.model.season import *


def test_creates_all_possible_pairings():
    season = StraightSeason(['A', 'B', 'C'], ['X', 'Y', 'Z'], "some_season")
    expected_pairings = [('A', 'X'), ('A', 'Y'), ('A', 'Z'),
                         ('B', 'X'), ('B', 'Y'), ('B', 'Z'),
                         ('C', 'X'), ('C', 'Y'), ('C', 'Z')]
    assert sorted(season.create_possible_pairings()) == sorted(expected_pairings)


def test_creates_all_scenarios():
    season = StraightSeason(['A', 'B', 'C'], ['X', 'Y', 'Z'], "some_season")
    expected = [
        {('A', 'X'), ('B', 'Y'), ('C', 'Z')},
        {('A', 'X'), ('B', 'Z'), ('C', 'Y')},
        {('A', 'Y'), ('B', 'X'), ('C', 'Z')},
        {('A', 'Y'), ('B', 'Z'), ('C', 'X')},
        {('A', 'Z'), ('B', 'X'), ('C', 'Y')},
        {('A', 'Z'), ('B', 'Y'), ('C', 'X')}]
    assert check_scenario_equality(season.scenarios, expected)


def test_registers_a_guess_for_a_3_couple_scenario():
    season = StraightSeason(['A', 'B', 'C'], ['X', 'Y', 'Z'], "some_season")
    guess = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}
    correct = 1

    expected = [
        {('A', 'X'), ('B', 'Z'), ('C', 'Y')},
        {('A', 'Y'), ('B', 'X'), ('C', 'Z')},
        {('A', 'Z'), ('B', 'Y'), ('C', 'X')}]

    new_scenarios = season.register_guess(guess, correct)
    assert check_scenario_equality(new_scenarios, expected)


def test_registers_a_guess_for_a_4_couple_scenario():
    season = StraightSeason(['A', 'B', 'C', 'D'], ['X', 'Y', 'Z', 'W'], "some_season")
    guess = {('A', 'X'), ('B', 'Y'), ('C', 'Z'), ('D', 'W')}
    correct = 2

    expected = [{('C', 'W'), ('D', 'Z'), ('A', 'X'), ('B', 'Y')},
                {('C', 'Y'), ('D', 'W'), ('A', 'X'), ('B', 'Z')},
                {('C', 'Z'), ('D', 'Y'), ('A', 'X'), ('B', 'W')},
                {('B', 'X'), ('C', 'Z'), ('A', 'Y'), ('D', 'W')},
                {('C', 'X'), ('A', 'Z'), ('D', 'W'), ('B', 'Y')},
                {('C', 'Z'), ('A', 'W'), ('D', 'X'), ('B', 'Y')}]

    new_scenarios = season.register_guess(guess, correct)
    assert check_scenario_equality(new_scenarios, expected)


def test_registers_a_false_truth_booth():
    season = StraightSeason(['A', 'B', 'C'], ['X', 'Y', 'Z'], "some_season")
    new_scenarios = season.register_truth_booth(('A', 'X'), correct=False)

    expected = [
        {('A', 'Y'), ('B', 'X'), ('C', 'Z')},
        {('A', 'Y'), ('B', 'Z'), ('C', 'X')},
        {('A', 'Z'), ('B', 'X'), ('C', 'Y')},
        {('A', 'Z'), ('B', 'Y'), ('C', 'X')}
    ]

    assert check_scenario_equality(new_scenarios, expected)


def test_registers_a_true_truth_booth():
    season = StraightSeason(['A', 'B', 'C', 'D'], ['X', 'Y', 'Z', 'W'], "some_season")
    new_scenarios = season.register_truth_booth(('A', 'X'), correct=True)

    expected = [
        {('D', 'W'), ('C', 'Z'), ('A', 'X'), ('B', 'Y')},
        {('D', 'Z'), ('C', 'W'), ('A', 'X'), ('B', 'Y')},
        {('B', 'Z'), ('D', 'W'), ('C', 'Y'), ('A', 'X')},
        {('D', 'Z'), ('C', 'Y'), ('A', 'X'), ('B', 'W')},
        {('B', 'Z'), ('D', 'Y'), ('C', 'W'), ('A', 'X')},
        {('D', 'Y'), ('C', 'Z'), ('A', 'X'), ('B', 'W')}
    ]

    assert check_scenario_equality(new_scenarios, expected)


def test_creates_a_bisexual_season():
    season = BisexualSeason(['A', 'B', 'C', 'D'], "some_season")
    actual = season.scenarios
    expected = [
        {('A', 'B'), ('C', 'D')},
        {('A', 'C'), ('B', 'D')},
        {('A', 'D'), ('B', 'C')}
    ]
    assert (check_scenario_equality(actual, expected))


def test_creates_possible_pairings_for_a_bisexual_season():
    season = BisexualSeason(['A', 'B', 'C', 'D'], "some_season")
    actual = season.create_possible_pairings()
    expected = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    assert (sorted(actual) == sorted(expected))


def test_registers_a_true_truth_booth_for_a_bisexual_season_regardless_of_order():
    truth_booths = [('A', 'B'), ('B', 'A')]
    for tb in truth_booths:
        season = BisexualSeason(['A', 'B', 'C', 'D'], "some_season")
        actual = season.register_truth_booth(tb, True)
        expected = [{('A', 'B'), ('C', 'D')}]
        assert (actual == expected)


def test_registers_a_false_truth_booth_for_a_bisexual_season_regardless_of_order():
    truth_booths = [('A', 'B'), ('B', 'A')]
    for tb in truth_booths:
        season = BisexualSeason(['A', 'B', 'C', 'D'], "some_season")
        actual = season.register_truth_booth(tb, False)
        expected = [{('A', 'D'), ('B', 'C')},
                    {('A', 'C'), ('B', 'D')}]
        assert (check_scenario_equality(actual, expected))


def test_registers_a_weekly_guess_for_a_bisexual_season_regardless_of_order():
    guesses = [[('A', 'B'), ('C', 'D')],[('B', 'A'), ('D', 'C')]]
    for guess in guesses:
        season = BisexualSeason(['A', 'B', 'C', 'D'], "some_season")
        actual = season.register_guess(guess, 2)
        expected = [{('A', 'B'), ('C', 'D')}]
        assert (check_scenario_equality(actual, expected))


def check_scenario_equality(actual, expected):
    return len([el for el in actual if el in expected]) == len(expected) and len(expected) == len(actual)
