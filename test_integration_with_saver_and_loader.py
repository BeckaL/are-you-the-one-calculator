from app import App
from input_output import InputOutputForTest

choose_to_load_season = ["2", "testStraightSeason"]
enter_truth_booth = ["1", "A,D", "t"]
enter_weekly_guess = ["2", "B", "D", "2"]
exit = ["3"]
instructions = choose_to_load_season + enter_truth_booth + enter_weekly_guess + exit

input_output = InputOutputForTest(instructions)

App(input_output).main()

def test_initial_season_display():
    welcome_message = "Welcome to the AYTO calculator."
    load_confirmation = "loaded season testStraightSeason"
    scenarios_introductory_text = "scenarios are"
    initial_scenario_output = '1: A + C, B + D\n' \
                              '2: A + D, B + C'
    initial_probability_table = '   A      B\n' \
                                'C  0.5    0.5  \n' \
                                'D  0.5    0.5  '

    assert (input_output.output[:5] ==
            [welcome_message, load_confirmation, scenarios_introductory_text, initial_scenario_output, initial_probability_table])
