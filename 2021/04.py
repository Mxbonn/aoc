import numpy as np
from aocd import data


def check_board(masked_board):
    rows = np.sum(masked_board, axis=1)
    cols = np.sum(masked_board, axis=0)
    if 5 in rows or 5 in cols:
        return True
    else:
        return False


def convert_data(data):
    data = data.split("\n\n")
    numbers = [int(n) for n in data[0].split(',')]
    np_boards = [np.array([[int(n) for n in l.split()] for l in board.splitlines()]) for board in data[1:]]
    return numbers, np_boards


def part_one(data):
    numbers, np_boards = convert_data(data)

    masked_boards = [np.zeros_like(b) for b in np_boards]
    for n in numbers:
        for board, masked_board in zip(np_boards, masked_boards):
            masked_board |= (board == n)
            if check_board(masked_board):
                return np.sum(board[(masked_board == 0)]) * n


def part_two(data):
    numbers, np_boards = convert_data(data)

    masked_boards = [np.zeros_like(b) for b in np_boards]
    board_already_won = [False] * len(np_boards)
    for n in numbers:
        for i, (board, masked_board) in enumerate(zip(np_boards, masked_boards)):
            already_won = board_already_won[i]
            if not already_won:
                masked_board |= (board == n)
                board_already_won[i] = check_board(masked_board)
                if all(board_already_won):
                    return np.sum(board[(masked_board == 0)]) * n


edata = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

elines = edata.splitlines()
if __name__ == '__main__':
    print(part_one(edata))
    print(part_one(data))
    print(part_two(edata))
    print(part_two(data))
