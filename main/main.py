"""The main file for testing."""

import matplotlib.pyplot as plt

from bandits import average_finder
from strategies import *

machine_no = 100
trial_no = 1000

random_strategy_regret = []
epsilon_first_strategy_regret = []
ucb_strategy_regret = []
thompson = []
strategy_list = ["random", "epsilon_first", "ucb", "thompson"]

number_of_iterations = 10

for i in range(number_of_iterations):
    random_strategy_regret.append(
        random_strategy_calculator(machine_no, trial_no).regret)
    epsilon_first_strategy_regret.append(
        epsilon_first_strategy(machine_no, trial_no).regret)
    ucb_strategy_regret.append(
        ucb_strategy(machine_no, trial_no, confidence_level=2).regret)
    thompson.append((thompson_sampling_strategy(machine_no, trial_no)).regret)

random_average = average_finder(random_strategy_regret, trial_no,
                                number_of_iterations)
epsilon_average = average_finder(epsilon_first_strategy_regret, trial_no,
                                 number_of_iterations)
ucb_average = average_finder(ucb_strategy_regret, trial_no,
                             number_of_iterations)
thompson_average = average_finder(thompson, trial_no, number_of_iterations)

plt.plot(random_average, label="random")
plt.plot(epsilon_average, label="epsilon")
plt.plot(ucb_average, label="ucb")
plt.plot(thompson_average, label="thompson")
plt.grid()
plt.legend()
plt.show()
