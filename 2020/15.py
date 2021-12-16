from aocd import submit


def part_one(numbers, spoken_n=2020):
    spoken = {n: i+1 for i, n in enumerate(numbers)}
    last = numbers[-1]
    for i in range(len(numbers) + 1, spoken_n + 1):
        spoken[last], last = i - 1, i - 1 - spoken[last] if last in spoken else 0
    return last


def part_two(numbers):
    return part_one(numbers, 30000000)


edata = """\
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_one([0,3,6]))
    print(part_one([0,3,1,6,7,5]))
    print(part_two([0,3,6]))
    print(part_two([0,3,1,6,7,5]))
