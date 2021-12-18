import ast
import functools
import itertools
import math
import re

from aocd import submit, data, lines


def fish_reduce(fish):
    while True:
        fish = "".join(fish)
        fish = re.findall(r"(\[|\]|,|\d+)", fish)
        nest_level = 0
        for i, char in enumerate(fish):
            if char == '[':
                nest_level += 1
            elif char == ']':
                nest_level -= 1
            if nest_level == 5:
                for j in reversed(range(i)):
                    if fish[j].isdigit():
                        fish[j] = f"{int(fish[j]) + int(fish[i+1])}"
                        break
                for j in range(i+5, len(fish)):
                    if fish[j].isdigit():
                        fish[j] = f"{int(fish[j]) + int(fish[i+3])}"
                        break
                fish = fish[:i] + ["0"] + fish[i+5:]
                break
        else:
            for i, char in enumerate(fish):
                if char.isdigit() and int(char) >= 10:
                    left = math.floor(int(char) / 2)
                    right = math.ceil(int(char) / 2)
                    fish[i] = f"[{left}, {right}]"
                    break
            else:
                break
    fish = "".join(fish)
    return fish


def add_and_reduce_fish(fish_a, fish_b):
    fish = f"[{fish_a},{fish_b}]"
    return fish_reduce(fish)


def magnitude(fish_list):
    if isinstance(fish_list, int):
        return fish_list
    else:
        return 3 * magnitude(fish_list[0]) + 2 * magnitude(fish_list[1])


def part_one(snailfish):
    fish = functools.reduce(add_and_reduce_fish, snailfish)
    fish = ast.literal_eval(fish)
    return magnitude(fish)


def part_two(snailfish):
    magnitudes = []
    for fish_a, fish_b in itertools.permutations(snailfish, 2):
        fish = add_and_reduce_fish(fish_a, fish_b)
        fish = ast.literal_eval(fish)
        magnitudes.append(magnitude(fish))
    return max(magnitudes)

edata = """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one(elines))
    print(part_one(lines))
    print(part_two(elines))
    print(part_two(lines))
    #submit(part_two(lines))
