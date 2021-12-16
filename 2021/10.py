from aocd import submit, data, lines
from collections import deque


points_lookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points2_lookup = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

bracket_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part_one(lines):
    error_score = 0
    for line in lines:
        closing_brackets = deque()
        for c in list(line):
            if c in bracket_mapping:
                closing_brackets.append(bracket_mapping[c])
            else:
                closing_bracket = closing_brackets.pop()
                if c != closing_bracket:
                    error_score += points_lookup[c]
                    break
    return error_score


def part_two(lines):
    error_scores = []
    for line in lines:
        closing_brackets = deque()
        for c in list(line):
            if c in bracket_mapping:
                closing_brackets.append(bracket_mapping[c])
            else:
                closing_bracket = closing_brackets.pop()
                if c != closing_bracket:
                    break
        else:
            score = 0
            for c in reversed(closing_brackets):
                score = score * 5 + points2_lookup[c]
            error_scores.append(score)
    return sorted(error_scores)[len(error_scores) // 2]


edata = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one(elines))
    print(part_one(lines))
    print(part_two(elines))
    print(part_two(lines))
