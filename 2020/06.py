from aocd import submit, data


def part_one(data):
    groups = data.split('\n\n')
    r = 0
    for group in groups:
        group = group.replace('\n', '')
        r += len(set(group))

    return r


def part_two(data):
    groups = data.split('\n\n')
    r = 0
    for group in groups:
        users = group.split('\n')
        common_q = set(users[0])
        for user in users[1:]:
            common_q &= set(user)
        r += len(common_q)
    return r


if __name__ == '__main__':
    print(part_one(data))
    print(part_two(data))

