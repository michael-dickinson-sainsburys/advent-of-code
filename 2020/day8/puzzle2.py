import utils


def main(instructions):
    acc = 0
    finished = False
    index = 0
    visited = set()
    while index not in visited:
        visited.add(index)
        op, value = instructions[index].split(" ")
        if op == "acc":
            acc += int(value.strip())
        if op == "jmp":
            index += int(value.strip())
        else:
            index += 1
        if index > len(instructions) - 1:
            finished = True
            break
    return finished, acc


if __name__ == "__main__":
    instructions = utils.read_input_file("code_instructions.txt")
    for index, instruction in enumerate(instructions):
        op, value = instruction.split(" ")
        if op == "acc":
            continue
        copy = instructions[:]
        if op == "jmp":
            copy[index] = copy[index].replace("jmp", "nop")
        if op == "nop":
            copy[index] = copy[index].replace("nop", "jmp")
        finished, acc = main(copy)
        if finished:
            print(acc)
            exit()
