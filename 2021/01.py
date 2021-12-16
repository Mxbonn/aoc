from aocd import numbers
import numpy as np


def part_one(sea_depths):
    increased = 0
    for i in range(1, len(sea_depths)):
        if sea_depths[i - 1] < sea_depths[i]:
            increased += 1

    return increased


def part_two(sea_dephts):
    measurements = np.convolve(sea_dephts, np.ones(3), mode='valid')
    increased = 0
    for i in range(1, len(measurements)):
        if measurements[i-1] < measurements[i]:
            increased += 1
    return increased


if __name__ == '__main__':
    result = part_two(numbers)
    print(result)
