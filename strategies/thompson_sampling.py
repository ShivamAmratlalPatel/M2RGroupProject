"""
Strategy uses the best possible machine given a probability.

This strategy uses a prior distribution of a uniform distribution and
computes beta posterior distributions. It then picks the beta distribution
which would give the chance of the highest value.
"""
from random import randint, random

from bandits import ThompsonMachine, random_argmax, Environment


def thompson_sampling_strategy(number_of_machines: int, number_of_trials: int,
                               means: list, gaussian: bool):
    """
    Return the total value of the thompson sampling strategy.

    :param means: list of means if being used
    :param gaussian: whether to use gaussian or Bernoulli distribution
    :param number_of_machines: number of slot machines
    :param number_of_trials: total number of trials
    :return: thompson environment
    """
    if len(means) != number_of_machines:
        means = [random() for i in range(number_of_machines)]
        print("error with means in thompson strategy")
    # Initialise the environment
    thompson_environment = Environment(number_of_machines, means, gaussian)
    thompson_environment.machine_list = []
    for i in range(number_of_machines):
        thompson_environment.machine_list.append(
            ThompsonMachine(expectation=random(), name="Machine " + str(i),
                            gaussian=gaussian))

    random_machine_number = randint(0, number_of_machines - 1)
    thompson_environment.machine_list[random_machine_number].run()
    thompson_environment.update()

    for i in range(number_of_trials - 1):
        machine_to_run = random_argmax(
            [machine.sample() for machine in
             thompson_environment.machine_list])
        thompson_environment.machine_list[machine_to_run].run()
        thompson_environment.update()

    # Return the environment.
    return thompson_environment
