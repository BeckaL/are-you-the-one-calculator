from main.app.app import App
from main.display.input_output import InputOutputForTest
import glob
from subprocess import call

choose_to_load_season = ["2", "testBiSeason"]
enter_weekly_guess = ["2", "A+D,C+B", "2"]
enter_truth_booth = ["1", "A,D", "t"]
save = ["3", "y"]
exit = ["4"]
instructions = choose_to_load_season + enter_weekly_guess + save + exit

input_output = InputOutputForTest(instructions)

App(input_output).main()


def test_initial_season_display():
    welcome_message = "Welcome to the AYTO calculator."
    load_confirmation = "loaded season testBiSeason"
    scenarios_introductory_text = "scenarios are"
    initial_scenario_output = '1: A + B, C + D\n' \
                              '2: A + D, C + B\n' \
                              '3: A + C, B + D'
    initial_probability_table = '   A      B      C      D\n' \
                                'A   x     0.33   0.33   0.33 \n' \
                                'B  0.33    x     0.33   0.33 \n' \
                                'C  0.33   0.33    x     0.33 \n' \
                                'D  0.33   0.33   0.33    x   '

    assert (input_output.output[:5] ==
            [welcome_message, load_confirmation, scenarios_introductory_text, initial_scenario_output,
             initial_probability_table])
    _clean_up_files("testBiSeason")


def test_display_after_truth_booth():
    scenarios_introductory_text = "scenarios are"
    scenario_output_after_truth_booth = '1: A + D, C + B'
    probability_table_after_truth_booth = '   A      B      C      D\n' \
                                          'A   x     0.0    0.0    1.0  \n' \
                                          'B  0.0     x     1.0    0.0  \n' \
                                          'C  0.0    1.0     x     0.0  \n' \
                                          'D  1.0    0.0    0.0     x   '
    assert (input_output.output[5:8] ==
            [scenarios_introductory_text, scenario_output_after_truth_booth, probability_table_after_truth_booth])


def test_saves():
    assert (input_output.output[8] == "Saved week 1")


def test_quits_after_showing_possibilties_again():
    _clean_up_files("testBiSeason")
    assert ("goodbye" in input_output.output)


#
def _clean_up_files(season_name):
    files = [file for file in glob.glob("{0}/week*.csv".format(season_name)) if
             file != "{0}/week0.csv".format(season_name)]
    for file in files:
        call(['rm', file])
