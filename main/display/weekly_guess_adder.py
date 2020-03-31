from main.model.season import StraightSeason, BisexualSeason
from main.display.input_output import StdInputOutput

def add_guess(season, input_output):
    if season.is_bisexual_season():
        return add_guess_for_bisexual_season(season, input_output)
    else:
        return add_guess_for_straight_season(season, input_output)

def add_guess_for_bisexual_season(season, input_output):
    raw_couples = input_output.input("Enter couples:\n").split(",")
    formatted_couples = {tuple(couple.split("+")) for couple in raw_couples}
    no_correct = int(input_output.input("How many couples are correct? \n"))
    new_possibilities = season.register_guess(formatted_couples, no_correct)
    return BisexualSeason(season.contestants, season.season_name, new_possibilities)


def bisexual_season_prompter(original_names_with_indices, remaining_names, input_output):
    remaining = [(i, x) for (i, x) in list(original_names_with_indices)]
    pass


def add_guess_for_straight_season(season, input_output):
    couples = {(woman, input_output.input("Enter partner for {w}".format(w=woman))) for woman in
               season.women}
    no_correct = int(input_output.input("How many couples are correct? \n"))
    new_possibilities = season.register_guess(couples, no_correct)
    return StraightSeason(season.women, season.men, season.season_name, new_possibilities)

# Basit,Jonathan,Kai,Kari,Jenna,Jasmine,Paige,Brandon,Max,Danny,Kylie,Justin,Nour,Amber,Remy,Aasha