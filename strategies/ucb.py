"""Upper Confidence Bound Strategy."""

from bandits import environment


def ucb(number_of_machines: int, number_of_trials: int):
    """
    Return the total value of the ucb strategy.

    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: value gained from strategy
    """
    # Initialise the environment
    machine_list = environment(number_of_machines, True)

    # Return the machine list
    return machine_list
