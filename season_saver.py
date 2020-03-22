from subprocess import call


class Saver():
    def __init__(self, season, seasonName, isBisexualSeason):
        self.season = season
        self.seasonName = seasonName
        self.isBisexualSeason = isBisexualSeason

    def saveNewSeason(self):
        if self.isBisexualSeason:
            call_with_args = './createNewBiSeason.sh {0}, {1}, {2}'.format(self.seasonName, self.season.scenarios, self.season.contestants)
        else:
            call_with_args = './createNewStraightSeason.sh {0}, {1}, {2}, {3}'.format(self.seasonName, self.season.scenarios, self.season.women, self.season.men)
        call(call_with_args)

