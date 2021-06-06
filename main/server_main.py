"""The main file for testing."""
import csv
import sys
from datetime import datetime

import matplotlib.pyplot as plt

import emailer as em
from bandits import average_finder
from strategies import *

machine_no = 10
trial_no = 20000
gaussian = True
number_of_iterations = 1

random_strategy_regret = []
epsilon_first_strategy_regret = []
ucb_strategy_regret = []
thompson = []
strategy_list = ["random", "epsilon_first", "ucb", "thompson"]

for i in range(number_of_iterations):
    random_strategy_regret.append(
        random_strategy_calculator(machine_no, trial_no, gaussian).regret)
    epsilon_first_strategy_regret.append(
        epsilon_first_strategy(machine_no, trial_no, epsilon=0.2,
                               gaussian=gaussian).regret)
    ucb_strategy_regret.append(
        ucb_strategy(machine_no, trial_no, confidence_level=2,
                     gaussian=gaussian).regret)
    thompson.append(
        (thompson_sampling_strategy(machine_no, trial_no, gaussian)).regret)
    print(str(number_of_iterations) + " completed at ", datetime.now())

random_average = average_finder(random_strategy_regret, trial_no,
                                number_of_iterations)
epsilon_average = average_finder(epsilon_first_strategy_regret, trial_no,
                                 number_of_iterations)
ucb_average = average_finder(ucb_strategy_regret, trial_no,
                             number_of_iterations)
thompson_average = average_finder(thompson, trial_no, number_of_iterations)

print("averages_calculated at ", datetime.now())

plt.plot(random_average, label="random")
plt.plot(epsilon_average, label="epsilon-first")
plt.plot(ucb_average, label="ucb")
plt.plot(thompson_average, label="thompson")
plt.xlabel("Round")
plt.ylabel("Cumulative Regret")
plt.grid()
plt.legend()
plt.savefig('test.png')

averages_list = [random_average, epsilon_average, ucb_average,
                 thompson_average]
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(averages_list)

em.send_email('test.png')
em.send_email('data.csv')
sys.exit()
