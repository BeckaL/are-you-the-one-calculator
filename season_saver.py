from subprocess import call
import glob
import re
from input_output import InputOutputForTest
# testStraightSeason

class Saver():
    def __init__(self, season):
        self.season = season
        self.season_name = season.season_name
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
       call(['./save_updated_scenarios.sh', self.season_name, self.scenarios_formatter(), str(self.new_week_number)])

    def saveNewSeason(self):
        if self.season.is_bisexual_season():
            call_with_args = ['./createNewBiSeason.sh', self.season_name, self.scenarios_formatter(), '\n'.join(self.season.contestants)]
        else:
            call_with_args = ['./createNewStraightSeason.sh', self.season_name, self.scenarios_formatter(), '\n'.join(self.season.women), '\n'.join(self.season.men)]
        call(call_with_args)

    def scenarios_formatter(self):
        results = []
        for solution in self.season.scenarios:
            results.append(["+".join(pairings) for pairings in solution])
        return "\n".join([",".join(solutions) for solutions in results])



