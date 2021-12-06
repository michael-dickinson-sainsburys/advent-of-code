from collections import namedtuple


def setup_puzzle(filename:str) -> tuple:
    puzzle_input = read_input_file(filename)
    return get_numbers(puzzle_input[0]), create_boards(puzzle_input[1:])


def read_input_file(filename: str = "input_file.txt") -> list:
    with open(filename) as input_file:
        raw_input = input_file.read().splitlines()
    return raw_input


def get_numbers(values: str) -> list:
    return values.split(",")


def create_boards(values: list) -> list:
    square = namedtuple("square", ["value", "marked"])
    boards = list()
    for row in values:
        if row:
            boards[-1].append([
                square(value=value, marked=False)
                for value in row.split()
            ])
        else:
            boards.append([])
    return boards


def mark_board(number: int, board: list) -> list:
    for row in board:
        for index, square in enumerate(row):
            if number == square.value:
                row[index] = square._replace(marked=True)
    return board


def check_board(board: list) -> list:
    index = 0
    for row in board:
        if all([square.marked for square in row]):
            return board
    while index < len(board):
        if all([row[index].marked for row in board]):
            return board
        index += 1
    return None


def get_unmarked_numbers(board: list) -> list:
    return [
        int(square.value)
        for row in board
        for square in row
        if not square.marked
    ]


def puzzle1(numbers: list, boards: list) -> int:
    for number in numbers:
        for index, board in enumerate(boards):
            board = mark_board(number, board)
            if check_board(board):
                return sum(get_unmarked_numbers(board)) * int(number)
    return None


def puzzle2(numbers: list, boards: list) -> int:
    won = list()
    for number in numbers:
        for index, board in enumerate(boards):
            board = mark_board(number, board)
            if check_board(board) and index not in won:
                score = sum(get_unmarked_numbers(board)) * int(number)
                won.append(index)
    return score


if __name__ == "__main__":
    test_numbers, test_boards = setup_puzzle("test_input.txt")
    full_numbers, full_boards = setup_puzzle("input_file.txt")
    assert(puzzle1(test_numbers, test_boards) == 4512)
    print(f'puzzle1 answer: {puzzle1(full_numbers, full_boards)}')
    assert(puzzle2(test_numbers, test_boards) == 1924)
    print(f'puzzle2 answer: {puzzle2(full_numbers, full_boards)}')
