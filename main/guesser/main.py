import time
from main.model.season_probabilities import ProbabilityCalculator
from main.display.probability_formatter import BiFormatter
from main.game_controller.controller import BisexualController, bisexual_contestants
from main.guesser.bisexual_season_guesser import BisexualGuesser
from main.guesser.guess_generator import Basic_Guess_Generator, Highest_Probability_Guess_Generator

if __name__ == "__main__":
    start_time = time.time()
    calculator = ProbabilityCalculator
    controller = BisexualController(contestants=bisexual_contestants[0:8])
    guesser = BisexualGuesser(controller, calculator, BiFormatter, Basic_Guess_Generator())
    guesser.run()
    print("--- completed in {:.3f} seconds ---".format(time.time() - start_time))
