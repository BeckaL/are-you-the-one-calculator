def add_guess(season, input_output):
    if season.is_bisexual_season():
        formatted_couples = add_guess_for_bisexual_season(season, input_output)
    else:
        formatted_couples = add_guess_for_straight_season(season, input_output)
    no_correct = int(input_output.input("How many couples are correct? \n"))
    new_possibilities = season.register_guess(formatted_couples, no_correct)
    return season.add_updated_scenarios(new_possibilities)


def add_guess_for_bisexual_season(season, input_output):
    return {tuple(couple.split("+")) for couple in input_output.input("Enter couples:\n").split(",")}


def add_guess_for_straight_season(season, input_output):
    print("women are {w}".format(w=season.women))
    return {(woman, input_output.input("Enter partner for {w}".format(w=woman))) for woman in
               season.women}
