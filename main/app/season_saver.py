from subprocess import call
import glob
import re
from main.display.input_output import InputOutputForTest
import os


class Saver():
    def __init__(self, season, new_season_name=None):
        self.season = season
        self.season_name = new_season_name or season.season_name
        self.new_week_number = self._get_new_week_number()

    def save(self):
        if self.new_week_number != 0:
            self.save_updated_season()
        else:
            self.saveNewSeason()
        return self.new_week_number

    def _get_new_week_number(self):
        return len(glob.glob("{0}/week*.csv".format(self.season_name)))

    def save_updated_season(self):
        with open("./{0}/week{1}.csv".format(self.season_name, self.new_week_number), "w") as f:
            f.write(self.scenarios_formatter())

    def saveNewSeason(self):
        os.mkdir("./{0}".format(self.season_name))
        with open("./{0}/week0.csv".format(self.season_name), "w") as f:
            f.write(self.scenarios_formatter())
        if self.season.is_bisexual_season():
           self.write_contestants("contestants.txt", self.season.contestants)
        else:
            self.write_contestants("men.txt", self.season.men)
            self.write_contestants("women.txt", self.season.women)

    def write_contestants(self, filename, contestants):
        with open("./{0}/{1}".format(self.season_name, filename), "w") as f:
            f.write('\n'.join(contestants))


    def scenarios_formatter(self):
        results = []
        for solution in self.season.scenarios:
            results.append(["+".join(pairings) for pairings in solution])
        return "\n".join([",".join(solutions) for solutions in results])
