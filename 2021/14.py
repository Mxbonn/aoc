import re
from collections import defaultdict

from aocd import submit, data, lines


def part_one(data):
    poly, rules = data.split('\n\n')
    rules = rules.splitlines()
    pair_count = defaultdict(int)
    for c1, c2 in zip(poly, poly[1:]):
        pair_count[c1 + c2] += 1
    for step in range(10):
        new_pair_count = defaultdict(int)
        for rule in rules:
            pattern, c = rule.split(' -> ')
            matches = pair_count[pattern]
            new_pair_count[pattern[0] + c] += matches
            new_pair_count[c + pattern[1]] += matches
        pair_count = new_pair_count
    char_count = defaultdict(int)
    char_count[poly[0]] += 1
    for pair, v in pair_count.items():
        char_count[pair[1]] += v
    return max(char_count.values()) - min(char_count.values())


edata = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one(edata))
    print(part_one(data))
