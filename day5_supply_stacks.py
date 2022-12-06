def main(plan: str) -> None:
    drawing, rearrangement = parse_plan(plan)
    stacks = stacks_from_drawing(drawing)
    stacks = apply_procedure(stacks, rearrangement)
    print("Part One:")
    print("".join(stack.pop() for stack in stacks))

    drawing, rearrangement = parse_plan(plan)
    stacks = stacks_from_drawing(drawing)
    stacks = apply_procedure2(stacks, rearrangement)
    print("Part Two:")
    print("".join(stack.pop() for stack in stacks))


def parse_plan(plan: str) -> tuple[list[str], list[str]]:
    stacks = []
    rearrangement = []
    past_the_drawing = False
    for line in plan.splitlines():
        if not past_the_drawing:
            if not line:
                past_the_drawing = True
            else:
                stacks.append(line)
        else:
            rearrangement.append(line)
    return stacks, rearrangement


def stacks_from_drawing(drawing: list[str]) -> list[list[str]]:
    stacks: list[list[str]] = []
    for _ in drawing.pop().split():
        stacks.append([])
    for line in reversed(drawing):
        for i, pos in enumerate(range(1, len(line), 4)):
            if line[pos] != " ":
                stacks[i].append(line[pos])
    return stacks


def apply_procedure(stacks: list[list[str]], procedure: list[str]) -> list[list[str]]:
    for step in procedure:
        _, number, _, orig, _, dest = step.split()
        for _ in range(int(number)):
            crate = stacks[int(orig) - 1].pop()
            stacks[int(dest) - 1].append(crate)
    return stacks


def apply_procedure2(stacks: list[list[str]], procedure: list[str]) -> list[list[str]]:
    for step in procedure:
        _, number, _, orig, _, dest = step.split()
        crates = stacks[int(orig) - 1][-int(number) :]
        for _ in range(int(number)):
            stacks[int(orig) - 1].pop()
        stacks[int(dest) - 1].extend(crates)
    return stacks


if __name__ == "__main__":
    INPUT = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

    main(INPUT)
