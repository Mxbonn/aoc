from aocd import submit, puzzle, examples  # noqa


def part_one(data):
    pass


def part_two(data):
    pass


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
            assert solution is not None
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
            assert solution is not None
            submit(solution)
