#!/usr/bin/env python3


def main(patch: str) -> None:
    nb_visible = 0
    score = 0
    for y, line in enumerate(patch.splitlines()):
        for x, _ in enumerate(line):
            nb_visible += visible(x, y, patch.splitlines())
            score = max(scenic_score(x, y, patch.splitlines()), score)

    print("Part One:")
    print(nb_visible)

    print("Part Two:")
    print(score)


def visible(x: int, y: int, patch: list[str]) -> bool:
    line = patch[y]
    if x in (0, len(line) - 1) or y in (0, len(patch) - 1):
        return True
    north = max(int(line[x]) for line in patch[:y])
    east = max(int(tree) for tree in line[x + 1 :])
    south = max(int(line[x]) for line in patch[y + 1 :])
    west = max(int(tree) for tree in line[:x])
    tree = int(line[x])
    return north < tree or east < tree or west < tree or south < tree


def scenic_score(x: int, y: int, patch: list[str]) -> int:
    height = int(patch[y][x])
    north_view = (
        viewing_distance(height, [int(line[x]) for line in patch[y - 1 :: -1]])
        if y > 0
        else 0
    )
    east_view = (
        viewing_distance(height, [int(tree) for tree in patch[y][x + 1 :]])
        if x < len(patch[y])
        else 0
    )
    south_view = (
        viewing_distance(height, [int(line[x]) for line in patch[y + 1 :]])
        if y < len(patch)
        else 0
    )
    west_view = (
        viewing_distance(height, [int(tree) for tree in patch[y][x - 1 :: -1]])
        if x > 0
        else 0
    )
    return north_view * east_view * south_view * west_view


def viewing_distance(height: int, trees: list[int]) -> int:
    for i, tree in enumerate(trees):
        if tree >= height:
            return i + 1
    return len(trees)


if __name__ == "__main__":
    INPUT = """30373
25512
65332
33549
35390
"""

    main(INPUT)
