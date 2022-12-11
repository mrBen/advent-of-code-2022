#!/usr/bin/env python3

from functools import reduce


def main(rucksacks: str) -> None:
    priorities_sum = 0
    for rucksack in rucksacks.splitlines():
        shared_item = split_and_intersect(rucksack)
        priorities_sum += priority_of("".join(shared_item))
    print("Part One:")
    print(priorities_sum)

    priorities_sum = 0
    rucksack_list = rucksacks.splitlines()
    for i in range(0, len(rucksack_list), 3):
        badge = reduce(lambda x, y: x & y, map(set, rucksack_list[i : i + 3]))
        priorities_sum += priority_of("".join(badge))
    print("Part Two:")
    print(priorities_sum)


def split_and_intersect(rucksack: str) -> str:
    first = set(rucksack[: len(rucksack) // 2])
    second = set(rucksack[len(rucksack) // 2 :])
    return "".join(first & second)


def priority_of(item_type: str) -> int:
    if item_type.islower():
        return ord(item_type) - ord("a") + 1
    return ord(item_type) - ord("A") + 27


if __name__ == "__main__":
    INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

    main(INPUT)
