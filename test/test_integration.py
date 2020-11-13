from main.app.app import App
from main.display.input_output import InputOutputForTest

choose_to_create_season = ["1", "1"]
create_season_without_saving = ["a,b,c", "d,e,f", "n"]
enter_truth_booth = ["1", "a,d", "t"]
enter_weekly_guess = ["2", "d", "e", "f", "1"]
exit = ["4"]
instructions = choose_to_create_season + create_season_without_saving + enter_truth_booth + enter_weekly_guess + exit


input_output = InputOutputForTest(instructions)

App(input_output).main()


def test_initial_season_display():
    welcome_message = "Welcome to the AYTO calculator."
    scenarios_introductory_text = "scenarios are"
    initial_scenario_output = '1: a + d, b + e, c + f\n' \
                              '2: a + d, b + f, c + e\n' \
                              '3: a + e, b + d, c + f\n' \
                              '4: a + f, b + d, c + e\n' \
                              '5: a + e, b + f, c + d\n' \
                              '6: a + f, b + e, c + d'
    initial_probability_table = '    d      e      f     \n' \
                                'a  0.33   0.33   0.33 \n' \
                                'b  0.33   0.33   0.33 \n' \
                                'c  0.33   0.33   0.33 '
    assert (input_output.output[:4] ==
            [welcome_message, scenarios_introductory_text, initial_scenario_output, initial_probability_table])


def test_display_after_truth_booth():
    scenarios_introductory_text = "scenarios are"
    scenario_output_after_truth_booth = '1: a + d, b + e, c + f\n' \
                                        '2: a + d, b + f, c + e'
    probability_table_after_truth_booth = '    d      e      f     \n' \
                                          'a  1.0    0.0    0.0  \n' \
                                          'b  0.0    0.5    0.5  \n' \
                                          'c  0.0    0.5    0.5  '
    assert (input_output.output[4:7] ==
            [scenarios_introductory_text, scenario_output_after_truth_booth, probability_table_after_truth_booth])


def test_display_after_weekly_guess():
    scenarios_introductory_text = "scenarios are"
    scenario_output_after_weekly_guess = '1: a + d, b + f, c + e'
    probability_table_after_weekly_guess = '    d      e      f     \n' \
                                           'a  1.0    0.0    0.0  \n' \
                                           'b  0.0    0.0    1.0  \n' \
                                           'c  0.0    1.0    0.0  '
    assert (input_output.output[7:10] ==
            [scenarios_introductory_text, scenario_output_after_weekly_guess, probability_table_after_weekly_guess])


def test_quits():
    assert (input_output.output[10] == "goodbye")
    assert (len(input_output.output) == 11)
