from aocd import submit, lines
from collections import defaultdict


def is_in_bag(contains_dict, bag):
    if bag not in contains_dict:
        return False
    else:
        in_bag = False
        for other_bag in contains_dict[bag]:
            if other_bag == "shiny gold":
                in_bag = True
                break
            else:
                in_bag |= is_in_bag(contains_dict, other_bag)
        return in_bag


def part_one(rules):
    contains = defaultdict(list)
    for rule in rules:
        words = rule.split(" ")
        if words[4] == "no":
            continue
        key_bag = f"{words[0]} {words[1]}"
        for i in range(4, len(words), 4):
            value_bag = f"{words[i+1]} {words[i+2]}"
            contains[key_bag].append(value_bag)
    matching_bags = 0
    for bag in contains.keys():
        if bag == "shiny gold":
            continue
        if is_in_bag(contains, bag):
            matching_bags += 1
    return matching_bags


def n_bags_in_bag(contains_dict, bag):
    if bag not in contains_dict:
        return 0
    else:
        n_bags = 0
        for other_bag in contains_dict[bag]:
            bags = n_bags_in_bag(contains_dict, other_bag) + 1
            n_bags += bags
        return n_bags


def part_two(rules):
    contains = defaultdict(list)
    for rule in rules:
        words = rule.split(" ")
        if words[4] == "no":
            continue
        key_bag = f"{words[0]} {words[1]}"
        for i in range(4, len(words), 4):
            value_bag = f"{words[i+1]} {words[i+2]}"
            for j in range(int(words[i])):
                contains[key_bag].append(value_bag)
    return n_bags_in_bag(contains, "shiny gold")


if __name__ == '__main__':
    print(part_one(lines))
    print(part_two(lines))