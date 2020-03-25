from season import BisexualSeason, StraightSeason
from season_saver import Saver
import glob
from subprocess import call


def test_saves_a_new_bi_season():
    season_name = "saver_test_1_season"
    _clean_up_files(season_name)

    _save_new_bisexual_season(season_name)
    assert (_files_are_present(season_name))
    _clean_up_files(season_name)


def test_saves_a_new_straight_season():
    season_name = "saver_test_2_season"
    _clean_up_files(season_name)

    _save_new_straight_season(season_name)
    assert (_files_are_present(season_name))
    _clean_up_files(season_name)


def test_saves_latest_results_of_bi_season():
    season_name = "bisexual_season_updater_1"
    _clean_up_files(season_name)

    _save_new_bisexual_season(season_name)
    updated_season = BisexualSeason(contestants=['A', 'B', 'C', 'D'],
                                    season_name=season_name,
                                    scenarios=[{('A', 'B'), ('C', 'D')}])
    Saver(updated_season).save()
    assert (_files_are_present(season_name, week=1))
    _clean_up_files(season_name)


def test_saves_latest_results_of_straight_season():
    season_name = "straight_season_updater_1"
    _clean_up_files(season_name)

    _save_new_straight_season(season_name)
    updated_season = StraightSeason(women=['A', 'B'],
                                    men=['C', 'D'],
                                    season_name=season_name,
                                    scenarios=[{('A', 'B'), ('C', 'D')}])
    Saver(updated_season).save()
    assert (_files_are_present(season_name, week=1))
    _clean_up_files(season_name)


def _files_are_present(season_name, week=0):
    week_files = _count_files_matching(season_name, "week{0}.csv".format(week))
    contestant_files = _count_files_matching(season_name, 'contestants.txt')
    men_files = _count_files_matching(season_name, 'men.txt')
    women_files = _count_files_matching(season_name, 'women.txt')
    return week_files == 1 and (contestant_files == 1 or (men_files == 1 and women_files == 1))


def _count_files_matching(season_name, file):
    return len(glob.glob('{0}/{1}'.format(season_name, file)))


def _save_new_bisexual_season(season_name):
    season = BisexualSeason(
        contestants=['A', 'B', 'C', 'D'],
        season_name = season_name,
        scenarios=[{('A', 'B'), ('C', 'D')}, {('A', 'C'), ('B', 'D')}])
    Saver(season).save()


def _clean_up_files(season_name):
    call(['rm', '-rf', season_name])
    assert not _files_are_present(season_name)


def _save_new_straight_season(season_name):
    season = StraightSeason(
        women=['A', 'B'],
        men=['C', 'D'],
        season_name=season_name,
        scenarios=[{('A', 'B'), ('C', 'D')}, {('A', 'D'), ('C', 'B')}])
    saver = Saver(season)
    saver.save()
