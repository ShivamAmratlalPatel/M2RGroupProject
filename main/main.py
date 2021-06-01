"""The main file for testing."""
from statistics import mean

from matplotlib.pyplot import bar, grid, show

from strategies import random_strategy, epsilon_first, strategy2, \
    thompson_sampling

machine_no = 10
trial_no = 1000

random_strat = []
epsilon_first_strat = []
strat2 = []
thompson = []
strategy_list = ["random", "strat1", "strat2", "thompson"]

number_of_iterations = 1

for i in range(number_of_iterations):
    random_strat.append(random_strategy(machine_no, trial_no))
    epsilon_first_strat.append(epsilon_first(machine_no, trial_no))
    strat2.append(strategy2(machine_no, trial_no))
    thompson.append(thompson_sampling(machine_no, trial_no))

bar(x=strategy_list,
    height=[mean(random_strat), mean(epsilon_first_strat), mean(strat2),
            mean(thompson)])
grid()
show()
