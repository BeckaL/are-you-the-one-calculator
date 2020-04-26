from main.model.couples_deriver import CouplesDeriver

def test_derives_no_matches_from_a_weekly_guess():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 2)]
    confirmed_matches = [('A', 'B'), ('E', 'F')]
    confirmed_no_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_no_matches": {('G', 'H'), ('I', 'J')}, "derived_matches": set()})

def test_does_not_derive_where_not_enough_information_is_available():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 2)]
    confirmed_matches = [('A', 'B')]
    confirmed_no_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_matches": set(), "derived_no_matches": set()})

def test_derives_information_across_multiple_weeks():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 2),
                      ([('A', 'B'), ('C', 'F'), ('E', 'G'), ('D', 'H'), ('I', 'J')], 2)]
    confirmed_matches = [('A', 'B'), ('E', 'F'), ('E', 'G')]
    confirmed_no_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_no_matches": {('G', 'H'), ('I', 'J'), ('C', 'F'), ('D', 'H')}, "derived_matches" : set()})


def test_derives_matches_from_a_weekly_guess():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 3)]
    confirmed_no_matches = [('A', 'B'), ('E', 'F')]
    confirmed_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_matches": {('G', 'H'), ('I', 'J')}, "derived_no_matches": set()})

def test_derives_matches_across_multiple_weeks():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 2),
                      ([('A', 'E'), ('C', 'D'), ('B', 'H'), ('G', 'J'), ('I', 'F')], 2)]
    confirmed_no_matches = [('A', 'B'), ('E', 'F'), ('G', 'H'), ('G', 'J'), ('I', 'F'), ('B', 'H')]
    confirmed_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_matches": {('I', 'J'), ('A', 'E')}, "derived_no_matches": set()})

def test_derives_matches_across_multiple_week_using_derived_information():
    weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 3),
                      ([('A', 'E'), ('C', 'D'), ('B', 'F'), ('G', 'H'), ('I', 'J')], 3)]
    confirmed_no_matches = [('A', 'B'), ('E', 'F')]
    confirmed_matches = [('C', 'D')]
    deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
    assert(deriver.derive() == {"derived_matches": {('G', 'H'), ('I', 'J')}, "derived_no_matches": {('A', 'E'), ('B', 'F')}})


#
# def test_derives_matches_across_multiple_week_using_derived_information():
#     weekly_guesses = [([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')], 3),
#                       ([('A', 'E'), ('C', 'D'), ('B', 'F'), ('G', 'J'), ('I', 'H')], 3)]
#     confirmed_no_matches = [('A', 'B'), ('E', 'F')]
#     confirmed_matches = [('C', 'D')]
#     deriver = CouplesDeriver(weekly_guesses, confirmed_matches, confirmed_no_matches)
#     assert(deriver.derive() == {"derived_matches": {('G', 'H'), ('I', 'J'), ('A', 'E'), ('B', 'F')}, "derived_no_matches": set()})
#
