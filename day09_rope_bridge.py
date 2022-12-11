#!/usr/bin/env python3


class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, motion: str) -> None:
        if motion == "R":
            self.x += 1
        elif motion == "U":
            self.y += 1
        elif motion == "L":
            self.x -= 1
        elif motion == "D":
            self.y -= 1

    def follow(self, x: int, y: int) -> None:
        dx = x - self.x
        dy = y - self.y

        if abs(dx) > 1 and abs(dy) > 1:
            self.x += dx // abs(dx)
            self.y += dy // abs(dy)
        else:
            if abs(dx) > 1:
                self.x += dx // abs(dx)
                if abs(dy) > 0:
                    self.y += dy // abs(dy)
            if abs(dy) > 1:
                self.y += dy // abs(dy)
                if abs(dx) > 0:
                    self.x += dx // abs(dx)


def main(series: str) -> None:
    head = Point()
    tail = Point()
    visited: set[tuple[int, int]] = set()

    for line in series.splitlines():
        motion, reps = line.split()
        for _ in range(int(reps)):
            head.move(motion)
            tail.follow(head.x, head.y)
            visited.add((tail.x, tail.y))

    print("Part One:")
    print(len(visited))

    rope = [
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
    ]
    visited = set()

    for line in series.splitlines():
        motion, reps = line.split()
        for _ in range(int(reps)):
            rope[0].move(motion)
            for i in range(1, len(rope)):
                rope[i].follow(rope[i - 1].x, rope[i - 1].y)
            visited.add((rope[-1].x, rope[-1].y))

    print("Part Two:")
    print(len(visited))


if __name__ == "__main__":
    INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

    main(INPUT)
