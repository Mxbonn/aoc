from aocd import submit, lines
import numpy as np


def part_one(data):
    t = int(data[0])
    busses = [int(n) for n in data[1].split(',') if n.isdigit()]

    i = 0
    while True:
        for bus in busses:
            if (t + i) % bus == 0:
                return bus * i
        i += 1


if __name__ == '__main__':
    print(lines)
    print(part_one(lines))
