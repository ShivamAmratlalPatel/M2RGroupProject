"""The main file for testing."""
from statistics import mean

from matplotlib.pyplot import bar, grid, show

from strategies import *

machine_no = 10
trial_no = 1000

random_strat = []
strat1 = []
strat2 = []
thompson = []
strategy_list = ["random", "strat1", "strat2", "thompson"]

number_of_iterations = 100

for i in range(number_of_iterations):
    random_strat.append(random_strategy(machine_no, trial_no))
    strat1.append(strategy1(machine_no, trial_no))
    strat2.append(strategy2(machine_no, trial_no))
    thompson.append(thompson_sampling(machine_no, trial_no))

bar(x=strategy_list,
    height=[mean(random_strat), mean(strat1), mean(strat2), mean(thompson)])
grid()
show()
