from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPPER = 2
    SCISSORS = 3


def main(strategy: str) -> None:
    score = 0
    for turn in strategy.splitlines():
        opponent, you = parse(turn)
        score += outcome(opponent, you) + you.value

    print(score)


def parse(turn: str) -> tuple[Shape, Shape]:
    first, second = turn.split()
    opponent = {"A": Shape.ROCK, "B": Shape.PAPPER, "C": Shape.SCISSORS}[first]
    you = {"X": Shape.ROCK, "Y": Shape.PAPPER, "Z": Shape.SCISSORS}[second]
    return opponent, you


def outcome(opponent: Shape, you: Shape) -> int:
    if opponent == you:
        return 3
    match opponent:
        case Shape.ROCK:
            return 6 if you == Shape.PAPPER else 0
        case Shape.PAPPER:
            return 6 if you == Shape.SCISSORS else 0
        case Shape.SCISSORS:
            return 6 if you == Shape.ROCK else 0


if __name__ == "__main__":
    INPUT = """A Y
B X
C Z
"""

    main(INPUT)
