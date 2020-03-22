from season import *
import glob
import re

class Loader():
    def __init__(self, season_name, isBisexualSeason):
        self.season_name = season_name
        self.isBisexualSeason = isBisexualSeason

    def load_all(self):
        if self.isBisexualSeason:
            pass
        else:
            scenarios = self.load_scenarios()
            women, men = self.load_contestants()
            return StraightSeason(women, men, scenarios)

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
            return self.read_lines_from_file("contestants.txt".format(self.season_name))
        else:
            return self.read_lines_from_file("women.txt"), self.read_lines_from_file("men.txt")

    def read_lines_from_file(self, filename):
        with open("{0}/{1}".format(self.season_name, filename), "r") as f:
            return f.read().splitlines()


l = Loader("testStraightSeason", False)
print(l.load_contestants())
print(l.load_scenarios())

l = Loader("testBiSeason", True)
print(l.load_contestants())