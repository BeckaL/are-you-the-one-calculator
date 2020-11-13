from main.app.app import App
from main.display.input_output import InputForTestWithStdOut
import time

choose_to_create_season = ["1", "1"]
create_season_without_saving = ["a,b,c,d,e,f,g,h,i,j", "k,l,m,n,o,p,q,r,s,t", "n"]
enter_truth_booth = ["1", "a,k", "t"]
enter_weekly_guess = ["2", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "1"]
exit = ["4"]
instructions = choose_to_create_season + create_season_without_saving + enter_truth_booth + enter_weekly_guess + exit

input_output = InputForTestWithStdOut(instructions)


def test_initial_season_display():
    start = time.time()
    # App(input_output).main()
    end = time.time()
    duration = (end - start)
    assert duration < 300
