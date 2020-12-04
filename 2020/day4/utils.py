import os


def read_input_file(filename: str = "input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.read()
    normalised_input = raw_input.split(2 * os.linesep)
    return [
        dict(y.split(":") for y in x.replace("\n", " ").split(" ") if y)
        for x in normalised_input
    ]
