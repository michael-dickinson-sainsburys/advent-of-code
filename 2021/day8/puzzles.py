def setup_puzzle(filename: str) -> list:
    puzzle_input = read_input_file(filename)
    output_digits = [(row.split(" | ")[0].split(), row.split(" | ")[1].split())
                     for row in puzzle_input]
    return output_digits


def read_input_file(filename: str = "input_file.txt") -> list:
    with open(filename) as input_file:
        raw_input = input_file.read().splitlines()
    return raw_input


def puzzle1(values: list) -> int:
    return len([
        digit
        for entry in values
        for digit in entry
        if len(digit) in [2, 3, 4, 7]
    ])


def puzzle2(values: list) -> int:
    count = 0
    for patterns, output_digit_codes in values:
        output_value = ""
        digit_signal_patterns = decode_signal_patterns(patterns)
        for digit_code in output_digit_codes:
            output_value += digit_signal_patterns["".join(sorted(digit_code))]
        count += int(output_value)
    return count


def decode_signal_patterns(patterns: list):
    sorted_patterns = sorted(patterns, key=len)
    digit_elements = {
        1: sorted_patterns[0],
        4: sorted_patterns[2],
        7: sorted_patterns[1],
        8: sorted_patterns[9]
    }
    top = list(set(digit_elements[7]) - set(digit_elements[1]))[0]
    bottom = [
        list(set(digit_elements[7] + digit_elements[4]) ^ set(pattern))[0]
        for pattern in sorted_patterns
        if len(list(set(digit_elements[7] + digit_elements[4]) ^ set(pattern))) == 1
        and list(set(digit_elements[7] + digit_elements[4]) ^ set(pattern))[0] != top
    ][0]
    left_bottom = list(set(digit_elements[8]) - set(digit_elements[4] + top + bottom))[0]
    left_top = [
        list(set(digit_elements[7] + bottom + left_bottom) ^ set(pattern))[0]
        for pattern in sorted_patterns
        if len(list(set(digit_elements[7] + bottom + left_bottom) ^ set(pattern))) == 1
    ][0]
    middle = list(set(digit_elements[4]) - set(digit_elements[1] + left_top))[0]
    right_bottom = [
        list(set(top + left_top + middle + bottom) ^ set(pattern))[0]
        for pattern in sorted_patterns
        if len(list(set(top + left_top + middle + bottom) ^ set(pattern))) == 1
    ][0]
    right_top = list(set(digit_elements[1]) - set(right_bottom))[0]
    # print(f"top: {top}, bottom: {bottom}, left-bottom: {left_bottom}, "
    #       f"left-top: {left_top}, middle: {middle}, "
    #       f"right-bottom: {right_bottom}, right-top: {right_top}")
    zero = "".join(sorted(top + right_top + right_bottom + bottom + left_bottom + left_top))
    one = "".join(sorted(right_top + right_bottom))
    two = "".join(sorted(top + right_top + middle + left_bottom + bottom))
    three = "".join(sorted(top + bottom + middle + one))
    four = "".join(sorted(left_top + middle + one))
    five = "".join(sorted(top + left_top + middle + right_bottom + bottom))
    six = "".join(sorted(five + left_bottom))
    seven = "".join(sorted(top + one))
    eight = "".join(sorted(zero + middle))
    nine = "".join(sorted(top + four + bottom))
    return {zero: "0", one: "1", two: "2", three: "3", four: "4", five: "5",
            six: "6", seven: "7", eight: "8", nine: "9"}


if __name__ == "__main__":
    test_input = setup_puzzle("test_input.txt")
    puzzle1_test_answer = puzzle1([row[1] for row in test_input])
    print(f"Puzzle 1 test answer: {puzzle1_test_answer}")
    assert puzzle1_test_answer == 26
    full_input = setup_puzzle("puzzle_input.txt")
    puzzle1_full_answer = puzzle1([row[1] for row in full_input])
    print(f"Puzzle 1 answer: {puzzle1_full_answer}")
    assert puzzle1_full_answer == 261
    puzzle2_test_answer = puzzle2(test_input)
    print(f"Puzzle 2 test answer: {puzzle2_test_answer}")
    assert puzzle2_test_answer == 61229
    puzzle2_full_answer = puzzle2(full_input)
    print(f"Puzzle 2 answer: {puzzle2_full_answer}")
    assert puzzle2_full_answer == 987553
