from collections import Counter


def setup_puzzle(filename: str) -> list:
    puzzle_input = read_input_file(filename)
    return [int(x) for x in puzzle_input[0].split(",")]


def read_input_file(filename: str = "input_file.txt") -> list:
    with open(filename) as input_file:
        raw_input = input_file.read().splitlines()
    return raw_input


def puzzle1(values: list) -> int:
    alignment_values = Counter()
    for alignment_value in range(max(values)):
        alignment_values[alignment_value] = sum(
            [abs(value - alignment_value) for value in values]
        )
    return alignment_values.most_common(len(alignment_values))[-1][1]


def puzzle2(values: list) -> int:
    alignment_values = Counter()
    for alignment_value in range(max(values)):
        temp_count = 0
        for value in values:
            for i in range(abs(value - alignment_value) + 1):
                temp_count += i
        alignment_values[alignment_value] = temp_count
    return alignment_values.most_common(len(alignment_values))[-1][1]


if __name__ == "__main__":
    test_positions = setup_puzzle("test_input.txt")
    puzzle1_test_answer = puzzle1(test_positions)
    print(f"Puzzle1 test answer: {puzzle1_test_answer}")
    assert puzzle1_test_answer == 37
    full_positions = setup_puzzle("input_file.txt")
    puzzle1_full_answer = puzzle1(full_positions)
    print(f"Puzzle1 answer: {puzzle1_full_answer}")
    assert puzzle1_full_answer == 345035
    test_positions = setup_puzzle("test_input.txt")
    puzzle2_test_answer = puzzle2(test_positions)
    print(f"Puzzle2 test answer: {puzzle2_test_answer}")
    assert puzzle2_test_answer == 168
    full_positions = setup_puzzle("input_file.txt")
    puzzle2_full_answer = puzzle2(full_positions)
    print(f"Puzzle2 answer: {puzzle2_full_answer}")
    assert puzzle2_full_answer == 97038163
