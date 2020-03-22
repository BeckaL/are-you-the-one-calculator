from season import *
import glob
import re

class Loader():
    def __init__(self, season_name, isBisexualSeason):
        self.season_name = season_name
        self.isBisexualSeason = isBisexualSeason

    def load_all(self):
        scenarios = self.load_scenarios()
        if self.isBisexualSeason:
            print("loading bisexual season")
            return BisexualSeason(self.load_contestants(), scenarios)
        else:
            return StraightSeason(*self.load_contestants(), scenarios)

    def get_latest_week_number(self):
        for name in glob.glob('{0}/week*.csv'.format(self.season_name)):
            return max([int(n) for n in re.findall("\d+", name)])

    def load_scenarios(self):
        week_number = self.get_latest_week_number()
        scenarios = self.read_lines_from_file("week{0}.csv".format(week_number))
        return list(self.format_scenarios(scenarios))

    def format_scenarios(self, scenarios):
        for scenario in scenarios:
            print([pairing for pairing in scenario.split(",")])
            yield set([tuple(pairing.split("+")) for pairing in scenario.split(",")])

    def load_contestants(self):
        if self.isBisexualSeason:
            print("loading contestants for a bisexual season")
            contestants = self.read_lines_from_file("contestants.txt".format(self.season_name))
            print("contestants are")
            print(contestants)

            return self.read_lines_from_file("contestants.txt".format(self.season_name))
        else:
            return self.read_lines_from_file("women.txt"), self.read_lines_from_file("men.txt")

    def read_lines_from_file(self, filename):
        with open("{0}/{1}".format(self.season_name, filename), "r") as f:
            return f.read().splitlines()