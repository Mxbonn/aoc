import numpy as np
from aocd import submit, data, lines


def part_one(lines):
    data = np.array([[int(n) for n in line] for line in lines])
    flashes = 0
    for i in range(100):
        data += 1
        while (data == 10).any():
            indices = np.where(data == 10)
            indices = set([(i, j) for i, j in zip(indices[0], indices[1])])
            while indices:
                i, j = indices.pop()
                data[max(0, i-1):min(10, i+2), max(0,j-1):min(10, j+2)] += 1
                extra_indices = np.where(data[max(0, i-1):min(10, i+2), max(0,j-1):min(10, j+2)] == 10)
                indices |= set([(max(0, i-1) + ii, max(0, j-1) + jj) for ii, jj in zip(extra_indices[0], extra_indices[1])])
        flashes += np.sum((data >= 10))
        data[data >= 10] = 0
    return flashes


def part_two(lines):
    data = np.array([[int(n) for n in line] for line in lines])
    flashes = 0
    count = 0
    while not (data == 0).all():
        count += 1
        data += 1
        while (data == 10).any():
            indices = np.where(data == 10)
            indices = set([(i, j) for i, j in zip(indices[0], indices[1])])
            while indices:
                i, j = indices.pop()
                data[max(0, i-1):min(10, i+2), max(0,j-1):min(10, j+2)] += 1
                extra_indices = np.where(data[max(0, i-1):min(10, i+2), max(0,j-1):min(10, j+2)] == 10)
                indices |= set([(max(0, i-1) + ii, max(0, j-1) + jj) for ii, jj in zip(extra_indices[0], extra_indices[1])])
        flashes += np.sum((data >= 10))
        data[data >= 10] = 0
    return count

edata = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_two(elines))
    print(part_two(lines))
    #submit(part_two(lines))
