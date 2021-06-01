"""
"""
from random import randint
from random import random

from bandits import total_value, ThompsonMachine, random_argmax


def thompson_sampling(number_of_machines: int, number_of_trials: int):
    """


    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: value gained from strategy
    """
    # Initialise the environment
    # Initialise empty machine list
    machine_list = []
    # Add n machines with a random expectation.
    for i in range(number_of_machines):
        machine_list.append(
            ThompsonMachine(expectation=random(), name="Machine " + str(i)))

    random_machine_number = randint(0, number_of_machines - 1)
    machine_list[random_machine_number].run()

    for i in range(number_of_trials - 1):
        machine_to_run = random_argmax(
            [machine.sample() for machine in machine_list])
        machine_list[machine_to_run].run()

    # Print the total value gained.
    return total_value(machine_list)
