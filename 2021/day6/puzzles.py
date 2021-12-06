import sys
from collections import Counter


def setup_puzzle(filename: str) -> tuple:
    puzzle_input = read_input_file(filename)
    laternfish = [int(fish) for fish in puzzle_input[0].split(",")]
    return laternfish


def read_input_file(filename: str = "input_file.txt") -> list:
    with open(filename) as input_file:
        raw_input = input_file.read().splitlines()
    return raw_input


def puzzle1(laternfish: list, iterations: int) -> list:
    while iterations > 0:
        new_laternfish = laternfish.count(0)
        laternfish = [
            fish - 1 if fish != 0 else 6
            for fish in laternfish
        ]
        for new_fish in range(new_laternfish):
            laternfish.append(8)
        iterations -= 1
    return len(laternfish)


def puzzle2(laternfish: list, iterations: int) -> dict:
    cycles_of_fish = Counter(laternfish)
    for iteration in range(1, iterations + 1):
        for key in range(9):
            cycles_of_fish[key - 1] = cycles_of_fish[key]
        if -1 in cycles_of_fish:
            cycles_of_fish[8] = cycles_of_fish[-1]
            cycles_of_fish[6] += cycles_of_fish[-1]
            del cycles_of_fish[-1]
    return sum(cycles_of_fish.values())


if __name__ == "__main__":
    test_laternfish = setup_puzzle("test_input.txt")
    puzzle1_test_answer = puzzle2(test_laternfish, 18)
    print(f'puzzle1 test answer: {puzzle1_test_answer}')
    assert(puzzle1_test_answer == 26)
    test_laternfish = setup_puzzle("test_input.txt")
    puzzle1_test_answer = puzzle2(test_laternfish, 80)
    print(f'puzzle1 test answer: {puzzle1_test_answer}')
    assert(puzzle1_test_answer == 5934)
    full_laternfish = setup_puzzle("input_file.txt")
    puzzle1_answer = puzzle2(full_laternfish, 80)
    print(f'puzzle1 answer: {puzzle1_answer}')
    assert(puzzle1_answer == 372984)
    test_laternfish = setup_puzzle("test_input.txt")
    puzzle2_test_answer = puzzle2(test_laternfish, 256)
    print(f'puzzle2 test answer: {puzzle2_test_answer}')
    assert(puzzle2_test_answer == 26984457539)
    full_laternfish = setup_puzzle("input_file.txt")
    puzzle2_answer = puzzle2(full_laternfish, 256)
    print(f'puzzle2 answer: {puzzle2_answer}')
