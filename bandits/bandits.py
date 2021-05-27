"""This file creates the Machine class which emulates a slot machine."""
from random import random

from scipy.stats import bernoulli


class Machine:
    """Create the machine class."""

    def __init__(self, expectation: float, name: str):
        """Initialize the class.

        :param expectation: actual expectation for bernouli realisations
        :param name: name of the machine
        """
        # Assigning values to class values.
        self.expectation = expectation
        self.realisations = []
        self.name = name

    def run(self):
        """Return a bernoulli realisation of the machine if run."""
        # Running a bernoulli trial
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
        # May need to be changed in future to give a more detialed response.
        return self.name

    def __str__(self):
        """Return the name of the machine."""
        return self.name


def environment(n: int):
    """
    Create the environment.

    :param n: number of slot machines
    :return: list of n machines
    """
    # Initialise empty machine list
    machine_list = []
    # Add n machines with a random expectation.
    for i in range(n):
        machine_list.append(
            Machine(expectation=random(), name="Machine " + str(i)))
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
    Calculate the machine with the highest realised expecation.

    :param machine_list:
    :return: the index of the machine with the highest realised expecation
    """
    # Create a list of all the realised expectations.
    # Should implement a check if any of the machines have not had any trials.
    realised_expectations = [machine.realised_expectation() for machine in
                             machine_list]
    # Return the index of the max of these realised expectations.
    return realised_expectations.index(max(realised_expectations))


def worst_machine(machine_list: list):
    """
    Calculate the machine with the lowest realised expecation.

    :param machine_list:
    :return: the index of the machine with the lowest realised expecation
    """
    # Create a list of all the realised expectations.
    # Should implement a check if any of the machines have not had any trials.
    realised_expecations = [machine.realised_expectation() for machine in
                            machine_list]
    # Return the index of the min of these realised expectations.
    return realised_expecations.index(min(realised_expecations))
