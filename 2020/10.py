import numpy as np
from aocd import submit, numbers


def part_one(numbers):
    numbers.sort()
    numbers = [0] + numbers + [numbers[-1] + 3]
    diff_1 = 0
    diff_3 = 0
    for i, j in zip(numbers, numbers[1:]):
        diff = j - i
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
    return diff_1 * diff_3


def part_two(numbers):
    numbers.sort()
    numbers = [0] + numbers + [numbers[-1] + 3]
    paths = np.zeros(numbers[-1] + 1)
    paths[0] = 1
    for n in numbers[1:]:
        p = 0
        for i in range(1, 4):
            if n - i in numbers:
                p += paths[n - i]
        paths[n] = p
    return paths[-1]


if __name__ == '__main__':
    print(part_one(numbers))
    print(part_two(numbers))
