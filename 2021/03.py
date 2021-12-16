import math
from aocd import lines
import numpy as np


def data_to_matrix(data):
    n_data = []
    for d in data:
        n_data.append(list(map(int, d)))
    return np.array(n_data)


def bit_array_to_binary(arr):
    return int("".join([str(b) for b in arr]), 2)


def part_one(diagnostics):
    m = data_to_matrix(diagnostics)
    c_sums = np.sum(m, axis=0)
    gamma = np.where(c_sums > m.shape[0] // 2, 1, 0)
    epsilon = np.where(c_sums > m.shape[0] // 2, 0, 1)
    gamma = int("".join([str(b) for b in gamma]), 2)
    epsilon = int("".join([str(b) for b in epsilon]), 2)
    return gamma * epsilon


def part_two(diagnostics):
    m = data_to_matrix(diagnostics)
    o = m
    for p in range(o.shape[1]):
        c_sums = np.sum(o, axis=0)
        mcvs = np.where(c_sums >= math.ceil(o.shape[0] / 2), 1, 0)
        mcv = mcvs[p]
        mask = np.array([row[p] == mcv for row in o])
        o = o[mask]
        if o.shape[0] == 1:
            break
    oxygen = bit_array_to_binary(o[0])
    c = m
    for p in range(c.shape[1]):
        c_sums = np.sum(c, axis=0)
        lcvs = np.where(c_sums >= math.ceil(c.shape[0] / 2), 0, 1)
        lcv = lcvs[p]
        mask = np.array([row[p] == lcv for row in c])
        c = c[mask]
        if c.shape[0] == 1:
            break
    co2 = bit_array_to_binary(c[0])
    return co2 * oxygen


if __name__ == '__main__':
    result = part_two(lines)
    print(result)
