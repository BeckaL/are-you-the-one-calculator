from season import *
from season_probabilities import *
from probability_formatter import *

def main():
    welcome()
    names = get_name_input()
    season = Season(*names)
    display_scenarios(season)
    display_probabilities(season, *names)
    updated_season = add_truth_booth(season)
    display_scenarios(updated_season)
    display_probabilities(updated_season, *names)

def add_truth_booth(season):
    couple = tuple(input("Enter couple: ").split(","))
    raw_result = input("Enter result (type 't' for true or 'f' for false): " )
    result = True if raw_result == "t" else False
    new_possibilities = season.register_truth_booth(couple, result)
    return Season(season.women, season.men, new_possibilities)


def get_name_input():
    raw_women = input("enter the names of the women: \n").split(",")
    trimmed_f_names = list(map(lambda name: name.strip(), raw_women))
    raw_men = input("enter the names of the men: \n").split(",")
    trimmed_m_names = list(map(lambda name: name.strip(), raw_men))
    return trimmed_f_names, trimmed_m_names


def display_scenarios(season):
    print("scenarios are")
    print(format_scenarios(season.scenarios))

def display_probabilities(season, women, men):
    probabilities_calculator = ProbabilityCalculator(season.createPossiblePairings(), season.scenarios)
    hash = probabilities_calculator.calculate()
    formatter = Formatter(hash, women, men)
    print(formatter.printable_grid())


def format_scenarios(scenarios):
    formatted_solutions = [format_solution(solution) for solution in scenarios]
    solutions_with_indexes = map(lambda index_and_solution: (str(index_and_solution[0] + 1), index_and_solution[1]), list(enumerate(formatted_solutions)))
    return "\n".join([": ".join(index_and_pair) for index_and_pair in solutions_with_indexes])


def welcome():
    print("Welcome to the AYTO calculator")
    print("Create a new season")


def format_solution(solution):
    return ", ".join([" + ".join(pair) for pair in solution])

main()