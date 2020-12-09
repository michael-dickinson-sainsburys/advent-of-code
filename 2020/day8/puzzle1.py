import utils


def main():
    instructions = utils.read_input_file("code_instructions.txt")
    acc = 0
    index = 0
    visited = set()
    while index not in visited:
        visited.add(index)
        op, value = instructions[index].split(" ")
        print(f"Index: {index}\tOp: {op}\tValue: {value}")
        if op == "jmp":
            index += int(value.strip())
            continue
        if op == "acc":
            acc += int(value.strip())
        index += 1
    if index in visited:
        print(f"Exiting early...")
    print(f"Acc = {acc}")


if __name__ == "__main__":
    main()
