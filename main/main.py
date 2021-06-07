"""The main file for testing."""

import matplotlib.pyplot as plt

from bandits import average_finder
from strategies import *

machine_no = 10
trial_no = 20000
gaussian = True
number_of_iterations = 10

random_strategy_regret = []
epsilon_first_strategy_regret = []
ucb_strategy_regret = []
thompson = []
strategy_list = ["random", "epsilon_first", "ucb", "thompson"]

for i in range(number_of_iterations):
    random_strategy_regret.append(
        random_strategy_calculator(machine_no, trial_no, gaussian).regret)
    epsilon_first_strategy_regret.append(
        epsilon_first_strategy(number_of_machines=machine_no,
                               number_of_trials=trial_no,
                               epsilon=0.06, gaussian=gaussian).regret)
    ucb_strategy_regret.append(
        ucb_strategy(machine_no, trial_no, confidence_level=2,
                     gaussian=gaussian).regret)
    thompson.append(
        (thompson_sampling_strategy(machine_no, trial_no, gaussian)).regret)

random_average = average_finder(random_strategy_regret, trial_no,
                                number_of_iterations)
epsilon_average = average_finder(epsilon_first_strategy_regret, trial_no,
                                 number_of_iterations)
ucb_average = average_finder(ucb_strategy_regret, trial_no,
                             number_of_iterations)
thompson_average = average_finder(thompson, trial_no, number_of_iterations)

# plt.style.use('classic')
# # plt.plot(random_average, label="random")
# plt.plot(epsilon_average, label="epsilon-first")
# plt.plot(ucb_average, label="ucb")
# plt.plot(thompson_average, label="thompson")
# plt.xlabel("Round")
# plt.ylabel("Cumulative Regret")
# plt.grid()
# plt.legend(loc='upper left', frameon=True)
# plt.show()

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(range(len(random_average)), random_average, 'p', alpha=0.5, lw=2,
        label='random')
ax.plot(range(len(epsilon_average)), epsilon_average, 'b', alpha=0.5, lw=2,
        label='epsilon-first')
ax.plot(range(len(ucb_average)), ucb_average, 'r', alpha=0.5, lw=2,
        label='ucb')
ax.plot(range(len(thompson_average)), thompson_average, 'g', alpha=0.5, lw=2,
        label='thompson')
ax.set_xlabel('Round')
ax.set_ylabel('Cumulative Regret')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='both', c='w', lw=2, ls='-')
# plt.title("GBR Modelling")
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.savefig('plot.png', dpi=1000, transparent=False, bbox_inches='tight')
plt.show()
