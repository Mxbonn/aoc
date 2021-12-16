from aocd import lines


def part_one(instructions):
    h_pos = v_pos = 0
    for instruction in instructions:
        command, movement = instruction.split(" ")
        movement = int(movement)
        if command == "forward":
            h_pos += movement
        elif command == "down":
            v_pos += movement
        elif command == "up":
            v_pos -= movement
        else:
            print(command)
    return h_pos * v_pos


def part_two(instructions):
    h_pos = v_pos = aim = 0
    for instruction in instructions:
        command, movement = instruction.split(" ")
        movement = int(movement)
        if command == "forward":
            h_pos += movement
            v_pos += movement * aim
        elif command == "down":
            aim += movement
        elif command == "up":
            aim -= movement
        else:
            print(command)
    return h_pos * v_pos


if __name__ == '__main__':
    result = part_two(lines)
    print(result)