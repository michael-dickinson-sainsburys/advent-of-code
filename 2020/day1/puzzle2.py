from itertools import product

import utils

sum_total = 2020

input_values_from_file = utils.read_input_file()
input_values = utils.convert_elements_in_list_to_integers(input_values_from_file)

for values in product(input_values, input_values, input_values):
    if sum(list(values)) == sum_total:
        print(values)
        print(f"The product of the values is: {values[0] * values[1] * values[2]}")
