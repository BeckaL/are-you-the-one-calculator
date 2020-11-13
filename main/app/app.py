from main.model.season import *
from main.model.season_probabilities import *
from main.display.probability_formatter import *
from main.app.season_loader import Loader
from main.app.season_saver import Saver
from main.display.weekly_guess_adder import add_guess


class App():
    def __init__(self, input_output):
        self.input_output = input_output

    def main(self):
        self.input_output.print("Welcome to the AYTO calculator.")
        action_int = int(self.input_output.input(
            "Press 1 to create a new season or 2 to load an existing season:"))
        if action_int == 1:
            season = self.create_season()
            self.run(season)
        elif action_int == 2:
            season_name = (self.input_output.input("Enter the name of the season:"))
            season = Loader(season_name).load_all()
            self.input_output.print("loaded season {0}".format(season_name))
            self.display_scenarios(season)
            self.display_probabilities(season)
            self.run(season)
        else:
            return quit

    def create_season(self):
        action_int = int(self.input_output.input("Press 1 to create a straight season or 2 to create a bi season"))
        if action_int == 1:
            return self.create_straight_season()
        elif action_int == 2:
            return self.create_bi_season()

    def create_straight_season(self):
        names = self.get_name_input()
        season = StraightSeason(*names)
        self.display_scenarios(season)
        self.display_initial_probabilities(season)
        return self.save(season)

    def create_bi_season(self):
        names = self.get_bi_contestants()
        season = BisexualSeason(names)
        self.display_scenarios(season)
        self.display_initial_probabilities(season)
        return self.save(season)

    def run(self, season):
        action = self.choose_action_in_season(season)
        while action != quit:
            updated_season = action(season)
            self.display_scenarios(updated_season)
            self.display_probabilities(updated_season)
            return self.run(updated_season)
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
            if season.season_name is None:
                season_name = self.input_output.input("enter season name: ")
                season_updated_with_name = season.add_name(season_name)
                new_week_number = Saver(season_updated_with_name).save()
                self.input_output.print("Saved week {0}".format(new_week_number))
                return season_updated_with_name
            else:
                new_week_number = Saver(season).save()
                self.input_output.print("Saved week {0}".format(new_week_number))
                return season
        else:
            return season

    def add_truth_booth(self, season):
        couple = tuple(self.input_output.input("Enter couple: ").split(","))
        raw_result = self.input_output.input("Enter result (type 't' for true or 'f' for false): ")
        result = True if raw_result == "t" else False
        new_possibilities = season.register_truth_booth(couple, result)
        return season.add_updated_scenarios(new_possibilities)

    def add_weekly_guess(self, season):
        return add_guess(season, self.input_output)

    def get_name_input(self):
        raw_women = self.input_output.input("enter the names of the women: \n").split(",")
        trimmed_f_names = list(map(lambda name: name.strip(), raw_women))
        raw_men = self.input_output.input("enter the names of the men: \n").split(",")
        trimmed_m_names = list(map(lambda name: name.strip(), raw_men))
        return trimmed_f_names, trimmed_m_names

    def get_bi_contestants(self):
        raw_contestants= self.input_output.input("enter the names of the contestants: \n").split(",")
        return list(map(lambda name: name.strip(), raw_contestants))

    def display_scenarios(self, season):
        len_scenarios = len(season.scenarios)
        if len_scenarios > 100:
            self.input_output.print("number of scenarios is {0}".format(len_scenarios))
        else:
            self.input_output.print("scenarios are")
            self.input_output.print(self.format_scenarios(season.scenarios))

    def display_probabilities(self, season):
        probabilities_calculator = ProbabilityCalculator(season.create_possible_pairings(), season.scenarios)
        hash = probabilities_calculator.calculate()
        if season.is_bisexual_season():
            formatter = BiFormatter(hash, season.contestants)
        else:
            formatter = Formatter(hash, season.women, season.men)
        self.input_output.print(formatter.printable_grid())

    def display_initial_probabilities(self, season):
        probabilities_calculator = ProbabilityCalculator(season.create_possible_pairings(), season.scenarios)
        if season.is_bisexual_season():
            formatter = BiFormatter(
                probabilities_calculator.calculate_initial_probabilities_bi_season(len(season.contestants)),
                season.contestants)
        else:
            formatter = Formatter(
                probabilities_calculator.calculate_initial_probabilities_straight_season(len(season.women)), season.women,
                season.men)
        self.input_output.print(formatter.printable_grid())

    def format_scenarios(self, scenarios):
        formatted_solutions = [self.format_solution(solution) for solution in scenarios]
        solutions_with_indexes = map(lambda index_and_solution: (str(index_and_solution[0] + 1), index_and_solution[1]),
                                     list(enumerate(formatted_solutions)))
        return "\n".join([": ".join(index_and_pair) for index_and_pair in solutions_with_indexes])

    def format_solution(self, solution):
        sorted_solution = sorted(list(solution), key=lambda tup: tup[0])
        return ", ".join([" + ".join(pair) for pair in sorted_solution])
