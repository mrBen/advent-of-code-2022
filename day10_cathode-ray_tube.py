#!/usr/bin/env python3


def main(program: str) -> None:
    register = 1
    cycle = 0

    interesting_cycles = [20, 60, 100, 140, 180, 220]
    sum_strengths = 0

    rows = ["", "", "", "", "", ""]

    for line in program.splitlines():
        cycle += 1
        if cycle in interesting_cycles:
            sum_strengths += register * cycle
        if (cycle - 1) % 40 in range(register - 1, register + 2):
            rows[(cycle - 1) // 40] += "#"
        else:
            rows[(cycle - 1) // 40] += "."

        instruction, *args = line.split()

        if instruction == "addx":
            cycle += 1
            if cycle in interesting_cycles:
                sum_strengths += register * cycle
            if (cycle - 1) % 40 in range(register - 1, register + 2):
                rows[(cycle - 1) // 40] += "#"
            else:
                rows[(cycle - 1) // 40] += "."
            register += int(args[0])

        elif instruction == "noop":
            pass

    print("Part One:")
    print(sum_strengths)

    print("Part Two:")
    for row in rows:
        print(row)


if __name__ == "__main__":
    INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

    main(INPUT)
