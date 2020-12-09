def read_input_file(filename: str = "input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.readlines()
    return raw_input
