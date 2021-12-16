from aocd import submit, data, lines
import re
import numpy as np
from collections import defaultdict


def part_one(data):
    rules, y_t, n_t = data.split("\n\n")
    m = re.findall(r'(\d+)-(\d+)', rules)
    valid = set()
    for r in m:
        l, u = int(r[0]), int(r[1])
        valid |= set(range(l, u + 1))
    n_t = n_t.splitlines()[1:]
    error_rate = 0
    for ticket in n_t:
        ticket = [int(t) for t in ticket.split(',')]
        for t in ticket:
            if t not in valid:
                error_rate += t
    return(error_rate)


def part_two(data):
    rules, y_t, n_t = data.split("\n\n")
    rule_ranges = {}
    rule_index = {}
    rule_indices = defaultdict(set)
    for rule in rules.split('\n'):
        field, values = rule.split(": ")
        ranges = values.split(" or ")
        values = set()
        for r in ranges:
            r = r.split("-")
            values |= set(range(int(r[0]), int(r[1]) + 1))
        rule_ranges[field] = values

    valid_tickets = []
    for ticket in n_t.splitlines()[1:]:
        ticket = [int(t) for t in ticket.split(',')]
        valid_ticket = True
        for t in ticket:
            if t not in set().union(*rule_ranges.values()):
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(ticket)

    for rule, ranges in rule_ranges.items():
        for i, c in enumerate(np.array(valid_tickets).T):
            valid = True
            for v in c:
                if v not in ranges:
                    valid = False
                    break
            if valid:
                rule_indices[rule].add(i)

    removed = set()
    for key in sorted(rule_indices, key=lambda k: len(rule_indices[k])):
        rule_indices[key] -= removed
        elem = rule_indices[key].pop()
        rule_index[key] = elem
        removed.add(elem)

    y_t = [int(n) for n in y_t.splitlines()[1].split(',')]
    result = 1
    for k, v in rule_index.items():
        if k.startswith("departure"):
            result *= y_t[v]

    return result



edata = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_two(data))
    submit(part_two(data))
