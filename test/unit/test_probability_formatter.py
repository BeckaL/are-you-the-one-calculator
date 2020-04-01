from main.display.probability_formatter import BiFormatter


def test_formats_for_one_character_names():
    probabilities = {('A', 'B'): 0.33, ('A', 'C'): 0.33, ('A', 'D'): 0.33, ('B', 'C'): 0.33, ('B', 'D'): 0.33,
                     ('C', 'D'): 0.33}
    formatter = BiFormatter(probabilities, ["A", "B", "C", "D"])
    print(formatter.printable_grid())
    expected_grid = "    A      B      C      D     \n" \
                    "A   x     0.33   0.33   0.33 \n" \
                    "B  0.33    x     0.33   0.33 \n" \
                    "C  0.33   0.33    x     0.33 \n" \
                    "D  0.33   0.33   0.33    x   "
    assert (formatter.printable_grid() == expected_grid)


def test_formats_for_multi_character_names():
    probabilities = {('Anthony', 'Bernadette'): 0.33, ('Anthony', 'C'): 0.33, ('Anthony', 'Dee'): 0.33, ('Bernadette', 'C'): 0.33, ('Bernadette', 'Dee'): 0.33,
                     ('C', 'Dee'): 0.33}
    formatter = BiFormatter(probabilities, ["Anthony", "Bernadette", "C", "Dee"])
    print(formatter.printable_grid())
    expected_grid = "            Anthony   Bernadette    C     Dee    \n" \
                    "Anthony       x          0.33      0.33   0.33 \n" \
                    "Bernadette   0.33         x        0.33   0.33 \n" \
                    "C            0.33        0.33       x     0.33 \n" \
                    "Dee          0.33        0.33      0.33    x   "
    print(expected_grid)
    assert (formatter.printable_grid() == expected_grid)