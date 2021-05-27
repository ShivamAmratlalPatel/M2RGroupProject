"""The main file for testing."""
from strategies import random_strategy, strategy1, strategy2
from statistics import mean

machine_no = 10
trial_no = 1000

random_strat = []
strat1 = []
strat2 = []

number_of_iterations = 1000

for i in range(number_of_iterations):
    random_strat.append(random_strategy(machine_no, trial_no))
    strat1.append(strategy1(machine_no, trial_no))
    strat2.append(strategy2(machine_no, trial_no))

print(mean(random_strat))
print(mean(strat1))
print(mean(strat2))
