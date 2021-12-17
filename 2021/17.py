import math
import re

from aocd import submit, data, lines


def triangular_number(n):
    return (n * (n + 1)) // 2


def part_one(target_str):
    y0, y1 = [int(y) for y in re.search(r"y=(.+)\.\.(.+)", target_str).groups()]
    y_probe = abs(y0) - 1
    max_height = triangular_number(y_probe)
    return max_height


def part_two(target_str):
    x0, x1 = [int(x) for x in re.search(r"x=(.+)\.\.(.+),", target_str).groups()]
    y0, y1 = [int(y) for y in re.search(r"y=(.+)\.\.(.+)", target_str).groups()]
    count = 0
    min_x_probe = math.floor((1/2) * (math.sqrt(8 * x0 + 1) + 1)) # https://www.wolframalpha.com/input/?i=solve+for+n%3A+%28n%5E2+-+n%29%2F2+%3E%3D+x
    for x in range(min_x_probe, x1 + 1):
        for y in range(y0, -y0):
            x_landing = y_landing = 0
            x_probe, y_probe = x, y
            while y_landing >= y0:
                x_landing += x_probe
                x_probe = max(0, x_probe - 1)
                y_landing += y_probe
                y_probe -= 1
                if x0 <= x_landing <= x1 and y0 <= y_landing <= y1:
                    count += 1
                    break
    return count


edata = """\
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one("target area: x=20..30, y=-10..-5"))
    print(part_one(data))
    print(part_two("target area: x=20..30, y=-10..-5"))
    print(part_two("target area: x=22..27, y=-10..-5"))
    print(part_two(data))
