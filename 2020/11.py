import copy
from collections import Counter

from aocd import submit, lines
import numpy as np


def round_seats(seats):
    new_seats = copy.deepcopy(seats)
    m, n = seats.shape
    for r in range(m):
        for c in range(n):
            adjacent = seats[max(0, r - 1):(min(r+2, m)), max(0, c - 1):(min(c+2, n))]
            if seats[r, c] == 'L' and ((adjacent == '#').sum() == 0):
                new_seats[r, c] = '#'
            if seats[r, c] == '#' and ((adjacent == '#').sum() >= 5):
                new_seats[r, c] = 'L'
    return new_seats


def part_one(data):
    data = np.array(data, dtype=str)
    data = data.view('U1').reshape((data.size, -1))
    while True:
        new_round_data = round_seats(data)
        if np.array_equal(new_round_data, data):
            return (new_round_data == '#').sum()
        data = copy.deepcopy(new_round_data)


def round2_seats(seats):
    new_seats = copy.deepcopy(seats)
    m, n = seats.shape
    for r in range(m):
        for c in range(n):
            occ = 0
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if dy == dx == 0:
                        continue
                    attempts = 1
                    while True:
                        i = r + dy * attempts
                        j = c + dx * attempts
                        if i in range(m) and j in range(n):
                            if seats[i, j] == '#':
                                occ += 1
                                break
                            if seats[i, j] == 'L':
                                break
                        else:
                            break
                        attempts += 1
            if seats[r, c] == 'L' and (occ == 0):
                new_seats[r, c] = '#'
            if seats[r, c] == '#' and (occ >= 5):
                new_seats[r, c] = 'L'
    return new_seats


def part_two(data):
    data = np.array(data, dtype=str)
    data = data.view('U1').reshape((data.size, -1))
    while True:
        new_round_data = round2_seats(data)
        if np.array_equal(new_round_data, data):
            return (new_round_data == '#').sum()
        data = copy.deepcopy(new_round_data)


if __name__ == '__main__':
    print(part_one(lines))
    print(part_two(lines))
