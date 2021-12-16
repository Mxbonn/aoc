from aocd import submit, lines


def part_one(seats):
    return (max(get_ids(seats)))


def get_ids(seats):
    ids = []
    for seat in seats:
        binary = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        row = int(binary[:7], 2)
        column = int(binary[7:], 2)
        ids.append(row * 8 + column)
    return ids


def part_two(seats):
    ids = sorted(get_ids(seats))
    for i, j in zip(ids, range(ids[0], ids[-1])):
        if i != j:
            return j


if __name__ == '__main__':
    print(part_one(lines))
    print(part_two(lines))
    submit(part_two(lines))
