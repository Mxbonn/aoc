from aocd import lines


def part_one(instructions):
    h_pos = v_pos = 0
    directions = ['N', 'E', 'S', 'W']
    d_pos = 1
    for instr in instructions:
        curr_m = directions[d_pos]
        action = instr[0]
        movement = int(instr[1:])
        if action == "F":
            action = curr_m
        if action == "N":
            v_pos += movement
        elif action == "E":
            h_pos += movement
        elif action == "S":
            v_pos -= movement
        elif action == "W":
            h_pos -= movement
        else:
            direction_change = movement // 90
            if action == "L":
                d_pos = (d_pos - direction_change) % 4
            elif action == "R":
                d_pos = (d_pos + direction_change) % 4

    return abs(h_pos) + abs(v_pos)


def pos_to_quadrant(h_pos, v_pos):
    if h_pos >= 0 and v_pos >= 0:
        return 0
    elif h_pos >= 0 and v_pos < 0:
        return 1
    elif h_pos < 0 and v_pos < 0:
        return 2
    elif h_pos < 0 and v_pos >= 0:
        return 3


def part_two(instructions):
    h_pos = v_pos = 0
    w_h_pos, w_v_pos = 10, 1
    for instr in instructions:
        action = instr[0]
        movement = int(instr[1:])
        if action == "F":
            h_pos += movement * w_h_pos
            v_pos += movement * w_v_pos
        elif action == "N":
            w_v_pos += movement
        elif action == "E":
            w_h_pos += movement
        elif action == "S":
            w_v_pos -= movement
        elif action == "W":
            w_h_pos -= movement
        else:
            movement = movement % 360
            if action == "L":
                movement = 360 - movement
            turns = movement // 90
            quadrant = pos_to_quadrant(w_h_pos, w_v_pos)
            quadrant = (quadrant + turns) % 4
            if (turns % 2) == 1:
                w_h_pos, w_v_pos = w_v_pos, w_h_pos
            if quadrant == 0:
                w_h_pos, w_v_pos = abs(w_h_pos), abs(w_v_pos)
            elif quadrant == 1:
                w_h_pos, w_v_pos = abs(w_h_pos), -abs(w_v_pos)
            elif quadrant == 2:
                w_h_pos, w_v_pos = -abs(w_h_pos), -abs(w_v_pos)
            elif quadrant == 3:
                w_h_pos, w_v_pos = -abs(w_h_pos), abs(w_v_pos)

    return abs(h_pos) + abs(v_pos)


if __name__ == '__main__':
    print(part_one(lines))
    print(part_two(lines))
