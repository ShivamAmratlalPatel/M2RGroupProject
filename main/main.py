"""The main file for testing."""
from statistics import mean

import matplotlib.pyplot as plt

from strategies import *

machine_no = 10
trial_no = 1000

random_strat = []
strat1 = []
strat2 = []
strategy_list = ["random", "strat1", "strat2"]

number_of_iterations = 1000

for i in range(number_of_iterations):
    random_strat.append(random_strategy(machine_no, trial_no))
    strat1.append(strategy1(machine_no, trial_no))
    strat2.append(strategy2(machine_no, trial_no))

plt.bar(x=strategy_list,
        height=[mean(random_strat), mean(strat1), mean(strat2)])
plt.grid()
plt.show()
