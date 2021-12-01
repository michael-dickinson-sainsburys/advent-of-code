import sys


def read_input_file(filename: str="input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.readlines()
    return raw_input


def convert_elements_in_list_to_integers(to_be_converted: list):
    return [
        int(x.strip())
        for x in to_be_converted
    ]


def puzzle1(values):
    counter = 0
    index = 1
    while index < len(values):
        counter += input_values[index] > input_values[index - 1]
        index += 1
    return counter


def puzzle2(values):
    counter = 0
    window_size = 3
    index = 0
    while index < len(values) - 2:
        first_window = sum(values[index:index+window_size])
        index += 1
        second_window = sum(values[index:index+window_size])
        counter += second_window > first_window
    return counter


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input_file.txt"
    print(f"Using {input_file} as input.")
    input_from_file = read_input_file(input_file)
    input_values = convert_elements_in_list_to_integers(input_from_file)
    number_of_times_a_depth_measurement_increases = puzzle1(input_values)
    print(f"Puzzle 1 answer: {number_of_times_a_depth_measurement_increases}")
    number_of_sliding_window_depth_measurement_increases = puzzle2(input_values)
    print(f"Puzzle 2 answer: "
          f"{number_of_sliding_window_depth_measurement_increases}")
