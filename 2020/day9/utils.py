def read_input_file(filename: str = "input_file.txt"):
    with open(filename) as input_file:
        raw_input = [int(x.strip()) for x in input_file.readlines()]
    return raw_input
