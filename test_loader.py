from season_loader import *


def test_loads_a_straight_season():
    loader = Loader(season_name="testStraightSeason", isBisexualSeason=False)
    actual_season = loader.load_all()
    expected_season = StraightSeason(
        women = ['C', 'D'],
        men = ['A', 'B'],
        scenarios = [
            {('A', 'B'), ('C', 'D')},
            {('A', 'D'), ('C', 'B')}
        ]
    )
    assert (straight_season_equality(expected_season, actual_season))


def test_loads_a_bi_season():
    loader = Loader(season_name="testBiSeason", isBisexualSeason=True)
    actual_season = loader.load_all()
    expected_season = BisexualSeason(
        contestants=['A', 'B', 'C', 'D'],
        scenarios=[
            {('A', 'B'), ('C', 'D')},
            {('A', 'D'), ('C', 'B')},
            {('A', 'C'), ('B', 'D')}
        ]
    )
    assert (bi_season_equality(expected_season, actual_season))


def straight_season_equality(expected, actual):
    return all([expected.men == actual.men, expected.women == actual.women, expected.scenarios == actual.scenarios])

def bi_season_equality(expected, actual):
    return all([expected.contestants == actual.contestants, expected.scenarios == actual.scenarios])