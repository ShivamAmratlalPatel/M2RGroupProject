"""This strategy randomly picks a slot machine to run."""
from random import randint

from bandits import environment, total_value

# Set inital parameters
number_of_machines = 5
number_of_trials = 100

# Initalise the environment.
machine_list = environment(number_of_machines)

# Randomly pick a machine for each trial.
for i in range(number_of_trials):
    random_machine_number = randint(0, number_of_machines-1)
    machine_list[random_machine_number].run()

# Calculate the total value generated.
print(total_value(machine_list))
