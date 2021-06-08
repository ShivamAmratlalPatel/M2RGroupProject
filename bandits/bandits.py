"""This file creates the Machine class which emulates a slot machine."""
from random import random

import numpy as np
from scipy.stats import bernoulli


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
        if gaussian:
            self.expectation = expectation
        self.realisations = []
        self.name = name
        self.gaussian = gaussian
        self.regret = []

    def run(self):
        """Return a  realisation of the machine if run."""
        # Running a bernoulli trial
        if self.gaussian:
            sigma = 1
            realisation = sigma * np.random.randn() + self.expectation
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
        self.gaussian = gaussian
        if self.gaussian:
            self.variance = 1
            self.tao_0 = 1 / self.variance
            self.mean = 0

    def run(self):
        """Return a  realisation of the machine if run."""
        self.n += 1
        super(ThompsonMachine, self).run()
        if self.gaussian:
            self.tao_0 += self.n
            self.mean = (self.tao_0 * self.mean + (1 / self.variance) * sum(
                self.realisations)) / (
                                self.tao_0 + self.n * (1 / self.variance))
        else:
            if self.realisations[-1] > 0:
                self.alpha += 1
            else:
                self.beta += 1

    def sample(self):
        """Return a value sampled from the beta distribution."""
        if self.gaussian:
            if len(self.realisations) == 0:
                return 0
            else:
                return (np.random.randn() / np.sqrt(self.tao_0)) + self.mean
        else:
            return np.random.beta(self.alpha, self.beta)

    def realised_expectation(self):
        """Return the realised expectation of the machine."""
        return super(ThompsonMachine, self).realised_expectation()


class UCBMachine(Machine):
    """Creates a UCB machine which works like a normal machine but now has a
    confidence level property. """

    def __init__(self, confidence_level, expectation: float, name: str,
                 gaussian: bool):
        """Initialise the machine."""
        super(UCBMachine, self).__init__(expectation, name, gaussian)
        self.confidence_level = confidence_level
        self.uncertainty = float('inf')

    def run(self):
        """Run the machine."""
        super(UCBMachine, self).run()
        self.uncertainty = self.confidence_level * (np.sqrt(
            np.log(len(self.realisations) + 1) / len(self.realisations)))

    def realised_expectation(self):
        """Return the realised expectation of the machine."""
        return super(UCBMachine, self).realised_expectation()

    def sample(self):
        """Return a sample of the estimated distribution of the machine."""
        return self.realised_expectation() + self.uncertainty


class Environment:
    """Environment class which hosts the machines."""

    def __init__(self, n: int, gaussian=False):
        """Initialise the environment."""
        self.gaussian = gaussian
        self.machine_list = []
        for i in range(n):
            self.machine_list.append(
                Machine(expectation=random(), name="Machine " + str(i),
                        gaussian=gaussian))
        self.regret = []

    def update(self):
        """Update the machine by calculating the regret."""
        mean_machines = []
        trial_numbers = []
        sum_of_realised_expectation = []
        for machine in self.machine_list:
            number_of_trials_for_machine = len(machine.realisations)
            expectation_for_machine = machine.expectation
            trial_numbers.append(number_of_trials_for_machine)
            mean_machines.append(expectation_for_machine)
            sum_of_realised_expectation.append(
                number_of_trials_for_machine * expectation_for_machine)

        highest_mean = max(mean_machines)
        number_of_trials = sum(trial_numbers)

        regret = highest_mean * number_of_trials - sum(
            sum_of_realised_expectation)

        self.regret.append(regret)


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
    values = np.asarray(value_list, dtype=object)
    return np.argmax(
        np.random.random(values.shape) * (values == values.max(initial=1)))


def average_finder(regret_list, trial_no, its_number):
    """Find the average of number of iterations."""
    result = []
    ci_list = []
    for j in range(0, trial_no):
        list_of_numbers = []
        for k in range(0, its_number):
            list_of_numbers.append(regret_list[k][j])
        result.append(np.average(list_of_numbers))

        ci = 1.96 * np.std(list_of_numbers) / np.sqrt(its_number)
        ci_list.append(ci)

    result = np.array(result)
    ci_array = np.array(ci_list)
    ci_plus = result + ci_array
    ci_minus = result - ci_array

    return result, ci_minus, ci_plus
