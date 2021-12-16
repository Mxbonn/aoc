from aocd import submit, numbers


def contains_sum(list, number):
    for a in list:
        for b in list:
            if a + b == number and a != b:
                return True
    return False


def part_one(numbers):
    preamble = 25
    for i in range(preamble, len(numbers)):
        if not contains_sum(numbers[i-preamble: i], numbers[i]):
            return numbers[i]


def part_two(numbers):
    invalid_number = part_one(numbers)
    for i in range(len(numbers)):
        l = [numbers[i]]
        for j in range(i + 1, len(numbers)):
            l.append(numbers[j])
            if sum(l) == invalid_number:
                return min(l) + max(l)
            elif sum(l) > invalid_number:
                break


if __name__ == '__main__':
    print(part_one(numbers))
    print(part_two(numbers))
    submit(part_two(numbers))
