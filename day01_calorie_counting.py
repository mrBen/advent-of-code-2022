#!/usr/bin/env python3


def main(the_list: str) -> None:
    calories = [0]
    for item in the_list.splitlines():
        try:
            calories[-1] += int(item)
        except ValueError:
            calories.append(0)

    calories.sort(reverse=True)

    print("Part One: ")
    print(calories[0])

    print("Part Two:")
    print(sum(calories[:3]))


if __name__ == "__main__":
    INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

    main(INPUT)
