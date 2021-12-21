import functools
import itertools

from aocd import submit, data, lines


def part_one(lines):
    p1_start = int(lines[0].split(":")[1])
    p2_start = int(lines[1].split(":")[1])
    p1_score = p2_score = 0
    rolls = 0
    die = 1
    while p1_score < 1000 and p2_score < 1000:
        if rolls // 3 % 2 == 0:
            p1_start = (p1_start + die*3 + 3) % 10 or 10
            p1_score += p1_start
        else:
            p2_start = (p2_start + die*3 + 3) % 10 or 10
            p2_score += p2_start
        die += 3
        rolls += 3
    return min(p1_score, p2_score) * rolls


def part_two(lines):
    p1_start = int(lines[0].split(":")[1])
    p2_start = int(lines[1].split(":")[1])
    return max(calc_wins(0, 0, p1_start, p2_start))


@functools.cache
def calc_wins(p1_score, p2_score, p1_start, p2_start):
    wins_p1 = wins_p2 = 0

    for die_rolls in itertools.product([1, 2, 3], repeat=3):
        new_p1_start = (p1_start + sum(die_rolls)) % 10 or 10
        new_p1_score = p1_score + new_p1_start
        if new_p1_score >= 21:
            wins_p1 += 1
        else:
            extra_wins_p2, extra_wins_p1 = calc_wins(p2_score, new_p1_score, p2_start, new_p1_start)
            wins_p1 += extra_wins_p1
            wins_p2 += extra_wins_p2
    return wins_p1, wins_p2

edata = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one(elines))
    print(part_one(lines))
    print(part_two(elines))
    print(part_two(lines))
