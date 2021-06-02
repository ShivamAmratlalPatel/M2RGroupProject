"""This file creates the Machine class which emulates a slot machine."""
from random import random

import numpy as np
from scipy.stats import norm, bernoulli


class Machine:
    """Create the machine class."""

    def __init__(self, expectation: float, name: str, gaussian: bool):
        """Initialize the class.

        :param expectation: actual expectation for realisations
        :param name: name of the machine
        :param gaussian: whether to use gaussian distribution or not
        """
        # Assigning values to class values.
        self.expectation = expectation
        self.realisations = []
        self.name = name
        self.gaussian = gaussian
        self.regret = []

    def run(self):
        """Return a  realisation of the machine if run."""
        # Running a bernoulli trial
        if self.gaussian:
            realisation = norm.pdf(0, loc=self.expectation, scale=5)
            if realisation > 0:
                self.realisations.append(realisation)
            else:
                self.realisations.append(0)
        else:
            self.realisations.append(bernoulli.rvs(size=1, p=self.expectation))

    def realised_expectation(self):
        """Return the realised expectation."""
        # Try to calculate the realised expectations.
        try:
            return sum(self.realisations) / len(self.realisations)
        except ZeroDivisionError:
            # If there have been no realisations
            # then return 0 rather than error.
            return 0

    def __repr__(self):
        """Return the name of the machine."""
        # May need to be changed in future to give a more detailed response.
        return self.name

    def __str__(self):
        """Return the name of the machine."""
        return self.name


class ThompsonMachine(Machine):
    """
    Create a machine to be used specifically for the Thompson strategy.

    This creates the same machine but also gives it alpha and beta
    attributes which are the number of successes and fails respectively.
    """

    def __init__(self, expectation: float, name: str, gaussian: bool):
        """Initialise the machine."""
        super(ThompsonMachine, self).__init__(expectation, name, gaussian)
        self.alpha = 1
        self.beta = 1
        self.n = 0

    def run(self):
        """Return a  realisation of the machine if run."""
        self.n += 1
        super(ThompsonMachine, self).run()
        if self.realisations[-1] > 0:
            self.alpha += 1
        else:
            self.beta += 1

    def sample(self):
        """Return a value sampled from the beta distribution."""
        return np.random.beta(self.alpha, self.beta)

    def realised_expectation(self):
        super(ThompsonMachine, self).realised_expectation()


class UCBMachine(Machine):
    def __init__(self, confidence_level, expectation: float, name: str,
                 gaussian: bool):
        super(UCBMachine, self).__init__(expectation, name, gaussian)
        self.confidence_level = confidence_level
        self.uncertainty = float('inf')

    def run(self):
        super(UCBMachine, self).run()
        self.uncertainty = self.confidence_level * (np.sqrt(
            np.log(len(self.realisations) + 1) / len(self.realisations)))

    def realised_expectation(self):
        return super(UCBMachine, self).realised_expectation()

    def sample(self):
        return self.realised_expectation() + self.uncertainty


def regret(machine_list):
    """Calculate the regret from a list of machines."""
    expectation_list = []
    mean_machines = []
    trial_numbers = []
    for machine in machine_list:
        expectation = machine.expectation
        trial_numbers.append(len(machine.realisations))
        expectation_list.append(float(sum(machine.realisations)))
        mean_machines.append(expectation)

    highest_mean: float = max(mean_machines)
    number_of_trials: int = sum(trial_numbers)
    sum_of_expectations_times_means: float = sum(expectation_list)

    return highest_mean * number_of_trials - sum_of_expectations_times_means


class Environment:
    def __init__(self, n: int, gaussian=False):
        self.machine_list = []
        for i in range(n):
            self.machine_list.append(
                Machine(expectation=random(), name="Machine " + str(i),
                        gaussian=gaussian))
        self.regret = []

    def update(self):
        self.regret.append(regret(self.machine_list))


def uncertainty(machine: Machine, confidence_level, t):
    """
    Calculate the uncertainty in the estimate of this socket's mean.

    :param machine: machine for uncertainty to be calculated for
    :param confidence_level: confidence level set by user
    :param t: current time step
    :return: the uncertainty of machine at time t
    """
    if machine.realised_expectation() == 0:
        return float('inf')
    return confidence_level * (np.sqrt(np.log(t) / len(machine.realisations)))


def total_value(machine_list: list):
    """Calculate the value gained given a list of machines.

    :param machine_list: list of machines
    :return the total value gained from the machines
    """
    # Sums all the values of all the machines in a list.
    machine_values = [sum(i.realisations) for i in machine_list]
    return int(sum(machine_values))


def best_machine(machine_list: list):
    """
    Calculate the machine with the highest realised expectation.

    :param machine_list:
    :return: the index of the machine with the highest realised expectation
    """
    # Create a list of all the realised expectations.
    # Should implement a check if any of the machines have not had any trials.
    realised_expectations = [machine.realised_expectation() for machine in
                             machine_list]
    # Return the index of the max of these realised expectations.
    return realised_expectations.index(max(realised_expectations))


def worst_machine(machine_list: list):
    """
    Calculate the machine with the lowest realised expectation.

    :param machine_list:
    :return: the index of the machine with the lowest realised expectation
    """
    # Create a list of all the realised expectations.
    # Should implement a check if any of the machines have not had any trials.
    realised_expectations = [machine.realised_expectation() for machine in
                             machine_list]
    # Return the index of the min of these realised expectations.
    return realised_expectations.index(min(realised_expectations))


def random_argmax(value_list):
    """Return the maximum machine for Thompson strategy."""
    values = np.asarray(value_list)
    return np.argmax(
        np.random.random(values.shape) * (values == values.max(initial=1)))
