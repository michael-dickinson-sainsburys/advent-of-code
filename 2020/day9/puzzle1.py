import itertools

import utils


def main(preamble_length: int = 25):
    numbers = utils.read_input_file("xmas_cypher.txt")
    index = preamble_length
    while index < len(numbers) - 1:
        start = index - preamble_length if index - preamble_length - 1 > 0 else 0
        if not find_sum_of_combination_equal_to_value(numbers[start:index],
                                                      numbers[index]):
            return numbers[index]
        index += 1
    return None


def find_sum_of_combination_equal_to_value(values, target):
    for combination in itertools.combinations(values, 2):
        if sum(combination) == target:
            return True
    return False


if __name__ == "__main__":
    print(f"The answer is {main()}")
