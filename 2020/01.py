from aocd import numbers


def part_one(expenses):
    for a in expenses:
        for b in expenses:
            if a + b == 2020:
                return a * b


def part_two(expenses):
    for a in expenses:
        for b in expenses:
            for c in expenses:
                if a + b + c == 2020:
                    return a * b * c


if __name__ == '__main__':
    print(part_one([1721, 979, 366, 299, 675, 1456]))
    print(part_two([1721, 979, 366, 299, 675, 1456]))
    print(part_one(numbers))
    print(part_two(numbers))
