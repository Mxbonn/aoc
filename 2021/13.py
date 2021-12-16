import numpy as np
from aocd import submit, data, lines
from collections import defaultdict


def part_one(data):
    paper = dict()
    coords, folds = data.split('\n\n')
    coords = [(int(d.split(',')[0]), int(d.split(',')[1])) for d in coords.split('\n')]
    for coord in coords:
        paper[coord] = 1
    folds = [(d.split('=')[0][-1], int(d.split('=')[1])) for d in folds.splitlines()]
    for fold in folds:
        c_pos = 0 if fold[0] == 'x' else 1
        split_line = fold[1]
        for coord in list(paper.keys()):
            if coord[c_pos] == split_line:
                print(coord)
                del paper[coord]
            elif coord[c_pos] > split_line:
                print(coord)
                del paper[coord]
                new_coord = list(coord)
                new_coord[c_pos] = 2 * split_line - coord[c_pos]
                paper[tuple(new_coord)] = 1
        break
    return len(paper)


def part_two(data):
    paper = dict()
    coords, folds = data.split('\n\n')
    coords = [(int(d.split(',')[0]), int(d.split(',')[1])) for d in coords.split('\n')]
    for coord in coords:
        paper[coord] = 1
    folds = [(d.split('=')[0][-1], int(d.split('=')[1])) for d in folds.splitlines()]
    for fold in folds:
        c_pos = 0 if fold[0] == 'x' else 1
        split_line = fold[1]
        for coord in list(paper.keys()):
            if coord[c_pos] == split_line:
                print(coord)
                del paper[coord]
            elif coord[c_pos] > split_line:
                print(coord)
                del paper[coord]
                new_coord = list(coord)
                new_coord[c_pos] = 2 * split_line - coord[c_pos]
                paper[tuple(new_coord)] = 1
    paper_board = np.empty((max(list(paper.keys()),key=lambda c: c[1])[1]+1, max(list(paper.keys()),key=lambda c: c[0])[0]+1), dtype=str)
    paper_board.fill('.')
    for coord in paper.keys():
        paper_board[coord[::-1]] = '#'
    print(paper_board)
    return len(paper)

edata = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

elines = edata.splitlines()


if __name__ == '__main__':
    np.set_printoptions(linewidth=300)
    print(part_two(edata))
    print(part_two(data))
    #submit(part_one(data))
