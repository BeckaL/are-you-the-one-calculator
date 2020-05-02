from abc import ABC, abstractmethod

class Guess_Generator(ABC):
    @abstractmethod
    def generate_truth_booth_guess(self, week_no, unknowns, matches):
        pass

    @abstractmethod
    def generate_match_up_ceremony_guess(self, season):
        pass


class Basic_Guess_Generator(Guess_Generator):
    def generate_truth_booth_guess(self, week_no, unknowns, matches):
        return list(unknowns.keys())[0] if len(unknowns) > 0 else guess_a_known_couple(matches)

    def generate_match_up_ceremony_guess(self, season):
        return {frozenset(pair) for pair in season.scenarios[0]}


class Highest_Probability_Guess_Generator(Guess_Generator):
    def generate_truth_booth_guess(self, week_no, unknowns, matches):
        if len(unknowns) == 0:
            return guess_a_known_couple(matches)
        chosen_pair, highest_probability = None, 0
        for pair, prob in unknowns.items():
            if highest_probability < prob < 1:
                chosen_pair = pair
                highest_probability = prob
        return chosen_pair


    def generate_match_up_ceremony_guess(self, season):
        return {frozenset(pair) for pair in season.scenarios[0]}


def guess_a_known_couple(matches):
    return list(matches)[0]