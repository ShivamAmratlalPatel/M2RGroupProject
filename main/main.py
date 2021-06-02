"""The main file for testing."""
from statistics import mean

from matplotlib.pyplot import bar, grid, show

from bandits import regret
from strategies import random_strategy, epsilon_first, strategy2

machine_no = 10
trial_no = 1000

random_strat = []
epsilon_first_strat = []
strat2 = []
thompson = []
strategy_list = ["random", "epsilon_first", "strat2"]

number_of_iterations = 1

for i in range(number_of_iterations):
    random_strat.append(regret(random_strategy(machine_no, trial_no)))
    epsilon_first_strat.append(regret(epsilon_first(machine_no, trial_no)))
    strat2.append(regret(strategy2(machine_no, trial_no)))
    # thompson.append(regret(thompson_sampling(machine_no, trial_no)))

bar(x=strategy_list,
    height=[mean(random_strat), mean(epsilon_first_strat), mean(strat2)])
grid()
show()
