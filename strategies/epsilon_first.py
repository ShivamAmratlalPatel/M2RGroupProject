"""
Random strategy then exploit best machine.

This strategy randomly picks a slot machine to run for half the trials.
Then runs the machine with the highest realised expectation for the rest of the
trials.
"""

from random import randint

from bandits import Environment, best_machine


def epsilon_first_strategy(number_of_machines: int, number_of_trials: int,
                           epsilon=0.06):
    """
    Calculate value gained using strategy1.

    This strategy randomly picks a slot machine to run for half the trials.
    Then runs the machine with the highest realised expectation for the rest
    of the trials.

    :type number_of_trials: int
    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: environment of testing
    """
    # Initialise the environment.
    epsilon_environment = Environment(number_of_machines, False)

    # Do half the number of trials randomly.
    for i in range(int(number_of_trials * epsilon)):
        random_machine_number = randint(0, number_of_machines - 1)
        epsilon_environment.machine_list[random_machine_number].run()
        epsilon_environment.update()

    # Calculate the best machine.
    best_machine_index = best_machine(epsilon_environment.machine_list)

    # Do the rest of the trials on the final half.
    for i in range(int(number_of_trials * (1 - epsilon))):
        epsilon_environment.machine_list[best_machine_index].run()
        epsilon_environment.update()

    # Return the environment.
    return epsilon_environment
