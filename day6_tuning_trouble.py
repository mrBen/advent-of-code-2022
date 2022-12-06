from collections import deque


def main(datastream: str) -> None:
    print("Part One:")
    last_four: deque[str] = deque()
    for i, char in enumerate(datastream):
        last_four.append(char)
        if len(last_four) > 4:
            last_four.popleft()
        if len(set(last_four)) == 4:
            print(i + 1)
            break

    print("Part Two:")
    last_fourteen: deque[str] = deque()
    for i, char in enumerate(datastream):
        last_fourteen.append(char)
        if len(last_fourteen) > 14:
            last_fourteen.popleft()
        if len(set(last_fourteen)) == 14:
            print(i + 1)
            break


if __name__ == "__main__":
    INPUT = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

    main(INPUT)
