import copy

from aocd import submit, data


def part_one(cucumbers):
    cucumbers = [list(row) for row in cucumbers.splitlines()]
    moved = True
    steps = 0
    rows = len(cucumbers)
    cols = len(cucumbers[0])
    while moved:
        moved = False
        new_cucumbers = copy.deepcopy(cucumbers)
        # First check east facing herd
        for row in range(rows):
            for col in range(cols):
                if cucumbers[row][col] == '>' and cucumbers[row][(col + 1) % cols] == '.':
                    moved = True
                    new_cucumbers[row][(col + 1) % cols] = '>'
                    new_cucumbers[row][col] = '.'
        cucumbers = new_cucumbers
        new_cucumbers = copy.deepcopy(cucumbers)
        # then check south facing herd
        for row in range(rows):
            for col in range(cols):
                if cucumbers[row][col] == 'v' and cucumbers[(row + 1) % rows][col] == '.':
                    moved = True
                    new_cucumbers[(row + 1) % rows][col] = 'v'
                    new_cucumbers[row][col] = '.'
        cucumbers = new_cucumbers
        steps += 1
    return steps


edata = """\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_one(edata))
    print(part_one(data))
    submit(part_one(data))
