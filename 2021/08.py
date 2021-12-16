import itertools
from collections import defaultdict

from aocd import submit, data, lines

d_to_seg = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}
seg_to_d = {seg:d for d, seg in d_to_seg.items()}

len_to_seg = {
    2: "cf",
    3: "acf",
    4: "bcdf",
    7: "abcdefg",
    5: "adg",
    6: "abfg",
}


def part_one(lines):
    count = 0
    for line in lines:
        patterns, outputs = [d.split() for d in line.split('|')]
        print(patterns, outputs)
        for d in outputs:
            if len(d) == len(d_to_seg[1]) or len(d) == len(d_to_seg[4]) or len(d) == len(d_to_seg[7]) or len(d) == len(
                    d_to_seg[8]):
                count += 1
    return count


def part_two(lines):
    count = 0
    for line in lines:
        patterns, outputs = [d.split() for d in line.split('|')]
        mapping = {}
        for d in reversed(sorted(patterns, key=lambda k: len(k))):
            seg = len_to_seg[len(d)]
            for l in seg:
                if l in mapping:
                    mapping[l] &= set(d)
                else:
                    mapping[l] = set(d)
            for l in set("abcdefg") - set().union(*[set(seg) for seg in d_to_seg.values() if len(seg) == len(d)]):
                if l in mapping:
                    mapping[l] -= set(d)
        # reverse mapping
        reverse_mapping = defaultdict(set)
        for og_s, new_segs in mapping.items():
            for s in new_segs:
                reverse_mapping[s].add(og_s)
        output = ""
        for o in outputs:
            correct_segs = ["".join(sorted(tup)) for tup in itertools.product(*[reverse_mapping[l] for l in o])]
            for seg in correct_segs:
                if seg in seg_to_d:
                    output += str(seg_to_d[seg])
        count += int(output)
    return count


def part_two_clever(lines):
    count = 0
    for line in lines:
        patterns, outputs = [[set(p) for p in d.split()] for d in line.split('|')]
        pattern_l = {len(p): p for p in patterns}
        n = ''
        for o in outputs:
            length = len(o)
            matches_with_7 = len(o&pattern_l[3])
            matches_with_4 = len(o&pattern_l[4])
            if length == 2:
                n += '1'
            elif length == 5 and matches_with_4 == 2:
                n += '2'
            elif length == 5 and matches_with_7 == 3:
                n += '3'
            elif length == 4:
                n += '4'
            elif length == 5 and matches_with_4 == 3:
                n += '5'
            elif length == 6 and matches_with_7 == 2:
                n += '6'
            elif length == 3:
                n += '7'
            elif length == 7:
                n += '8'
            elif length == 6 and matches_with_4 == 4:
                n += '9'
            else:
                n += '0'
        count += int(n)
    return count


edata = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | \
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | \
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | \
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | \
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | \
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | \
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | \
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | \
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | \
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | \
fgae cfgab fg bagce
"""
elines = edata.splitlines()

if __name__ == '__main__':
    print(part_two(elines))
    print(part_two(lines))
    print(part_two_clever(lines))
