import numpy as np
import torch
import torch.nn.functional as F
from aocd import data


def part_one(data):
    return process(data, 2)


def part_two(data):
    return process(data, 50)


def process(data, times):
    algorithm, _, *image = data.splitlines()
    algorithm = [int(c == "#") for c in algorithm]
    image = torch.from_numpy(np.array([[int(p == "#") for p in list(row)] for row in image])).unsqueeze(0).unsqueeze(0)
    kernel = 2 ** torch.arange(8, -1, -1).reshape((1, 1, 3, 3))
    for i in range(times):
        pad_val = int(algorithm[0] == 1 and algorithm[-1] == 0 and (i % 2) == 1)
        image = F.pad(image, (2, 2, 2, 2), value=pad_val)
        image = F.conv2d(image, kernel)
        image.apply_(lambda x: algorithm[x])

    return torch.sum(image).item()


edata = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##\
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###\
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.\
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....\
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..\
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....\
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one(edata))
    print(part_one(data))
    print(part_two(edata))
    print(part_two(data))
