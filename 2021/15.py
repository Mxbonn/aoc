import heapq

import numpy as np
from aocd import submit, data, lines


def part_one(lines):
    cave = np.array([[int(n) for n in line] for line in lines])
    rows, cols = cave.shape
    target = (rows - 1, cols - 1)
    # DIJKSTRA
    dists = np.full_like(cave, 1000000)
    visited = np.zeros_like(cave, dtype=bool)
    dists[0, 0] = 0
    priority_queue = [(0, 0, 0)]
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while not visited.all():
        d, r, c = heapq.heappop(priority_queue)
        if (r,c) == target:
            return dists[target]
        visited[(r, c)] = True
        for dr, dc in neighbours:
            if r + dr in range(rows) and c + dc in range(cols) and not visited[(r+dr, c+dc)]:
                alt = dists[(r,c)] + cave[(r+dr,c+dc)]
                if alt < dists[(r+dr, c+dc)]:
                    dists[(r+dr, c+dc)] = alt
                    heapq.heappush(priority_queue, (alt, r+dr, c+dc))


def part_two(lines):
    cave = np.array([[int(n) for n in line] for line in lines])
    rows, cols = cave.shape
    large_cave = np.zeros((rows * 5, cols * 5), dtype=int)
    for r in range(5):
        for c in range(5):
            r_cave = cave + r + c
            r_cave[r_cave >= 10] -= 9
            large_cave[rows*r:rows*r+rows, cols*c:cols*c+cols] = r_cave
    cave = large_cave
    rows, cols = cave.shape
    target = (rows - 1, cols - 1)
    # DIJKSTRA
    dists = np.full_like(cave, 1000000)
    visited = np.zeros_like(cave, dtype=bool)
    dists[0, 0] = 0
    priority_queue = [(0, 0, 0)]
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while not visited.all():

        d, r, c = heapq.heappop(priority_queue)
        if (r,c) == target:
            return d
        visited[(r, c)] = True
        for dr, dc in neighbours:
            if r + dr in range(rows) and c + dc in range(cols) and not visited[(r+dr, c+dc)]:
                alt = d + cave[(r+dr,c+dc)]
                if alt < dists[(r+dr, c+dc)]:
                    dists[(r+dr, c+dc)] = alt
                    heapq.heappush(priority_queue, (alt, r+dr, c+dc))

edata = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_two(elines))
    print(part_two(lines))
    #submit(part_one(lines))
