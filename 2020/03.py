from aocd import lines,submit


def part_one(forest, right=3, down=1):
    n_trees = 0
    n = len(forest[0])
    pos = 0
    for i, trees in enumerate(forest[1:]):
        if (i + 1) % down != 0:
            continue
        pos = (pos + right) % n
        if trees[pos] == '#':
            n_trees += 1
    return n_trees


def part_two(forest):
    return part_one(forest, 1, 1) * part_one(forest, 3, 1) * part_one(forest, 5, 1) * part_one(forest, 7, 1) * part_one(
        forest, 1, 2)


if __name__ == '__main__':
    print(part_one(lines,3,1))
    print(part_two(lines))
    #submit(part_two(lines))
