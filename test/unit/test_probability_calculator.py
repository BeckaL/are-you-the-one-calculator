from main.model.season_probabilities import *


def test_calculates_probabilities_for_all_pairings():
    pairings = [("A", "X"), ("A", "Y"), ("A", "Z"),
                ("B", "X"), ("B", "Y"), ("B", "Z"),
                ("C", "X"), ("C", "Y"), ("C", "Z")
                ]
    scenarios = [
        {("A", "X"), ("B", "Y"), ("C", "Z")},
        {("A", "X"), ("B", "Z"), ("C", "Y")},
        {("A", "Y"), ("B", "X"), ("C", "Z")},
        {("A", "Y"), ("B", "Z"), ("C", "X")},
        {("A", "Z"), ("B", "X"), ("C", "Y")},
        {("A", "Z"), ("B", "Y"), ("C", "X")}
    ]
    expected_probabilities = {
        ("A", "X"): 0.33, ("A", "Y"): 0.33, ("A", "Z"): 0.33,
        ("B", "X"): 0.33, ("B", "Y"): 0.33, ("B", "Z"): 0.33,
        ("C", "X"): 0.33, ("C", "Y"): 0.33, ("C", "Z"): 0.33}
    calc = ProbabilityCalculator(pairings, scenarios)
    assert calc.calculate() == expected_probabilities

