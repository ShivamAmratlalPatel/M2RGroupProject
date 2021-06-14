"""Strategy randomly picks a slot machine to run."""
from random import randint

from random import random

from bandits import Environment


def random_strategy_calculator(number_of_machines: int, number_of_trials: int,
                               means: list, gaussian=False, ):
    """
    Calculate value gained using random strategy.

    :param gaussian: whether to use gaussian or Bernoulli distribution
    :param number_of_machines: number of slot machines
    :param means: list of the means of the machine
    :param number_of_trials: total number of trials
    :return: random strategy environment
    """
    if len(means) != number_of_machines:
        means = [random() for i in range(number_of_machines)]
        print("error with means in random strategy")
    # Initialise the environment.
    random_environment = Environment(number_of_machines, means, gaussian)

    # Randomly pick a machine for each trial.
    for i in range(number_of_trials):
        random_machine_number: int = randint(0, number_of_machines - 1)
        random_environment.machine_list[random_machine_number].run()
        random_environment.update()

    # Return environment
    return random_environment
