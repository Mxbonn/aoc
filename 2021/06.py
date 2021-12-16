from aocd import data


def part_one(timers, days=80):
    producers = [timers.count(i) for i in range(9)]
    for i in range(days):
        p = producers.pop(0)
        producers.append(p)
        producers[6] += p
    return sum(producers)


def part_two(timers):
    return part_one(timers, 256)


edata = """\
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one([3, 4, 3, 1, 2]))
    print(part_one([int(n) for n in data.split(',')]))
    print(part_two([3, 4, 3, 1, 2]))
    print(part_two([int(n) for n in data.split(',')]))
