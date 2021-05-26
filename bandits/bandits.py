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
        self.expectation = expectation
        self.realisations = []
        self.name = name

    def run(self):
        """Return a bernoulli realisation of the machine if run."""
        self.realisations.append(bernoulli.rvs(size=1, p=0.6))

    def realised_expecation(self):
        """Return the realised expectation."""
        try:
            return sum(self.realisations) / len(self.realisations)
        except ZeroDivisionError:
            return "No realisations have been done for " + self.name

    def __repr__(self):
        """Return the name of the machine."""
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
    machine_list = []
    for i in range(n):
        machine_list.append(
            Machine(expectation=random(), name="Machine " + str(i)))
    return machine_list


def total_value(machine_list: list):
    """Calculate the value gained given a list of machines.

    :param machine_list: list of machines
    :return the total value gained from the machines
    """
    machine_values = [sum(i.realisations) for i in machine_list]
    return int(sum(machine_values))


def best_machine(machine_list: list):
    """
    Calculate the machine with the highest realised expecation
    :param machine_list:
    :return: the index of the machine with the highest realised expecation
    """
    realised_expecations = [machine.realised_expecation() for machine in
                           machine_list]
    return realised_expecations.index(max(realised_expecations))
