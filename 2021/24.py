import re

import z3
from aocd import data


def solve(program, maximize=True):
    solver = z3.Optimize()
    z = 0
    monad = 0
    program = parse_program(program)
    for block, (div, check, offset) in enumerate(program):
        w = z3.Int(f"w{block}")
        monad = monad * 10 + w
        solver.add(z3.And(w >= 1, w <= 9))
        z = z3.If(w == z % 26 + check, z / div, 26 * z / div + w + offset)
    solver.add(z == 0)
    if maximize:
        solver.maximize(monad)
    else:
        solver.minimize(monad)
    print(solver.check())
    return solver.model().eval(monad)


def parse_program(program):
    div_check_offsets = []
    for block in program.split('inp w\n')[1:]:
        div = int(re.search(r"div z (-?\w+)", block).groups()[0])
        check = int(re.search(r"add x (-?\w+)\neql", block).groups()[0])
        offset = int(re.search(r"add y (-?\w+)\nmul y x\nadd z y", block).groups()[0])
        div_check_offsets.append([div, check, offset])
    return div_check_offsets


def part_one(data):
    return solve(data, True)


def part_two(data):
    return solve(data, False)


if __name__ == '__main__':
    print(part_one(data))
    print(part_two(data))
