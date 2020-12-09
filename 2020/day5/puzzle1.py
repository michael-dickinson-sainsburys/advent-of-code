import utils


class BspTree(object):
    def __init__(self,
                 length: int,
                 upper_indicator: str,
                 lower_indicator: str):
        self.node_max = length - 1
        self.node_min = 0
        self.operation = {upper_indicator: self.add,
                          lower_indicator: self.subtract}

    def find_node(self, identifier: str):
        for indicator in identifier:
            self.traverse(indicator)
        if self.node_min == self.node_max:
            return int(self.node_min)
        else:
            print("Not enough indicators supplied to determine the node.")
            print(f"Range of nodes: {self.node_min} to {self.node_max}")
            raise(TypeError("Not enough indicators supplied to determine the node."))

    def traverse(self, indicator: str):
        try:
            self.operation[indicator]()
        except KeyError as e:
            print(f"Unknown indicator: {e}")
        # print(f"{indicator} reduces rows to {self.node_min} to {self.node_max}")

    def subtract(self):
        self.node_max = (self.node_min + self.node_max - 1) / 2

    def add(self):
        self.node_min = (self.node_min + self.node_max + 1) / 2


def main():
    seat_ids = list()
    for boarding_pass in utils.read_input_file("boarding_passes.txt"):
        plane_length = BspTree(length=128, upper_indicator="B", lower_indicator="F")
        row = plane_length.find_node(boarding_pass[:7])
        plane_width = BspTree(length=8, upper_indicator="R", lower_indicator="L")
        column = plane_width.find_node(boarding_pass[7:])
        # print(f"'FBFBBFFRLR' represents seat: row {row}, column {column}")
        seat_id = row * 8 + column
        print(f"Seat id: {seat_id}")
        seat_ids.append(seat_id)
    for x in range(sorted(seat_ids)[0], sorted(seat_ids)[-1]):
        if x not in seat_ids:
            print(f"Missing seat id: {x}")
    print(f"Highest seat id: {sorted(seat_ids)[-1]}")
    print(f"Lowest seat id: {sorted(seat_ids)[0]}")


if __name__ == "__main__":
    main()
