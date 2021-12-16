from aocd import submit, lines


def acc_loop_or_exit(instructions):
    accessed = set()
    acc = 0
    i = 0
    while True:
        if i in accessed:
            return acc, True
        elif i == len(instructions):
            return acc, False
        accessed.add(i)
        instr = instructions[i]
        operation, argument = instr.split(" ")
        argument = int(argument)
        if operation == "acc":
            acc += argument
            i += 1
        elif operation == "jmp":
            i += argument
        elif operation == "nop":
            i+= 1
        else:
            raise ValueError


def part_one(instructions):
    val, _ = acc_loop_or_exit(instructions)
    return val


def part_two(instructions):
    for i in range(len(instructions)):
        instr = instructions[i]
        loop = True
        if "nop" in instr:
            instructions[i] = instr.replace("nop", "jmp")
            val, loop = acc_loop_or_exit(instructions)
            instructions[i] = instr
        elif "jmp" in instr:
            instructions[i] = instr.replace("jmp", "nop")
            val, loop = acc_loop_or_exit(instructions)
            instructions[i] = instr
        if not loop:
            return val


if __name__ == '__main__':
    print(part_one(lines))
    print(part_two(lines))
