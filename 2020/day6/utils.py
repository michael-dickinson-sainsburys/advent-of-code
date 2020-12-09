import os


def read_input_file(filename: str = "input_file.txt"):
    with open(filename) as input_file:
        raw_input = input_file.read()
    group_answers = raw_input.split(2 * os.linesep)
    return [
        set(y.strip() for y in x.split(os.linesep))
        for x in group_answers
    ]
