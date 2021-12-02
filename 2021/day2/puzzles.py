import operator
import sys
from functools import reduce


def read_input_file(filename: str="input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.readlines()
    return raw_input


def convert_elements_in_list_to_instructions(to_be_converted: list):
    return [
        (x.strip().split(" ")[0], int(x.strip().split(" ")[1]))
        for x in to_be_converted
    ]


def puzzle1(values):
    position = {
        "forward": 0,
        "up": 0,
        "down": 0
    }
    for value in values:
        position[value[0]] += value[1]
    return position['forward'], position['down'] - position['up']


def puzzle2(values):
    operation = {
        "up": operator.__sub__,
        "down": operator.__add__
    }
    aim = 0
    depth_value = 0
    horizontal_postition = 0
    for value in values:
        if value[0] == "forward":
            horizontal_postition += value[1]
            depth_value += (aim * value[1])
        else:
            aim = reduce(operation[value[0]], [aim, value[1]])
    return horizontal_postition, depth_value


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input_file.txt"
    print(f"Using {input_file} as input.")
    input_from_file = read_input_file(input_file)
    input_values = convert_elements_in_list_to_instructions(input_from_file)
    horizontal, depth = puzzle1(input_values)
    print(f"Puzzle 1\n{'=' * 8}\n"
          f"Horizontal position is {horizontal}\n"
          f"Depth is {depth}\n"
          f"Puzzle 1 answer: {horizontal * depth}")
    horizontal, depth = puzzle2(input_values)
    print(f"\n{'-' * 24}\n")
    print(f"Puzzle 2\n{'=' * 8}\n"
          f"Horizontal position is {horizontal}\n"
          f"Depth is {depth}\n"
          f"Puzzle 2 answer: {horizontal * depth}")
