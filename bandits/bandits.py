"""This file creates the Machine class which emulates a slot machine."""
from random import random

import numpy as np
from scipy.stats import norm, bernoulli


class Machine:
    """Create the machine class."""

    def __init__(self, expectation: float, name: str, gaussian: bool):
        """Initialize the class.

        :param expectation: actual expectation for Bernoulli realisations
        :param name: name of the machine
        """
        # Assigning values to class values.
        self.expectation = expectation
        self.realisations = []
        self.name = name
        self.gaussian = gaussian

    def run(self):
        """Return a bernoulli realisation of the machine if run."""
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
            # then return string rather than error.
            return "No realisations have been done for " + self.name

    def __repr__(self):
        """Return the name of the machine."""
        # May need to be changed in future to give a more detailed response.
        return self.name

    def __str__(self):
        """Return the name of the machine."""
        return self.name


class ThompsonMachine(Machine):
    def __init__(self, expectation: float, name: str, gaussian: bool):
        super(ThompsonMachine, self).__init__(expectation, name, gaussian)
        self.alpha = 1
        self.beta = 1
        self.n = 0

    def run(self):
        self.n += 1
        super(ThompsonMachine, self).run()
        if self.realisations[-1] > 0:
            self.alpha += 1
        else:
            self.beta += 1

    def sample(self):
        """ return a value sampled from the beta distribution """
        return np.random.beta(self.alpha, self.beta)


def environment(n: int, gaussian=False):
    """
    Create the environment.

    :param n: list of machines
    :param gaussian: whether to use a gaussian or Bernoulli distribution
    :return the total value gained from the machines
    """
    # Initialise empty machine list
    machine_list = []
    # Add n machines with a random expectation.
    for i in range(n):
        machine_list.append(
            Machine(expectation=random(), name="Machine " + str(i),
                    gaussian=gaussian))
    return machine_list


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
    """ a random tie-breaking argmax"""
    values = np.asarray(value_list)
    return np.argmax(
        np.random.random(values.shape) * (values == values.max(initial=1)))
