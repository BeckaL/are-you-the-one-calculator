from subprocess import call


class Saver():
    def __init__(self, season, season_name, is_bisexual_season):
        self.season = season
        self.season_name = season_name
        self.is_bisexual_season = is_bisexual_season

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



