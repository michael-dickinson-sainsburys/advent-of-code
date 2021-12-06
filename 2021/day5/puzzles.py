from collections import namedtuple


def parse_coords(self):
    starting_coord, ending_coords = self.coords.split(" -> ")
    self.x1, self.y1 = starting_coord.split(",")
    self.x2, self.y2 = ending_coords.split(",")


def setup_puzzle(filename: str) -> tuple:
    puzzle_input = read_input_file(filename)
    Vent = namedtuple('Vent', 'x1 y1 x2 y2')
    vents = list()
    max_x = 0
    max_y = 0
    for vent in puzzle_input:
        x1, y1, x2, y2 = [
            int(y)
            for x in vent.split(" -> ")
            for y in x.split(",")
        ]
        vents.append(Vent(x1, y1, x2, y2))
        max_x = max([x1, x2, max_x])
        max_y = max([y1, y2, max_y])
    vent_map = [[0 for col in range(max_y + 1)] for row in range(max_x + 1)]
    return vents, vent_map


def read_input_file(filename: str = "input_file.txt") -> list:
    with open(filename) as input_file:
        raw_input = input_file.read().splitlines()
    return raw_input


def add_vent_to_map(vent: namedtuple, vent_map: list) -> list:
    if vent.x1 == vent.x2:
        for y in range(vent.y1, vent.y2 + 1 if vent.y2 > vent.y1 else vent.y2 - 1, 1 if vent.y2 > vent.y1 else -1):
            vent_map[y][vent.x1] += 1
    elif vent.y1 == vent.y2:
        for x in range(vent.x1, vent.x2 + 1 if vent.x2 > vent.x1 else vent.x2 - 1, 1 if vent.x2 > vent.x1 else -1):
            vent_map[vent.y1][x] += 1
    else:
        x = range(vent.x1,
                  vent.x2 + 1 if vent.x2 > vent.x1 else vent.x2 - 1,
                  1 if vent.x2 > vent.x1 else -1)
        y = range(vent.y1,
                  vent.y2 + 1 if vent.y2 > vent.y1 else vent.y2 - 1,
                  1 if vent.y2 > vent.y1 else -1)
        for point in zip(x, y):
            vent_map[point[1]][point[0]] += 1
    return vent_map


def count_danger_spots(vent_map: list) -> int:
    count = 0
    for row in vent_map:
        count += len(row) - row.count(0) - row.count(1)
    return count


def puzzle1(vents: list, vent_map: list) -> int:
    for vent in vents:
        if vent.x1 == vent.x2 or vent.y1 == vent.y2:
            vent_map = add_vent_to_map(vent, vent_map)
    return count_danger_spots(vent_map)


def puzzle2(vents: list, vent_map: list) -> int:
    for vent in vents:
        vent_map = add_vent_to_map(vent, vent_map)
    # print("\n".join(["".join([str(x).replace("0", ".") for x in row]) for row in vent_map]))
    return count_danger_spots(vent_map)


if __name__ == "__main__":
    test_vents, test_vent_map = setup_puzzle("test_input.txt")
    puzzle1_test_answer = puzzle1(test_vents, test_vent_map)
    print(f'puzzle1 test answer: {puzzle1_test_answer}')
    assert(puzzle1_test_answer == 5)
    full_vents, full_vent_map = setup_puzzle("input_file.txt")
    puzzle1_answer = puzzle1(full_vents, full_vent_map)
    print(f'puzzle1 answer: {puzzle1_answer}')
    test_vents, test_vent_map = setup_puzzle("test_input.txt")
    puzzle2_test_answer = puzzle2(test_vents, test_vent_map)
    print(f'puzzle2 test answer: {puzzle2_test_answer}')
    assert(puzzle2_test_answer == 12)
    full_vents, full_vent_map = setup_puzzle("input_file.txt")
    print(f'puzzle2 answer: {puzzle2(full_vents, full_vent_map)}')
