from season import *
from season_probabilities import *
from probability_formatter import *
from season_loader import Loader
from season_saver import Saver


class App():
    def __init__(self, input_output):
        self.input_output = input_output

    def main(self):
        self.input_output.print("Welcome to the AYTO calculator.")
        action_int = int(self.input_output.input(
            "Press 1 to create a new season or 2 to load an existing season:"))
        if action_int == 1:
            season = self.create_season()
            self.run(season, season.women, season.men)
        elif action_int == 2:
            season_name = (self.input_output.input("Enter the name of the season:"))
            season = Loader(season_name).load_all()
            self.input_output.print("loaded season {0}".format(season_name))
            self.display_scenarios(season)
            self.display_probabilities(season, season.women, season.men)
            self.run(season, season.women, season.men)
        else:
            return quit

    def create_season(self):
        names = self.get_name_input()
        season = StraightSeason(*names)
        self.display_scenarios(season)
        self.display_probabilities(season, *names)
        return season

    def run(self, season, women, men):
        action = self.choose_action_in_season(season)
        while action != quit:
            updated_season = action(season)
            self.display_scenarios(updated_season)
            self.display_probabilities(updated_season, women, men)
            return self.run(updated_season, women, men)
        self.quit()

    def choose_action_in_season(self, season):
        action_int = int(self.input_output.input(
            "Choose action: press 1 for adding a truth booth or 2 for adding a weekly guess, or 3 to save the week. Press anything else to quit: "))
        if action_int == 1:
            return self.add_truth_booth
        elif action_int == 2:
            return self.add_weekly_guess
        elif action_int == 3:
            return self.save
        else:
            return quit

    def quit(self):
        self.input_output.print("goodbye")
        return

    def save(self, season):
        confirmation = self.input_output.input("are you sure you want to save? press'y' for yes")
        if confirmation == "y":
            bisexual_season = type(season).__name__ == "BisexualSeason"
            print("isBisexualSeason is")
            print(bisexual_season)
            print("season scenarios are {0}".format(season.scenarios))
            print("season name is {0}".format(season.season_name))
            new_week_number = Saver(season, bisexual_season).save()
            self.input_output.print("Saved week {0}".format(new_week_number))
        return season

    def add_truth_booth(self, season):
        couple = tuple(self.input_output.input("Enter couple: ").split(","))
        raw_result = self.input_output.input("Enter result (type 't' for true or 'f' for false): ")
        result = True if raw_result == "t" else False
        new_possibilities = season.register_truth_booth(couple, result)
        return StraightSeason(season.women, season.men, season.season_name, new_possibilities)

    def add_weekly_guess(self, season):
        couples = {(woman, self.input_output.input("Enter partner for {w}".format(w=woman))) for woman in season.women}
        no_correct = int(self.input_output.input("How many couples are correct? \n"))
        new_possibilities = season.register_guess(couples, no_correct)
        return StraightSeason(season.women, season.men, season.season_name, new_possibilities)

    def get_name_input(self):
        raw_women = self.input_output.input("enter the names of the women: \n").split(",")
        trimmed_f_names = list(map(lambda name: name.strip(), raw_women))
        raw_men = self.input_output.input("enter the names of the men: \n").split(",")
        trimmed_m_names = list(map(lambda name: name.strip(), raw_men))
        return trimmed_f_names, trimmed_m_names

    def display_scenarios(self, season):
        self.input_output.print("scenarios are")
        self.input_output.print(self.format_scenarios(season.scenarios))

    def display_probabilities(self, season, women, men):
        probabilities_calculator = ProbabilityCalculator(season.create_possible_pairings(), season.scenarios)
        hash = probabilities_calculator.calculate()
        formatter = Formatter(hash, women, men)
        self.input_output.print(formatter.printable_grid())

    def format_scenarios(self, scenarios):
        formatted_solutions = [self.format_solution(solution) for solution in scenarios]
        solutions_with_indexes = map(lambda index_and_solution: (str(index_and_solution[0] + 1), index_and_solution[1]),
                                     list(enumerate(formatted_solutions)))
        return "\n".join([": ".join(index_and_pair) for index_and_pair in solutions_with_indexes])

    def format_solution(self, solution):
        sorted_solution = sorted(list(solution), key=lambda tup: tup[0])
        return ", ".join([" + ".join(pair) for pair in sorted_solution])
