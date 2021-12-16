from aocd import submit, data, lines
import numpy as np


def part_one(data):
    data = np.array(data)
    pos = np.median(data)
    return int(np.sum(np.abs(data - pos)))


def part_two(data):
    data = np.array(data)
    pos = int(np.floor(np.mean(data)))
    dist = np.abs(data - pos)
    fuel = 0
    for d in dist:
        fuel += d * (d + 1) // 2
    return fuel

edata = """\
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one([16,1,2,0,4,2,7,1,2,14]))
    print(part_one([int(n) for n in data.split(',')]))
    print(part_two([16,1,2,0,4,2,7,1,2,14]))
    print(part_two([int(n) for n in data.split(',')]))
