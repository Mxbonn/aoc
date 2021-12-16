import math
from collections import defaultdict

from aocd import lines


def part_one(data):
    crossed = defaultdict(int)
    for line in data:
        x1, y1 = [int(n) for n in line.split(' -> ')[0].split(',')]
        x2, y2 = [int(n) for n in line.split(' -> ')[1].split(',')]
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    crossed[(x, y)] += 1
    return len([True for x, y in crossed.items() if y >= 2])


def part_two(data):
    crossed = defaultdict(int)
    for line in data:
        x1, y1 = [int(n) for n in line.split(' -> ')[0].split(',')]
        x2, y2 = [int(n) for n in line.split(' -> ')[1].split(',')]
        if x1 == x2:
            x_range = [x1] * (abs(y1 - y2) + 1)
        else:
            step = int(math.copysign(1, x2 - x1))
            x_range = range(x1, x2 + step, step)
        if y1 == y2:
            y_range = [y1] * (abs(x1 - x2) + 1)
        else:
            step = int(math.copysign(1, y2 - y1))
            y_range = range(y1, y2 + step, step)
        for x, y in zip(x_range, y_range):
            crossed[(x, y)] += 1
    return len([True for x, y in crossed.items() if y >= 2])


edata = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one(elines))
    print(part_one(lines))
    print(part_two(elines))
    print(part_two(lines))
