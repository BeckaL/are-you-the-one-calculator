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
        return unknowns[0] if len(unknowns) > 0 else list(matches)[0]

    def generate_match_up_ceremony_guess(self, season):
        return {frozenset(pair) for pair in season.scenarios[0]}