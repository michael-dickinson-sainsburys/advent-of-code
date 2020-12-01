from itertools import product

sum_total = 2020

with open("input_file.txt") as input_file:
  raw_input = input_file.read().splitlines()

input = [
  int(x.strip())
  for x in raw_input
]

for values in product(input, input, input):
  if sum(list(values)) == sum_total:
    print(values)
    print(f"The product of the values is: {values[0] * values[1] * values[2]}")
