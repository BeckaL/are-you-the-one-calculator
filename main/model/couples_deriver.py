class CouplesDeriver():
    def __init__(self, weekly_guesses, confirmed_matches, confirmed_no_matches):
        self.weekly_guesses = weekly_guesses
        self.confirmed_matches = confirmed_matches
        self.confirmed_no_matches = confirmed_no_matches
        self.derived_no_matches = []

    def derive(self, i=0, derived_matches=set(), derived_no_matches=set()):
        if i >= len(self.weekly_guesses):
            return {"derived_no_matches": derived_no_matches, "derived_matches": derived_matches}
        (guess, no_correct) = self.weekly_guesses[i]
        unknown_couples = set([couple for couple in guess if
                               not couple_in_list(self.confirmed_matches, couple) and not couple_in_list(
                                   self.confirmed_no_matches, couple)])
        return self.derive(i + 1, derived_matches.union(self.derive_matches(guess, no_correct, unknown_couples)),
                           derived_no_matches.union(self.derive_no_matches(guess, no_correct, unknown_couples)))

    def derive_no_matches(self, guess, no_correct, unknown_couples):
        unknown_couples_are_no_matches = number_of_couples_in_guess_from_list(guess, self.confirmed_matches) == no_correct
        return unknown_couples if unknown_couples_are_no_matches else set()

    def derive_matches(self, guess, no_correct, unknown_couples):
        unknown_couples_are_matches = len(guess) - number_of_couples_in_guess_from_list(guess, self.confirmed_no_matches) == no_correct
        return unknown_couples if unknown_couples_are_matches else set()

def number_of_couples_in_guess_from_list(guess, list):
    return len([couple for couple in list if couple_in_list(guess, couple)])


def couple_in_list(list, couple):
    a, b = couple
    return (a, b) in list or (b, a) in list
