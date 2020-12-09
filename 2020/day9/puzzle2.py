import utils


def main(invalid_number: int):
    numbers = utils.read_input_file("xmas_cypher.txt")
    for pointer in range(len(numbers) - 1):
        found, high = find_contiguous_values_equal_to_value(numbers, pointer, invalid_number)
        if found:
            weak_data = numbers[pointer:high]
            return min(weak_data) + max(weak_data)


def find_contiguous_values_equal_to_value(values, start, target):
    high_pointer = start + 1
    while sum(values[start:high_pointer]) < target:
        high_pointer += 1
    if sum(values[start:high_pointer]) == target:
        return True, high_pointer
    return False, None


if __name__ == "__main__":
    print(f"The answer is {main(23278925)}")
