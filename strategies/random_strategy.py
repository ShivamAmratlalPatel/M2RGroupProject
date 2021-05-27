"""This strategy randomly picks a slot machine to run."""
from random import randint

from bandits import environment, total_value


def random_strategy(number_of_machines: int, number_of_trials: int):
    """
    Calculate value gained using random strategy.

    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: value gained from strategy
    """
    # Initialise the environment.
    machine_list = environment(number_of_machines)

    # Randomly pick a machine for each trial.
    for i in range(number_of_trials):
        random_machine_number = randint(0, number_of_machines - 1)
        machine_list[random_machine_number].run()

    # Calculate the total value generated.
    return total_value(machine_list)
