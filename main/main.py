"""The main file for testing."""

import matplotlib.pyplot as plt
import numpy as np

from strategies import random_strategy, epsilon_first_strategy, ucb_strategy

machine_no = 10
trial_no = 1000

random_strategy_regret = []
epsilon_first_strategy_regret = []
ucb_strategy_regret = []
# thompson = []
strategy_list = ["random", "epsilon_first", "ucb"]

number_of_iterations = 10

for i in range(number_of_iterations):
    random_strategy_regret.append(random_strategy(machine_no, trial_no).regret)
    epsilon_first_strategy_regret.append(
        epsilon_first_strategy(machine_no, trial_no).regret)
    ucb_strategy_regret.append(
        ucb_strategy(machine_no, trial_no, confidence_level=2).regret)
    # thompson.append(regret(thompson_sampling(machine_no, trial_no)))


def average_finder(regret_list):
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
plt.legend()
plt.show()
