#!/usr/bin/env python3


def main(program: str) -> None:
    register = 1
    cycle = 0
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    sum_strengths = 0

    for line in program.splitlines():
        cycle += 1
        if cycle in interesting_cycles:
            sum_strengths += register * cycle

        instruction, *args = line.split()

        if instruction == "addx":
            cycle += 1
            if cycle in interesting_cycles:
                sum_strengths += register * cycle
            register += int(args[0])

        elif instruction == "noop":
            pass

    print("Part One:")
    print(sum_strengths)


if __name__ == "__main__":
    INPUT = """noop
noop
noop
addx 4
addx 3
addx 3
addx 3
noop
addx 2
addx 1
addx -7
addx 10
addx 1
addx 5
addx -3
addx -7
addx 13
addx 5
addx 2
addx 1
addx -30
addx -8
noop
addx 3
addx 2
addx 7
noop
addx -2
addx 5
addx 2
addx -7
addx 8
addx 2
addx 5
addx 2
addx -12
noop
addx 17
addx 3
addx -2
addx 2
noop
addx 3
addx -38
noop
addx 3
addx 4
noop
addx 5
noop
noop
noop
addx 1
addx 2
addx 5
addx 2
addx -3
addx 4
addx 2
noop
noop
addx 7
addx -30
addx 31
addx 4
noop
addx -24
addx -12
addx 1
addx 5
addx 5
noop
noop
noop
addx -12
addx 13
addx 4
noop
addx 23
addx -19
addx 1
addx 5
addx 12
addx -28
addx 19
noop
addx 3
addx 2
addx 5
addx -40
addx 4
addx 32
addx -31
noop
addx 13
addx -8
addx 5
addx 2
addx 5
noop
noop
noop
addx 2
addx -7
addx 8
addx -7
addx 14
addx 3
addx -2
addx 2
addx 5
addx -40
noop
noop
addx 3
addx 4
addx 1
noop
addx 2
addx 5
addx 2
addx 21
noop
addx -16
addx 3
noop
addx 2
noop
addx 1
noop
noop
addx 4
addx 5
noop
noop
noop
noop
noop
noop
noop
"""

    main(INPUT)
