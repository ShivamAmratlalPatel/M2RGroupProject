"""The main file for testing."""
import sys

import matplotlib.pyplot as plt
import numpy as np

from emailer.emailer import send_email
from strategies import *

machine_no = 100
trial_no = 100

random_strategy_regret = []
epsilon_first_strategy_regret = []
ucb_strategy_regret = []
thompson = []
strategy_list = ["random", "epsilon_first", "ucb", "thompson"]

number_of_iterations = 1

for i in range(number_of_iterations):
    random_strategy_regret.append(
        random_strategy_calculator(machine_no, trial_no).regret)
    epsilon_first_strategy_regret.append(
        epsilon_first_strategy(machine_no, trial_no).regret)
    ucb_strategy_regret.append(
        ucb_strategy(machine_no, trial_no, confidence_level=2).regret)
    thompson.append((thompson_sampling_strategy(machine_no, trial_no)).regret)


def average_finder(regret_list):
    """Find the average of number of iterations."""
    result = []

    for j in range(0, trial_no):
        list_of_numbers = []
        for k in range(0, number_of_iterations):
            list_of_numbers.append(regret_list[k][j])
        result.append(np.average(list_of_numbers))
    return result


plt.plot(average_finder(random_strategy_regret), label="random")
plt.plot(average_finder(epsilon_first_strategy_regret), label="epsilon")
plt.plot(average_finder(ucb_strategy_regret), label="ucb")
plt.plot(average_finder(thompson), label="thompson")
plt.xlabel("Iteration")
plt.ylabel("Cummulative Regret")
plt.grid()
plt.legend()
plt.savefig('test.png')

send_email()
sys.exit()
