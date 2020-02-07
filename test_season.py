from season import *


def test_creates_all_possible_pairings():
    season = Season(["A","B"], ["X", "Y"])
    assert sorted(season.createPossiblePairings()) == sorted([("A", "X"), ("A", "Y"), ("B", "X"), ("B", "Y")])
