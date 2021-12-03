import sys
from collections import Counter


def read_input_file(filename: str="input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.readlines()
    return raw_input


def convert_elements_in_list_to_strings(to_be_converted: list):
    return [
        str(x.strip())
        for x in to_be_converted
    ]


def puzzle1(values):
    gamma = list()
    epsilon = list()
    for index in range(len(values[0])):
        most_commmon_bit = find_most_common_bit(values, index)
        gamma.append(most_commmon_bit)
        epsilon.append(str(1 - int(most_commmon_bit)))
        index += 1
    return int("".join(gamma), 2), int("".join(epsilon), 2)


def puzzle2(values):
    co2 = reduce_list(values, "most")
    oxygen = reduce_list(values, "least")
    return int(str(oxygen), 2), int("".join(co2), 2)


def reduce_list(values, order):
    index = 0
    while len(values) > 1:
        if order == "most":
            interesting_bit_value = find_most_common_bit(values, index)
        else:
            interesting_bit_value = \
                str(1 - int(find_most_common_bit(values, index)))
        values = [
            value for value in values if value[index] == interesting_bit_value
        ]
        index += 1
    return values[0]


def find_most_common_bit(values: list, index: int, precedent: int = 1) -> str:
    counter = Counter([value[index] for value in values])
    most_common_bit, count = counter.most_common(1)[0]
    if count == len(values)/2:
        most_common_bit = precedent
    return str(most_common_bit)


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input_file.txt"
    print(f"Using {input_file} as input.")
    input_from_file = read_input_file(input_file)
    input_values = convert_elements_in_list_to_strings(input_from_file)
    gamma_rate, epsilon_rate = puzzle1(input_values)
    print(f"Puzzle 1\n{'=' * 8}\n"
          f"Gamma rate is {gamma_rate}\n"
          f"Epsilon rate  is {epsilon_rate}\n"
          f"Puzzle 1 answer: {gamma_rate * epsilon_rate}")
    oxygen_generator_rating, co2_generator_rating = puzzle2(input_values)
    print(f"Puzzle 2\n{'=' * 8}\n"
          f"Oxygen generator rating is {oxygen_generator_rating}\n"
          f"CO2 generator rating is {co2_generator_rating}\n"
          f"Puzzle 2 answer: {oxygen_generator_rating * co2_generator_rating}")
