from aocd import submit, data, lines
from collections import defaultdict
import re


def result(mask, value):
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    return value


def result2(mask, value):
    value = f"{value:0{len(mask)}b}"
    r = "".join([m if m == "X" else str(int(m) | int(v)) for v,m in zip(value, mask)])
    return r


def part_one(lines):
    mem = defaultdict(int)
    mask = lines[0].split()[-1]
    for instr in lines:
        if instr.startswith("mask"):
            mask = instr.split()[-1]
        else:
            m = re.search(r'(\d+)\D+(\d+)', instr)
            address = int(m.group(1))
            value = int(m.group(2))
            mem[address] = result(mask, value)

    return sum(mem.values())


def part_two(lines):
    mem = defaultdict(int)
    mask = lines[0].split()[-1]
    for instr in lines:
        if instr.startswith("mask"):
            mask = instr.split()[-1]
        else:
            m = re.search(r'(\d+)\D+(\d+)', instr)
            address = int(m.group(1))
            value = int(m.group(2))
            r = result2(mask, address)
            n_floats = r.count('X')
            for i in range(2**n_floats):
                b_i = f"{i:0{n_floats}b}"
                a = r
                for j in range(n_floats):
                    a = a.replace("X", b_i[j], 1)
                mem[a] = value

    return sum(mem.values())

edata = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one(elines))
    print(part_one(lines))
    print(part_two(elines))
    print(part_two(lines))
