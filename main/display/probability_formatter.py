import math

class Formatter():
    def __init__(self, probabilities_hash, women, men):
        self.probabilities_hash = probabilities_hash
        self.women = women
        self.men = men

    def longest_name_length(self):
        return max([len(name) for name in self.women + self.men])

    def top_left_space(self):
        return " " * self.longest_name_length() + "  "

    def pad_contestant_name_in_header(self, name):
        min_number_length = 4
        left_padding = math.floor((min_number_length - len(name))/2)
        right_padding = math.ceil((min_number_length - len(name))/2)
        end_space = "   "
        return left_padding * " " + name + right_padding * " " + end_space

    def pad_row_label(self, name):
        padding_required = self.longest_name_length() - len(name)
        return name + " " * padding_required

    def printable_grid(self):
        top_row = [self.top_left_space() + "".join([self.pad_contestant_name_in_header(c) for c in self.women])]
        probability_rows = [self.probabilities_for_woman(w) for w in self.women]
        other_rows = [[self.pad_row_label(self.men[i])] + probability_rows[i] for i in
                      range(len(self.men))]
        printable_other_rows = ["  ".join(row) for row in other_rows]
        rows = top_row + printable_other_rows
        return "\n".join(rows)

    def probabilities_for_woman(self, woman):
        return list(map(lambda man: self.pad_digit(self.probabilities_hash[(woman, man)], len(man)), self.men))

    def pad_digit(self, n, length_of_name):
        left_padding = math.floor((length_of_name - 4)/2) * " "
        right_padding = math.ceil((length_of_name - 4)/2) * " "
        string_n = str(n)
        no_of_spaces = 5 - len(string_n)
        return left_padding + string_n + (" " * no_of_spaces) + right_padding


class BiFormatter():
    def __init__(self, probabilities_hash, contestants):
        self.probabilities_hash = probabilities_hash
        self.contestants = contestants

    def printable_grid(self):
        top_row = [self.top_left_space() + "".join([self.pad_contestant_name_in_header(c) for c in self.contestants])]
        probability_rows = [self.probabilities_for_contestant(c) for c in self.contestants]
        other_rows = [[self.pad_row_label(self.contestants[i])] + probability_rows[i] for i in
                      range(len(self.contestants))]
        printable_other_rows = ["  ".join(row) for row in other_rows]
        rows = top_row + printable_other_rows
        return "\n".join(rows)

    def top_left_space(self):
        return " " * self.longest_name_length() + "  "

    def pad_contestant_name_in_header(self, name):
        min_number_length = 4
        left_padding = math.floor((min_number_length - len(name))/2)
        right_padding = math.ceil((min_number_length - len(name))/2)
        end_space = "   "
        return left_padding * " " + name + right_padding * " " + end_space


    def longest_name_length(self):
        return max([len(name) for name in self.contestants])

    def pad_row_label(self, name):
        padding_required = self.longest_name_length() - len(name)
        return name + " " * padding_required

    def probabilities_for_contestant(self, contestant):
        return [self.pad_digit(self.lookup_couple_in_probabilities_hash(contestant, other_contestant), len(other_contestant)) for
                other_contestant in self.contestants]

    def lookup_couple_in_probabilities_hash(self, a, b):
        if a == b:
            return ' x '
        else:
            try:
                probability = self.probabilities_hash[(a, b)]
            except KeyError:
                probability = self.probabilities_hash[(b, a)]
        return probability

    def pad_digit(self, n, length_of_name):
        left_padding = math.floor((length_of_name - 4)/2) * " "
        right_padding = math.ceil((length_of_name - 4)/2) * " "
        string_n = str(n)
        no_of_spaces = 5 - len(string_n)
        return left_padding + string_n + (" " * no_of_spaces) + right_padding
