def read_input_file(filename: str="input_file.txt"):
    with open("input_file.txt") as input_file:
        raw_input = input_file.readlines()
    return raw_input


def convert_elements_in_list_to_integers(to_be_converted: list):
    return [
        int(x.strip())
        for x in to_be_converted
    ]
