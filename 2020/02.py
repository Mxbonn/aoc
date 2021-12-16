from aocd import lines, submit
import re


def part_one(passwords):
    valid = 0
    for rule in passwords:
        m = re.search(r'(\d+)-(\d+)\s(.):\s(.+)', rule)
        min_v = int(m.group(1))
        max_v = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        occurances = password.count(char)
        if min_v <= occurances <= max_v:
            valid +=1
    return valid


def part_two(passwords):
    valid = 0
    for rule in passwords:
        m = re.search(r'(\d+)-(\d+)\s(.):\s(.+)', rule)
        min_v = int(m.group(1)) - 1
        max_v = int(m.group(2)) - 1
        char = m.group(3)
        password = m.group(4)
        if (password[min_v] == char) != (password[max_v] == char):
            valid += 1
    return valid


if __name__ == '__main__':
    submit(part_two(lines))
