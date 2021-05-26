"""
Random strategy then discards the worst machine in each round.

This strategy randomly picks a slot machine to run for x percentage of the
trials. Then discards the machine with the worst realised expectation.
This process then continues till their is one machine left for a round.
"""

from bandits import environment, total_value, worst_machine

number_of_machines = 5
number_of_trials = 100
number_of_trials_per_round = int(number_of_trials / number_of_machines)

machine_list = environment(number_of_machines)
discarded_list = []

for i in range(number_of_machines):
    number_of_trials_per_machine_per_round = int(
        number_of_trials_per_round / len(machine_list))
    for j in range(len(machine_list)):
        for k in range(number_of_trials_per_machine_per_round):
            machine_list[j].run()
    machine_to_be_removed = machine_list[worst_machine(machine_list)]
    machine_list.remove(machine_to_be_removed)
    discarded_list.append(machine_to_be_removed)

print(total_value(discarded_list))
