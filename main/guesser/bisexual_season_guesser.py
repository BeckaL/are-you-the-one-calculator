from main.model.season import BisexualSeason
from main.game_controller.controller import pair_at, BisexualController, bisexual_contestants
from main.model.season_probabilities import ProbabilityCalculator
from main.display.probability_formatter import BiFormatter
from main.maths.factorials import double_factorial
from main.guesser.guesser_messages import *
import random


class BisexualGuesser:
    def __init__(self, controller, calculator, formatter):
        self.controller = controller
        self.initial_possible_pairings = None
        self.matches = set()
        self.no_matches = set()
        self.unknowns = []
        self.calculator = calculator
        self.formatter = formatter

    def run(self):
        random.shuffle(self.controller.contestants)
        season = BisexualSeason(contestants=self.controller.contestants)
        self.initial_possible_pairings = season.create_possible_pairings()
        display_initial_number_of_scenarios(season.contestants)
        return self.guess_until_solved(season, 1)

    def guess_until_solved(self, season, week_no):
        display_week(week_no)
        display_solution(self.controller.solution)
        truth_booth_guess = self.guess_couple(week_no)
        season_after_truth_booth = self.update_season_with_guess(truth_booth_guess, self.truth_booth_result, season)
        match_up_ceremony_guess = self.generate_match_up_ceremony_guess(season_after_truth_booth)
        season_after_match_up_ceremony = self.update_season_with_guess(match_up_ceremony_guess, self.match_up_ceremony,
                                                                       season_after_truth_booth)
        if self.check_if_solved(week_no):
            return display_exit_message()
        else:
            return self.guess_until_solved(season_after_match_up_ceremony, week_no + 1)

    def update_season_with_guess(self, guess, season_updater_function, season):
        updated_season = season_updater_function(guess, season)
        display_number_of_possibilities(updated_season)
        self.process_knowledge(updated_season)
        return updated_season

    def check_if_solved(self, week_no):
        solved = len(self.matches) == len(self.controller.contestants) / 2
        display_solution_message(self.controller.solution, self.matches, week_no) if solved else None
        return solved

    def process_knowledge(self, season):
        probabilities_hash = self.calculator(self.initial_possible_pairings, season.scenarios).calculate()
        display_probabilities_in_grid(self.formatter, probabilities_hash, season.contestants)
        new_matches, new_no_matches, unknowns = self.get_new_matches_no_matches_and_unknowns(probabilities_hash)
        display_new_matches_and_no_matches(new_matches, new_no_matches)
        self.update_matches_no_matches_and_unknowns(new_matches, new_no_matches, unknowns)
        print_knowns_and_unknowns(self.matches, self.no_matches, self.unknowns)

    def update_matches_no_matches_and_unknowns(self, new_matches, new_no_matches, unknowns):
        self.matches = self.matches.union(new_matches)
        self.no_matches = self.no_matches.union(new_no_matches)
        self.unknowns = unknowns

    def get_new_matches_no_matches_and_unknowns(self, probabilities_hash):
        new_matches, new_no_matches, new_unknowns = set(), set(), []
        for (pair, probability) in probabilities_hash.items():
            if probability == 0 and frozenset(pair) not in self.no_matches:
                new_no_matches.add(frozenset(pair))
            if probability == 1 and frozenset(pair) not in self.matches:
                new_matches.add(frozenset(pair))
            elif 0 < probability < 1:
                new_unknowns.append(frozenset(pair))
        return new_matches, new_no_matches, new_unknowns


    def guess_couple(self, week_no):
        if week_no == 1:
            random.shuffle(self.controller.contestants)
            return pair_at(0, self.controller.contestants)
        return self.unknowns[0] if len(self.unknowns) > 0 else list(self.matches)[0]


    def match_up_ceremony(self, guess, season):
        number_correct = self.controller.number_correct_in_guess(guess)
        display_match_up_guess_and_result_message(guess, number_correct)
        return season.add_updated_scenarios(season.register_guess(guess, number_correct))

    def generate_match_up_ceremony_guess(self, season):
        return {frozenset(pair) for pair in season.scenarios[0]}

    def truth_booth_result(self, pair, season):
        is_correct = self.controller.is_couple(pair)
        display_truth_booth_guess_message(pair, is_correct)
        self.matches.add(pair) if is_correct else self.no_matches.add(pair)
        return season.add_updated_scenarios(season.register_truth_booth(pair, is_correct))


if __name__ == "__main__":
    calculator = ProbabilityCalculator
    controller = BisexualController(contestants=bisexual_contestants[0:10])
    guesser = BisexualGuesser(controller, calculator, BiFormatter)
    guesser.run()
