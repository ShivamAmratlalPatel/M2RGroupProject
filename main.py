"""The main file."""
from random import randint

from bandits import environment, total_value

number_of_machines = 5

machine_list = environment(number_of_machines)

number_of_goes = 100
for i in range(number_of_goes):
    random_machine_number = randint(0, number_of_machines-1)
    machine_list[random_machine_number].run()

print(total_value(machine_list))
