"""Upper Confidence Bound Strategy."""
from random import random, randint

from bandits import Environment, UCBMachine, random_argmax


def ucb_strategy(number_of_machines: int, number_of_trials: int,
                 confidence_level):
    """
    Return the total value of the ucb strategy.

    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :param confidence_level: the confidence level set by user
    :return: UCB environment
    """
    # Initialise the environment
    ucb_environment = Environment(number_of_machines, True)
    ucb_environment.machine_list = []
    for i in range(number_of_machines):
        ucb_environment.machine_list.append(
            UCBMachine(expectation=random(), name="Machine " + str(i),
                       gaussian=True, confidence_level=confidence_level))

    random_machine_number = randint(0, number_of_machines - 1)
    ucb_environment.machine_list[random_machine_number].run()
    ucb_environment.update()

    for i in range(number_of_trials - 1):
        machine_to_run = random_argmax(
            [machine.sample() for machine in ucb_environment.machine_list])
        ucb_environment.machine_list[machine_to_run].run()
        ucb_environment.update()

    # Return the environment.
    return ucb_environment
