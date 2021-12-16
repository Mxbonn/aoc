from aocd import submit, data, lines
from collections import defaultdict, deque, Counter


def part_one(lines):
    cave = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        cave[a].append(b)
        if b != 'start':
            cave[a].append(b)
        if a != 'start':
            cave[b].append(a)
    paths_in_progress = set([('start', c) for c in cave['start']])
    finished_paths = set()
    while paths_in_progress:
        path = paths_in_progress.pop()
        last_node = path[-1]
        for c in cave[last_node]:
            if c == "end":
                finished_paths.add(path + (c,))
            elif c.islower() and c in path:
                continue
            else:
                paths_in_progress.add(path + (c,))
    return(len(finished_paths))


def part_two(lines):
    cave = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        if b != 'start':
            cave[a].append(b)
        if a != 'start':
            cave[b].append(a)
    paths_in_progress = set([('start', c) for c in cave['start']])
    finished_paths = set()
    while paths_in_progress:
        path = paths_in_progress.pop()
        last_node = path[-1]
        visited_small_cave_twice = False
        counter = Counter(path[1:])
        for c, count in counter.items():
            if c.islower() and count > 1:
                visited_small_cave_twice = True
                break
        for c in cave[last_node]:
            if c == "end":
                finished_paths.add(path + (c,))
            elif visited_small_cave_twice and c.islower() and c in path:
                continue
            else:
                paths_in_progress.add(path + (c,))
    return(len(finished_paths))


edata = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
edata = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""
elines = edata.splitlines()


if __name__ == '__main__':
    print(part_two(elines))
    print(part_two(lines))
    submit(part_two(lines))
