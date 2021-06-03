"""This strategy randomly picks a slot machine to run."""
from random import randint

from bandits import Environment


def random_strategy_calculator(number_of_machines: int, number_of_trials: int):
    """
    Calculate value gained using random strategy.

    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: random strategy environment
    """
    # Initialise the environment.
    random_environment = Environment(number_of_machines, False)

    # Randomly pick a machine for each trial.
    for i in range(number_of_trials):
        random_machine_number: int = randint(0, number_of_machines - 1)
        random_environment.machine_list[random_machine_number].run()
        random_environment.update()

    # Return environment
    return random_environment
