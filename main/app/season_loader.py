from main.model.season import *
import glob
import re

class Loader():
    def __init__(self, season_name):
        self.season_name = season_name
        self.isBisexualSeason = self._is_bisexual_season()

    def load_all(self):
        scenarios = self.load_scenarios()
        if self.isBisexualSeason:
            return BisexualSeason(self.load_contestants(), self.season_name, scenarios)
        else:
            return StraightSeason(*self.load_contestants(), self.season_name, scenarios)

    def _is_bisexual_season(self):
        return len(glob.glob('{0}/contestants.txt'.format(self.season_name))) == 1

    def get_latest_week_number(self):
        return len(glob.glob('{0}/week*.csv'.format(self.season_name))) - 1

    def load_scenarios(self):
        week_number = self.get_latest_week_number()
        scenarios = self.read_lines_from_file("week{0}.csv".format(week_number))
        return list(self.format_scenarios(scenarios))

    def format_scenarios(self, scenarios):
        for scenario in scenarios:
            yield set([tuple(pairing.split("+")) for pairing in scenario.split(",")])

    def load_contestants(self):
        if self.isBisexualSeason:
            return self.read_lines_from_file("contestants.txt".format(self.season_name))
        else:
            return self.read_lines_from_file("women.txt"), self.read_lines_from_file("men.txt")

    def read_lines_from_file(self, filename):
        with open("{0}/{1}".format(self.season_name, filename), "r") as f:
            return f.read().splitlines()