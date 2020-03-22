from season_loader import *


def test_loads_a_season():
    seasonName = "testStraightSeason"
    isBiSeries = False
    loader = Loader(seasonName, isBiSeries)
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


def straight_season_equality(expected, actual):
    print(expected.scenarios)
    print(actual.scenarios)
    return all([expected.men == actual.men, expected.women == actual.women, expected.scenarios == actual.scenarios])
