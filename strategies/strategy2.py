"""
Random strategy then discards the worst machine in each round.

This strategy randomly picks a slot machine to run for x percentage of the
trials. Then discards the machine with the worst realised expectation.
This process then continues till their is one machine left for a round.
"""

from bandits import environment, total_value, worst_machine


def strategy2(number_of_machines: int, number_of_trials: int):
    """
    Calculate value gained from strategy2.

    This strategy randomly picks a slot machine to run for x percentage of the
    trials. Then discards the machine with the worst realised expectation.
    This process then continues till their is one machine left for a round.

    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: value gained from strategy
    """
    # Calculate the number of trials per round.
    number_of_trials_per_round = int(number_of_trials / number_of_machines)

    # Initialise the environment
    machine_list = environment(number_of_machines)

    # Initialise empty list for discarded machines.
    discarded_list = []

    # Iterate through number of rounds which is equivalent to number of
    # machines.
    for i in range(number_of_machines):
        # Calculate the number of trials per machine per round.
        number_of_trials_per_machine_per_round = int(
            number_of_trials_per_round / len(machine_list))
        # Iterate through each machine.
        for j in range(len(machine_list)):
            # Run k number of trials on each machine.
            for k in range(number_of_trials_per_machine_per_round):
                machine_list[j].run()
        # Find the worst machine.
        machine_to_be_removed = machine_list[worst_machine(machine_list)]
        # Remove the machine.
        machine_list.remove(machine_to_be_removed)
        # Add it to the discarded list.
        discarded_list.append(machine_to_be_removed)

    # Calculate the total value gained.
    return total_value(discarded_list)
