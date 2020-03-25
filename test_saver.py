from season import BisexualSeason, StraightSeason
from season_saver import Saver
import glob
from subprocess import call


def test_saves_a_new_bi_season():
    season_name = "saver_test_1_season"
    clean_up_files(season_name)

    season = BisexualSeason(
        contestants=['A', 'B', 'C', 'D'],
        scenarios=[{('A', 'B'), ('C', 'D')}, {('A', 'C'), ('B', 'D')}])
    saver = Saver(season=season, is_bisexual_season=True, season_name=season_name)
    saver.saveNewSeason()
    assert (files_are_present(season_name))


def test_saves_a_new_straight_season():
    season_name = "saver_test_2_season"
    clean_up_files(season_name)

    season = StraightSeason(
        women=['A', 'B'],
        men=['C', 'D'],
        scenarios=[{('A', 'B'), ('C', 'D')}, {('A', 'D'), ('C', 'B')}])
    saver = Saver(season=season, is_bisexual_season=False, season_name=season_name)
    saver.saveNewSeason()
    assert (files_are_present(season_name))


def files_are_present(season_name):
    week_files = count_files_matching(season_name, "week*.csv")
    contestant_files = count_files_matching(season_name, 'contestants.txt')
    men_files = count_files_matching(season_name, 'men.txt')
    women_files = count_files_matching(season_name, 'women.txt')
    return week_files == 1 and (contestant_files == 1 or (men_files == 1 and women_files == 1))


def count_files_matching(season_name, file):
    return len(glob.glob('{0}/{1}'.format(season_name, file)))


def clean_up_files(season_name):
    call(['rm', '-rf', season_name])
    assert not files_are_present(season_name)
