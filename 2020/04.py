from aocd import data, submit
import re


required_fields = {
    'byr': (lambda s: len(s) == 4 and 1920 <= int(s) <= 2002),
    'iyr': (lambda s: len(s) == 4 and 2010 <= int(s) <= 2020),
    'eyr': (lambda s: len(s) == 4 and 2020 <= int(s) <= 2030),
    'hgt': (lambda s: (s[-2:] == "cm" and s[:-2].isdigit() and 150 <= int(s[:-2]) <= 193) or (s[-2:] == "in" and s[:-2].isdigit() and 59 <= int(s[:-2]) <= 76)),
    'hcl': (lambda s: s[0] == '#' and len(s) == 7 and all(["0" <= c <= "9" or "a"<= c <= "f" for c in s[1:]])),
    'ecl': (lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    'pid': (lambda s: s.isdigit() and len(s) == 9)
}


def part_one(data):
    passports = data.split('\n\n')
    n_valid = 0
    for passport in passports:
        valid = True
        for field in required_fields.keys():
            valid = valid and field in passport
        if valid:
            n_valid += 1

    return n_valid


def part_two(data):
    passports = data.split('\n\n')
    n_valid = 0
    for passport in passports:
        valid = True
        for field in required_fields:
            m = re.search(f'{field}:(\S+)', passport)
            if m is not None:
                valid = valid and required_fields[field](m.group(1))
            else:
                valid = False
                break
        if valid:
            n_valid += 1
    return n_valid


if __name__ == '__main__':
    print(part_one(data))
    print(part_two(data))
