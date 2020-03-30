class Formatter():
    def __init__(self, probabilities_hash, women, men):
        self.probabilities_hash = probabilities_hash
        self.women = women
        self.men = men

    def printable_grid(self):
        top_row = ["   " + "      ".join(self.women)]
        probability_rows = [self.probabilities_for_woman(w) for w in self.women]
        other_rows = [[self.men[i]] + probability_rows[i] for i in range(len(self.men))]
        printable_other_rows = ["  ".join(row) for row in other_rows]
        rows = top_row + printable_other_rows
        return "\n".join(rows)

    def probabilities_for_woman(self, woman):
        return list(map(lambda man: self.pad_digit(self.probabilities_hash[(woman, man)]), self.men))

    def pad_digit(self, n):
        string_n = str(n)
        no_of_spaces = 5 - len(string_n)
        return string_n + (" " * no_of_spaces)


class BiFormatter():
    def __init__(self, probabilities_hash, contestants):
        self.probabilities_hash = probabilities_hash
        self.contestants = contestants

    def printable_grid(self):
        top_row = ["   " + "      ".join(self.contestants)]
        probability_rows = [self.probabilities_for_contestant(c) for c in self.contestants]
        other_rows = [[self.contestants[i]] + probability_rows[i] for i in range(len(self.contestants))]
        printable_other_rows = ["  ".join(row) for row in other_rows]
        rows = top_row + printable_other_rows
        return "\n".join(rows)

    def probabilities_for_contestant(self, contestant):
        return list(map(lambda other_contestant: self.pad_digit(
            self.lookup_couple_in_probabilities_hash(contestant, other_contestant)),
                        self.contestants))

    def lookup_couple_in_probabilities_hash(self, a, b):
        if a == b:
            return ' x '
        else:
            try:
                probability = self.probabilities_hash[(a, b)]
            except KeyError:
                probability = self.probabilities_hash[(b, a)]
        return probability

    def pad_digit(self, n):
        string_n = str(n)
        no_of_spaces = 5 - len(string_n)
        return string_n + (" " * no_of_spaces)
