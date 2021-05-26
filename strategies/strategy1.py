"""
Random strategy then exploit best machine.

This strategy randomly picks a slot machine to run for half the trials.
Then runs the machine with the highest realised expectation for the rest of the
trials.
"""

from random import randint

from bandits import environment, total_value, best_machine

number_of_machines = 5

machine_list = environment(number_of_machines)

number_of_trials = 100
for i in range(int(number_of_trials / 2)):
    random_machine_number = randint(0, number_of_machines - 1)
    machine_list[random_machine_number].run()

best_machine_index = best_machine(machine_list)

for i in range(int(number_of_trials / 2)):
    machine_list[best_machine_index].run()

print(total_value(machine_list))
