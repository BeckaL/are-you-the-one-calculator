import random


from main.game_controller.controller import pair_at
from main.guesser.guesser_messages import *
from main.maths.factorials import double_factorial
from main.model.season import BisexualSeason
from main.model.season_probabilities import ProbabilityCalculator


class BisexualGuesser:
    def __init__(self, controller, calculator, formatter, guesser):
        self.controller = controller
        self.all_poss_pairings = None
        self.current_probability_hash = None
        self.calculator = calculator
        self.formatter = formatter
        self.guesser = guesser

    def run(self):
        random.shuffle(self.controller.contestants)
        season = BisexualSeason(contestants=self.controller.contestants)
        self.all_poss_pairings = season.create_possible_pairings()
        initial_probabilities = self.calculator(self.all_poss_pairings,[]).calculate_initial_probabilities_bi_season(len(self.controller.contestants))
        self.current_probability_hash = ProbabilitiesHash(initial_probabilities)
        display_probabilities_in_grid(self.current_probability_hash.probabilities, season.contestants)
        display_initial_number_of_scenarios(season.contestants)
        return self.guess_until_solved(season, 1)

    def guess_until_solved(self, season, week_no):
        display_start_of_week_info(week_no, self.controller.solution)
        truth_booth_guess = self.guesser.generate_truth_booth_guess(week_no, self.current_probability_hash.unknowns, self.current_probability_hash.matches)
        season_after_truth_booth = self.update_season_with_guess(truth_booth_guess, self.truth_booth_result, season)
        match_up_ceremony_guess = self.guesser.generate_match_up_ceremony_guess(season_after_truth_booth)
        season_after_match_up_ceremony = self.update_season_with_guess(match_up_ceremony_guess, self.match_up_ceremony,
                                                                               season_after_truth_booth)
        if season_after_match_up_ceremony.solved:
            return display_solution_message(self.controller.solution, self.current_probability_hash.matches, week_no)
        return self.guess_until_solved(season_after_match_up_ceremony, week_no + 1)

    def update_season_with_guess(self, guess, season_updater_function, season):
        updated_season = season_updater_function(guess, season)
        display_number_of_possibilities(updated_season)
        self.process_knowledge(updated_season)
        return updated_season

    def process_knowledge(self, season):
        probabilities_hash = ProbabilitiesHash(self.calculator(self.all_poss_pairings, season.scenarios).calculate())
        display_probabilities_in_grid(probabilities_hash.probabilities, season.contestants)
        display_new_knowledge(*self.get_new_knowledge(probabilities_hash))
        self.current_probability_hash = probabilities_hash
        print_current_knowledge(*probabilities_hash.get_current_knowledge())

    def get_new_knowledge(self, probabilities_hash):
        new_matches, new_no_matches = set(), set()
        for (pair, probability) in probabilities_hash.probabilities.items():
            old_probability = self.current_probability_hash.probabilities[pair]
            if probability == 0 and probability != old_probability:
                new_no_matches.add(frozenset(pair))
            if probability == 1 and probability != old_probability:
                new_matches.add(frozenset(pair))
        return new_matches, new_no_matches

    def match_up_ceremony(self, guess, season):
        number_correct = self.controller.number_correct_in_guess(guess)
        solved = number_correct == len(self.controller.contestants) / 2
        display_match_up_guess_and_result_message(guess, number_correct)
        return season.add_updated_scenarios(season.register_guess(guess, number_correct)).update_solved(solved)

    def truth_booth_result(self, pair, season):
        is_correct = self.controller.is_couple(frozenset(pair))
        display_truth_booth_guess_message(pair, is_correct, self.current_probability_hash.probabilities[pair])
        self.current_probability_hash.probabilities[pair] = 1 if is_correct else 0
        return season.add_updated_scenarios(season.register_truth_booth(pair, is_correct))


class ProbabilitiesHash():
    def __init__(self, hash):
        self.probabilities = hash
        self.matches = self.matches()
        self.no_matches = self.no_matches()
        self.unknowns = self.unknowns()

    def get_current_knowledge(self):
        return self.matches, self.no_matches, self.unknowns

    def matches(self):
        return {pair: prob for pair, prob in self.probabilities.items() if prob == 1}

    def no_matches(self):
        return {pair: prob for pair, prob in self.probabilities.items() if prob == 0}

    def unknowns(self):
        return {pair: prob for pair, prob in self.probabilities.items() if 0 < prob < 1}
