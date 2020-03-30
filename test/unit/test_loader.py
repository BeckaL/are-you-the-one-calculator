from main.app.season_loader import *


def test_loads_a_straight_season():
    season_name = "testStraightSeason"
    loader = Loader(season_name=season_name)
    actual_season = loader.load_all()
    expected_season = StraightSeason(
        women = ['A', 'B'],
        men = ['C', 'D'],
        season_name=season_name,
        scenarios = [
            {('A', 'C'), ('B', 'D')},
            {('A', 'D'), ('B', 'C')}
        ]
    )
    assert (straight_season_equality(expected_season, actual_season))


def test_loads_a_bi_season():
    loader = Loader(season_name="testBiSeason")
    actual_season = loader.load_all()
    expected_season = BisexualSeason(
        contestants=['A', 'B', 'C', 'D'],
        season_name="testBiSeason",
        scenarios=[
            {('A', 'B'), ('C', 'D')},
            {('A', 'D'), ('C', 'B')},
            {('A', 'C'), ('B', 'D')}
        ]
    )
    assert (bi_season_equality(expected_season, actual_season))


def straight_season_equality(expected, actual):
    return all([expected.season_name == actual.season_name, expected.men == actual.men, expected.women == actual.women, expected.scenarios == actual.scenarios])

def bi_season_equality(expected, actual):
    return all([expected.season_name == actual.season_name, expected.contestants == actual.contestants, expected.scenarios == actual.scenarios])