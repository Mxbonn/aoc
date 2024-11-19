from aocd import submit, puzzle, examples  # noqa

puzzle = puzzle


def part_one(data):
    lines = data.splitlines()
    sum = 0
    for line in lines:
        numbers_line = "".join(filter(str.isdigit, line))
        line_sum = int(numbers_line[0] + numbers_line[-1])
        sum += line_sum
    return sum


def part_two(data):
    mapping = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }
    for key, value in mapping.items():
        data = data.replace(key, value)
    return part_one(data)


if __name__ == "__main__":
    correct_solution = True
    if not puzzle.answered_a:
        print("Part One:")
        for example in puzzle.examples:
            calculated_solution = part_one(example.input_data)
            correct_solution = (
                correct_solution and str(calculated_solution) == example.answer_a
            )
            if not correct_solution:
                print(example.input_data)
                print(calculated_solution, example.answer_a)
                break
        else:
            solution = part_one(puzzle.input_data)
            print(solution)
            submit(solution)
    else:
        print("Part Two:")
        for example in puzzle.examples:
            print(example)
            if example.answer_b is None:
                continue
            calculated_solution = part_two(example.input_data)
            correct_solution = (
                correct_solution and str(calculated_solution) == example.answer_b
            )
            if not correct_solution:
                print(example.input_data)
                print(calculated_solution, example.answer_b)
                break
        else:
            solution = part_two(puzzle.input_data)
            print(solution)
            submit(solution)
