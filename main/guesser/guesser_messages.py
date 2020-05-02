from main.maths.factorials import double_factorial


def display_match_up_guess_and_result_message(guess, number_correct):
    print("guessing for match up ceremony: {0}\n number correct is {1}".format(format_guess(guess), number_correct))


def display_truth_booth_guess_message(pair, correct):
    result_message = "PERFECT MATCH" if correct else "NO MATCH"
    print('guessing couple for truth booth: {0}\n{1}'.format(format_couple(pair), result_message))


def display_solution_message(solution, matches, week_no):
    print("solution was {0}".format(format_guess(solution)))
    print("guessed solution {0}".format(format_guess(matches)))
    print("guessed in {0} weeks".format(week_no))


def display_number_of_possibilities(season):
    print("number of possibilities is now {0}".format(len(season.scenarios)))


def display_exit_message():
    print("exiting")


def display_initial_number_of_scenarios(contestants):
    print("number of possible solutions is {0}".format(double_factorial(len(contestants) - 1)))


def display_probabilities_in_grid(formatter, probabilities_hash, contestants):
    print(formatter(probabilities_hash, contestants).printable_grid())


def format_guess(set_of_sets):
    return ", ".join([format_couple(pair) for pair in set_of_sets])


def format_couple(couple):
    return " + ".join(couple)


def format_dict(dict):
    return ", ".join([format_couple(pair) + ": " + str(p) for pair, p in dict.items()])


def print_knowns_and_unknowns(matches, no_matches, unknowns):
    print("current knowledge!")
    print("known matches are {0}".format(format_guess(matches)))
    print("known no matches are {0}".format(format_guess(no_matches)))
    print("unknowns are {0}".format(format_dict(unknowns)))


def display_new_matches_and_no_matches(new_matches, new_no_matches):
    print("new derived matches: {0}".format(", ".join([format_couple(pair) for pair in new_matches])))
    print("new derived no_matches: {0}".format(", ".join([format_couple(pair) for pair in new_no_matches])))


def display_start_of_week_info(week_no, solution):
    print("week is {0}".format(week_no))
    print("solution is {0}".format(format_guess(solution)))
