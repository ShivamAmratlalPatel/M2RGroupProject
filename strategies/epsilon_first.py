"""
Random strategy then exploit best machine.

This strategy randomly picks a slot machine to run for half the trials.
Then runs the machine with the highest realised expectation for the rest of the
trials.
"""

from random import randint

from bandits import environment, total_value, best_machine


def epsilon_first(number_of_machines: int, number_of_trials: int):
    """
    Calculate value gained using strategy1.

    This strategy randomly picks a slot machine to run for half the trials.
    Then runs the machine with the highest realised expectation for the rest
    of the trials.

    :type number_of_trials: int
    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: value gained from strategy
    """
    # Initialise the environment
    machine_list = environment(number_of_machines, True)

    # Do half the number of trials randomly.
    for i in range(int(number_of_trials / 2)):
        random_machine_number = randint(0, number_of_machines - 1)
        machine_list[random_machine_number].run()

    # Calculate the best machine
    best_machine_index = best_machine(machine_list)

    # Do the rest of the trials on the final half.
    for i in range(int(number_of_trials / 2)):
        machine_list[best_machine_index].run()

    # Print the total value gained.
    return total_value(machine_list)
