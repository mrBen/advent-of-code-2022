def main(assignments: str) -> None:
    count = 0
    for pair in assignments.splitlines():
        first, second = pair.split(",")
        count += fully_contains(first, second)
    print("Part One:")
    print(count)

    count = 0
    for pair in assignments.splitlines():
        first, second = pair.split(",")
        count += overlap(first, second)
    print("Part Two:")
    print(count)


def fully_contains(first: str, second: str) -> bool:
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    return (
        int(first_start) >= int(second_start) and int(first_end) <= int(second_end)
    ) or (int(first_start) <= int(second_start) and int(first_end) >= int(second_end))


def overlap(first: str, second: str) -> bool:
    first_start, first_end = first.split("-")
    second_start, second_end = second.split("-")
    return int(first_end) >= int(second_start) and int(first_start) <= int(second_end)


if __name__ == "__main__":
    INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

    main(INPUT)
