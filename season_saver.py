from subprocess import call
import glob
import re


class Saver():
    def __init__(self, season, season_name, is_bisexual_season):
        self.season = season
        self.season_name = season_name
        self.is_bisexual_season = is_bisexual_season
        self.new_week_number = self._get_new_week_number()

    def save(self):
        if self.new_week_number != 0:
            return self.save_updated_season()
        else:
            return self.saveNewSeason()

    def _get_new_week_number(self):
        return len(glob.glob("{0}/week*.csv".format(self.season_name)))

    def save_updated_season(self):
       call(['./save_updated_scenarios.sh', self.season_name, self.scenarios_formatter(), str(self.new_week_number)])

    def saveNewSeason(self):
        if self.is_bisexual_season:
            call_with_args = ['./createNewBiSeason.sh', self.season_name, self.scenarios_formatter(), '\n'.join(self.season.contestants)]
        else:
            call_with_args = ['./createNewStraightSeason.sh', self.season_name, self.scenarios_formatter(), '\n'.join(self.season.women), '\n'.join(self.season.men)]
        call(call_with_args)

    def scenarios_formatter(self):
        results = []
        for solution in self.season.scenarios:
            results.append(["+".join(pairings) for pairings in solution])
        return "\n".join([",".join(solutions) for solutions in results])



