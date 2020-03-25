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

