import sys

import utils

TREE_MAP = utils.read_input_file(filename="input.txt")
X_INCREMENT = 1
Y_INCREMENT = 3


def is_a_tree(x, y):
    return TREE_MAP[x][y % 30] == "#"


def next_location(x, y):
    return x + X_INCREMENT, y + Y_INCREMENT


def main(current_x: int = 0, current_y: int = 0) -> int:
    trees_encountered = 0
    for row in TREE_MAP:
        if is_a_tree(current_x, current_y):
            trees_encountered += 1
        current_x, current_y = next_location(current_x, current_y)
    print(f"Number of trees encountered: {trees_encountered}")
    return


if __name__ == "__main__":
    try:
        start_x = sys.argv[1]
    except IndexError:
        start_x = 0
    try:
        start_y = sys.argv[1]
    except IndexError:
        start_y = 0
    main(start_x, start_y)
