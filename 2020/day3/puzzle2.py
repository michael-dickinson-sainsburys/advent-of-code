import utils


class TreeMap(object):
    def __init__(self,
                 x_increment: int,
                 y_increment: int,
                 map_file: str = "input.txt",
                 starting_x: int = 0,
                 starting_y: int = 0):
        self.x_increment = x_increment
        self.y_increment = y_increment
        self.map = utils.read_input_file(filename=map_file)
        self.repeat = len(self.map[0]) - 1
        self.current_x = starting_x
        self.current_y = starting_y
        self.trees_encountered = 0

    def check_for_tree(self):
        if self.current_x < len(self.map) and \
                self.map[self.current_x][self.current_y % self.repeat] == "#":
            self.trees_encountered += 1

    def get_next_location(self):
        self.current_x += self.x_increment
        self.current_y += self.y_increment

    def check_for_trees(self):
        for row in self.map:
            self.check_for_tree()
            self.get_next_location()


def main():
    combinations = [(1, 1),
                    (1, 3),
                    (1, 5),
                    (1, 7),
                    (2, 1)]
    answer = 1
    for combination in combinations:
        map = TreeMap(combination[0], combination[1])
        map.check_for_trees()
        print(f"Number of trees encountered on slope "
              f"R{combination[1]}D{combination[0]}: "
              f"{map.trees_encountered}")
        answer *= map.trees_encountered
    print(f"And the answer is: {answer}")


if __name__ == "__main__":
    main()
