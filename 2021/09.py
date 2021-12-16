import numpy as np
from scipy.ndimage import label
from aocd import submit, data, lines


def part_one(lines):
    h_map = np.array([[int(n) for n in list(line)] for line in lines])
    total_risk = 0
    row_range = range(h_map.shape[0])
    col_range = range(h_map.shape[1])
    for i in row_range:
        for j in col_range:
            val = h_map[i,j]
            adjacent_locs = []
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if i + dx in row_range and j + dy in col_range:
                    adjacent_locs.append(h_map[i+dx, j+dy])
            if all(val < np.array(adjacent_locs)):
                total_risk += val + 1
    return total_risk


def part_two(lines):
    h_map = np.array([[int(n) for n in list(line)] for line in lines])
    low_points = []
    row_range = range(h_map.shape[0])
    col_range = range(h_map.shape[1])
    for i in row_range:
        for j in col_range:
            val = h_map[i,j]
            adjacent_locs = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    if i + dx in row_range and j + dy in col_range:
                        adjacent_locs.append(h_map[i+dx, j+dy])
            if all(val < np.array(adjacent_locs)):
                low_points.append((i, j))
    basins = []
    for low_p in low_points:
        basin_points = []
        to_check_points = set()
        to_check_points.add(low_p)
        while to_check_points:
            p = to_check_points.pop()
            i,j = p
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ii, jj = i+dx, j+dy
                if ii in row_range and jj in col_range and (ii, jj) not in basin_points and h_map[ii, jj] < 9:
                    to_check_points.add((ii,jj))
            basin_points.append(p)
        basins.append(len(basin_points))
    return np.prod(sorted(basins)[-3:])


def part_one_clever(lines):
    h_map = np.array([[int(n) for n in list(line)] for line in lines])
    padded_map = np.pad(h_map, 1, constant_values=9)
    mask = (h_map < padded_map[:-2, 1:-1]) & (h_map < padded_map[2:, 1:-1])\
           & (h_map < padded_map[1:-1, :-2]) & (h_map < padded_map[1:-1, 2:])
    return np.sum(h_map[mask] + 1)


def part_two_clever(lines):
    h_map = np.array([[int(n) for n in list(line)] for line in lines])
    label_map = h_map != 9
    partitioned_map, _ = label(label_map)
    _, counts = np.unique(partitioned_map[partitioned_map > 0], return_counts=True)
    return np.prod(sorted(counts)[-3:])


edata = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one(elines))
    print(part_one_clever(elines))
    print(part_one(lines))
    print(part_one_clever(lines))
    print(part_two(elines))
    print(part_two_clever(elines))
    print(part_two(lines))
    print(part_two_clever(lines))
